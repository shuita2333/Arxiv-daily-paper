# 📦 其他研究 | 2026年06月11日

> 本类共 **269** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-269](./part-06.md)

---

### 151. [A Hybrid Edge-Cloud Architecture for Low-Latency Entitlement Verification in Resource-Constrained Devices](https://arxiv.org/abs/2606.10536)

**<font color=#1a73e8>作者：</font>** Pravin Nagare, Aditya Sabbineni, Devendra Dahiphale 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As digital media consumption shifts toward large-scale Over-the-Top (OTT) platforms, the efficiency of the control plane, specifically entitlement and identity verification, has become a critical factor in user experience. Current architectures often rely on synchronous cloud-tethered validation flows that introduce significant latency, especially on resource-constrained consumer electronics. This paper proposes a Hybrid Edge-Cloud Entitlement Framework designed to minimize user-perceived friction. By implementing a secure, local caching layer within device middleware and utilizing an Adaptive Entitlement Cache with Proactive Refresh (AEC-PR) algorithm, we decouple the user interaction from backend network variability. We evaluate the performance on ARM Cortex-A series hardware, demonstrating that localized cryptographic verification reduces authorization latency from a mean of 422.8ms to 18.4ms (a 95.6% reduction) while mitigating implementation-level side-channel risks through deterministic Ed25519 arithmetic and TEE isolation.

---


### 152. [GRAR: Glass-induced Reflection Artifact Removal in LiDAR Point Clouds](https://arxiv.org/abs/2606.10541)

**<font color=#1a73e8>作者：</font>** Wanpeng Shao, Zeyi Guo, Bo Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Terrestrial Laser Scanning (TLS) point clouds captured in urban environments frequently suffer from glass-induced reflection artifacts, severely degrading downstream applications. Existing reflection artifact removal methods generally rely on ideal reflection symmetry assumptions, yet their performance is limited by inaccurate glass estimation and insufficient geometric representations. To address these issues, we propose a novel unified framework aimed at robust reflection artifact removal: In the first stage, we leverage a multi-modal vision foundation model to produce initial glass masks, which are then refined using geometric cues to achieve high-precision glass regions, followed by glass completion to recover missing regions caused by no-return measurements on transparent surfaces; In the second stage, we propose a physics-driven descriptor, termed Reflection-aware Local-Global Geometric Similarity (RE-LGGS), which is grounded in actual laser reflection geometry and jointly encodes multi-scale geometric structures and orientation consistency using PCA-based local shape representations, thereby significantly improving robustness against imperfect observations. Extensive experiments on multiple public TLS datasets demonstrate that our framework consistently outperforms state-of-the-art methods in reflection artifacts removal.

---


### 153. [Flexible Flows for Biological Sequence Design](https://arxiv.org/abs/2606.10543)

**<font color=#1a73e8>作者：</font>** Yogesh Verma, Dani Korpela, Harri Lähdesmäki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing functional biological sequences requires navigating vast discrete spaces under strict evolutionary and biophysical constraints. Discrete Flow Matching (DFM) offers a generative framework over such spaces, but existing approaches rely on biologically uninformative couplings and offer limited flexibility for variable-length sequence generation and fine-grained control. We propose a structured coupling that encodes domain-specific preferences among sequence elements, biasing the source distribution toward plausible regions without modifying the flow objective or training procedure. Building on this, we introduce a latent edit-based rate parameterization that models variable-length generation via edit operations conditioned on a shared global latent, akin to a latent variable model, while remaining tractable. We further introduce a latent classifier-free guidance mechanism that steers generation coherently in continuous latent space, along with Dirichlet-prior temperature scaling for test-time control over edit operations. Our method achieves state-of-the-art performance across diverse biological sequence tasks, including density estimation, unconditional and conditional DNA sequence generation, and peptide sequence generation.

---


### 154. [PrismAvatar: Pseudo-Multiview Reconstruction and Subpixel Prism Rendering for Real-Time Stereoscopic Communication](https://arxiv.org/abs/2606.10550)

**<font color=#1a73e8>作者：</font>** Chufeng Fang, Dongdong Teng, Lilin Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time stereoscopic video communication has long been a goal of immersive telepresence, yet practical systems still require specialized capture rigs or reduce remote users to a single portrait view. We present PrismAvatar, a Gaussian head-avatar system that connects monocular avatar capture with subpixel-encoded glasses-free lenticular display for real-time autostereoscopic communication. From a monocular portrait video, PrismAvatar reconstructs a controllable head avatar and optimizes it for the lateral viewing zones induced by the display. The method uses natural head turns as pseudo-multiview (PMV) supervision to constrain regions that are otherwise weakly observed in monocular training, including hair, ears, jaw contours, and neck boundaries. Reliable side frames are yaw-binned, aligned to virtual cameras, and supervised within a strict head-and-hair domain; contour-aware losses and staged regularization further suppress ghosting, alpha leakage, and depth instability while preserving lateral detail. At runtime, PrismAvatar renders 32 virtual views and encodes them into a 4K lenticular raster with calibrated subpixel-routing masks. The live-tracker prototype sustains 10.65 FPS, and a subject-specific distilled driver raises the same display pipeline to 38.49 FPS.

---


### 155. [Benchmarking Knowledge Editing using Logical Rules](https://arxiv.org/abs/2606.10554)

**<font color=#1a73e8>作者：</font>** Tatiana Moteu Ngoli, NDah Jean Kouagou, Hamada M. Zahera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in real-world applications that require access to up-to-date knowledge. However, retraining LLMs is computationally expensive. Therefore, knowledge editing techniques are crucial for maintaining current information and correcting erroneous assertions within pre-trained models. Current benchmarks for knowledge editing primarily focus on recalling edited facts, often neglecting their logical consequences. To address this limitation, we introduce a new benchmark designed to evaluate how knowledge editing methods handle the logical consequences of a single fact edit. Our benchmark extracts relevant logical rules from a knowledge graph for a given edit. Then, it generates multi-hop questions based on these rules to assess the impact on logical consequences. Our findings indicate that while existing knowledge editing approaches can accurately insert direct assertions into LLMs, they frequently fail to inject entailed knowledge. Specifically, experiments with popular methods like ROME and FT reveal a substantial performance gap, up to 24%, between evaluations on directly edited knowledge and on entailed knowledge. This highlights the critical need for semantics-aware evaluation frameworks in knowledge editing.

---


### 156. [Hidden Consensus:Preference-Validity Compression in Human Feedback](https://arxiv.org/abs/2606.10569)

**<font color=#1a73e8>作者：</font>** Dorcas Chia Ern Chua, Karen Myn Hui Lee, Jia Yue Tan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard RLHF pipelines often reduce heterogeneous human judgments into a single scalar reward target. We argue that this reduction can mis-measure alignment in structurally plural societies, where disagreement may reflect culturally, historically, linguistically, regionally, or normatively grounded interpretations rather than annotation noise. We call this failure Preference-Validity Compression, the collapse of multiple plural-valid response options into a single optimization target. Using Malaysia as a diagnostic setting, we analyze RLHF-style feedback aggregation through preference events linking prompts, responses, and acceptability judgments across interpretive frames. Across 321 preference events from 20 participants and 107 trio-annotated prompts, 79% of prompts contain more than one majority-supported response that single-winner aggregation would discard, and apparent dominance gaps between top responses diminish when all majority-supported options are considered. Participants frequently select multiple acceptable responses, and discarded responses demonstrably reflect coherent local, practical, or cultural frames. These findings show that majority aggregation in this corpus measures argmax acceptability rather than plural alignment. We treat this as a measurement-validity issue and argue that future alignment methods should satisfy Validity-Preserving Consistency, remaining stable across plural-valid interpretive frames rather than collapsing them into a single reward target.

---


### 157. [Convergence of Monte Carlo Optimistic Policy Iteration: Beyond Uniform State-Action Updates](https://arxiv.org/abs/2606.10580)

**<font color=#1a73e8>作者：</font>** Octave Oliviers, Glenn Vinnicombe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The asymptotic behaviour of Monte Carlo optimistic policy iteration (MC-O-PI) is a long-standing open question. When the model of the environment is unknown, as is common in practice, the only known condition that guarantees convergence to optimality is impractical. In its canonical form, this condition requires that the episodes used for policy evaluation be initialised uniformly over the entire state-action space. This paper strictly relaxes that requirement. Specifically, we prove that initial-visit MC-O-PI converges to optimality even when updates are uniform only over the actions within each state. This allows episodes to start in different states at arbitrary frequencies; a realistic implementation when the state space is large or unknown but the action space in each state is manageable. The proof departs from the classical analysis of Tsitsiklis whose central commutativity argument no longer applies when states are updated at different frequencies. Instead, we first show that the mean-field dynamics of MC-O-PI generate monotonically improving policies when updates are uniform over the actions in each state, and then prove that noise cannot consistently prevent this improvement by extending the lock-in argument of the combined stability-ODE method. This approach suggests a new way to study optimistic policy-iteration algorithms in general.

---


### 158. [Drawing with Strangers: Population Scaling Drives Zero-Shot Mutual Intelligibility in Emergent Sketching](https://arxiv.org/abs/2606.10582)

**<font color=#1a73e8>作者：</font>** Jooyeon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalization in emergent communication has largely focused on novel inputs or linguistic structures, yet the capacity for agents to communicate with strangers from strictly disjoint communities remains relatively unexplored. In this work, we formalize this capability as \textit{zero-shot mutual intelligibility (ZMI)}: successful communication between independently trained populations without prior exposure. Leveraging emergent sketching -- in which agents communicate through sets of drawn strokes -- as a visually grounded modality, we find that scaling the training population substantially improves ZMI across independent groups. Crucially, as we scale the population size, in-group communicative variation increases, preventing co-adaptation into homogeneity. Simultaneously, cross-group variation decreases, indicating a structural convergence toward a certain type of universality. Further analysis reveals that this universality is achieved through perceptual grounding: scaled populations increasingly anchor their emergent sketches on the objective visual resemblance of the target images. Together, these results position ZMI as a distinct axis of generalization in emergent communication and suggest a route toward socially interoperable artificial agents.

---


### 159. [NOVA: Symbolic Regression Discovery of Interpretable Car-Following and Lane-Change Models with Driver Heterogeneity](https://arxiv.org/abs/2606.10583)

**<font color=#1a73e8>作者：</font>** Ishak Abassi, Nassim Ali Bouazzouni, Farah Ibelaiden 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present NOVA, an autonomous symbolic regression framework that identifies interpretable car-following and lane-change structures from raw trajectory data with minimal behavioral priors. Applied to 4,765,788 active driving observations from the NGSIM I-80 and US-101 datasets, NOVA's deterministic Rust-powered search engine evaluates over 10,000 candidate algebraic structures and identifies a compact two-term acceleration model under a forward-shifted rolling-mean prediction target. Evaluated under two complementary preprocessing pipelines, NOVA achieves $RMSE = 1.376 m/s^2$ ($R^2 = 15.57\%$) on the intent-forecasting benchmark, outperforming the best recalibrated symbolic-regression baseline (SR-LLM, PNAS~2025) by 0.135 m/s$^2$ in RMSE under an identical evaluation protocol. Across eight independent experiments, a single dominant nonlinear term emerges as a robust backbone of human car-following; a residual-guided extension further links the selected structure to an established psychophysical theory of collision avoidance. The discovered feature operators transfer zero-shot between freeway sites with under 3 pp $R^2$ loss. Extended to lane-change modelling within a multinomial logit framework, NOVA achieves 67.4\% balanced accuracy under strict vehicle-ID holdout on 502 unseen drivers, surpassing existing lane-changing baselines by +29.8 percentage points on a three-class problem.

---


### 160. [Dirichlet-Guided Group Forecasting for Alleviating Over-smoothing in Time Series Forecasting](https://arxiv.org/abs/2606.10592)

**<font color=#1a73e8>作者：</font>** Xingyu Zhang, Jingyao Wang, Xin Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting often suffers from over-smoothing, especially when future dynamics are multi-modal. Forecasts may follow the coarse trend of the observed future, but fail to preserve sharp changes, oscillations, turning points, and regime transitions that define plausible dynamic evolution. In this work, we revisit over-smoothing from the perspective of latent dynamical mode compression: under partial observation and single-realization supervision, multiple plausible future modes can be weakened, merged, or averaged during forecasting. Based on this view, we propose Dirichlet-Guided Group Forecasting (DGF), a mode-preserving forecasting framework that explicitly models multiple mode-conditioned predictive distributions and uncertainty over their selection probabilities. DGF uses a Dirichlet-guided hierarchical sampling mechanism and reward-based optimization to encourage forecasts that are accurate, dynamically consistent, and mode-distinct. Extensive experiments on real-world forecasting benchmarks show that DGF reduces over-smoothing while improving forecasting accuracy, diversity, and dynamical consistency.

---


### 161. [From Data Heterogeneity to Convergence: A Data-Centric Review of Federated Learning](https://arxiv.org/abs/2606.10595)

**<font color=#1a73e8>作者：</font>** Huong Nguyen, Mickaël Bettinelli, Amirhossein Ghaffari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) has emerged as a promising solution for data hunger in centralized learning. This paradigm enables privacy with multiple clients to train a shared-task model collaboratively without exposing their local data. While being a key component in any learning system, data is also a primary source of vulnerabilities and challenges, and a major determinant of a stable and well-converged training. Existing FL reviews describe general foundations, security practices, opportunities, challenges, and applications, without delving into diverse aspects of data and considering problems from the data perspective. They rarely provide a data-lens synthesis that links concrete data properties, split protocols, and defenses to convergence speed and stability. This survey fills that gap with three advances. First, we analyze non-IID into measurable traits and rank their influence on convergence as strong, medium, or light, explaining the mechanisms behind each and reconciling evidence across images, texts, and graphs. Second, we connect experimental splitting practices to the real phenomena they emulate, expose the artifacts they introduce, and show how those artifacts affect target accuracy. Third, we analyze how data-related vulnerabilities and their proposed defenses affect convergence, reporting performance under clean and adversarial conditions to make the convergence-robustness trade-off explicit. To our knowledge, this is the first survey to provide a complete understanding of data-related challenges that govern FL. With clear takeaways distilled for each concern, our work serves as actionable guidance, helping practitioners design their system with predictable convergence and stability.

---


### 162. [Embedding Hybrid Systems into Continuous Latent Vector Fields](https://arxiv.org/abs/2606.10596)

**<font color=#1a73e8>作者：</font>** Sangli Teng, Hang Liu, Koushil Sreenath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work proves that an $n$-dimensional hybrid system can be embedded into an $m$-dimensional Euclidean space equipped with a continuous vector field on its embedded image whenever $m>2n$. This result suggests that an intrinsically discontinuous hybrid system generically admits a continuous extrinsic representation that is well-posed for differentiable optimization. Building on this existence theorem, we show that a latent Neural ODE with consistency loss in both the latent and state space can accurately recover the flow of hybrid systems. Extensive experiments suggest the proposed method outperforms the existing method in learning hybrid systems with varying geometries from only time series data.

---


### 163. [Geometry-Aware Reinforcement Learning for 2D Irregular Nesting](https://arxiv.org/abs/2606.10611)

**<font color=#1a73e8>作者：</font>** Auguste Lehuger, Guillaume Henon-Just  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional heuristic solvers for the 2D irregular nesting problem share a fundamental limitation: they are blind to polygon geometry, relying on guided brute-force to navigate the continuous placement space with minimal geometrical guidance. In this paper, we argue that Reinforcement Learning is uniquely positioned to overcome this bottleneck. By pairing an optimization policy with a geometry-aware neural encoder, an agent can automatically discover rich geometric priors directly from data, utilizing these learned intuitions to strategically guide exploration. To realize this, we introduce the Polygons Transformer (PoT), a novel architecture that encodes 2D continuous vector geometries while allowing cross-polygons attention. We couple this novel architecture with a Combinatorial Optimization Reinforcement Learning (CORL) training framework to find optimal solutions. To support this paradigm, we release an open-source training dataset derived from complex geographic contours alongside a dedicated evaluation benchmark. Our empirical validation demonstrates that our trained agent achieves area utilization performance highly competitive with Sparrow, the state-of-the-art heuristic solver, proving that reinforcement learning can successfully discover and exploit geometric awareness for precise spatial tasks.

---


### 164. [Fast and Highly Expressive Policy Learning for Offline Reinforcement Learning via Bootstrapped Flow Q-Learning](https://arxiv.org/abs/2606.10613)

**<font color=#1a73e8>作者：</font>** Thanh Nguyen, Tri Ton, Hongbin Choe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based Q-learning has emerged as a powerful paradigm for offline reinforcement learning, but its reliance on multi-step denoising makes both training and inference computationally expensive and brittle. Recent efforts to accelerate diffusion Q-learning toward single-step action generation typically introduce auxiliary networks, policy distillation, or multi-phase training, which frequently compromise simplicity, stability, or performance. To address these limitations, we introduce Bootstrapped Flow Q-Learning (BFQ), a novel framework that enables accurate single-step action generation during both training and inference, without auxiliary networks or distillation procedures. BFQ adopts a divide-and-conquer view of the displacement vector along the flow path: it begins by learning short-range displacements that can be accurately estimated from the Flow Matching marginal velocity, and bootstraps these components to directly learn a noise-to-action mapping in a single step. This formulation eliminates multi-step denoising, resulting in a learning procedure that is substantially faster, simpler, and more robust. Extensive D4RL evaluations show that BFQ improves performance while significantly reducing computational cost compared to multi-step diffusion baselines, demonstrating that single-step action generation suffices for high-performance offline Reinforcement Learning.

---


### 165. [Two-Way Confidential VMs (2cVM): Collaborative Confidential Computing for Mutually Distrustful Parties](https://arxiv.org/abs/2606.10615)

**<font color=#1a73e8>作者：</font>** Jordi Thijsman, Merlijn Sebrechts, Stefan Lefever 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Collaborative computation across organizations is often constrained by the need to process sensitive data and proprietary code without exposing them to untrusted infrastructure or participants. Cryptographic approaches such as fully homomorphic encryption and secure multi-party computation provide strong confidentiality but remain impractical for general workloads due to their extreme computational cost. We present the Two-Way Confidential Virtual Machine (2cVM), a two-layer architecture that pairs a hardware trusted execution environment with an intra-workload isolation layer. Unlike regular Confidential Virtual Machines, 2cVM enforces mutual isolation between co-resident workloads, ensuring that participants retain control over their data and code. All computation in 2cVM is governed by a Commitment Manifest that enumerates participants, component composition, permitted data channels, and authorized outputs; the manifest is locked to the VM and incorporated into attestation evidence, making the policy immutable and independently verifiable throughout the VM's lifetime. A proof-of-concept realization combines AMD SEV-SNP for hardware protection with the WebAssembly Component Model for fine-grained sandboxing of participant code. Evaluation on commodity hardware across four benchmark classes shows that the two isolation layers do not accumulate linearly: once a workload executes inside the WebAssembly sandbox, the marginal cost of enabling hardware memory protection is small. Overhead is workload-dependent, governed primarily by memory access pattern, ranging from negligible for sequential workloads to approximately 2x for irregular, pointer-chasing access patterns. These results indicate that 2cVM provides a practical and verifiable foundation for privacy-preserving collaborative computation.

---


### 166. [Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents](https://arxiv.org/abs/2606.10616)

**<font color=#1a73e8>作者：</font>** Qingcan Kang, Liu Mingyang, Shixiong Kai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon language agents accumulate observations, reasoning traces, and retrieved facts that exceed their finite context windows, making memory retention a fundamental resource-allocation problem. Existing memory systems improve management through heuristic scoring, retrieval optimization, or learned compression, but largely treat retention as a local decision problem and do not explicitly model its long-term consequences under realistic observability constraints. To fill this gap, we formulate memory retention as a constrained stochastic optimization problem with explicit budget feasibility, evidence utility, and delayed costs including miss penalties, reacquisition delays, and stale-information risk. We then propose OSL-MR (Observability-Safe Learning for Memory Retention), a novel framework that enforces a strict separation between online-observable features and offline-available supervision (OAS). OSL-MR combines an evidence learner trained from realized evidence supervision with a Mixed-Score heuristic that serves both as a deployable online-safe baseline and as a structured inductive prior for learning. The resulting policy learns query-conditioned evidence value directly from interaction data while remaining deployable under the same observability constraints. Experiments on LOCOMO and LongMemEval show that OSL-MR consistently outperforms recency-based methods, Generative Agents-style scoring, and other heuristic baselines, particularly under tight memory budgets. The Mixed-Score prior further improves precision while preserving recall, and sensitivity analysis demonstrates robustness across a wide range of cost configurations.

---


### 167. [SSR-Merge: Subspace Signal Routing for Training-Free LoRA Merging in Diffusion Models](https://arxiv.org/abs/2606.10617)

**<font color=#1a73e8>作者：</font>** Zhengxuan Wei, Yi Dong, Zonghui Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) merging can efficiently combine diverse generative capabilities from multiple trained LoRAs for a diffusion model. However, existing LoRA merging techniques often suffer from severe parameter interference, causing destructive collisions in the shared parameter space. To address this, we propose Subspace Signal Routing (SSR), which resolves interference by routing internal signals instead of performing parameter-space merge. Specifically, SSR first constructs a unified subspace by concatenating candidate LoRAs along the rank dimension. Next, SSR employs an inverse correlation matrix to decorrelate mixed signals within this space. Finally, a directional guide matrix steers these purified signals into their respective task-specific subspaces. We provide a rigorous theoretical analysis proving that SSR aligns with the Ordinary Least Squares (OLS) solution, thereby ensuring mathematical optimality. We utilize the additivity of sufficient statistics to design a streaming algorithm. This enables on-the-fly updates that significantly reduce memory overhead and computation time. Extensive experiments validate that SSR significantly outperforms state-of-the-art methods while maintaining comparable efficiency. Code is available at this https URL.

---


### 168. [snaproot: Decentralized File Integrity Verification Using Blockchain-Anchored Cryptographic Hashing](https://arxiv.org/abs/2606.10625)

**<font color=#1a73e8>作者：</font>** Arslan Brömme, Tarkan Yavas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of digital content has made reliable integrity verification increasingly important. Existing solutions rely either on centralized authorities, which introduce trust dependencies and single points of failure, or on decentralized storage systems that incur prohibitive resource overhead. In this paper, we present snaproot, a lightweight system that implements the hash-anchoring paradigm of Haber and Stornetta on the Solana blockchain to provide efficient, decentralized file integrity verification. snaproot generates a SHA-256 hash of a file and stores it immutably on-chain as a permanent reference record. Verification is performed by recomputing the hash and comparing it to the stored value, yielding a deterministic binary outcome. We describe a four-tier trust architecture comprising three realized tiers and one prospective tier for long-term persistence beyond the lifetime of any single blockchain. We present a formal threat model, a security analysis grounded in the second-preimage resistance of SHA-256, and an empirical evaluation on Solana Devnet across file sizes from 1 KB to 500 MB. A central conceptual contribution is the explicit separation between existence proof, the key-independent claim that a file existed at a given time, and authorship proof, the key-dependent binding between a record and a specific wallet identity. This separation allows existence guarantees to survive key loss while preserving stronger authorship claims where keys are retained. We position snaproot against OpenTimestamps, OriginStamp, and Chainpoint and discuss limitations with respect to pre-registration manipulation and AI-generated content.

---


### 169. [Profy: Interpretable Visualization of Expertise-Dependent Motor Skills Toward Supporting Piano Practice](https://arxiv.org/abs/2606.10627)

**<font color=#1a73e8>作者：</font>** Kazuki Kawamura, Fujiki Nakamura, Hayato Nishioka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The quality of piano performance depends on nuanced timing, articulation, and dynamic control, but practice feedback is often summary-based and hard to act on. We introduce Profy, a weakly supervised system that learns from take-level labels derived from aggregated listener ratings (expert-labeled vs. amateur-labeled) to produce time-aligned highlights for review during piano practice. We collected synchronized 1 kHz key-motion and audio from 73 pianists and used 1,083 valid takes for modeling and evaluation. The model outputs clip-level predictions together with evidence scores on a shared resampled model time base for visualization. On 20 amateur clips from short technique studies annotated by 21 expert pianists, the displayed highlight score aligns with passages that expert pianists marked for review despite training without localized labels (Pearson r=0.61, ROC-AUC 0.75). Rather than summarizing a take with a single global score, Profy helps learners decide where to inspect next by supporting scrubbing, looping, and focused replay of time-localized passages associated with expert-amateur differences.

---


### 170. [Is Fairness Truly Fair? Towards Reliable Lipschitz Fairness in Multi-Task Learning via Fixed-\texorpdfstring{$δ$}{delta} Alignment](https://arxiv.org/abs/2606.10632)

**<font color=#1a73e8>作者：</font>** Junbo Ding, Xin Zang, Chenchen Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lipschitz-style individual fairness formalizes the idea that semantically similar examples should receive similar predictions, but its evaluation in multi-task learning (MTL) can be confounded by method-induced representation scales. This paper identifies threshold confounding: when the auditing tolerance is derived from each model's own representation distances, different algorithms are compared under different semantic thresholds. A threshold-drift analysis further shows how Bias rankings can change and identifies sufficient conditions for ranking preservation.
We propose \textbf{ReLiF}, a reliability-aware framework that separates evaluation-time fixed-$\delta$ auditing from training-time controlled regularization. ReLiF uses a shared reference tolerance for comparable auditing and a violation-rate feedback controller to keep the Lipschitz surrogate active without letting it dominate stochastic training. This work also develops supporting analysis for threshold drift, reference-tolerance selection, and the relationship between the huberized training surrogate and its unsmoothed positive-margin counterpart.
Experiments on clinical time-series benchmarks and NYUv2 (NYU Depth V2) dense prediction show that fixed-$\delta$ auditing exposes utility--fairness trade-offs that method-dependent thresholds can obscure. On NYUv2 with a ResNet50 backbone, ReLiF achieves competitive utility while substantially reducing aligned bias under shared fixed thresholds. On clinical benchmarks, ReLiF yields controlled fairness-regularized trade-offs, while fixed-$\delta$ auditing reveals that task-balancing baselines can sometimes achieve lower bias and that genuine utility--fairness trade-offs persist. These results support fixed-$\delta$ auditing as a semantically consistent protocol for evaluating Lipschitz fairness in MTL.

---


### 171. [ChartLens: A Dual-Branch Framework for Chart Data Correction and Factual Summary Refinement](https://arxiv.org/abs/2606.10640)

**<font color=#1a73e8>作者：</font>** Hao Liu, Ruping Cao, Kun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this report, we present our champion solution for the DataMFM Challenge Track 2: Chart Understanding. This track requires models to recover structured chart data and generate faithful natural-language summaries from chart images. To address the complementary requirements of accurate data extraction and factual narration, we propose ChartLens, a dual-branch framework for chart data correction and summary refinement. ChartLens consists of two key modules: Structure-Aware CSV Verification and Correction (SAVC) and Text-Retention-Guided Summary Refinement (TRSR). SAVC improves the reliability of structured data extraction through verification and correction, while TRSR enhances summary generation by preserving critical textual and numerical evidence from charts. By combining model adaptation, correction-based generation, and OCR-assisted evidence grounding, ChartLens improves both structured data recovery and summary factuality. On the test set, our final system achieves an overall score of 69.10 and ranks first in Track 2, demonstrating its effectiveness for accurate chart understanding. Our code will be released at: this https URL.

---


### 172. [PhysMetrics.Weather: An Evaluation Framework for Physical Consistency in ML Weather Models](https://arxiv.org/abs/2606.10642)

**<font color=#1a73e8>作者：</font>** Emma Kasteleyn, Timo Maier, Axel Lauer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning weather prediction (MLWP) models have achieved impressive forecasting performance at a small fraction of the computational costs required for traditional physics-based methods. However, they are primarily (1) data-driven and (2) evaluated using pixel-wide error metrics (e.g., RMSE), so there are no guarantees that their forecasts are consistent with known physical laws. We introduce this http URL, an evaluation framework that assesses the physical realism of MLWP models across three types of metrics: conservation, spectral, and dynamical. By quantifying physical realism, this tool guides the development of physics-informed architectures and helps evaluate whether MLWP models are reliable for operational use. Our framework is available on Github at this https URL.

---


### 173. [ManiSplat: Manipulation Trajectory Synthesis from Monocular Video via Decoupled 3D Gaussian Splatting](https://arxiv.org/abs/2606.10645)

**<font color=#1a73e8>作者：</font>** Wenhao Hu, Haonan Zhou, Liu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic and interactive 3D scenes from real-world observations remains a fundamental challenge in computer vision and robotics. While recent advances in 3D Gaussian Splatting have enabled high-fidelity static reconstruction, extending it to interactive environments with articulated robots and manipulable objects remains difficult due to complex contact interactions and abrupt pose changes. To address these challenges, we introduce ManiSplat, a unified framework that reconstructs controllable and decoupled Gaussian digital twins directly from monocular ego-view robotic videos. Our method introduces a Graph-Structured Disentangled Representation that separates the robot, objects, and background into independently optimizable Gaussian subfields organized within a scene graph. To ensure stability, we propose a Task-Oriented Spatio-Temporal Alignment module that leverages the inherent logic of manipulation tasks-alternating between Motion and Skill phases-to construct accurate pseudo-ground-truth trajectories. Finally, a joint photometric-geometric optimization ensures the reconstructed scenes are temporally coherent, physically consistent, and simulation-ready. Extensive experiments demonstrate that our approach reconstructs interaction-driven dynamic scenes with high fidelity and controllability, effectively supporting downstream robotic tasks and policy learning.

---


### 174. [Layer Order Semantics for Automata-Based Cybersecurity](https://arxiv.org/abs/2606.10649)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Layered cybersecurity pipelines transform evidence before they decide on it, and the order of those transformations determines which security facts become visible to which layer. This paper gives layer order a finite-state semantics built from a layer-order automaton, deterministic sequential security transducers, evidence markers, and a final decision automaton. The worked case is HTTP request desynchronization: front-end and back-end processors compute incompatible request boundaries, and the same trace is detected or missed according to whether framing evidence reaches the parser-differential layer before it commits. The results separate completed-trace recognition, online editing, decision synthesis, and faithful enforcement; characterize faithful online enforcement as the regular prefix-closed case under causal visibility; and show that regular policies beyond that boundary remain recognizable without becoming deployable enforcers. The framework is monolithically equivalent to finite-output deterministic edit automata, while preserving layer-local invariants such as marker birth, marker survival, and reorder-sensitive visibility. A concrete parser-pair semantics identifies the forbidden marker factor with this http URL, this http URL, this http URL, and HTTP/2-downgrade boundary disagreement under the stated abstraction, and a contextual reorder congruence classifies which component permutations induce the same decision language. The result is an automata-theoretic account of order-sensitive security failures and a compositional vocabulary for auditing, synthesizing, and comparing layered enforcement pipelines.

---


### 175. [Dynamic Linear Attention](https://arxiv.org/abs/2606.10650)

**<font color=#1a73e8>作者：</font>** Xin Wang, Hui Shen, Boyuan Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The scalability of Large Language Models (LLMs) to long contexts is fundamentally constrained by the quadratic complexity of standard attention, motivating the adoption of linear attention mechanisms with sub-quadratic cost. To improve representation capacity under long contexts, recent approaches organize memory in a multi-state manner. However, existing multi-state linear attention methods rely on fixed state merging policies that cannot adapt to dynamically varying token importance, irreversibly obscuring critical tokens and causing severe error accumulation over long sequences. To address this limitation, we propose DLA, a dynamic memory modeling framework for multi-state linear attention. DLA introduces (i) Information-Aware Dynamic State Merging, which adaptively determines state boundaries based on token-level information variation, preserving high-resolution representations around semantic transitions while aggressively summarizing stable regions, and (ii) Capacity-Bounded Memory Modeling, which maintains a fixed-size, chronologically ordered state cache by selectively merging adjacent low-information states to control memory growth with minimal information loss. We pre-train DLA on two different linear attention models and evaluate on 16 datasets across three categories. Experimental results demonstrate the superiority of DLA over state-of-the-art.

---


### 176. [Speaker Group Encoding in Self-supervised Speech Recognition Models](https://arxiv.org/abs/2606.10654)

**<font color=#1a73e8>作者：</font>** Felix Herron, Solange Rossato Alexandre Allauzen, Benoit Favre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate what self-supervised speech recognition models (S3Ms) learn about speaker groups (SGs). We examine several states of S3Ms: pretrained, finetuned on speaker identification (SID), finetuned on automatic speech recognition (ASR), and ASR-finetuned using a fairness enhancing algorithm. We find that S3Ms encode information about several speaker group categories (SGCs), including their gender, age, dialect, ethnicity, and whether they are a native speaker. We find that finetuning for SID amplifies certain SGCs, namely those whose variance is more phonetic in nature, though it does not amplify other SGCs, namely those whose variance is more semantic in nature. On the other hand, finetuning for ASR discards phonetically variant speaker group information (SGI) but retains semantically variant SGI. We find that ASR algorithms designed for fairness improvement change to what extent SGI is encoded in S3Ms; however, this is primarily true for for phonetically variant SGCs, and less true for semantically variant SGCs. We discuss how SGI is encoded by each layer, and identify subdimensions of embeddings responsible for encoding different SGCs. Finally, we discuss how our findings could be beneficial in designing fairer ASR algorithms.

---


### 177. [Envision4D: Envisioning Visual Futures via Feed-forward 4D Gaussian Splatting for Autonomous Driving](https://arxiv.org/abs/2606.10656)

**<font color=#1a73e8>作者：</font>** Qi Song, Yifei He, Chi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting the future evolution of dynamic scenes is crucial in autonomous driving. However, existing feed-forward paradigms are primarily designed for interpolation. When extended to future extrapolation, they suffer from ghosting artifacts under large displacements and are constrained by simplified motion assumptions or strict future priors. To overcome these challenges, we propose Envision4D, a fully self-supervised feed-forward framework for pose-free future extrapolation. Specifically, we introduce a Future Pose Prediction module that infers future camera parameters via an iterative denoising process. Furthermore, to capture non-linear dynamics, we propose In-layer Temporal Attention and employ Conditioned Motion Lifting, which transforms the highly uncertain extrapolation process into robust relational mappings. Finally, a Progressive Training Strategy is utilized to stabilize unsupervised motion learning against error accumulation. Extensive experiments demonstrate that Envision4D achieves state-of-the-art performance, significantly outperforming existing methods in future view synthesis.

---


### 178. [Are We Evaluating Knowledge or Phrasing? Mitigating MCQA Sensitivity with ParaEval](https://arxiv.org/abs/2606.10657)

**<font color=#1a73e8>作者：</font>** João Maria Janeiro, Mathurin Videau, Andrea Caciolai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple-choice (MCQA) benchmarks are the standard for evaluating pretrained large language models, but their reliance on log-likelihood scoring makes them unreliable. Specifically, standard scores are highly sensitive to the exact phrasing (surface form) of the answers, conflating a model's familiarity with a specific phrase with its actual capability. We demonstrate this flaw using a controlled testbed of 1B-8B models trained on the same knowledge. Despite having identical knowledge, standard metrics falsely report a performance gap of over 2 points. To solve this, we propose ParaEval, an evaluation framework that queries models using multiple paraphrases per answer option. By scoring each model based on its most favorable phrasing, ParaEval successfully reduces the false performance gap to below 1 point. We confirm that these evaluation artifacts, and the improvements from ParaEval, persist in frontier 70B and 120B open-source models. Ultimately, ParaEval provides a robust and efficient way to evaluate true underlying capability rather than surface-form familiarity.

---


### 179. [Post-Quantum Secure Federated DeFi for Inclusive Banking](https://arxiv.org/abs/2606.10658)

**<font color=#1a73e8>作者：</font>** Swati Sachan, Dale Fickett, Richard Buchinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advances in error-corrected qubits have accelerated the timeline for practical quantum computing. It poses a threat to cryptographic primitives used to secure financial systems, government infrastructure, communication networks, and DeFi (Decentralized Finance) ecosystems. This paper introduces a post-quantum secure federated DeFi framework that enables inter-bank collaboration to improve the inclusivity of individuals underserved by local lenders due to limited financial histories. Multiple banks contribute encrypted information batches to a virtual server, where lattice-based Fully Homomorphic Encryption (FHE) enables end-to-end homomorphic computation. The server fuses local data-driven probabilistic assessments, expert beliefs, and verifiable evidence generated by the NASA-IBM Prithvi Geospatial Foundation Model (GFM), in encrypted format. Decentralized technologies are employed to ensure tamper-proof evidence and auditable accountability for all encrypted data exchanges between institutions and the server. The framework is tested on agricultural lending decisions for rural borrowers in Virginia.

---


### 180. [Decentralized Multi-Agent Systems with Shared Context](https://arxiv.org/abs/2606.10662)

**<font color=#1a73e8>作者：</font>** Yuzhen Mao, Azalia Mirhoseini  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks. However, most existing MAS rely on centralized orchestration, where a main agent assigns work, collects outputs, and merges results. As the number of subtasks grows, this controller becomes a communication and integration bottleneck. We propose Decentralized Language Models (DeLM), a MAS framework that decentralizes coordination through parallel agents, a shared verified context, and a task queue. Agents asynchronously claim subtasks, read accumulated progress, perform local reasoning, and write back compact verified updates. The shared context acts as a common communication substrate, enabling agents to build on one another's verified progress without routing every update through a central controller. Empirically, DeLM improves both software-engineering test-time scaling and long-context reasoning. On SWE-bench Verified, DeLM achieves the best performance across Avg.@1, Pass@2, and Pass@4, with gains of up to 10.5 percentage points over the strongest baseline, while reducing cost per task by roughly 50%. On LongBench-v2 Multi-Doc QA, DeLM achieves the highest average accuracy across four frontier model families, improving over the strongest baseline by up to 5.7 percentage points. The code is available on our project website at this https URL.

---


### 181. [Analyzing Training-Free Corruption Detection for Object Detection Datasets](https://arxiv.org/abs/2606.10666)

**<font color=#1a73e8>作者：</font>** Christian Sieberichs, Simon Geerkens, Thomas Waschulzik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Annotation errors are widespread in computer vision datasets and can significantly degrade the performance of systems trained on them, particularly in complex tasks such as object detection. Several approaches exist to identify annotation errors, including training-free feature-space methods which provide a fast and interpretable way to analyze annotations. However, the behavior on object detection annotations, which include semantic and spatial information, remains largely unexplored.
In this work we analyze the applicability of feature-space-based approaches for detecting annotation errors in object detection datasets. By adapting an existing feature-space method, we show that such approaches reliably expose semantic mislabel, while positional errors remain difficult to detect. We evaluate this behavior across multiple pretrained embedding models, synthetic noise types (symmetric, asymmetric, and positional), and real-world annotation errors using VOC2012 and KITTI.
All code and real-world corruptions are publicly available at the following repository: this https URL ChristianSieberichs/BoundingBox\_corruption\_detection

---


### 182. [In Defense of Information Leakage in Concept-based Models](https://arxiv.org/abs/2606.10669)

**<font color=#1a73e8>作者：</font>** Mateo Espinosa Zarlenga  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept-based models (CMs), deep neural networks that ground their predictions on representations aligned with human-understandable concepts (e.g., "round", "stripes", etc.), have been shown to learn representations that leak concept-irrelevant information. As the traditional narrative goes, this leakage is undesirable and should be eradicated as it leads to uninterpretable models. In this paper, we posit that this conventional view of leakage in CMs is not only ill-posed, as the evidence of how leakage makes a model less interpretable is often inconclusive, but also bound to lead to impractical CMs under common real-world constraints. Specifically, we argue that in real-world settings where concept incompleteness is the norm, some leakage is often necessary for constructing accurate and intervenable CMs. To this end, we propose that there is such a thing as benign leakage and show that, by optimizing a reframing of the typical CM training objective, CMs can encourage and exploit this form of leakage without sacrificing accuracy or intervenability.

---


### 183. [FadeMem: Distance-Aware Memory Consolidation for Autoregressive Video Diffusion](https://arxiv.org/abs/2606.10671)

**<font color=#1a73e8>作者：</font>** Yu Lu, Junjie Yang, Piotr Koniusz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generators synthesize long videos by generating successive temporal segments, but their historical KV cache grows with video length. Existing bounded-cache methods reduce this cost with local windows, sink tokens, or compressed memory states, yet they usually assign fixed roles to different parts of the history. We propose FadeMem, a distance-aware KV memory consolidation mechanism that organizes historical KV blocks into a temporal hierarchy under a fixed cache budget. This design is motivated by frequency-dependent temporal decay: fine details decorrelate quickly, while coarse scene structure and identity remain useful over longer horizons. During generation, new history is inserted as fine-grained entries, while older adjacent entries are progressively merged under a power-law temporal allocation schedule, yielding a dense-near, sparse-far memory within one cache. Without architectural changes, FadeMem preserves recent context for short-term dynamics and compact long-range anchors for identity and scene coherence. Experiments show improved subject consistency, background stability, and temporal coherence over existing bounded-cache strategies.

---


### 184. [One Step Closer to Ground Truth: A Multi-Scale Residual-Aware Representation Learning Pipeline for Predicting Time Series Data](https://arxiv.org/abs/2606.10678)

**<font color=#1a73e8>作者：</font>** Amrijit Biswas, Mustafa Kamal, Robin Krambroeckers 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based models have emerged as leading paradigms in time-series forecasting in recent years, employing self-attention mechanisms to capture long-range dependencies. Despite their success, these single-stage forecasting architectures exhibit persistent systematic residual biases arising from structural discrepancies, unmodeled stochastic components, or inadequate multi-scale temporal representations. This limitation persists when residuals are treated as irreducible noise, precluding adaptive correction of structured error patterns. To address this limitation, we introduce a two-stage, model-agnostic framework that explicitly decouples forecasting and residual learning into distinct stages of representation learning. A base transformer first generates the initial predictions. Subsequently, a dedicated meta-corrector dynamically models structured error patterns across multivariate channels, preserves cross-variable dependencies, and iteratively refines the residual bias of the base transformer. By formalizing this pipeline as a hypothesis space expansion, our framework addresses approximation limitations inherent in single-stage architectures, removes reliance on restrictive assumptions, and enables end-to-end learning of complex error dynamics. Evaluated on eight popular benchmark datasets using established protocols, our approach achieves state-of-the-art performance, with significant improvements in standard metrics (MSE, MAE). The results demonstrate the framework's ability to mitigate systematic biases and enhance robustness to complex temporal dynamics, advancing the practical applicability of transformer-based forecasting models.

---


### 185. [PL-KKT-hPINN: Enforcing Nonlinear Equality Constraints on Neural Networks via Piecewise-Linear Projection](https://arxiv.org/abs/2606.10682)

**<font color=#1a73e8>作者：</font>** Fateme Mohammad Mohammadi, Hector Budman, Joshua L. Pulsipher  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While physics-informed neural networks (PINNs) have shown strong potential for process modeling, physical equations are only enforced as soft constraints during training, and thus, they do not guarantee constraint satisfaction at inference. We propose a framework, called piecewise-linear Karush--Kuhn--Tucker hard-constrained PINNs (PL-KKT-hPINNs), that strictly enforces nonlinear equality constraints through piecewise-linear projection. This extends the KKT-hPINN framewor, which exactly enforces linear equalities through the Karush--Kuhn--Tucker (KKT) conditions associated with orthogonally projecting neural network outputs onto the constraint feasible region. The method is demonstrated on a continuous stirred-tank reactor (CSTR) case study for both one and two inputs. Results show that PL-KKT-hPINN preserves predictive accuracy comparable to that of a standard neural network while achieving substantially lower constraint violations. In addition, the proposed model shows improved robustness in low-data regimes, yielding lower RMSE than the unconstrained neural network for limited training sample sizes. These results demonstrate that PL-KKT-hPINN provides a computationally efficient and physically consistent framework for surrogate modeling of nonlinear chemical engineering systems.

---


### 186. [Don't waste SAM](https://arxiv.org/abs/2606.10696)

**<font color=#1a73e8>作者：</font>** Nermeen Abou Baker, Uwe Handmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Meta AI has recently released the Segment Anything Model (SAM), which demonstrates exceptional zero-shot image segmentation performance across various tasks with remarkable accuracy. Despite its inability to provide accurate segmentation across multiple research fields, SAM still serves as a valuable starting point for supporting the segmentation pipeline process, particularly for tasks that require extensive and senior skills annotations. This study aims to evaluate the generalization of SAM and fine-tuning SAM models using three waste segmentation datasets. Although they are captured from real scenes as SAM was pretrained on, these datasets present several challenges, including occlusions, deformable objects, transparency, and objects easily confused with backgrounds. In our findings, the fine-tuned SAM-ViT-H model outperforms the state-ofthe-art Zerowaste, and TACO datasets with a significant increase of +30 in IoU, and it closely approaches performance levels of TrashCan 1.0, with only a -1.44 difference. After evaluating these popular waste datasets, it became evident that fine-tuning SAM as a foundational model is a crucial step for providing better generalization for downstream waste segmentation tasks. Therefore, SAM should not be disregarded or wasted.

---


### 187. [Using the YOLOv12 Model for Verifying the Correct Color Sequence of Wires in Network Cables (Patch Cords) on the Production Line](https://arxiv.org/abs/2606.10699)

**<font color=#1a73e8>作者：</font>** Amin Doroodchi, Danial Soleimany  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the production process of network cables, ensuring the correct color sequence of wire pairs inside the standard connector plays a critical role in the final performance of the cable, as any misplacement or color-ordering error can lead to defective products and impose significant costs. Traditional inspection methods based on visual examination through digital microscopes are typically time-consuming, tedious, and prone to human error. In this study, an intelligent system based on the twelfth version of the YOLO1 object detection model was developed to identify the position and verify the correct color sequence of wires in patch cords. The dataset used consisted of 2,500 images captured from microscopic views of network connectors, which were divided into 70% for training, 15% for validation, and 15% for testing. The proposed model, leveraging a single-stage architecture and attention mechanisms during learning, achieved highly accurate wire detection with approximately 98% precision. Additionally, the overall mean accuracy, classification precision, and recall were around 95%, 99%, and 98%, respectively. The results demonstrate that this system can reliably and in real time verify the correctness of wire color sequencing on the production line without the need for human intervention, thereby reducing human error and enhancing efficiency in the manufacturing process.

---


### 188. [Vector Map as Language: Toward Unified Remote Sensing Vector Mapping](https://arxiv.org/abs/2606.10701)

**<font color=#1a73e8>作者：</font>** Yinglong Yan, Yunkai Yang, Haoyi Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing vector mapping aims to generate structured maps of geospatial entities, such as buildings, roads, and water bodies, from remote sensing imagery. In practice, vector maps usually contain multiple category layers and heterogeneous entity structures, requiring a unified model for diverse mapping needs. However, existing methods typically represent vector objects as polygons or graphs, making them suitable only for specific categories: polygons poorly capture topological relations, while graphs often blur instance boundaries. We observe that language, as a natural medium for human communication, offers a flexible and expressive representation that can accommodate heterogeneous map elements, including geometry, semantics, and topolog. Motivated by this insight, we propose Vector Map as Language (VecLang), a unified paradigm that reformulates multiclass vector mapping as structured text generation. VecLang encodes the common elements of different geospatial entities into a GeoJSON-like vector language, enabling cross-category modeling within a shared textual format. To generate this language reliably, we design a progressive vision-language mapping framework that first localizes vectorization units and then generates structured map elements. We further introduce Hierarchical Vector Language Optimization, which uses reinforcement learning to improve syntax validity, content fidelity, and map executability. We also build VecMap-Bench with 54K images and 800K instances, supporting training and evaluation across standard and generalization settings. Extensive experiments demonstrate that VecLang handles both single-class and multiclass vector mapping while achieving strong cross-dataset and open-vocabulary generalization. The model and dataset are publicly available at this https URL.

---


### 189. [From Observation to Intervention: A Causal Audit of Expert Importance in Mixture-of-Experts Models](https://arxiv.org/abs/2606.10703)

**<font color=#1a73e8>作者：</font>** Leonard Engmann, Christian Medeiros Adriano, Holger Giese  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability methods routinely use population-level summary statistics over observed model behaviour to license claims about the effects of targeted interventions on specific computations; in Pearl's terms, they treat rung-1 associational evidence as if it supported rung-2 interventional conclusions, a move whose validity is rarely tested. We examine one concrete instance: the use of routing statistics in Mixture-of-Experts (MoE) pruning, where utilization rates, activation norms, and routing weight distributions are treated as predictors of which experts can be removed without functional cost. A token-level interventional audit across three high-redundancy MoE architectures (OLMoE-1B-7B-0924, Qwen1.5-MoE-A2.7B, DeepSeek-V2-Lite) finds no observational metric predicts causal expert importance after multiple-comparison correction in any model, with effect sizes below Cohen's $d = 0.17$ across all 60 metric-layer combinations. A per-token routing weight control rules out insufficient power, recovering a single Bonferroni-significant signal at OLMoE's final MoE layer ($d = +0.231$, $p = 0.0013$). Existing pruning methods succeed in this regime not by identifying dispensable experts but because early-layer redundancy renders most selection criteria interchangeable. Our results provide an explicit counterexample to the common inferential step from population-level observational summaries to token-level interventional claims about expert importance, and illustrate how interventional audits can calibrate the evidential standards for interpretability claims.

---


### 190. [Event-Driven Reinforcement Learning Enables Long-Horizon Control in Semiconductor Fabrication](https://arxiv.org/abs/2606.10705)

**<font color=#1a73e8>作者：</font>** Yavar Yeganeh, Mahsa Shekari, Nicla Frigerio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning promises to optimize sequential decisions in large-scale systems. Semiconductor manufacturing systems are stochastic and highly constrained environments where heterogeneous wafers traverse hundreds of processing steps across extensive equipment networks. These characteristics yield complex, high-dimensional decision problems with delayed feedback and long-horizon requirements, complicating production planning and control. We propose a deep reinforcement learning framework for multi-objective policy optimization at this scale. Specifically, we formulate control as a centralized-agent problem, where a core policy coordinates system-wide decisions, while system evolution is represented as an interconnected temporal process driven by discrete events. Accordingly, we develop a tailored event-driven temporal-difference formulation that remains general and can be integrated with various policy optimization methods under relevant training settings. We investigate several core model-free algorithms incorporated into this framework and evaluate their effectiveness using high-fidelity simulations of diverse, industry-real operating scenarios. Across extensive validation experiments, agents trained in both offline and online settings show significant and consistent gains in throughput and utilization. We further evaluate performance and generalization across training phases, clarifying the relative strengths of alternative reinforcement learning formulations and algorithms. Overall, the results support the scalability, generality, and transferability of the proposed framework for controlling event-driven complex adaptive systems.

---


### 191. [Attention Expansion: Enhancing Keyphrase Extraction from Long Documents with Attention-Augmented Contextualized Embeddings](https://arxiv.org/abs/2606.10716)

**<font color=#1a73e8>作者：</font>** Roberto Martínez-Cruz, Alvaro J. López-López, José Portela  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-trained language models (PLMs) have achieved strong performance in keyphrase extraction (KPE), largely due to their ability to generate rich contextualized representations. However, long-document KPE remains challenging because salient keyphrase evidence may be scattered across distant document sections that cannot be jointly captured within the limited context window of most PLMs. Although long-context large language models (LLMs) can process broader textual contexts, their computational cost limits their practicality for efficient and high-throughput KPE. To overcome this limitation, we propose an attention expansion mechanism that augments PLM token representations with information from surrounding out-of-context chunks using pre-trained word embeddings. The proposed mechanism expands the effective contextual scope of PLM-based KPE models without requiring full-document attention or expensive LLM-based inference. We evaluate our approach across five PLM backbones, including general-purpose, scientific, task-specific, and long-context encoders, using two training regimes and five benchmark corpora from scientific and news domains. Experimental results demonstrate that attention expansion consistently enhances KPE performance across all evaluation settings, outperforming state-of-the-art models and yielding notable improvements in F1 score. The improvements extend to domain-specific, task-specialized, and native long-context models, showing that the proposed mechanism provides complementary information rather than merely compensating for limited input length. These results establish attention expansion as an efficient and effective strategy for long-document KPE.

---


### 192. [Transformer Based Model for Spatiotemporal Feature Learning in EEG Emotion Recognition](https://arxiv.org/abs/2606.10718)

**<font color=#1a73e8>作者：</font>** Xinglong Cui, Dian Gu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is a widely adopted technique for monitoring brain activity, offering valuable insights into neurological states due to its high temporal resolution and cost-effectiveness. To enhance the analysis of complex EEG data, we propose EEG-TransNet, an architecture designed to capture temporal, regional, and synchronous features of EEG signals. EEG-TransNet introduces three key modules: 1) a preprocessing and feature extraction module leveraging ResNet and wavelet-based denoising, 2) a Local Self-Attention Block for regional feature learning, and 3) a Fuzzy-Attention Synchronous Transformer (FAST) to model spatiotemporal dependencies. Through extensive experiments on three EEG datasets (BETA, SEED, and DepEEG), the proposed model consistently outperforms other methods in terms of classification accuracy and robustness across varying signal lengths. Ablation studies confirm the contribution of the Local Self-Attention Block in improving performance, and the inclusion of depthwise separable convolutions in the decoder reduces computational complexity while maintaining high accuracy. EEG-TransNet's ability to generalize across subjects with minimal performance variation highlights its potential as a robust tool for EEG-based brain activity classification and emotion recognition tasks.

---


### 193. [Fingerprinting All AI Cluster I/O Without Mutually Trusted Processors](https://arxiv.org/abs/2606.10724)

**<font color=#1a73e8>作者：</font>** Naci Cankaya, Jakub Kryś, Jonathan Ng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In preparation for potential international agreements on artificial intelligence, the development of verification infrastructure for AI data centres is vital. We propose a method for cryptographically committing all information entering and leaving a data centre: Hashes are computed by network taps placed on all the information-carrying wires between the cluster and the outside world, enabling an auditor to retroactively challenge the preimage data to be sent to a privacy-preserving verification facility performing compliance checks. Our goal is to make it infeasible to covertly exfiltrate the results of undisclosed workloads in the cluster through the tapped wires. To this end, we specify the architecture of a ``Secure Gateway Device'', which handles the erasure of covert channels that post-hoc verification on hashed data cannot address: analogue and timing side-channels, as well as steganography in network protocol headers. The architecture eliminates the need for any processors trusted by both the Prover and the Verifier, leveraging passive optical fibre splitters and coin-flip protocols for random number generation where needed. We expect development costs of a demonstration device to be roughly equivalent to the cost of a small team of engineers for a few months, with a comparatively small bill of materials.

---


### 194. [Pre-AF 13: An Interpretable Atrial Fibrillation Risk Score Mined from Discharge Reports](https://arxiv.org/abs/2606.10725)

**<font color=#1a73e8>作者：</font>** Olga Shakhmatova, Dmitrii Kriukov, Daniil Larionov 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background. Atrial fibrillation (AF) is the most prevalent cardiac arrhythmia and a major determinant of prognosis. Established AF risk scores rely on factors (older age, hypertension) nearly ubiquitous among patients with cardiovascular disease (CVD), offering limited stratification in this high-risk group. Most target long-term (5-10 year) rather than medium-term prediction. We developed interpretable ML models predicting AF risk over a 24-month and entire follow-up horizon in CVD patients using routinely collected hospital data.
Methods. Single-center retrospective study of electronic health records from the National Research Cardiology Center (Russia) for patients aged >=18 with CVD but without pre-existing AF, hospitalized more than once between January 2012 and May 2019. A custom NLP pipeline transformed unstructured discharge reports into 73 structured features, combining a rule-based parser with transformer-based NER. Using LightAutoML we built a full model (73 features), a simple model (reduced subset), and a linear model for a bedside risk score. Performance was assessed by ROC AUC, compared with CHARGE-AF, C2HEST, MHS, and HAVOC, and interpreted via SHAP.
Results. Of 80,576 records from 45,000 patients, 17,562 met inclusion criteria; 1,438 (8.19%) developed AF. The full model reached ROC AUC 0.735 (24-month) and 0.696 (entire follow-up); the simple model was nearly identical (0.725, 0.696). All non-linear models outperformed the four clinical risk scores (ROC AUC 0.53-0.64). The simple model uses 13 features and is named Pre-AF 13. SHAP identified age and left atrial volume as dominant predictors. A linear risk score (Pre-AF 9) stratified observed 24-month AF incidence from ~7% to 36%.
Conclusion. Interpretable ML models built from routinely collected EHR data identify high-AF-risk CVD patients, outperforming established clinical risk scores.

---


### 195. [SPACR: Single-Pass Adaptive Training of Uncertainty-Aware Conformal Regressors](https://arxiv.org/abs/2606.10734)

**<font color=#1a73e8>作者：</font>** Soundouss Messoudi, Sylvain Rousseau, Sébastien Destercke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal Prediction (CP) provides robust uncertainty guarantees for predictive models, but is typically applied post hoc, which misaligns model training with the conformal goal of producing efficient (i.e, narrow) intervals. We propose SPACR (Single-Pass Adaptive Conformal Regressor), a novel method for directly training uncertainty-aware regressors within a differentiable loss. SPACR jointly optimizes efficiency and validity without batch-splitting or a predefined confidence levels during training. As a result, a single SPACR model yields valid prediction intervals at multiple confidence levels during inference, avoiding the costly retraining required by methods like DOICR. Experiments on diverse datasets show that SPACR consistently gives tighter intervals and better coverage-efficiency trade-offs compared to standard CP and DOICR, while significantly reducing computational costs.

---


### 196. [Patient-Level Diagnosis of Acute Myeloid Leukemia via Deep Learning Analysis of Bone Marrow Smear](https://arxiv.org/abs/2606.10735)

**<font color=#1a73e8>作者：</font>** Yuqi Ma, Tianyi Wang, Weihua Meng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bone marrow smear review remains important for acute myeloid leukemia (AML) assessment, but manual single-cell interpretation is labor-intensive and patient-level diagnosis requires aggregation of many cellular observations. We present a cell-to-patient deep learning pipeline for AML-assisted diagnosis from bone marrow smear images. The study included 258 patients from six anonymized centers, including a main cohort of 169 patients from Centers 1-3 and an external validation cohort of 89 patients from Centers 4-6. A 16-category cell annotation vocabulary was used to describe the global cellular composition, including granulocytic, monocytic, erythroid, lymphoid, eosinophilic, and other cells. Rather than identifying strict AML blasts or leukemic blasts, the model targets an expert-defined composite category termed Composite Blast-like Cells (CBLC), comprising N, N1, M, M1, R, R1, J, and J1 according to the project-wide morphological standard. A fixed YOLO-based segmentation module detected cells, predicted contours were matched to expert polygon annotations by contour IoU, and standardized single-cell crops were generated. An EfficientNet-B0 classifier was trained through a two-stage GT-to-YOLO and YOLO-to-YOLO strategy with class-imbalance correction, center-border regularization, and morphology-assisted supervision. Cell-level predictions were aggregated into patient-level CBLC ratios for AML-oriented diagnostic support. The pipeline achieved stable internal validation and maintained external generalization, with ensemble weighted F1-scores of 0.9076, 0.8696, and 0.9124 on Centers 4, 5, and 6, respectively.

---


### 197. [Detecting Knowledge Gaps from Conversational AI Interactions Using Curriculum Prerequisite Graphs](https://arxiv.org/abs/2606.10736)

**<font color=#1a73e8>作者：</font>** Youssef Medhat, Junsoo Park, Ploy Thajchayapong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large online courses generate thousands of student questions directed at conversational AI teaching assistants, yet these interaction logs remain largely untapped as diagnostic signals. We present a pipeline that maps student questions from a conversational AI teaching assistant to curriculum topics using a few-shot text classifier, grounded in a GPT-4-extracted prerequisite knowledge graph of course concepts. Evaluated on 1,340 question events from 164 students in a graduate-level AI course, our classifier achieves 80.0% accuracy across 43 labels (42 curriculum topics plus an "unknown" abstention class). Topic-level question volume correlates significantly with student self-reported difficulty from an independent mid-semester survey (rho = 0.491, p = 0.008, n = 28 topics), providing convergent evidence that the classified question stream reflects genuine topic difficulty. These results demonstrate that conversational AI interaction logs, mapped onto curriculum structure, carry actionable signals about topic-level knowledge gaps and provide instructors with a curriculum-grounded view of which topics warrant attention.

---


### 198. [DD-INR: Dynamics-Driven Implicit Neural Representation for Accelerated Whole-Brain Functional MRI Reconstruction](https://arxiv.org/abs/2606.10756)

**<font color=#1a73e8>作者：</font>** Qiaoxin Li, Caini Pan, Pierre-Antoine Comby 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accelerated acquisition of fMRI enables enhanced detection of neurovascular (BOLD) activity in the brain, but image reconstruction becomes challenging with high k-space undersampling: Task-evoked BOLD signals are small in magnitude, which traditional anatomical MRI reconstruction methods fail to recover, as they favor spatial accuracy over temporal fidelity. We present DD-INR, a Dynamics-Driven Implicit Neural Representation framework tailored for accelerated fMRI that benefits from incoherent time-varying sampling and a tailored spatiotemporal prior, outperforming traditional methods, demonstrated in simulation and in-vivo acquisition, both in terms of image quality and retrieval of activation patterns. DD-INR achieves this by splitting the fMRI data into a static background and a temporally varying dynamic component, representing only the dynamics with a dedicated INR, thereby focusing the model's capacity on activation-relevant changes while remaining compact. In general, DD-INR provides a promising framework for accelerated fMRI reconstruction, with the potential to improve the sensitivity and robustness of fMRI studies within practical scan time limits. The source code is available at this https URL.

---


### 199. [ArabiGEE: A Hierarchical Taxonomy for Arabic Grammatical Error Explanation](https://arxiv.org/abs/2606.10765)

**<font color=#1a73e8>作者：</font>** Khaled Elhady, Omar Kallas, Nizar Habash 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce ArabiGEE, the first comprehensive Arabic grammatical error explanation (GEE) taxonomy grounded in explicit error types. Unlike existing GEE approaches that treat explanation generation as free-form text, ArabiGEE organizes grammatical explanations through a hierarchical structure spanning orthographic, morphological, syntactic, and lexical dimensions. The taxonomy consists of 27 error types, 140 correction types, and 324 associated explanations. We apply ArabiGEE to manually annotate portions of existing Arabic grammatical error correction corpora and demonstrate how structured grammatical explanations can support automatic evaluation of LLMs on Arabic GEE. Our code and data are publicly available.

---


### 200. [ZODS-RS -- Zero-training Oriented Detection & Segmentation for Remote Sensing](https://arxiv.org/abs/2606.10769)

**<font color=#1a73e8>作者：</font>** Zuan Gu, Tianhan Gao, Langxu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote-sensing and UAV applications need models that generalize across platforms and viewpoints without task-specific training. Yet training-free pipelines often falter on oriented geometry, scale/rotation variation, and crowded ports or airfields, and rarely unify detection and segmentation. We introduce ZODS-RS, a training-free, closed-form pipeline that outputs horizontal boxes (HBB) and instance masks. Built on DINOv3 dense features and SAM-style proposals, ZODS-RS chains: PP (prototype purification via Tyler covariance), R-SEM (rotation-scale equivariant matching with separable kernels and global Hungarian assignment), and UAM (uncertainty-aware pixelwise merging with adaptive priors and optional negative prototypes). A lightweight CWLA fuses multiple DINOv3 layers. On FAIR1M (HBB) we obtain $\mathrm{mAP}_{0.50:0.95}=\mathbf{13.06}$ and $\mathrm{AP}_S=\mathbf{2.93}$ \emph{(class-averaged over ship/airplane)}; on xView (HBB) we report $\mathrm{mAP}=\mathbf{16.69}$. On our UAV dataset, ZODS-RS achieves mask $\mathrm{mIoU}=\mathbf{31.10}$ and improves small-object AP by $\mathbf{+30.70}$ over Grounded-SAM on a single 5090. This work offers a unified, \emph{no-training} solution for horizontal-box detection plus instance segmentation in aerial imagery; provides explicit closed-form formulations for PP/R-SEM/UAM tightly coupled with DINOv3; and demonstrates \emph{consistent} gains on small and crowded targets and under cross-domain shifts while keeping deployment simple.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-269](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
