<script lang="ts">
	import { getContext, onMount } from 'svelte';
	import { WEBUI_NAME } from '$lib/stores';
	import { getPowerBIEmbedConfig } from '$lib/apis/powerbi';

	import { Report, service, factories, models } from 'powerbi-client';

	const i18n = getContext('i18n');
	let api_error = false;

	onMount(async () => {
		try {
			const embedConfig = await getPowerBIEmbedConfig();

			// Set up the configuration object that determines what to embed and how to embed it.
			let embedConfiguration = {
				type: 'report',
				tokenType: models.TokenType.Embed,
				accessToken: embedConfig.accessToken,
				id: embedConfig.reportId,
				embedUrl: embedConfig.embedUrl,
				pageView: 'fitToWidth',
				settings: {
					background: models.BackgroundType.Transparent,
					panes: {
						pageNavigation: {
							visible: false
						}
					}
				}
			};

			// Get a reference to the HTML element that contains the embedded report.
			let embedContainer = document.getElementById('embedContainer');

			// Create a new service object
			let reportService = new service.Service(factories.hpmFactory, factories.wpmpFactory, factories.routerFactory);

			// Embed the report.
			if (embedContainer) {
				new Report(reportService, embedContainer, embedConfiguration);
			}
		} catch (error) {
			api_error = true;
		}
	});
</script>

<svelte:head>
	<title>
		{$i18n.t('Adoption Dashboard')} | {$WEBUI_NAME}
	</title>
</svelte:head>

<div class="min-h-screen max-h-[100dvh] w-full flex justify-center dark:text-white">
	<div class="flex flex-col justify-start w-full overflow-y-auto">
		<div class="max-w-2xl mx-auto w-full px-3 md:px-0 my-10">
			<div class=" text-2xl font-semibold mb-3">{$i18n.t('Adoption Dashboard')}</div>
			<hr class=" dark:border-gray-700 my-2.5" />
		</div>
		<div class=" mx-auto w-full px-3 md:px-0">
			<div class="mx-auto w-full px-3 md:px-0">
				<div
					id="embedContainer"
					class="h-[calc(100vh-11rem)] w-full"
				>
					{#if api_error}
						<div class="flex justify-center mt-5">
							<div class="text-red-500">{$i18n.t('Failed to load the report')}</div>
						</div>
					{/if}
				</div>
			</div>
		</div>
	</div>
</div>