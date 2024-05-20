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
                <div class="date">
                    {{ day.date }}
                </div>
                <div class="indicator">
    
                </div>
            </div>
        </div>

        
    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'

.month
    display: flex
    flex-direction: column
    width: 142px

    &:not(:last-child)
        margin-right: 30px
    .name
        font-family: "JetBrains ExtraLight", sans-serif
        font-size: 18px
    
    .string
        display: flex
        flex-wrap: wrap

        .day
            display: flex
            flex-direction: column
            align-items: center
            width: 16px
            margin-top: 3px

            &:not(:last-child)
                margin-right: 5px

            .date
                width: 12px
                height: 12px
                font-family: "JetBrains ExtraLight", sans-serif
                font-size: 8px

            .indicator
                width: 16px
                height: 16px
                background-color: $background
                border: solid 0.5px
                border-radius: 4px
</style>