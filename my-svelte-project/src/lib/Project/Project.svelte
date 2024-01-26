

<script lang="ts">
    // @ts-ignore
    let project = {
      "id": 1,
      "name": "Project Gamma",
      "description": "Aenean sit amet ligula id nulla euismod eleifend vel nec orci.",
      "start_date": "2024-05-01",
      "end_date": "2024-12-31",
      "status": "completed",
      "budget": "100000.00",
      "cost_to_date": "80000.00",
      "project_manager": "Robert Johnson",
      "created_at": "2024-01-26T11:04:17.944315Z",
      "updated_at": "2024-01-26T11:04:17.944315Z"
    };
   
  </script>
  
 
  
  <div class="card">
    <div class="pricing-block-content">
      <p class="pricing-plan">{project.name}</p>
      <div class="price-value" data-currency="$ USD" data-currency-simple="USD">
        <p class="price-number">${project.budget}</p>
        <div id="priceDiscountCent">/project</div>
      </div>
      <div class="pricing-note">Status: {project.status}</div>
      <ul class="check-list" role="list">
        
      </ul>
    </div>
  </div>
  
  

<style>

    /*Neo Brutalism pricing card*/
.card {
  width: 190px;
  background: #00ffa0;
  padding: 1rem;
  border-radius: 1rem;
  border: 0.5vmin solid #05060f;
  box-shadow: 0.4rem 0.4rem #05060f;
  overflow: hidden;
  color: black;
}

/*Card content*/
.pricing-block-content {
  display: flex;
  height: 100%;
  flex-direction: column;
  gap: 0.5rem;
}

.pricing-plan {
  color: #05060f;
  font-size: 1.3rem;
  line-height: 1.25;
  font-weight: 700;
}

.price-value {
  display: flex;
  color: #05060f;
  font-size: 1.8rem;
  line-height: 1.25;
  font-weight: 700;
}

.pricing-note {
  opacity: 0.8;
}

/*Checklist*/
.check-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.check-list-item {
  display: flex;
  align-items: center;
  gap: 4px;
}

</style>