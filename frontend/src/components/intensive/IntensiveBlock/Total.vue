<script setup>
import { useRootStore } from '@/stores/root';
import { storeToRefs } from 'pinia';
import { reactive } from 'vue';

const rootStore = useRootStore();
const { tip } = storeToRefs(rootStore);

const props = defineProps({
    name:{
        type: String,
        required: true
    },
    gifUrl:{
        type: String,
    },
    text:{
        type: String,
    },
    data:{
        type: Number,
        required: true
    }
})

let minutes;
let hours;

function getUnitAbsoluteMin(){
    minutes = props.data
    hours = Math.round(props.data / 60)
};

getUnitAbsoluteMin();

let isMinutes = true;

const time = reactive({
    present: hours,
    tooBig: null
});



function formatting(){
    if(isMinutes){
        time.present = hours
        isMinutes = false
    }else{
        time.present = minutes
        isMinutes = true
    }

    let strPress = String(time.present)

    if(strPress.length > 5){
        time.tooBig = true
    }else{
        time.tooBig = false
    }

};

formatting();

</script>
<template>
    <div class="total" @click="formatting()">
        <div class="title">

            {{ props.name }}
            <VTooltip v-if="tip">
                <div class="info-icon" ></div>
                <template #popper>
                    <div class="tip">
                        <img :src="props.gifUrl" class="giffile">
                        {{ props.text }}
                    </div>
                </template>
            </VTooltip>
        </div>

        <div class="total-time">
            <VTooltip v-if="time.tooBig">
                <p><span v-if="isMinutes">minutes</span><span v-else>hours</span></p>
                <template #popper>
                    <div class="tip">
                        {{ time.present }}<span v-if="isMinutes">minutes</span><span v-else>hours</span>
                    </div>
                </template>
            </VTooltip>
            <VTooltip v-else>
                <p>{{ time.present }}  <span v-if="isMinutes">m</span><span v-else>h</span></p>
                <template #popper>
                    <div class="tip">
                        {{ time.present }}<span v-if="isMinutes">minutes</span><span v-else>hours</span>
                    </div>
                </template>
            </VTooltip>
        </div>
        <div class="click">click</div>

    </div>
</template>
<style lang="sass" scoped>
@import '@/assets/style/main'

.total
    cursor: pointer
    margin: 0 5px
    width: 210px
    height: 116px
    font-family: "JetBrains Bold", sans-serif
    font-size: 42px


    @include respond-to(sm)
        display: none
    
    .click-unit
        display: flex


            

.title
    display: flex
.total-time
    width: 210px
    height: 44px
    font-family: "JetBrains ExtraLight", sans-serif

.click
    color: #9f9f9f
    display: flex
    justify-content: center
    width: 56px
    height: 18px
    margin: 10px 0
    font-family: "JetBrains ExtraLight", sans-serif
    font-size: 10px
    border: solid 1px
    border-radius: 12px


</style>