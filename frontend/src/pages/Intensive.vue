<script setup>
import Header from 'components/Header.vue'
import IntensiveBlock from 'components/intensive/IntensiveBlock.vue'


</script>
<template>
    <Header/>
    <div class="intensive">
        <div class="block">
            <div class="title">Intensive</div>
            <div class="btns">
                <el-button type="success" round class="first">add</el-button>
                <el-button type="danger" round class="second">list</el-button>
            </div>
            
        </div>
        <IntensiveBlock/>
    </div>
</template>
<style lang="sass" scoped>
@import '../assets/style/main'

.intensive
    display: flex
    flex-direction: column
    padding-bottom: 100px


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
            
            .first
                background-color: #247531

                &:hover,
                &:active
                    background-color: #449050
            
            .second
                background-color: #C18C26

                &:hover,
                &:active
                    background-color: #DBA948
        
</style>