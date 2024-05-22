<script setup>
import {Plus, Histogram } from '@element-plus/icons-vue'
import { useRootStore } from '@/stores/root';
import { storeToRefs } from 'pinia';

import Button from './IntensiveBlock/Button.vue';
import Total from './IntensiveBlock/Total.vue';
import Week from './IntensiveBlock/Week.vue';
const rootStore = useRootStore()
const { tip } = storeToRefs(rootStore)

</script>
<template>
    <div class="intensive-block">
        <div class="wrapper">
            <div class="img"></div>
            <div class="name-btns">
                Redis 
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
                :name="'Total'" 
                :gifUrl="'.\\src\\assets\\img\\steve.gif'"
                :text="'Сколько вы занимались за все время.'"
                />
    
                <Total 
                :name="'Month'"
                :gifUrl="'.\\src\\assets\\img\\calendar.gif'"
                :text="'Сколько вы занимались за месяц.'"
                />
            </div>
            
            <Week
            :gifUrl="'.\\src\\assets\\img\\cat.gif'"
            />
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
    height: 295px
    border-radius: 10px
    

    &:not(:last-child)
        margin-bottom: 30px
        

.wrapper
    display: flex
    align-items: center

    .totals
        display: flex
        


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
        font-family: "JetBrains Medium"
        font-size: 42px
        width: 230px
        height: 160px

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