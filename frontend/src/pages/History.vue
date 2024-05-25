<script setup>
import {
  Search,
} from '@element-plus/icons-vue'
import Header from 'components/Header.vue';4
import history from './dataset/history.json'
import HistoryBlock from 'components/history/HistoryBlock.vue';
import { useRoute, useRouter } from 'vue-router';
import { ref }  from 'vue';

const date = ref('')
const search = ref('')
const router = useRouter();


function goBack(){
    router.go(-1)
}

</script>
<template>
    <Header/>
    <div>
        <div class="block">
            <div class="title">History</div>
            <div class="btns">
                <el-button type="danger" round class="second" @click="goBack()">back</el-button>
            </div>
        </div>
        <div class="history-list">
            <div class="filters">
                <el-input
                v-model="search"
                style="width: 240px"
                class="search-input mr10px"
                placeholder="Type something"
                :prefix-icon="Search"
                />
                
                <div class="date-select mr10px">
                    <el-date-picker
                    v-model="date"
                    type="daterange"
                    range-separator="To"
                    start-placeholder="Start date"
                    end-placeholder="End date"
                    />
                </div>
                <el-button 
                :icon="Search" 
                circle 
                />
            </div>
            <HistoryBlock
            v-for="h in history.data"
            :key="key"
            :history="h"

            />
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '../assets/style/main'

.title
    font-family: "JetBrains ExtraBold", sans-serif
    font-size: 64px

    @media (min-width: $min_mobile) and (max-width: $max_mobile)
        font-size: 44px

.block
    display: flex
    align-items: center
    margin-bottom: 40px
    @media (min-width: $min_mobile) and (max-width: $max_pad)
        margin-bottom: 20px
        flex-direction: column
        align-items: flex-start

    .btns
        display: flex

        button

            margin-left: 30px
            padding: 23px 25px
            font-family: "JetBrains ExtraLight", sans-serif
            font-size: 25px

            @media (min-width: $min_mobile) and (max-width: $max_pad)
                margin: 10px
                margin-right: 30px
                margin-left: 0

        .second
            background-color: #633A34
            border: none

            &:hover,
            &:active
                background-color: #844e46

.history-list
    display: flex
    flex-direction: column
    align-items: center
    padding-top: 1em
    background-color: #ffffff
    width: 100%
    height: 1000px
    border-radius: 30px

.filters
    display: flex
    flex-wrap: wrap
    justify-content: center
    align-items: center
    width:100%
    height: 138px
    margin-bottom: 20px


    .search-input
        height: 32px
    
    .mr10px
        margin-right: 10px
        

</style>