<template>
    <form class="flex justify-center mt-10 py-16 bg-blue-200 mx-10 rounded-3xl shadow-xl">
        <div class="transform scale-125">
            <div>
                <label for="subject_name" class="rounded-lg text-lg">科目名稱</label>
                <br>
                <select name="subject_name"
                        v-model="data['subject_name']"
                        id="subject_select"
                        class="block mt-1 rounded-lg w-52"
                >
                    <option v-for="(item, index) in subject_names_list" :key="index">
                        {{item['subject_name']}}
                    </option>
                </select>
            </div>

            <div class="mt-1">
                <label for="detail">細節</label>
                <input type="text" name="detail" v-model="data['hw_detail']" 
                    class="mb-1 px-3 rounded-lg block w-52"
                >
                <div class="mb-1 block">
                    <label class="mr-2 rounded">頁面</label>
                    <br>
                    <select name="paegs-from" v-model.number="nubmer_list['from']"
                            class="mr-1 rounded"
                    >
                        <option disabled>空</option>
                        <option v-for="i in 1000" :key="i">
                            {{i}}
                        </option>
                    </select>
                    <span>-</span>
                    <select name="pages-to" class="ml-1"
                            v-model.number="nubmer_list['to']"
                    >
                        <option disabled>空</option>
                        <option v-for="i in 1000" :key="i">
                            {{i}}
                        </option>
                    </select>
                </div>

                <div class="block">
                    <label for="reminding_time_date">日期</label>
                    <br>
                    <input type="date" name="reminding_time_date" class="rounded"
                    >
                    <br>
                    <label for="reminding_time_time">時間</label>
                    <br>
                    <input type="time" name="reminding_time_time" class="rounded"
                            v-model="data['reminding_time']"
                    >
                </div>
                <button @click="modifySubjectInfo" class="bg-green-600 mr-4 mt-2 h-10 w-20 rounded-lg">
                    送出
                </button>
                <button @click="deleteSubjectInfo" class="bg-red-600 ml-2 mt-2 h-10 w-20 rounded-lg">
                    刪除
                </button>
            </div>
        </div>
    </form>
</template>

<script>
import { ref, reactive , inject } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import api_addr from '../api/ip.js'

export default {
    setup() {
        const axios = inject('axios')
        const router = useRouter()
        const route = useRoute()
        const ip = [`${api_addr}/modify/${route.params.id}`, `${api_addr}/subject_names_list`]

        
        const data = reactive({
            "subject_name": "",
            "hw_detail": "",
            "pages": "",
            "reminding_time": "",
            "reminding_date": ""
        })

        let subject_names_list = ref([])

        let nubmer_list = reactive({
            "from": 1,
            "to": 1
        })

        axios.get(ip[0])
        .then( response => {
            data['subject_name'] = response.data['subject_name']
            data['hw_detail'] = response.data['hw_detail']
            data['pages'] = response.data['pages']
            data['reminding_time'] = response.data['reminding_time']
            data['reminding_date'] = response.data['reminding_date']
            nubmer_list['from'] = data['pages'].split('-')[0]
            nubmer_list['to'] = data['pages'].split('-')[1]
        })

        axios.get(ip[1])
        .then(response => {
            subject_names_list.value = response.data
        })

        async function modifySubjectInfo() {
            router.push('/')
            await axios.put(ip[0], {
                data: {
                    "name": data['subject_name'],
                    "detail": data['hw_detail'],
                    "pages": nubmer_list['from'] + '-' + nubmer_list['to'],
                    "reminding_time": data['reminding_time'],
                    "reminding_date": data['reminding_date']
                }
            })
        }

        async function deleteSubjectInfo() {
            router.push('/')
            await axios.delete(ip[0])
        }
        
        return {
            data: data,
            modifySubjectInfo: modifySubjectInfo,
            deleteSubjectInfo: deleteSubjectInfo,
            subject_names_list: subject_names_list,
            nubmer_list: nubmer_list,
        }
    },
}
</script>

<style>

</style>