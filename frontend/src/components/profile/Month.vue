<script setup>
const props = defineProps({
    month:{
        type: Object,
        required: true
    }
})

console.log(props.month);

</script>
<template>
    <div class="month">
        <div class="name">{{props.month.name}}</div>
        <div  class="string">
            <div v-for="day in props.month.days"  :key="day" class="day">
                <div class="date">{{ day.date }}</div>
                <div class="indicator">
    
                </div>
            </div>
        </div>

        
    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'
@import '../../assets/style/indicator-day'

.month
    @include flex-column
    width: 142px

    &:not(:last-child)
        margin-right: 30px
    .name
        font-family: "JetBrains ExtraLight", sans-serif
        font-size: 18px
    
    .string
        display: flex
        flex-wrap: wrap


</style>