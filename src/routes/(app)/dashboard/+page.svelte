<script lang="ts">
	import { getContext } from 'svelte';

	import { WEBUI_NAME } from '$lib/stores';

	const i18n = getContext('i18n');
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
				<iframe
					class="h-[calc(100vh-11rem)] w-full"
					title="university.activity-web"
					src="https://app.powerbi.com/reportEmbed?reportId=b4592138-0ad0-4814-bd89-c291965b3f15&autoAuth=true&ctid=a924227e-3ef4-426c-8c8d-931f5666f9f6"
					frameborder="0"
					allowFullScreen="true"
				/>
			</div>
		</div>
	</div>
</div>
