# goals
- practice devops practices 
1. build images and publish to acr -> build the web app from acr
2. deploy to staging server -> swap with gradual rollout -> initially split the traffic

[x] just created a new finction app -> container-func-westeu-dev
[x] configured with both user assigned managed identiry and system asssigned identity with roele asignments for staroage and app insights iwth blob data cintaributeor and monitoring data publisher respectively
[x] user assigned managed identity -> user-assigned-identity-for-container-func-westeu-dev

next step

-> http triggered finction app wdeployed from acr using github actions 
