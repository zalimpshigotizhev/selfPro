<script setup>
import { useRootStore } from '@/stores/root';
import { storeToRefs } from 'pinia';

const rootStore = useRootStore();
const { tip } = storeToRefs(rootStore);

const props = defineProps({
    icon:{
        type: Object,
        required: true
    },
    gifUrl:{
        type: String,
        required: true
    }
})
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
            <div  class="day">
                <div class="date">
                    mon
                </div>
                <div class="indicator">
    
                </div>
            </div>
            <div  class="day">
                <div class="date">
                    tue
                </div>
                <div class="indicator">
    
                </div>
            </div>
            <div  class="day">
                <div class="date">
                    wed
                </div>
                <div class="indicator">
    
                </div>
            </div>
            <div  class="day">
                <div class="date">
                    thu
                </div>
                <div class="indicator">
    
                </div>
            </div>
            <div  class="day">
                <div class="date">
                    fri
                </div>
                <div class="indicator">
    
                </div>
            </div>
            <div  class="day">
                <div class="date">
                    sat
                </div>
                <div class="indicator">
    
                </div>
            </div>
            <div  class="day">
                <div class="date">
                    sun
                </div>
                <div class="indicator">
    
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '@/assets/style/main'
@import '@/assets/style/indicator-day'
.week
    display: flex
    flex-direction: column
    align-items: center
    font-family: "JetBrains ExtraLight", sans-serif
    font-size: 10px 
    width: 45px
    height: 160px

    .week-days
        display: flex
        flex-wrap: wrap
</style>