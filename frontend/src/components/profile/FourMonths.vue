<script setup>
import Month from './Month.vue'
import { useRootStore } from '../../stores/root';
import { storeToRefs } from 'pinia';


const rootStore = useRootStore()
rootStore.getLastFourMonths()
const { four_months } = storeToRefs(rootStore)

</script>
<template>
    <div class='root'>
        <div class="title">Four months</div>
        <div class="intensive">
            <div class="two-months">
                <Month :month = 'four_months[0]'/>
                <Month :month = 'four_months[1]'/>
            </div>
            <div class="two-months">
                <Month :month = 'four_months[2]'/>
                <Month :month = 'four_months[3]'/>
            </div>
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'

.root
    @include flex-column
    margin-left: 30px
    padding-right: 60px

    @media (min-width: $min_mobile) and (max-width: $max_mobile)
        margin-top: 40px

    .title
        font-family: "JetBrains Bold", sans-serif
        font-size: 25px
    
    .intensive
        display: flex
        flex-direction: column

        .two-months
            display: flex
            width: 314px
            margin: 10px

</style>