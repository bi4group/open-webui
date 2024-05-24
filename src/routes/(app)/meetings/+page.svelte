<script lang="ts">
	import { marked } from 'marked';
	import { WEBUI_NAME, user } from '$lib/stores';
	import { getContext, onMount } from 'svelte';
	import { getMeetingsList } from '$lib/apis/meetings';

	const i18n = getContext('i18n');

	let meetingList = [];
	let selectedMeeting = '';
	let api_error = false;
	let missing_token = false;
	let loading = true;

	onMount(async () => {
	if ($user && $user.fireflies_api_key == null) {
		missing_token = true;
		loading = false;
		return;
	}

	try {
		const res = await getMeetingsList(localStorage.token);

		if (res) {
			meetingList = res.data.transcripts;
			selectedMeeting = res.data.transcripts[0];
			loading = false;

			meetingList.forEach((meeting) => {
				meeting.dateString = new Date(meeting.dateString).toLocaleDateString(i18n.locale, {
					year: 'numeric',
					month: 'long',
					day: 'numeric',
					hour: 'numeric',
					minute: 'numeric'
				});

				meeting.summary.overview = marked(meeting.summary.overview.replace(/\n/g, '<br/>'));
				meeting.summary.shorthand_bullet = marked(meeting.summary.shorthand_bullet.replace(/\n/g, '<br/>'));

				meeting.participants = new Set(meeting.participants[0].split(',').concat(meeting.participants.slice(1)));
			});
		}
	} catch (error) {
		console.log(error);
		api_error = true;
		loading = false;
	}
});
</script>

<svelte:head>
	<title>{$i18n.t('Meetings')} | {$WEBUI_NAME}</title>
</svelte:head>

<div class="min-h-screen max-h-[100dvh] w-full flex justify-center dark:text-white">
	{#if missing_token}
		<div class="max-w-8xl mx-auto w-full px-7 mt-10">
			<p>{$i18n.t('You need to connect your Fireflies account to view your meetings. Upload your API token in your Account settings.')}</p>
		</div>
	{:else}
		<div class="flex flex-col justify-start w-1/3 overflow-y-auto pl-7">
			<div class="max-w-8xl mx-auto w-full px-3 md:px-0 mt-10">
				<h1 class="text-3xl font-bold">{$i18n.t('Meetings')}</h1>
			</div>

			{#if loading}
				<div class="max-w-8xl mx-auto w-full px-3 md:px-0 mt-10">
					<p>{$i18n.t('Loading results...')}</p>
				</div>
			{/if}

			{#if api_error}
				<div class="max-w-8xl mx-auto w-full px-3 md:px-0 mt-10">
					<p>{$i18n.t('An error occurred while fetching the meetings list.')}</p>
				</div>
			{/if}

			{#if !api_error && !loading && meetingList.length === 0}
				<div class="max-w-8xl mx-auto w-full px-3 md:px-0 mt-10">
					<p>{$i18n.t('No meetings found.')}</p>
				</div>
			{/if}

			{#if !api_error && meetingList.length > 0}
				<div class="flex flex-col gap-2 w-fit px-3 md:px-0 mt-3">
					{#each meetingList as meeting}
							<button
								class="text-lg text-start font-bold rounded-xl px-3.5 py-2 hover:bg-gray-100 dark:hover:bg-gray-900"
								on:click={() => {
									selectedMeeting = meeting
								}}
							>{meeting.title}</button>
					{/each}
				</div>
			{/if}
		</div>

		<div class="flex flex-col justify-start w-2/3 overflow-y-auto">
			{#if !api_error && meetingList.length > 0}
			<div class="max-w-8xl mx-auto w-full px-3 md:px-0 mt-10">
				<div class="flex flex-col">
					<h1 class="text-3xl font-bold">{$i18n.t('Meeting summary')}</h1>
					<span class="text-xl">{selectedMeeting.title}</span>
				</div>

				<div class="flex flex-col mt-5 gap-7 pb-12 pr-12">
					<div class="flex flex-row gap-20">
						<div class="flex flex-col">
							<span class="text-lg">{$i18n.t('Date')}</span>
							<span class="text-sm font-bold">{selectedMeeting.dateString}</span>
						</div>
						<div class="flex flex-col">
							<span class="text-lg">{$i18n.t('Meeting duration')}</span>
							<span class="text-sm font-bold">{selectedMeeting.duration} {$i18n.t('minutes')}</span>
						</div>
					</div>

					<div>
						<span class="font-bold text-lg">{$i18n.t('Participants')}</span>
						<div class="grid grid-cols-3 gap-2">
							{#each selectedMeeting.participants as participant}
								<span class="text-sm">{participant}</span>
							{/each}
						</div>
					</div>

					<div class="flex flex-col">
						<span class="font-bold text-lg">{$i18n.t('Key points')}</span>
						{#if selectedMeeting.summary.shorthand_bullet === ''}
							<span class="text-sm">{$i18n.t('No key points available.')}</span>
						{:else}
							<span class="text-sm">{@html selectedMeeting.summary.shorthand_bullet}</span>
						{/if}
					</div>

					<div class="flex flex-col">
						<span class="font-bold text-lg">{$i18n.t('Meeting summary')}</span>
						{#if selectedMeeting.summary.overview === ''}
							<span class="text-sm">{$i18n.t('No summary available.')}</span>
						{:else}
							<span class="text-sm">{@html selectedMeeting.summary.overview}</span>
						{/if}
					</div>
				</div>
			</div>
			{/if}
		</div>
	{/if}
</div>