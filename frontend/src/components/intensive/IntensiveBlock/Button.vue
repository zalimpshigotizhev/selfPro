<script setup>
const props = defineProps({
    icon:{
        type: Object,
        required: true
    }
})
</script>
<template>
        <el-button type="primary" :icon="props.icon"></el-button>
</template>
<style lang="sass" scoped>
@import '@/assets/style/main'

</style>