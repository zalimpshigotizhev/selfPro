<script setup>
import {Plus, Histogram } from '@element-plus/icons-vue'
// export default {
    
// }
</script>
<template>
    <div class="intensive-block">
        <div class="wrapper">
            <div class="img"></div>
            <div class="name-btns">
                Redis 
                <div class="btns">
                    <el-button type="primary" :icon="Plus"></el-button>
                    <el-button type="primary" :icon="Histogram"></el-button>
                </div>

            </div>
            <div class="total">
                <div class="title">Total</div>
                <div class="total-time">13 h.</div>
                <div class="click">click</div>
            </div>
            <div class="total">
                <div class="title">Month</div>
                <div class="total-time">13 h.</div>
                <div class="click">click</div>
            </div>
            <div class="week">
                week
                <div class="week-days">
                    <div  class="day">
                        <div class="date">
                            12
                        </div>
                        <div class="indicator">
            
                        </div>
                    </div>
                    <div  class="day">
                        <div class="date">
                            12
                        </div>
                        <div class="indicator">
            
                        </div>
                    </div>
                    <div  class="day">
                        <div class="date">
                            12
                        </div>
                        <div class="indicator">
            
                        </div>
                    </div>
                    <div  class="day">
                        <div class="date">
                            12
                        </div>
                        <div class="indicator">
            
                        </div>
                    </div>
                    <div  class="day">
                        <div class="date">
                            12
                        </div>
                        <div class="indicator">
            
                        </div>
                    </div>
                    <div  class="day">
                        <div class="date">
                            12
                        </div>
                        <div class="indicator">
            
                        </div>
                    </div>
                    <div  class="day">
                        <div class="date">
                            12
                        </div>
                        <div class="indicator">
            
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="sass" scoped>
@import '../../assets/style/main'
@import '../../assets/style/indicator-day'

.intensive-block
    display: flex
    align-items: center
    background-color: white
    width: 1250px
    height: 295px
    border-radius: 10px
        

.wrapper
    display: flex
    align-items: center



    .img
        width: 360px
        height: 160px
        margin: 50px
        border-radius: 8px
        background: url("../../assets/img/redis.png")
        background-size: cover
        background-position: center center
        background-repeat: no-repeat
    
    .name-btns
        display: flex
        flex-direction: column
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
    
    .total
        cursor: pointer
        margin: 0 5px
        width: 210px
        height: 116px
        font-family: "JetBrains Bold", sans-serif
        font-size: 42px

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


.week
    display: flex
    flex-direction: column
    align-items: center
    font-family: "JetBrains ExtraLight", sans-serif
    font-size: 10px 
    width: 45px
    height: 140px

    .week-days
        display: flex
        flex-wrap: wrap

                    

</style>