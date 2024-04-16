# MEC App


## MEC Apps
### Create a MEC App and a MEC App Descriptor
### Instantiate a MEC App
### Deploy a MEC App
### Update a MEC APP
### Terminate a MEC APP


## MEC App Descriptor Fields

- mec-appd
  - id
  - name
  - provider
  - soft-version
  - version
  - mec-version
  - info-name
  - description

- virtual-compute
  - id
  - logical-node-reqs
    - id
    - logical-node-requirement-details
      - key
      - value
  - request-additional-capabilities
    - name
    - support-mandatory
    - min-requested-additional-capability-version
    - preferred-requested-additional-capability-version
    - target-performance-parameters
      - key
      - value
  - compute-requirements
    - key
    - value

- virtual-memory
  - mem-size
  - mem-oversubscription-policy
  - vdu-mem-requirements
    - key
    - value
  - numa-enabled

- virtual-cpu
  - architecture
  - cpu-count
  - cpu-clock
  - cpu-oversubscription-policy
  - vdu-cpu-requirements
    - key
    - value
  - cpu-pinning
    - pinning-policy
    - pinning-rule
      - key
      - value

- virtual-disk:
  - id: 
  - size-of-storage
  - vdu-storage-requirements
    - key: 
    - value
  - rdma-enabled
  - sw-image-id

- sw-image
  - id
  - name
  - version
  - checksum
  - container-format
  - disk-format
  - min-disk
  - min-ram
  - size
  - sw-image
  - operating-system
  - supported-virtualisation-environment

- virtual-storage:
  - id: 
  - type-of-storage: 
    - block-storage:
        - size-of-storage: 
        - vdu-storage-requirements:
            - key: 
              value: 
        - rdma-enabled: 
        - sw-image-id: 
    - object-storage:
        - max-size-of-storage: 
    - file-storage:
        - size-of-storage: 
        - file-system-protocol: 
        - int-virtual-link-id: 
    - nfvi-maintenance-info:
        - impact-notification-lead-time: 
        - is-impact-mitigation-requested: 
        - supported-migration-time: 
        - max-undetectable-interruption-time: 
        - min-recovery-time-between-impacts: 
        - max-number-of-impacted-instances:
            - id: 
            - group-size: 
            - max-number-of-impacted-instances: 

- ext-cpd
  - id
  - k8s-cluster-net
  - virtual-network-interface-requirements
    - id
    - name
    - description
    - support-mandatory
    - network-interface-requirements
      - key
      - value
    - niclo-requirements
      - id
      - logical-node-requirement-details
        - key
        - value
  - layer-protocol
  - cp-role
  - description
  - trunk-mode
  - security-group-rule-id
  - cp-protocol
    - associated-layer-protocol
    - address-data
      - id
      - address-type
      - l2-address-data
      - l3-address-data
        - ip-address-assignment
        - ip-address-type
        - number-of-ip-addresses
        - floating-ip-activated
        - fixed-ip-address

- service-required
  - name
  - category
    - href
    - id
    - name
    - version
  - version
  - transport-dependencies
    - id
    - transport
      - name
      - description
      - type
      - protocol
      - version
      - security
        - oauth2-info
          - grant-types
          - token-endpoint
    - serializers
    - labels
  - requested-permissions

- service-optional
  - name
  - category
    - href
    - id
    - name
    - version
  - version
  - transport-dependencies
    - id
    - transport
      - name
      - description
      - type
      - protocol
      - version
      - security
        - oauth2-info
          - grant-types
          - token-endpoint
    - serializers
    - labels
  - requested-permissions

- service-produced
  - name
  - category
    - href
    - id
    - name
    - version
  - version
  - transports-supported
    - id
    - transport
      - name
      - description
      - type
      - protocol
      - version
      - security
        - oauth2-info
          - grant-types
          - token-endpoint
    - serializers
    - labels

- feature-required
  - name
  - version

- feature-optional
  - name
  - version

- transport-dependencies
  - id
  - transport
    - name
    - description
    - type
    - protocol
    - version
    - security
      - oauth2-info
        - grant-types
        - token-endpoint
  - serializers
  - labels

- traffic-rule
  - id
  - filter-type
  - priority
  - traffic-filter
    - id
    - src-address
    - dst-address
    - src-port
    - dst-port
    - protocol
    - tag
    - uri
    - packet-label
    - src-tunnel-address
    - tgt-tunnel-address
    - tgt-tunnel-address
    - src-tunnel-port
    - dst-tunnel-port
    - qci
    - dscp
    - tc
  - action
  - dst-interface
    - id
    - interface-type
    - tunnel-info
      - tunnel-type
      - tunnel-dst-address
      - tunnel-src-address
    - src-mac-address
    - dst-mac-address
    - dst-ip-address

- dns-rule
  - id
  - domain-name
  - ip-address-type
  - ip-address
  - ttl

- latency
  - max-latency

- terminate-app-instance-op-config
  - min-graceful-termination-timeout
  - max-recommended-graceful-termination-timeout
  - vnf-parameters
    - key
    - value

- change-app-instance-state-op-config
  - min-graceful-stop-timeout
  - max-recommended-graceful-stop-timeout
  - vnf-parameters
    - key
    - value

- user-context-transfer-capability
  - stateful-application
  - user-context-transfer-support

- network-policy
  - steered-network
    - cellular-network
    - wifi-network
    - fixed-access-network

- artifacts
  - name
  - description
  - type
  - file




