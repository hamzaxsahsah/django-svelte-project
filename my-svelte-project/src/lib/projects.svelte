<script>
// @ts-nocheck

    import { onMount } from "svelte";
    import Project from "./Project/Project.svelte";
    let project = []
    onMount(async () => {
		project = await fetch('http://127.0.0.1:8000/apis/projects/?format=json').then((x) => x.json());
    console.log(project)
	});

</script>
<div>
{#each project as item }
    <Project project={item}></Project>
{/each}
</div>

<style></style>