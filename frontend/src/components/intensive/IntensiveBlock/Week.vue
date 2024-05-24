<script setup>
import { useRootStore } from '@/stores/root';
import { storeToRefs } from 'pinia';

const rootStore = useRootStore();
const { tip } = storeToRefs(rootStore);

const props = defineProps({
    gifUrl:{
        type: String,
        required: true
    },
    week: {
        type: Object,
        required: true
    }
})



function transLevelToHex(level){
    if(level == 1 || level == null){return "#E1E1E1"}
    if(level == 2){return "#C2E8C5"}
    if(level == 3){return "#CAFFCE"}
    if(level == 4){return "#B7FFBC"}
    if(level == 5){return "#9AFFA1"}
    if(level == 6){return "#78FF82"}
    if(level == 7){return "#54FF61"}
    if(level == 8){return "#5DE367"}
    if(level == 9){return "#5FCF67"}
    if(level == 10){return "#45994B"}
}

function normalizeWeek(week){
    // Изменяет значение дней недели
    // В Hex-цвета для индикаторов
    const keys = Object.keys(week)
    const len = keys.length
    const result = {}
    for (let i=0; i < len; i++){
        let key = keys[i]
        result[key] = transLevelToHex(week[key])
    }
    return result
}
let week = normalizeWeek(props.week);

console.log(week);
</script>

<template>
    <div class="week">
        <VTooltip v-if="tip">
            <div class="info-icon" ></div>
            <template #popper>
                <div class="tip">
                    <img :src="props.gifUrl" class="giffile">
                    Сколько времени вы занимались на этой неделе.
                </div>
            </template>
        </VTooltip>
        week
        <div class="week-days">
            <div  class="day" v-for="(value, key) in week" :key='key'>
                <div class="date">
                    {{ key }}
                </div>
                <div class="indicator" :style="`background-color:${value};`">
    
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '@/assets/style/main'
@import '@/assets/style/indicator-day'
.week
    @include flex-column
    align-items: center
    font-family: "JetBrains ExtraLight", sans-serif
    font-size: 10px 
    width: 45px
    height: 160px

    .week-days
        display: flex
        flex-wrap: wrap
</style>