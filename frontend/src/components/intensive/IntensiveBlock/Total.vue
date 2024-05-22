<script setup>
import { useRootStore } from '@/stores/root';
import { storeToRefs } from 'pinia';

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
    }
})


</script>
<template>
    <div class="total">
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

        <div class="total-time">13 h.</div>
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