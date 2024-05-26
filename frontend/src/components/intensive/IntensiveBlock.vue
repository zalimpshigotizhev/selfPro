<script setup>
import {Plus, Histogram } from '@element-plus/icons-vue'
import { useRootStore } from '@/stores/root';
import { storeToRefs } from 'pinia';
import {normalizeColor, getText} from '../../scripts/main.js'
import Button from './IntensiveBlock/Button.vue';
import Total from './IntensiveBlock/Total.vue';
import Week from './IntensiveBlock/Week.vue';

const rootStore = useRootStore()
const { tip } = storeToRefs(rootStore)

const props = defineProps({
    data:{
        type: Object,
        require: true
    }
})


const name = getText(props.data.name, 7)



const rgbaColor = normalizeColor(props.data.color)

</script>
<template>
    <div class="intensive-block" :style="`background-color: ${rgbaColor};`">
        <div class="wrapper">
            <div class="img"></div>
            <div class="info">
                <div class="name-btns">

                    <VTooltip>
                        <p class="name">{{ name }}</p>
                        <template #popper>
                            <div class="tip">
                                {{ data.name }} 
                            </div>
                        </template>
                    </VTooltip>

                    <div class="btns">
                        <Button
                        :icon="Plus"
                        
                        />
                        <Button
                        :icon="Histogram"
                        />
                    </div>
                </div>
                <div class="totals">
                    
                    <Total 
                    class="tot"
                    :name="'Total'" 
                    :gifUrl="'.\\src\\assets\\img\\steve.gif'"
                    :text="'Сколько вы занимались за все время.'"
                    :data="data.total"/>

                    <Total 
                    class="tot"
                    :name="'Month'"
                    :gifUrl="'.\\src\\assets\\img\\calendar.gif'"
                    :text="'Сколько вы занимались за месяц.'"
                    :data="data.total_m"
                    />
                </div>
                
                <Week
                :gifUrl="'.\\src\\assets\\img\\cat.gif'"
                :week="data.week"
                />
            </div>
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'

.intensive-block
    display: flex
    align-items: center
    background-color: white
    max-width: 1250px
    max-height: 490px
    min-height: 260px
    border-radius: 10px

    &:not(:last-child)
        margin-bottom: 30px
        

.wrapper
    display: flex
    align-items: center
    flex-wrap: wrap
    @include respond-to(sm)
        padding-bottom: 30px 

    .totals
        display: flex
        .tot
            &:nth-child(1)
                @include respond-to(md)
                    display: none
            &:nth-child(2)
                @include respond-to(lg)
                    display: none

    .info
        display: flex

        @include respond-to(sm)
            width: 90%
            justify-content: center
            padding-bottom: 30px

    .img
        max-width: 360px
        min-width: 260px
        max-height: 160px
        min-height: 116px
        margin: 50px
        border-radius: 8px
        background: url("../../assets/img/redis.png")
        background-size: cover
        background-position: center center
        background-repeat: no-repeat

        
    
    .name-btns
        @include flex-column
        justify-content: space-around
        

        .name
            margin: 0
            font-family: "JetBrains Medium"
            font-size: 35px
            width: 230px

        @include respond-to(sm)

        .btns
            .el-button
                padding: 20px 25px
                border: none

                &:first-child
                    background: rgb(34,193,195)
                    background: linear-gradient(160deg, rgba(34,193,195,1) 14%, rgba(6,185,48,1) 100%)

                    &:hover,
                    &:active
                        background: rgb(34,193,195)
                        background: linear-gradient(160deg, rgba(34,193,195,0.6) 14%, rgba(6,185,48,0.6) 100%)
                
                &:last-child
                    background: rgb(110,59,32)
                    background: linear-gradient(142deg, rgba(110,59,32,1) 0%, rgba(132,103,85,1) 100%)

                    &:hover,
                    &:active
                        background: rgb(110,59,32)
                        background: linear-gradient(142deg, rgba(110,59,32,1) 0%, rgba(132,103,85,1) 60%)
    





                    

</style>