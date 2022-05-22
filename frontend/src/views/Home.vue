<template>
  <div class="home">
    <div class="mb-4 border-b border-gray-100 flex justify-end px-4">
      <router-link to="/create">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
          </svg>
      </router-link>
    </div>
    <!-- v-for show data column -->
    <div class="px-1">
        <router-link :to="`/modify/${item['id']}`" v-for="(item, index) in data" :key="index">
            <div class="grid grid-cols-12 bg-blue-100
                rounded-lg shadow-lg h-16 font-bold mb-4" 
            >
                <div class="col-span-2">
                    <h3 class="text-xs md:text-lg px-2 py-1">{{item['subject_name']}}</h3>
                </div>
                <div class="col-span-4 text-xs ml-4 md:text-sm">
                    <p>{{item['hw_detail']}}</p>
                </div>
                <div class="col-span-4 text-xs md:text-base">
                    <p>{{item['reminding_date'] + ' ' + item['reminding_time']}}</p>
                </div>
                <div class="col-span-2 text-sm md:text-lg">
                    {{item['pages']}}
                </div>
            </div>
        </router-link>
    </div>
  </div>
</template>

<script>
import { inject, ref } from 'vue'
import api_addr from '../api/ip.js'

export default {
  setup() {
    const ip = `${api_addr}/info`
    const axios = inject('axios')
    let data = ref([])
    axios.get(ip)
    .then( response => {
      data.value = response.data 
    })

    return {
      data: data,
    }
  }
}
</script>