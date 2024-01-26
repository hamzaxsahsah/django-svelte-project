<script>
  import { onMount } from 'svelte';
    import Projects from './lib/projects.svelte';
  let response  = []
  
	let data;
	onMount(async () => {
		response = await fetch('http://127.0.0.1:8000/apis/projects/?format=json').then((x) => x.json());
    console.log(response)
	});
</script>

<h1>Projects</h1>
<Projects></Projects>

<style>

</style>