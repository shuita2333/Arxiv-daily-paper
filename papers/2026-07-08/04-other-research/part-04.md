# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 151. [LBTCap: A Lightweight Bilateral Transformer for Real-Time Remote Sensing Image Change Captioning](https://arxiv.org/abs/2607.03320)

**<font color=#1a73e8>作者：</font>** Licheng Zhang, Siew-Kei Lam, Naveed Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing image change captioning (RSICC) generates natural-language descriptions of semantic changes between paired remote sensing images (RSIs), supporting applications such as urban planning, disaster response, and environmental monitoring. Although recent methods achieve strong captioning accuracy, most overlook computational efficiency and inference speed, which are essential for real-time deployment in practice. To this end, we propose LBTCap, a lightweight RSICC framework built on a bilateral Transformer that jointly models pre- and post-change features for efficient processing of paired RSIs. Specifically, we introduce a bilateral attention mechanism for paired inputs: the two temporal images are projected into separate queries and keys by the same query and key matrices shared across the two images, the value is formed from their concatenation, and the two resulting attention maps are combined by a learnable, structurally bilateral weighting instead of a fixed subtraction. This design keeps both temporal branches explicit while remaining compact, and, together with a truncated backbone and grouped-query attention, LBTCap uses only 39.99M parameters, of which the change-aware encoder accounts for just 2.78M. Extensive experiments on two public RSICC datasets show that LBTCap matches or closely approaches the accuracy of state-of-the-art methods while using far fewer parameters and running at markedly higher inference speed, with the benefit of the bilateral formulation most pronounced in the low-resource setting, demonstrating a favorable accuracy-efficiency trade-off for practical RSICC.

---


### 152. [From Gentlemen to Frontiermen: Masculine Formations in English-Language Fiction (1771--1930)](https://arxiv.org/abs/2607.03323)

**<font color=#1a73e8>作者：</font>** Rong Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masculinity in nineteenth-century fiction is not a single ideal but a field of competing scripts. Drawing on 150 British and American canonical novels from the txtLAB Novel450 corpus, published between 1771 and 1930, this paper examines the changing relative prominence of competing models of masculine authority. To focus the analysis on masculine characterisation, the study extracts male-character-centred text windows by using coreference resolution to group names, nominal mentions, and pronouns into character-specific reference chains. It then fits an unsupervised structural topic model with publication year and author gender as topic-prevalence covariates. The model identifies six distinct masculine formations: aristocratic-chivalric, Christian manhood, gentlemanly respectability, country squire, professional-commercial, and imperial/adventure. Across the corpus, formations tied to inherited rank and sacred authority decline, while those organised around paid work and adventure rise. The largest increase occurs not in professional-commercial breadwinning but in imperial/adventure masculinity, particularly the frontier-wilderness register. The trajectory points to a reallocation from inherited and sacred status towards achieved, commercial, and expansionary forms of masculine authority. Adventurous and commercial formations are also more prevalent in novels by authors recorded as male. Because these formations emerge without a seeded vocabulary yet align with categories established in independent scholarship, the article offers a reproducible method for measuring the reorganisation of gendered authority across the long nineteenth century.

---


### 153. [From General Actions to Domain-Specific Monitoring: Prior-Adaptive Transfer for Skeleton-Based Action Recognition](https://arxiv.org/abs/2607.03327)

**<font color=#1a73e8>作者：</font>** Hao Wang, Di Yang, Jiangtao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based action recognition models have recently shown strong performance on large-scale benchmarks with general actions. However, directly transferring them to domain-specific tasks e.g., healthcare monitoring, is often suboptimal, as such tasks are narrow in scope and may be relevant to only a subset of general motion priors. Moreover, not all pretrained motion patterns are equally useful for a specific task, and retaining less relevant components may hinder adaptation and increase computational cost. To address these challenges, we propose Prior-Adaptive Transfer of Skeletons (PATS), a framework that adapts general skeleton-based models by selectively retaining task-relevant motion priors while filtering redundant ones during transfer. PATS follows a standard pipeline that extracts skeleton signals from videos and employs a spatio-temporal backbone pre-trained on general actions. The key contribution lies in a novel Adaptive Prior Transfer module, which performs model compression as a prior selection mechanism through iterative pruning and refinement. Experiments on two specific action recognition tasks, Alzheimer's detection and fall detection, show consistent improvements in both performance and efficiency over competitive baselines. The code will be released upon acceptance.

---


### 154. [Beyond Post-Quantization: Native Hash Learning with a Dedicated HASH Token](https://arxiv.org/abs/2607.03328)

**<font color=#1a73e8>作者：</font>** Xinze Liu, Ding Wang, Hengjie Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient large-scale image retrieval requires compact representations that preserve semantic similarity under fast Hamming-space search. Deep hashing is appealing, but most existing CNN- and ViT-based methods still follow a post-quantization paradigm, where continuous visual features are first learned and binary codes are then produced by a terminal hash projection or binarization operation. This late code generation creates a feature-to-code discrepancy between the continuously optimized representation space and the discrete Hamming space used for retrieval. To address this limitation, we propose HashViT, a Vision Transformer framework for native hash token learning. Instead of treating hashing as a terminal readout, HashViT introduces a dedicated HASH token that serves as a persistent, hash-oriented retrieval state inside the transformer. The HASH token is structurally decomposed into a Hash Register for direct binary code generation and a Semantic Workspace for preserving auxiliary continuous semantics. To enable effective workspace-to-register interaction, we further design a lightweight Hash Refinement Adapter that progressively refines the Hash Register across transformer layers. As a result, binary-oriented representations are formed through token evolution within the backbone, rather than being abruptly induced by an output-level projection. HashViT is optimized with a unified objective that combines learnable semantic center supervision, class-token similarity distillation, and quantization regularization, encouraging the HASH token to encode semantically structured and compact binary representations. Extensive experiments on three widely used benchmarks demonstrate that HashViT achieves state-of-the-art or highly competitive retrieval performance while preserving the efficiency of compact Hamming codes. Code is available at this https URL.

---


### 155. [Statistically Meaningful Geometry (SMG) Beyond the Euclidean Paradigm, with Application to Generative AI](https://arxiv.org/abs/2607.03329)

**<font color=#1a73e8>作者：</font>** Bing Cheng, Yi-Shuai Niu, Howell Tong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional uniform convergence bounds and empirical risk minimization break down in massive over-parameterized models, such as large language transformers and biological sequence networks. With near-infinite unconstrained internal degrees of freedom, their optimization landscapes develop flat vertical gauge valleys, rendering classical generalization metrics vacuous and inducing severe pathologies, specifically generative hallucination and catastrophic forgetting. We introduce the Statistically Meaningful Geometry (SMG) framework, an information-geometric paradigm lifting deterministic parametric models into infinite-dimensional non-parametric Orlicz statistical manifolds. Modeling the total state space as a differential fiber bundle ($\mathcal{M}, \mathcal{B}, \pi, \mathcal{V}, \mathcal{H}, \omega$), we establish a Two-Fold Inference Paradigm. We formalize an Ehresmann connection 1-form $\omega$ as a dynamic geometric filter that strips away vertical gauge noise (Structural Internal Directions, or SID) and isolates learning trajectories along the strictly non-degenerate horizontal distribution (Statistical Variational Directions, or SVD$\chi$). We prove that under connection-filtered pre-training, out-of-distribution predictive variance is strictly upper-bounded by the finite diameter of the identifiable quotient base manifold $\mathcal{B}$, establishing a hard geometric containment of generative hallucinations. By projecting downstream updates onto the orthogonal complement of the historical horizontal carriage, we formalize the SMG Sequential Adaptation Flow, proving the total non-asymptotic elimination of catastrophic forgetting. SMG replaces empirical fine-tuning heuristics with coordinate-free topological constraints, bridging advanced differential geometry with structural reliability in AI.

---


### 156. [GrowFields: Compositional 4D Neural Fields for Topology-Changing Plant Growth](https://arxiv.org/abs/2607.03330)

**<font color=#1a73e8>作者：</font>** Joaquin Gajardo, Michele Volpi, Marko Mihajlovic 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantifying plant growth dynamics from sparse longitudinal 3D observations is fundamental for agriculture and plant sciences. Yet, plants pose unique challenges: they undergo intricate non-rigid deformations, exhibit changing topology as new organs emerge, and often lack explicit temporal correspondences between consecutive data acquisitions due to newly formed tissue. Methods designed for general scenes struggle to model topology changes and asynchronous organ growth characteristic of plants. To address these challenges, we introduce GrowFields, a compositional dynamic neural field representation for organ-aware 4D plant growth modelling from point cloud time series. Our approach decomposes a plant into its constituent organs and aligns each organ into its own canonical coordinate frame, isolating intrinsic growth patterns from global plant motion. We then learn a shared continuous neural deformation field that models temporal dynamics across all organs, conditioned on learnable per-organ latent codes capturing organ identity and growth characteristics. The resulting modular yet unified representation naturally accommodates the asynchronous development of plant organs while remaining grounded in the practical setting of organ-level plant tracking. We evaluate GrowFields on growth sequences from four plant species, assessing geometric fitting and organ tracking accuracy using manually annotated leaf-tip trajectories. Results demonstrate consistent improvements in spatial precision, temporal coherence, and morphological fidelity over a range of existing representations.

---


### 157. [FedAvg for HAR: Exploring the Tradeoff Between Personalized and Generalization Accuracy](https://arxiv.org/abs/2607.03334)

**<font color=#1a73e8>作者：</font>** Andrea De Luna, Susanna Peretti, Chiara Contoli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The federated learning (FL) paradigm fosters distributed pervasive computing combined with artificial intelligence techniques, allowing for optimized data usage and improved mitigation of privacy concerns. Indeed, model training occurs on the client's local devices, and model parameters are subsequently shared with a centralized server. However, there is a need to find a tradeoff between models' personalization and generalization capabilities. In this paper, we design and implement several testing scenarios devoted to evaluating and comparing the centralized, local, and federated paradigm performances. We also design and implement a scenario that emulates a change in clients' data. We then present experimental results of the FedAvg algorithm applied to the Human Activity Recognition (HAR) domain to understand the trade-off between personalized and generalized accuracy. Results show that, although FedAvg confirms a higher degree of personalization capabilities while keeping a high degree of generalization with respect to the traditional centralized learning, this result is not so obvious under stressful conditions, such as when varying class distribution over clients.

---


### 158. [CSympNet-ID: conformal-symplectic map learning for linearly damped Hamiltonian systems](https://arxiv.org/abs/2607.03339)

**<font color=#1a73e8>作者：</font>** Jiale Gong, Pengzhan Jin, Dongyang Kuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning dissipative dynamics from discrete observations is essential for reliable long-horizon prediction and physically meaningful parameter identification. For linearly damped Hamiltonian systems, the exact flow is generally not symplectic but conformally symplectic, contracting the canonical symplectic form by a scalar factor that reflects the net dissipation. We propose Conformal Symplectic Networks with damping identification (CSympNet-ID), a discrete-time map-learning framework that learns the one-step flow map directly from snapshot pairs while enforcing exact discrete conformal symplecticity by construction, without penalty terms or projection. The architecture composes an exact symplectic neural core with explicit diagonal scaling layers whose factors are parameterized exponentially by a scalar damping-rate parameter, thereby guaranteeing positivity and interpretability of the learned dissipation factor. We establish a scaling-conjugacy factorization for conformal symplectic maps and derive a pointwise-in-step density result for CSympNet-ID. We evaluate an irregular-step damped oscillator, a damped spring-mass chain, a damped nonlinear cubic oscillator, and additional high-dimensional extensions. CSympNet-ID gives the most favorable overall results among the compared models in the reported experiments, particularly in data-scarce regimes, target contraction-law recovery, and high-dimensional tests where unstructured baselines degrade rapidly.

---


### 159. [Efficient Decentralized Multi-task Dataset Valuation via Model Merging](https://arxiv.org/abs/2607.03346)

**<font color=#1a73e8>作者：</font>** Mohammadsajad Alipour, Mohammad Mohammadi Amiri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate and efficient dataset valuation is essential for enabling fair and transparent data marketplaces, especially when multiple contributors provide data for training multi-task models. Most existing valuation methods, however, are limited to single-task settings, overlooking scenarios where a buyer aims to optimize performance across multiple downstream tasks. Moreover, traditional valuation approaches, such as Shapley-based or retraining-based methods, are computationally expensive and poorly suited for decentralized environments without a trusted central coordinator and with strict privacy constraints. We propose DMVM (Decentralized Multi-task Valuation via Model Merging), a novel framework that bypasses retraining and data sharing by leveraging task arithmetic to infer dataset contributions directly from model combinations. Instead of retraining or sharing raw data, DMVM quantifies how models trained on different datasets combine in parameter space to infer each dataset's marginal utility across multiple tasks. This formulation yields a valuation process that is scalable, computationally efficient, and explicitly aligned with multi-task generalization behavior. To support decentralized deployment, we introduce a secure aggregation protocol that enables collaborative valuation without revealing individual model parameters or private data. We also provide theoretical error bounds characterizing the approximation quality of DMVM and validate our framework through comprehensive experiments on computer vision and natural language processing tasks.

---


### 160. [The Multiscale Single-Index Model: A Stylized Model for Hierarchical Feature Learning](https://arxiv.org/abs/2607.03347)

**<font color=#1a73e8>作者：</font>** Joan Bruna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the Multiscale Single-Index Model (MSIM), first introduced in \cite{oymak2021learning}, as a stylized model for hierarchical learning with \emph{scale separation}. Each layer extracts a shared single-index feature at one physical scale and passes it to the next, thus defining a tractable setting in which to study how deep architectures learn multiscale representations. Under non-degeneracy and delocalization assumptions on the link function and planted features respectively, for fixed depth $K$ and local scale $d$, the first Wiener chaos of the target behaves as a perturbed spiked tensor, where the perturbation of order $d^{-1/2}$ comes from the non-linearity -- revealing the MSIM as a natural non-linear analogue of the Tensor PCA model \cite{montanari2014statistical}. While this perturbative picture is sufficient to enable efficient spectral recovery based on Tensor unfolding (as already observed in \cite{oymak2021learning}), it is not precise enough for the analysis of backpropagation gradient-based methods. In this work, we address this limitation by performing a fine-grained analysis of the Wiener chaos using Edgeworth expansions. In the first chaos, this gives a finite-rank hierarchy at scales $d^{-q/2}$. In higher chaoses, balanced flattenings exhibit staircase singular-value plateaus of size $d^{-\rho/2}$ and multiplicity $d^{\rho}$ under a natural higher-chaos non-cancellation condition. Using this higher-chaos structure, and under an additional slow Hermite-energy tail condition, we first establish shallow-network approximation lower bounds, quantifying the benefit of depth in this model. Next, and most importantly, we prove that online SGD on the correlation objective, where all layers evolve in the same timescale, achieves $1 - o_d(1)$ recovery with $n = \widetilde{O}( d^{K-1})$ samples, recovering the same sample complexity as in the linear counterpart.

---


### 161. [Present but Not Remembered: Auditing How Frozen VLAs Encode, Deploy, and Steer Visual History](https://arxiv.org/abs/2607.03372)

**<font color=#1a73e8>作者：</font>** Chih-Ting Liao, Xin Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A frozen vision-language-action model (VLA) receives recent observations at every decision step, yet prior work has focused on adding memory rather than asking how existing history is represented and used. We study this temporal axis using layer-resolved linear probing and causal interchange interventions across three VLAs from two architecture families. We find a three-part dissociation. First, past-frame content remains linearly decodable throughout the network. Second, information unique to history beyond the current frame is nearly absent, indicating that stored history is largely a redundant copy of the present. Third, history is causally deployed only when the current frame is heavily degraded, while the action readout progressively loses dependence on history through the network. Although all models encode history similarly, their deployment strategies differ: under the same occlusion, one architecture increasingly relies on history as a fallback, whereas the other relies on it less. We further introduce a training-free temporal deployment audit that distinguishes these regimes. In the fallback regime, re-injecting history neither repairs occlusion nor disambiguates actions, confirming the redundancy of the stored representation. In the other regime, the same intervention reliably steers the predicted action toward the donor history. These results show that steerability depends on how history is deployed rather than whether it is encoded. VLAs do not forget the past; they largely fail to represent it as information distinct from the present. Our findings suggest that future memory augmentation should inject information unique to the past rather than simply more history.

---


### 162. [TemporalGS: Training-Free Plug-and-Play Acceleration for 3D Gaussian Splatting Rendering via Temporal Priors](https://arxiv.org/abs/2607.03390)

**<font color=#1a73e8>作者：</font>** Yuhongze Zhou, Zihao Yang, Xinxin Zuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has revolutionized novel-view synthesis with its fast and high-fidelity rendering. However, rendering at high FPS and low latency across various scenes remains a challenge, especially when large amounts of 3D Gaussian ellipsoids appear in the scene. To address this issue, we introduce TemporalGS, to the best of our knowledge, the first training-free plug-and-play algorithmic approach to accelerate 3DGS rendering without any post-training or post-processing, implemented on top of tile-based software rasterization. The key idea is that, instead of rendering frames independently as 3DGS, we leverage the temporal priors, represented by novel geometry and appearance buffers, etc., to reduce redundancy of Gaussian preprocessing, sorting, and rasterization operations of consecutive frames. Specifically, we propose two acceleration strategies: (1) temporal dynamic culling, which filters out Gaussians that contribute less to current frame rendering; (2) selective rendering, which renders only a small portion of tiles that cannot be approximated by the temporal priors. By adapting and interleaving these two strategies, TemporalGS yields a simple but effective plug-and-play solution for 3DGS rendering speed-up without any training. Extensive experiments show that TemporalGS achieves comparable or even better performance compared to existing state-of-the-art post-training or post-processing-based 3DGS rendering acceleration approaches. TemporalGS can significantly enhance the rendering speed of various 3DGS methods, achieving up to $1.48\times$ acceleration, while maintaining competitive rendering quality. We further extend our TemporalGS to hardware rasterization-based 3DGS to show the portability of our algorithm.

---


### 163. [Scalable Differentially Private Data Compression via Diffusion and Stochastic Codes](https://arxiv.org/abs/2607.03392)

**<font color=#1a73e8>作者：</font>** Gergely Flamich, Oykü Sıla Güner, Yanxiao Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The ever-increasing collection of personal data has created mounting pressure to develop technologies that protect sensitive aspects of individual identity. Differential privacy (DP) provides a principled framework with strong formal guarantees and has already achieved practical success. However, releasing high-dimensional data, such as images, has remained elusive: releasing uncompressed privatized data requires significant storage. At the same time, no effective data compression scheme exists that can compress high-resolution data with privacy guarantees.
We address this challenge with DP-DiPP, a compression pipeline that combines stochastic codes with diffusion models. DP-DiPP is highly flexible: the practitioner has direct control over the compression rate-privacy-utility tradeoff. As the theoretical backbone, we extend the Poisson private representation (PPR) to encode the outputs of privacy mechanisms. We then combine it with DiffC, a diffusion-based lossy data compression method, to obtain a differentially private image compressor. Our experiments on privatized image classification on CIFAR-10 demonstrate that DP-DiPP significantly outperforms the baseline, achieving a 10-30 times better compression while retaining comparable privacy guarantees and utility.

---


### 164. [From Mobile Data to Business Insights: An End-to-End Analytics Framework for Large-Scale Urban Mobility Analysis and Decision Support](https://arxiv.org/abs/2607.03394)

**<font color=#1a73e8>作者：</font>** Thiago Andrade, Shazia Tabassum, Miguel E. P. Silva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real time location data derived from mobile applications is a powerful tool for addressing various urban challenges, including tourism planning, parking management, bus route optimization, and resource allocation. Besides, it offers invaluable insights for shaping strategic decisions in commercial domains such as location based services, market share analysis, and behavioral profiling. In this expansive study, we aim to address all of the aforementioned challenges by investigating the behaviors and patterns of smartphone users within urban environments, particularly in the domains of tourism, transportation, and retail. Our approach encompasses the development of a sophisticated data platform from inception to implementation, which includes the formulation of use cases, architectural design, and implementation of modules. We employ state of the art techniques and technologies, including data anonymization, ETL pipelines, and utilizing Google BigQuery and Vertex AI for data processing and machine learning model development. A modular architecture based on reusable analytical building blocks was developed to generate data products that support multiple stakeholder driven use cases. Additionally, we apply interactive data visualization techniques via Power BI to facilitate the effective interpretation of analytical findings by stakeholders. The developed models address a wide range of mobility analytics tasks, including mobility profiling, frequent trajectory mining, area of influence analysis, traffic anomaly detection, and origin destination pattern analysis. The results demonstrate the framework's ability to capture user mobility dynamics at fine spatial and temporal resolutions, providing actionable insights for urban planning and strategic business decision making.

---


### 165. [Execution Divergence Graphs:Effective Discovery of Control-Flows from Execution Traces as Fuzzing Feedback](https://arxiv.org/abs/2607.03396)

**<font color=#1a73e8>作者：</font>** Yu-De Lin, Nils Ole Tippenhauer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fuzz testing is a popular approach to the security testing of proprietary software. Efficient testing strategies rely on execution feedback to guide the input generation process, particularly when the basic blocks in the binary can be directly observed and instrumented. Unfortunately, collecting such feedback is impossible in scenarios such as in-situ fuzzing of black-box devices and the fuzzing of obfuscated compiled binaries. In this work, we discuss approaches to guide the fuzzer using feedback derived from a control-flow-graph-like (CFG-like) structure constructed from runtime execution.
We start by outlining a simple divergence-detection approach that identifies unique execution traces, and then present an improved approach based on an Execution Divergence Graph (EDG). We implement both approaches and demonstrate that they outperform a baseline blind fuzzer. In addition, we discuss particular challenges, such as repeated code execution in loops, and show that the EDG-based approach handles them effectively. We then demonstrate that our approach enables effective fuzzing of a number of obfuscated targets, and compare its performance in scenarios where static instrumentation is impossible. While we focus on a scenario in which full instruction traces are directly observable by the attacker, our scheme can also be applied in scenarios with other feedback channels, such as power consumption.

---


### 166. [Efficient bias mitigation in T2I diffusion models using Concept Graphs](https://arxiv.org/abs/2607.03397)

**<font color=#1a73e8>作者：</font>** Mansi, Avinash Kori, Francesco Leofante  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-Image diffusion models often propagate harmful bias inherited from the training data. Existing bias mitigation techniques typically intervene only at the text encoder or provide inference-time guidance, often leading to generations that collapse into semantically incoherent outputs. To address these limitations, we introduce CO-ALIGN (Concept Ontology Alignment), a novel bias mitigation approach based on concept-graph alignment that operates on the model's internal concept ontology. By aligning concepts within the text encoder and denoiser, CO-ALIGN achieves substantial bias reduction while preserving generative integrity. We demonstrate the effectiveness of concept-graph alignment across three paradigms: text-encoders, denoisers and joint text-denoiser ontology alignment. CO-ALIGN outperforms the state of the art, improving fairness by $30\%$, $\Delta FID=11.4$ in image quality, $2.8\%$ in image fidelity, all while reducing semantically incoherent outputs by $88\%$. Beyond bias mitigation, we show that CO-ALIGN benefits other downstream tasks as well. In particular, our experiments demonstrate that better-aligned internal ontologies enhance concept unlearning robustness across multiple unlearning techniques.

---


### 167. [Second MOASEI Competition at AAMAS'2026: A Technical Report](https://arxiv.org/abs/2607.03399)

**<font color=#1a73e8>作者：</font>** Ceferino Patino, Tyler J. Billings, Alireza Saleh Abadi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We describe the 2026 Methods for Open Agent Systems Evaluation Initiative (MOASEI) Competition, a benchmark event for evaluating multi-agent decision-making under open-system conditions. Building on the inaugural 2025 competition, the 2026 edition retained wildfire fighting, cybersecurity, and ride-sharing domains while adding a bonus wildfire track with frame openness, in which agent equipment states such as suppressant capacities and firefighting range vary over time. The competition also expanded its reporting metrics to emphasize total task completions, mean task-completion time, and mean value of completed tasks. Participation in 2026 was limited: eight teams registered, but only one team submitted a final entry, and that entry targeted the ride-sharing track. The submitted DLC approach used planning and replanning to solve routing problems across agents as passengers appeared. This report summarizes the 2026 competition design, highlights differences from the previous year, and reports ride-sharing evaluation results against baseline policies. DLC is recognized as the 2026 ride-sharing track winner among submitted teams.

---


### 168. [LeanDY: Type-Based and Trace-Based Symbolic Protocol Verification in Lean](https://arxiv.org/abs/2607.03406)

**<font color=#1a73e8>作者：</font>** Simon Jeanteur, Lorenzo Veronese, Magdalena Soltiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-aided formal verification is a widely used approach for the symbolic analysis of cryptographic protocols. However, many modern protocols rely on features that remain challenging for existing techniques. In particular, reasoning about state, time-dependent behavior, inductively defined data structures, unbounded executions, and conditional secrecy requires a level of expressiveness that is difficult to reconcile with effective automation. As a result, protocol verification has largely followed two disjoint paths: fully automated methods with limited expressiveness, or interactive proofs in general-purpose theorem provers that offer flexibility but only limited, non-specialized automation.
We present an orthogonal approach that bridges this gap by combining compositional type-based reasoning with trace-based reasoning, enabling modular verification of stateful and unbounded protocols. Guided by the language-and-automation co-design (LAC) principle, our approach delivers protocol-specific automation while retaining high expressiveness. We implement this framework as the LeanDY library for the Lean proof assistant, building on and extending the design of DY*, and combining protocol-specific automation with interactive proofs. Our framework supports, in a unified setting, a broad class of functional and security requirements, including secrecy and authentication for stateful protocols, as well as recursive conditional secrecy for protocols using XOR. We formalize SegWit-style blockchain primitives in LeanDY and demonstrate its expressiveness by carrying out an in-depth formalization of payment channels on top of this blockchain model, verifying punishment mechanisms and properties that depend on chain liveness.

---


### 169. [Handwriting Trajectory Recovery with Diffusion Models](https://arxiv.org/abs/2607.03422)

**<font color=#1a73e8>作者：</font>** Hiroki Nagamatsu, Shoji Toyota, Seiichi Uchida  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering online pen trajectories from offline handwriting images, often referred to as handwriting trajectory recovery (stroke recovery), is an offline-to-online conversion task with applications in stroke-level editing and forensic analysis. We propose, to the best of our knowledge, the first diffusion-model-based framework for this task. Our method formulates trajectory recovery as image-conditioned generation and uses a denoising diffusion model to sample pen trajectories consistent with the observed ink trace. Through extensive quantitative evaluations on CASIA-OLHWDB (1.0-1.1), we verify that the proposed approach enables accurate recovery even for complex multi-stroke characters, substantially improving both temporal similarity (DTW/LDTW) and shape fidelity (AIoU) over representative prior methods such as PEN-Net and Cross-VAE. We further show that the model captures general stroke-order tendencies and generalizes to classes unseen during training, exemplified by cross-script transfer: a model trained on Chinese characters can recover reasonable stroke orders for Latin letters to some extent.

---


### 170. [Securing Multi-Tool AI Agent Chains With Dynamic, Real-Time Compositional Policies](https://arxiv.org/abs/2607.03423)

**<font color=#1a73e8>作者：</font>** Chris Schneider, Kriti Faujdar, Philipp Schoenegger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern AI agent implementations such as frontier coding agents chain multiple tools at runtime that create a security surface that per-tool guardrails are unable to address, as individually permitted tools can violate organizational policies when composed. We propose the Dynamic Security Control Compositor (DSCC), a two-phase approach to compositional security for multi-tool agent chains. In Phase 1, at session checkout, a Most Restrictive Set (MRS) algorithm composes per-tool security policies into a single effective policy with a formal monotonicity invariant that extending a chain can only tighten the result, blocking incompatible combinations before any tool executes. Outputs of any tool call propagate their classification constraints into a session-level taint state, so subsequent invocations must satisfy the most restrictive constraints seen so far. In Phase 2, at runtime, the system tracks the sensitivity of data the agent touches through a monotonic taint state and revokes the session if the accumulated exposure would make a subsequent tool call a policy violation. Together, these phases provide defense in depth, where static composition prevents unsafe chains from starting, and runtime taint tracking catches violations that emerge from the specific data used. We provide a reference implementation on 32 tools governed by 16 NIST SP 800-53 aligned policies and evaluate it under two composition modes. In the default clearance mode, permitted combinations are partitioned into classification-level clusters, blocking 79.2% of policy pairs and 95.5% of triples. The alternative taint mode admits mixed-classification chains within the exfiltration boundary, blocking 42.5% and 60.5% respectively. We discuss the governance implications for organizations deploying multi-tool agents, including the utility-security tradeoff and the changes needed to operationalize chain-aware policies.

---


### 171. [Personalized Causal Recourse: A Human-In-The-Loop Approach](https://arxiv.org/abs/2607.03425)

**<font color=#1a73e8>作者：</font>** Denise Tampieri, Giovanni De Toni, Paolo Giudici  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Algorithmic recourse addresses the challenge of providing tailored recommendations to users affected by unfavorable machine learning decisions, in potentially high-stakes scenarios. Traditional approaches to recourse often rely on the closest counterfactual explanations or assume a priori knowledge of a user's causal structure, resulting in interventions that overlook individual contexts and specific feature interactions. To overcome these limitations, we study a human-in-the-loop framework that iteratively approximates the user's structural causal model through interactive queries via Bayesian inference before producing recourse recommendations. This framework exploits humans' feedback to improve the identification of causal effects, allowing personalized recourse that is plausible, cost-effective, and aligned with the actual causal dependencies of each user. As a proof of concept, we evaluate this framework through simulated human responses. Our simulations across linear and non-linear causal models show promising results, though challenges remain in capturing complex, non-linear structures, emphasizing the importance of accurate approximations and robust noise distribution modeling.

---


### 172. [How Much of the Routing Gap Is Real? Decomposing the Router-to-Oracle Gap into Reproducible Specialist Advantage and Single-Draw Label Noise](https://arxiv.org/abs/2607.03436)

**<font color=#1a73e8>作者：</font>** Teng-Ruei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routing among large language models (LLMs) promises better quality at lower cost, motivated by the reported gap between learned routers and a per-instance oracle. But that oracle is computed from a single correctness label per (query, model), so under stochastic decoding it is one Bernoulli draw, not a reproducible property. We recast the question structurally: the expected per-instance oracle decomposes as $O^{\exp}=O^{\mathrm{repro}}+\Delta$, into reproducible single-commit headroom $O^{\mathrm{repro}}$ and a non-negative single-commit selection floor $\Delta$. Our main result is a recoverability asymmetry: this floor is closed by no single-commit router, yet is recovered by test-time sampling -- best-of-$K$ on the committed model, at the oracle's own budget, dominates the independent-pool single-draw oracle. The cap needs no cross-model independence; we prove it with the exact decomposition and noise-share bounds that shrink as the budget grows. The procedure adds no new router, only resampling. The floor's magnitude is a prospective, conservative localization, not an audit: our primary target LLMRouterBench (33 models, 391,645 instances) defines its oracle as a per-query union over single $T=0.2$ generations -- by construction a union of stochastic single draws. Since $O^{\mathrm{repro}}$ is non-identifiable from the released $k=1$ matrix, we estimate the noise share by fresh $k\ge20$ resampling under one-sided, dependence- and guessing-floor-corrected bounds, recasting 'model-recall failure' as thin-support union inflation. On a controlled open-model re-generation, single-draw noise is a substantial minority of the gap -- larger on an unsaturated benchmark, approaching half on the hardest queries where no model is reliable -- while the majority remains recoverable specialist advantage. We release a multi-sample oracle evaluation protocol for routing benchmarks.

---


### 173. [Evaluating Affective Objectives: Statistical Numbing in Data Visualization](https://arxiv.org/abs/2607.03445)

**<font color=#1a73e8>作者：</font>** Elsie Lee-Robbins, Eytan Adar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualizations can help audiences understand the scale of tragedies, such as the consequences of natural disasters, war, genocide, and pandemics. In these cases, a visualization designer's default behavior may be to focus on communicating quantitative information: numbers, statistics, and trends. However, this may not reflect higher-level affective objectives to inspire their audience to care about an issue, empathize with others, or take action to help those in need. Worse, standard visualizations may conflict with these goals, as statistics can numb emotions and reduce prosocial feelings toward people in need. Designers have developed strategies to increase affective responses through data visualizations, such as blending data narratives and personal narratives about individuals. In this paper, we explore three design strategies for communicating a humanitarian crisis: data-driven, human-driven, or mixed narratives. We conducted an empirical study to explore the effect of statistical numbing in the context of these types of narratives in the format of data videos. In particular, we measure prosocial feelings and behaviors by giving participants the option of donating money as part of the study. We find that human-driven narratives (photographs and stories of individuals) elicited the highest donations and that the mixed narrative combination led to the lowest donations. We discuss the limitations of this study and the implications of pursuing affective objectives and the numbing of empathy in data visualization design.

---


### 174. [CaresAI at SMM4H-HeaRD 2026: Predicting TNM Staging](https://arxiv.org/abs/2607.03466)

**<font color=#1a73e8>作者：</font>** Joseph Itopa Abubakar, Jorge Jarme, Favour Igwezeke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study aims to predict Tumor, Node, and Metastasis (TNM) stage labels independently, with the Cancer Genome Atlas (TCGA) pathology report as the sixth shared task of SMM4H-HeaRD 2026. The problem is framed as three multi-label classification tasks. We explore both classical and deep learning approaches using Term Frequency-Inverse Document Frequency (TF-IDF) features and embeddings from ClinicalBERT, BioBERT, and PubMedBERT. These representations are used with Logistic Regression (LR), Light Gradient Boosting Machine (LightGBM), Feed-Forward Neural Networks (FFNN), and Wide Residual Networks (WRN). Our results show that individual embeddings perform similarly to the TNM label classification, while their combination improves its predictive ability. WRN achieves AUROC scores of 0.839 (T), 0.8502 (N), and 0.803 (M) with F1-scores of 0.622, 0.702, and 0.9337, respectively, for the training phase. LightGBM with TF-IDF performs best with AUROC scores of 0.9368 (T), 0.9524 (N), and 0.8311 (M) and F1-scores of 0.7559 (T), 0.7384 (N), and 0.7017 (M) during the training phase. Furthermore, the result of the Codabench for the test sets indicates a Macro-F1 score of 0.978, 0.957, and 0.879 for the T, N, and M categories respectively for test set 1; while test set 2 records a Macro-F1 score for T, N, and M is 0.807, 0.767, 1.0 respectively. However, performance declined during the evaluation phase of the test sets, a drop from 0.938 to 0.858 of test set 1 to 2, for the Macro-F1 score across all stages; suggesting limitations in model generalizability, sensitivity to class imbalance, and challenges in processing lengthy clinical documents. Although this study provides an efficient baseline model and a reproducible pipeline, further optimization and validation are required before it can be considered suitable for use in a real-world clinical setting.

---


### 175. [PhysMirror: Physics-Aware Mirror Object Generation](https://arxiv.org/abs/2607.03470)

**<font color=#1a73e8>作者：</font>** Xuan-Bach Mai, Duy-Phuc Nguyen, Quoc-Van Le 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing physically accurate mirror reflections remains a fundamental challenge for modern text-to-image diffusion models, which are increasingly critical for generating synthetic training data for embodied AI and robotic perception. These models typically struggle with strict geometric constraints, leading to hallucinations that degrade the utility of the synthetic data. To address this, we introduce a novel, end-to-end physics-aware generation framework namely PhysMirror that natively enforces projective geometry through explicit 3D spatial priors. Our method automatically lifts prompted objects into 3D meshes and constructs a lightweight, mathematically exact mirror scene within a simulated environment. By rendering this explicit 3D scene, we extract precise 2D conditioning elements, such as depth maps and segmentation maps, that serve as robust guiding signals for downstream diffusion models, guiding them to generate images with physically correct mirror reflections. Moreover, we introduce Mirror Consistency Score (MCS), reference-free, fully automated metric that quantifies physical correctness using dense feature matching and vanishing point convergence. Experimental results on our newly constructed MirrOB dataset demonstrate that our approach outperforms state-of-the-art baselines in reflection accuracy and physical realism, while maintaining strong text-to-image semantic alignment, providing a reliable pipeline for embodied AI data generation. The source code is released at this https URL.

---


### 176. [MUTE: Return-Preserving Communication Unlearning for Efficient Multi-Agent Coordination](https://arxiv.org/abs/2607.03473)

**<font color=#1a73e8>作者：</font>** Rui Zuo, Qinwei Huang, Mingyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Inter-agent communication is critical for coordinating Multi-Agent Reinforcement Learning (MARL) agents under partial observability to perform effectively in cooperative games; however, real-world bandwidth constraints demand sparse interactions. Prior approaches primarily address this trade-off by optimizing information-theoretic surrogates. We argue that these statistical proxies are fundamentally misaligned with the true objective: a message can be highly informative yet irrelevant to the joint return of the task. In this work, we propose Message Unlearning for Targeted Efficiency (MUTE), a framework that views communication reduction as a value-guided machine unlearning problem. MUTE rigorously quantifies the Counterfactual Message Value using an attention-based estimator, and systematically unlearns the transmission of low-value messages from a policy trained without any communication constraints. This is achieved through a dual-objective mechanism that enforces communication sparsity while preserving the return of the original joint policy. We derive a theoretical upper bound on the performance gap induced by this sparsification, guaranteeing controlled return degradation. We also empirically evaluate MUTE on various complex multi-agent environments, achieving 80% to 90% bandwidth reduction while maintaining performance comparable to state-of-the-art baselines.

---


### 177. [Learning from Lost Provenance: Multiple Instance Learning for Cancer Registry Tumor Group Classification](https://arxiv.org/abs/2607.03481)

**<font color=#1a73e8>作者：</font>** Leonard Ruocco, Jonathan Simkin, Lovedeep Gondora 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modernizing cancer registries with deep learning is opening new opportunities to automate labor-intensive tasks such as the coding of pathology reports. However, progress is constrained by the scarcity of report-level human-annotated training data. Cancer registries generate substantial volumes of expert-assigned labels as a routine product of their operations, but these exist at the patient level and are not linked to the individual pathology reports that informed them, limiting their direct use for training models. We develop an efficient framework for training deep learning classifiers by leveraging these operationally-generated labels without requiring per-report human annotation, demonstrated for tumor group classification at the BC Cancer Registry. We use Attention-Based Multiple Instance Learning (ABMIL) to recover the lost link between patient-level labels and the reports that informed them, leveraging the attention the model places on each report to distil a large, noisily-labeled corpus into a compact, high-quality per-report training dataset. A classifier fine-tuned on a distilled dataset achieved a macro F1 of 0.83, outperforming established baselines across most tumor groups. By turning routine operational labels into high-quality training data without additional annotation or large-scale computing infrastructure, ABMIL offers a practical and accessible route to automating cancer registry workflows.

---


### 178. [Lacuna Inc. at SemEval-2026 Task 4: Structurally Gated State-Space Models for Disentangling Narrative Similarity](https://arxiv.org/abs/2607.03482)

**<font color=#1a73e8>作者：</font>** Aleksey Kudelya, Rafif Alshawi, Alexander Shirnin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we present the Invariant-Variant Disentangled State-Space Model (IVD-SSM), our submission to SemEval-2026 Task 4 on Narrative Story Similarity and Narrative Representation Learning. Evaluating narrative similarity is a profound computational challenge that requires models to look past concrete, superficial elements such as specific names, actors, objects, or settings to isolate and compare abstract patterns of causality and plot progression. To model these extended causal chains without the quadratic bottlenecks of standard Transformers, we leverage a hybrid State-Space Model (Jamba-1.5-Mini). Building upon this backbone, we introduce the Structurally Gated Alignment (SGA) head, a novel, differentiable algorithmic architecture. The SGA head operates on two scales: a heavily strided Macro-path maps the coarse structural skeleton of a story, which then acts as a gating mechanism to filter a full-resolution Micro-path, actively suppressing semantic noise and superficial keyword overlaps. Evaluated on both pairwise comparative judgments (Track A) and dense representation learning (Track B), our approach demonstrates that explicitly disentangling structural invariants from lexical variants provides a robust, principled framework for deep narrative understanding.

---


### 179. [Towards Diverse and Comprehensive Benchmarks for Mutual Information Estimation](https://arxiv.org/abs/2607.03487)

**<font color=#1a73e8>作者：</font>** Alberto Foresti, Ivan Butakov, Alexander Tolmachev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mutual information (MI) estimation is a central problem in machine learning and statistics; however, existing benchmarks typically evaluate estimators on simplified, low-dimensional distributions, leaving their performance on complex, realistic data largely unexplored. We address this gap with a comprehensive benchmarking framework grounded in a unified copula-theoretic perspective that subsumes existing benchmarks as special cases. Within this framework, we propose two complementary families of tests: a copula-first family that systematically varies ground-truth MI, dimensionality, and marginal complexity using synthetic and flow-based transformations; and a marginals-first family that couples real-world image data with controlled dependency structures, extending the classic same-class-pairing paradigm. We use this suite to extensively evaluate three classes of estimators: non-parametric, discriminative, and generative. Contrary to prevailing assumptions, our results indicate that there is no universal winner: each category can systematically outperform all other estimators under specific setups. By analyzing these cases, we identify fundamental estimation barriers and propose new tests that more effectively stress these specific limitations. We share the open source code at this https URL.

---


### 180. [Learning to Generate Multiple Objects from Dense and Occluded Layouts](https://arxiv.org/abs/2607.03488)

**<font color=#1a73e8>作者：</font>** Bach-Hoang Ngo, Si-Tri Ngo, Hieu Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models fail to generate correct object counts in dense scenes, where overlapping instances collapse into indistinguishable structures despite appearing visually plausible. We identify this as instance ownership collapse: tokens from overlapping objects interact freely through attention, while heavily occluded instances receive weak supervision due to their small visible areas. We address this through layout-aware attention biases that softly bias token interactions toward region-consistent grouping and suppress cross-instance leakage, paired with an amodal-balanced loss that amplifies gradients for occluded objects based on their occlusion level. To enable systematic evaluation, we introduce OverlapDepth-45K, a benchmark of densely overlapping scenes with amodal supervision. Our approach substantially improves count accuracy and prevents instance merging while preserving image quality. Project page: this https URL

---


### 181. [Towards Standardized Light Field Quality Assessment: Hybrid Subjective Benchmarking and Objective Metric Evaluation](https://arxiv.org/abs/2607.03494)

**<font color=#1a73e8>作者：</font>** Saeed Mahmoudpour, Mylene C. Q. Farias, Gi-Mun Um 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benchmarking immersive media coding solutions, especially in the standardization context, requires reliable and reproducible subjective quality assessment (QA) procedures, along with objective quality metrics that remain accurate across different distortion types. This paper presents a standardized workflow for light field QA, developed and deployed in the context of JPEG Pleno standardization activities, which integrates benchmark generation, a hybrid subjective evaluation, and objective metric analysis into a common workflow. The benchmark is designed to encompass not only traditional coding-only artifacts but also distortions that arise in processing pipelines in which light field encoding is accompanied with view synthesis and reconstruction techniques. A hybrid subjective method is proposed enabling fine-grained assessment by combining reference-anchored quality rating with targeted pairwise refinement in perceptually ambiguous regions. The reliability of subjective scores is verified using statistical consistency analyses between observers of two cohorts. Finally, a large set of objective metrics is systematically evaluated in terms of global prediction accuracy, local agreement in ambiguous quality regions, and robustness across distortion families. The results show that several metrics achieve strong agreement for coding-only stimuli, but their performance consistently drops when view synthesis distortions are included. The analysis further highlights the importance of view-pooling strategy in the design of future light field quality metrics. The work provides a reproducible and standardization-ready framework for fine-grained light field QA, while identifying key limitations of current objective metrics under emerging coding pipelines. The subjectively annotated dataset is publicly available at this https URL.

---


### 182. [Reading Between the Dots: Decoding Hidden Computation across Filler Tokens](https://arxiv.org/abs/2607.03502)

**<font color=#1a73e8>作者：</font>** Kaley Brauer, Claudio Mayrink Verdun, Samuel Marks  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier LLMs can perform multi-step reasoning over content-free filler tokens like dots or counting sequences, producing correct answers with no visible chain-of-thought (CoT). This is a limit case for behavioral oversight, where surface tokens carry no information about the underlying reasoning. But hidden from the output is not the same as hidden from us. On four task families (fact retrieval, parallel numeric composition, string manipulation, and in-context computation), two open-weights frontier models (DeepSeek V3, Kimi K2) compute over filler tokens in a structured, legible way: attention routes the question through the filler region to the answer, logit-lens readouts show retrieved facts emerging early and their composition crystallizing in late layers, and KV-cache transplants at filler positions causally swap outputs between examples. We introduce an unsupervised decoding pipeline that takes only hidden states as input and recovers intermediate values with 80-95% accuracy (best LLM judge) across both models and all four tasks, without ground-truth labels or training. Hidden computation that defeats behavioral CoT monitoring is, on these tasks, directly readable from the residual stream, suggesting monitorability is a property of the model's full computational trace, not just its surface tokens.

---


### 183. [A Near-Linear-Time Solver for Graph $p$-Laplacian Semi-Supervised Learning via Continuation in $p$](https://arxiv.org/abs/2607.03503)

**<font color=#1a73e8>作者：</font>** Oren E. Livne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-based semi-supervised learning (SSL) propagates a few labels over a similarity graph by minimizing a Dirichlet-type energy. The standard quadratic ($p=2$) energy reduces to a single graph-Laplacian solve, but it degenerates exactly where SSL is most useful when labels are scarce: gathering more unlabeled data drives the $p=2$ estimate to a near-constant function whenever $d\ge2$ (Nadler-Srebro-Zhou). Well-posedness requires the nonlinear $p$-Laplacian energy with $p>d$. Existing solvers reduce this to a sequence of weighted Laplacian solves, but their reference implementations use a direct sparse factorization or ichol-preconditioned CG instead. Plugging a near-linear Laplacian solver is not straightforward: at large $p$ the conductance weights degenerate near flat-gradient edges, making the system nearly singular and causing stagnation without a damped outer iteration. We close this gap. Recasting $p$-Laplacian SSL as a source-form nonlinear Laplacian flow $B\rho_p(B^\top x)=b$ and solving by damped chord-Newton continuation in $p$, every linearized system stays well-conditioned and can be delegated to a near-linear Laplacian engine. On size-scaled graph families the wall-clock is empirically $m^{0.96}$-$m^{1.02}$ per family (approximate Cholesky default), and a pooled fit across 228 SuiteSparse graphs gives $m^{1.19}$ vs.\ $m^{1.45}$ for direct factorization; the solver handles a $6.8\times10^7$-edge social network in minutes. Memory is the binding constraint: Cholesky fill reaches $10$-$280\times$ the graph nonzeros vs.\ our $O(m)$ hierarchy. Against the released FCL solver we are $1.5$-$14\times$ faster at matched accuracy. On MNIST $10$-NN, $p=3$ scores $64\%$ at one label per class vs.\ $36\%$ for $p=2$. Code: this https URL.

---


### 184. [Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model](https://arxiv.org/abs/2607.03509)

**<font color=#1a73e8>作者：</font>** Xinyin Ma, Julius Berner, Chao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in large-scale generative models has substantially advanced video generation, yet existing methods remain constrained by a rigid inference paradigm. Bidirectional diffusion models excel at global coherence and visual fidelity but suffer from slow inference, while autoregressive models offer efficient and streaming generation at the cost of long-range consistency and exposure bias. We introduce Flex-Forcing, a unified training and inference framework that enables a video diffusion model to seamlessly operate under both bidirectional and autoregressive generation regimes. The core idea is a flexible chunking mechanism jointly defined over the temporal axis and denoising steps. This design allows the model to (1) perform flexible chunking according to different device budgets, (2) perform bidirectional inference across chunks for global structure planning, while generating frames autoregressively within each chunk for efficient and fine-grained synthesis, and (3) perform any-order, any-timestep autoregressive generation without the strict causal constraint. Extensive experiments on multiple video generation benchmarks demonstrate that Flex-Forcing achieves consistently better video quality, long-video stability than strong baselines with a rigid inference schedule, while offering faster inference.

---


### 185. [Mixture-of-Gaussians-Guided Schedule Design for Brownian Bridge Diffusion Models](https://arxiv.org/abs/2607.03517)

**<font color=#1a73e8>作者：</font>** Ron Levi, Michael Elad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brownian Bridge Diffusion Models (BBDM) offer an appealing framework for image restoration and inverse problems by constructing a stochastic bridge from the clean signal directly to the degraded observation, rather than to pure noise. Despite their promise, the choice of bridge schedule is typically inherited from heuristics, and a principled analytical framework for schedule design has been lacking. In this work, we develop such a framework by offering a novel analysis of BBDM reverse dynamics under a Mixture-of-Gaussians (MoG) prior. This setting yields a closed-form ideal posterior and a corresponding MMSE denoiser, while the BBDM-induced reconstruction law is captured analytically through a tractable surrogate. Building on these expressions, we formulate two complementary schedule-design objectives: a Wasserstein criterion targeting perceptual quality and an MSE criterion targeting reconstruction fidelity. Our work exposes an inherent tradeoff between the two and proves the existence of universal schedules for both that are independent of the degradation and prior. Extensive experiments on controlled MoG settings confirm full alignment between theory and practice, and experiments on the FFHQ dataset across inpainting, deblurring, and super-resolution tasks validate the practical value of our schedule-design criteria.

---


### 186. [On the Convergence of Adam, Revisited](https://arxiv.org/abs/2607.03519)

**<font color=#1a73e8>作者：</font>** Steven Heilman, Sampad Mohanty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that projected Adam for online optimization with arbitrary moment decay parameters $\beta_1,\beta_2\in[0,1)$ can have average regret bounded away from zero. A similar result of Reddi-Kale-Kumar from 2018 required $\beta_1<\sqrt{\beta_2}$. Similar to their result, we use a three-periodic sequence of linear functions on $[-1,1]$ with slopes $c,-1,-1$, though we use $c$ slightly larger than $2$. This nonzero average regret result extends to Adam variants such as AdamW, RMSProp, NAdam, Adan, AdaMax, Muon, and to an i.i.d. variant of the three-periodic sequence of slopes for Adam.

---


### 187. [Co-Adaptive Multi-Task LoRA: Transfer-Aware, Label-Free Control of Domain Participation](https://arxiv.org/abs/2607.03522)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Lin Tang, Ming Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a single low-rank adapter on many domains at once is multi-task learning: the domains must be co-learned, and how they share the adapter decides whether they help or hurt one another. Most efficient fine-tuning pipelines ignore this and train on a fixed, uniform mixture, leaving two coupled questions unanswered: how much should each domain participate, and which domains should be co-trained given that some transfer positively and others interfere? We show that both answers can be read off cheaply and without labels. A forward pass of the current shared adapter over a small unlabeled probe yields, per domain, a competence signal whose level tracks remaining headroom and whose trajectory tracks learning speed; the drift of these probe representations yields a signed cross-domain affinity that predicts pairwise transfer. We fold both into CoDA, a co-adaptive controller that solves a small entropy-regularized quadratic program on the simplex to set each domain's participation -- jointly its loss weight and its share of the sampled data -- rewarding high-headroom, still-learning, mutually synergistic domains and damping interfering ones. The controller is forward-only, adds no trainable parameters, and wraps any multi-task LoRA pipeline. Across five heterogeneous domains and two backbones, CoDA improves the average over uniform mixing, learned mixtures, gradient-surgery multi-task optimizers, and online data selection while using half the data, and lowers cross-domain gradient conflict. We prove that the competence signal tracks domain risk, that the participation program has a unique fixed point reached by a contraction, and that its solution performs transfer-aware water-filling; analysis, ablations, and controls corroborate each claim.

---


### 188. [Perceptual Flow Matching for Few-Step Generative Modeling](https://arxiv.org/abs/2607.03524)

**<font color=#1a73e8>作者：</font>** Chuyang Zhao, Yifei Song, Hongfa Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Perceptual Flow Matching (PFM), a simple yet effective framework for few-step generation in flow-matching models. Rather than performing velocity regression in the conventional VAE latent space, PFM supervises flow matching in a perceptual feature space using pretrained perceptual models. This simple change substantially improves the few-step generation capability of flow-matching models, reducing the number of sampling steps from 35-50 to 4-8 while preserving generation quality. Unlike existing acceleration and distillation approaches, PFM requires neither teacher models nor auxiliary score networks and can be integrated into standard flow-matching training pipelines with minimal modifications. Extensive experiments on image generation, video generation, and image editing tasks demonstrate that PFM consistently produces high-quality results while producing fewer artifacts than existing distillation-based methods. We further show that perceptual supervision shifts the regression minimizer from mean-seeking to mode-seeking, biasing predictions toward on-manifold modes that remain accurate under coarse few-step integration. Our results reveal that standard flow-matching training can naturally yield high-quality few-step generators when supervised in an appropriate representation space. We hope this insight inspires future research into representation-aware objectives for efficient generative modeling.

---


### 189. [Mental Health Disorder Detection Beyond Social Media: A Systematic Review of Available Datasets](https://arxiv.org/abs/2607.03540)

**<font color=#1a73e8>作者：</font>** Sadiya Sayara Chowdhury Puspo, Ana-Maria Bucur, Stevie Chancellor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting mental health disorders in a timely manner is an important societal challenge. NLP and machine learning (ML) methods used to assist with detection rely on data collected primarily from social media. However, such datasets often have sampling biases and inherent ethical and privacy issues. One avenue to overcome these limitations is non-social media data. We present the first comprehensive review of non-social media, free-text datasets for mental health research. We use the PRISMA methodology to conduct our survey and we review datasets available in multiple languages. We find that non-social media free-text based datasets are predominantly focused on English and on detecting depression. These datasets also vary in demographics, platforms, data types, annotation techniques, and methodologies. This systematic review also reveals key gaps and highlights opportunities to develop more diverse, reliable and clinically-relevant resources.

---


### 190. [Applying Answer Set Programming with Fuzzy Membership Functions: a Case Study](https://arxiv.org/abs/2607.03550)

**<font color=#1a73e8>作者：</font>** Luca Ferragina, Ilenia Galati, Lorena Gullone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human reasoning often operates through qualitative concepts expressed by linguistic labels such as high, low, expensive, or cheap, whose interpretation depends on context and is usually vague, despite being rooted in numerical data. This paper explores a novel fuzzy-logic-based qualitative extension of Answer Set Programming (ASP) to bridge numerical information and qualitative reasoning. The underlying language, formally introduced in a separate work, provides a principled framework that avoids rigid thresholds and supports robust reasoning under vagueness. Focusing on a representative use case, we illustrate how the framework integrates numerically grounded inputs (such as outputs of machine learning models) with symbolic reasoning over qualitative labels. Key features, including learning-based membership functions and semantically enriched predicates, enable the combination of expert knowledge, contextual factors, and subjective interpretations within a unified declarative setting.

---


### 191. [WeightCLIP: Aligning Datasets and Models for Weight Space Learning](https://arxiv.org/abs/2607.03551)

**<font color=#1a73e8>作者：</font>** Aron Asefaw, Konstantinos Tzevelekakis, Damian Falk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight space learning aims to learn representations of neural network (NN) weights, enabling different downstream tasks. Existing approaches show promising performance, but lacking a way to shape these weight-space representations using information about the datasets the models were trained on, thus limiting downstream applications. We propose WeightCLIP, a method for learning a dataset-aligned latent space for neural networks, where datasets information is induced during training. The NNs are encoded as latent representations using an autoencoder, while dataset samples are encoded using a dataset encoder. The two representations are aligned using a contrastive objective, effectively reshaping the weight-space representations according to the datasets. We demonstrate that such representations can be used for different downstream tasks, including mapping dataset information to a weight-space representation that decode to strong models. In addition, we introduce a latent refinement process for generating models that outperforms standard fine-tuning. Overall, our results demonstrate that explicitly incorporating dataset information improves what can be achieved with weight-space representations across retrieval, generation, and refinement. Code will be available at this https URL.

---


### 192. [iVISION-2DCD: A Long-Term Change Detection Dataset for Large-Scale Outdoor Construction Monitoring](https://arxiv.org/abs/2607.03553)

**<font color=#1a73e8>作者：</font>** Dayou Mao, Yuchen Lin, Ashkan Ebadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automation in construction is essential for reducing costs and human errors in large-scale projects. We approach the construction progress monitoring from the aspect of detecting changes in construction sites. As construction buildings continue to evolve in geometry and appearance over time, change detection need to be performed from arbitrary camera viewpoints. This necessitates developing 2D Change Detection (2DCD) algorithms that operate robustly across diverse camera perspectives at construction sites. While developing and evaluating such systems is data-intensive, no open-source benchmark dataset exists at the intersection of 2D change detection and construction automation research. Data collection using Unmanned Aerial Vehicles (UAVs) is gaining its popularity in outdoor large-scale surveying. However, in active construction sites conducting drone missions equipped with high-end sensors imposes safety concerns. Flight trajectory and collected camera viewpoints can be significantly limited. To address this critical gap, we introduce iVISION-2DCD, a large-scale synthetically generated dataset from dense LiDAR point clouds with photorealistic input images and accurate ground truth annotations. Our dataset formally defines the problem of viewpoint-robust 2DCD at construction sites and captures the inherent complexities of real-world deployment. In this paper, we present our systematic methodology for synthetic data generation, developing novel view synthesis techniques to overcome bi-temporal alignment and viewpoint diversity challenges, and implementing semi-automated semantic segmentation with change label generation while preserving challenging real-world cases. Benchmark evaluations using state-of-the-art 2DCD algorithms demonstrate that iVISION-2DCD poses novel research challenges for the computer vision and robotics communities.

---


### 193. [Latent Clarity: Bridging World-Model Kinematics to Semantic Manifolds for Video Anomaly Anticipation](https://arxiv.org/abs/2607.03558)

**<font color=#1a73e8>作者：</font>** Abu Anas Ibn Samad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous video anomaly detection is dominated by reactive Multiple Instance Learning (MIL) that collapses spatiotemporal features into scalar scores. We introduce PULS (Predictive Unified Latent Space), a continuous semantic world-model pipeline comprising two modules: a 490M-parameter KSD Bridge (Kinematic-to-Semantic Distillation) and a 16.8M-parameter Anticipatory State Predictor (ASP). The KSD Bridge maps V-JEPA 2 physical tensors into the 2048-d Qwen3-VL-Embedding-2B text-aligned hypersphere, trained on a subset of UCF-Crime. This translation alone yields a chunk-level AUROC of 0.8994 for UCF-Crime and 0.8162 for out-of-distribution XD-Violence without MIL or hierarchical fusion.
We introduce and validate the Latent Clarity Hypothesis: because JEPA's temporal predictor discards aleatoric pixel noise while preserving kinematics, anticipated future representations are more semantically separable than observed presents. The ASP sharpens these anticipated future latents, achieving 44.5% mean 14-way zero-shot VQA accuracy (exceeding observation baseline by +9.6 pp). Applying the ASP to Observation Tensors collapses accuracy to 7.3% (random chance), proving Anticipation and Observation occupy distinct sub-manifolds. A Triple-Track Lead-Time protocol with an L1-surprise gate yields a peak +8.9 pp anticipatory advantage at T-0.5s (p < 0.001, N = 1,000 permutation), separating physical anticipation from static scene priors. Zero-shot transfer to XD-Violence confirms that Newtonian-invariant kinematic representations generalize out-of-distribution.

---


### 194. [How to Avoid Debate: Scalable AI Safety via Doubly-Efficient Interactive Proofs](https://arxiv.org/abs/2607.03561)

**<font color=#1a73e8>作者：</font>** Liyan Chen, Yael Tauman Kalai, Zoe Xi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI models continue to develop powerful capabilities, it becomes critical that we are able to verify that their output is aligned with our intentions. A recent line of work focuses on verification via debate, a model of interactive proofs where two competing powerful provers, or AI models, debate each other to convince a weak verifier, or a human, of the correctness of their claim. However, debate assumes that the two AI models possess equal abilities and that one of them is truthful, which may not be realistic.
In this work, we show \emph{how to avoid debate}: we initiate the study of \emph{single-prover} interactive proofs for AI safety. Prior results in single-prover interactive proofs do not immediately carry over to the AI safety setting: for example, they do not work when the computation has access to an oracle, such as to human judgment or an external database such as the web. We present doubly-efficient single-prover interactive proofs and arguments for oracle-aided computations (also known as relativizing proofs), in the settings where (1) the computation is robust, in the sense that the output does not change if at most a small fraction of the answers to oracle queries are incorrect, or (2) the oracle is a low-degree polynomial. These results suggest that interactive verification is possible even without debate, under structured or noise-tolerant oracle access.

---


### 195. [XPlainVerse: A Million-Scale Benchmark for Explainable Deepfake Detection](https://arxiv.org/abs/2607.03562)

**<font color=#1a73e8>作者：</font>** Abhijeet Narang, Kartik Kuckreja, Shreya Ghosh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As deepfake detection models increasingly produce natural language explanations, their reasoning often remains weakly grounded in visual artifacts, limiting reliability and user trust. Existing benchmarks mainly evaluate classification accuracy, overlooking whether explanations reflect the actual manipulations. This gap hinders progress toward deployable, explainable deepfake detection systems. To this end, we introduce XPlainVerse, a large-scale benchmark designed for joint deepfake detection and human-centered explanation. XPlainVerse comprises one million real and manipulated images, pairing authentic images from five established sources with forgeries generated by twelve off-the-shelf image editing and synthesis models. We further propose a multi-stage filtering pipeline, Edit-Check, to verify if manipulations satisfy their intended edits, enabling reliable reasoning supervision at scale. Beyond dataset scale, XPlainVerse provides two complementary explanation styles: technical explanations for expert analysis and simplified explanations optimized for non-technical users. To evaluate explanation quality beyond surface similarity, we propose novel metrics, EntityScore and EvidenceScore, that measure reasoning fidelity by checking whether explanations correctly identify manipulated entities and visual evidence. Human annotations on 2,000 explanation pairs validate our dataset quality against human judgment. We believe XPlainVerse will establish grounded explanation quality as a measurable dimension of deepfake detection and support scalable research on trustworthy, interpretable models.

---


### 196. [EPRA U-Net: An Efficient Pyramid Residual Attention Framework for Accurate Infarct Segmentation in Diffusion-Weighted MRI](https://arxiv.org/abs/2607.03568)

**<font color=#1a73e8>作者：</font>** Hasan Ulutas, Muhammet Emin Sahin, Mustafa Fatih Erkoc 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: Accurate identification of acute ischemic infarcts on diffusion-weighted magnetic resonance imaging (DWI) is a critical prerequisite for reliable lesion quantification and effective clinical decision support in the management of cerebrovascular events. Methods: This study presents EPRA U-Net (Efficient Pyramid Residual Attention U-Net), a task-specific integrated architecture for efficient and accurate infarct segmentation of DWI images. In the proposed architecture, an EfficientNet-based encoder was used as a hierarchical feature extractor with a minimized parameterization. In addition, a Residual-Recurrent (R2) block (recurrent unrolling step t = 2, following the original formulation) and Atrous Spatial Pyramid Pooling (ASPP) were integrated to enhance the performance of spatial dependency modeling. Additionally, a dual attention mechanism was incorporated to highlight lesion-related activations while concurrently enabling the suppression of extraneous background responses. To prioritize lesion detection consistent with clinical imperative, a Tversky loss function was adopted, emphasizing the sensitivity of detection over its specificity during the optimization process. Results: Experimental evaluations were conducted utilizing an in-house dataset comprising 167 patients with 4,895 DWI slices; subsequently, the performance of the proposed EPRA U-Net was assessed in comparison with state-of-the-art models, specifically UNet++, DeepLabV3+, and TransUNet. The experimental results suggest that EPRA U-Net attained superior performance, evidenced by a pixel-aggregated Dice of 0.8984, a per-sample Dice of 0.9469, an IoU of 0.8155, a Recall of 0.8887, a Lesion F1 of 0.9378, and an HD95 of 11.62 px. Furthermore, a clear reduction in the rate of missed lesions, specifically by 16%, 25%, and 29%, was observed when compared with UNet++, DeepLabV3+, and TransUNet, respectively.

---


### 197. [Teacher Supervision over Representation Equivalence Classes](https://arxiv.org/abs/2607.03572)

**<font color=#1a73e8>作者：</font>** Sang Il Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation is usually framed as a choice of what to match in the teacher - its logits, hidden features, or sample relations - which presupposes that the teacher's representation has absolute coordinates to match. It does not: a pretrained representation is identifiable only up to an orthogonal-and-isotropic-scaling equivalence class, so a student should learn the teacher's equivalence class, not its features. The organizing fact is that capability is the teacher's output function, a class invariant that factors through the quotient by the class action, so an objective recovers capability exactly when it is defined there. This makes absolute feature matching ill-posed, and admissible supervision a matter of targeting class invariants (Gram structure, CKA, principal subspaces) or aligning coordinates first, unifying feature matching, relational distillation, alignment, and grafting in one geometric account. We validate our framework on Qwen2.5 and Llama-3.1. A restoration study recovers a corrupted model's representation (CKA ~ 0.99) but not its capability, and an ablation isolates the cause: output-function (logit) matching drives capability, while matching hidden representations aligns geometry without restoring function. Recovery is confined to the corpus-covered region, and a graft study confirms that boundary overlap predicts transplant success but is necessary, not sufficient.

---


### 198. [Differentiate the Evaluator, Not the Program: An Efficient Runtime Representation for Neuro-Symbolic Learning](https://arxiv.org/abs/2607.03574)

**<font color=#1a73e8>作者：</font>** Lucas Sheneman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly propose executable scientific models whose value depends on both their symbolic structure and their fitted continuous parameters. This makes parameter calibration the bottleneck of program-and-parameter co-search: an outer loop can generate thousands of candidate programs, but each needs an inner gradient-based optimization before it can be assessed. Staging each candidate into its own differentiable graph makes individual models fast but sacrifices the program-as-data property that keeps search fluid; interpreter-based approaches preserve programs as runtime data but pay interpreter overhead that dominates the numerical work.
We present the Native Differentiable Virtual Machine (NDVM), a runtime representation that differentiates executable programs without compiling each candidate into a separate graph. NDVM separates symbolic structure from differentiable numeric state: tags, symbols, environments, and control remain native runtime data, while numeric payloads live in dense batched buffers with exact reverse-mode gradients recorded along the realized execution trace, so one evaluator walk is amortized across large populations of parameter vectors. A locked cost model of a real differentiable self-hosted Scheme interpreter motivates the design. We realize NDVM as a native runtime with forward and gradient equivalence to the reference backend, about 60x per-lane batch amortization, near-linear multicore scaling, and two independent front ends. In fixed-budget co-search over LLM-proposed programs, NDVM reaches high-quality solutions about 24x sooner in wall-clock time, suggesting runtime differentiation as a practical systems foundation for scientific discovery workflows.

---


### 199. [When Geometry Aligns: Dihedral Hidden-State Transformations in UNet, ViT, and DiT Architectures](https://arxiv.org/abs/2607.03580)

**<font color=#1a73e8>作者：</font>** Mojtaba Faramarzi, Alex Lamb, Irina Rish  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion architectures now encompass convolutional UNets as well as transformer-based designs such as Diffusion Transformers (DiTs), inspired by Vision Transformers (ViTs), yet the effects of structured geometric perturbations within these architectures remain poorly understood. We study this question through a unified framework that applies reflection-based elements of the dihedral group to intermediate hidden states as controlled internal interventions, contrasting geometrically consistent and inconsistent variants. Using activation-level diagnostics, including Self-Consistency Shift (SCS), Activation Mass Scatter (AMS), and Drift, we analyze feature stability and geometric drift. We find that consistent transformations improve stability, while inconsistent ones induce predictable, architecture-specific failures. In the main Stable Diffusion 2.1 U-Net study, we evaluate seven intervention modes over three seeds and complement the internal diagnostics with image-level FID, KID, CLIP score, and LPIPS diversity. Taken together with supporting ViT and controlled DiT analyses, these results establish geometric consistency as a key principle for stable hidden-state interventions in spatially structured vision and diffusion models.

---


### 200. [PLGSA-Transformer: Periocular Landmark-Guided Attention with Occlusion-Adaptive Cosine Thresholding for Cross-Modal Masked and Unmasked Face Recognition](https://arxiv.org/abs/2607.03581)

**<font color=#1a73e8>作者：</font>** Dana A Abdullah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of facial masks, accelerated by COVID-19 and mandated in security-sensitive settings, has exposed limitations of conventional face recognition systems. Existing approaches relying on fixed cosine thresholds, non-adaptive CNNs, and purely data-driven features fail to generalize when facial regions are occluded, creating a gap between lab performance and real-world deployability. This paper proposes PLGSA-Transformer, a cross-modal face matching framework with three contributions. First, Periocular Landmark-Guided Spatial Attention (PLGSA) uses MediaPipe landmarks to compute Gaussian heatmaps over the eye, brow, and forehead regions, fusing them with EfficientNetB3 features via a learnable residual gate to direct attention toward discriminative visible regions. Second, a Hybrid CNN-Transformer Branch reshapes feature maps into tokens processed by a two-layer Multi-Head Self-Attention encoder, enabling cross-regional dependency modelling. Third, the Occlusion-Adaptive Cosine Threshold (OACT) is a jointly trained head that raises the matching threshold in proportion to predicted occlusion severity. The model is evaluated on 858 images from Zenodo MDMFR (60%), Kaggle CelebA-HQ masked collection (25%), and author-collected images (15%), spanning both genders, ages 21-75, with varied mask types, trained via a unified loss combining contrastive verification, identity classification, and occlusion cross-entropy. PLGSA-Transformer achieves 97.22% pair verification accuracy with ROC AUC 1.0000, surpassing VGG-16-based MUFM (Abdullah et al., 2025; 95.0%), HOG classifiers (Adnan et al., 2020; 85.0%), and Feature-based Structural Measure (Shnain et al., 2017; 86.61%). These results confirm that encoding periocular geometry into attention, with Transformer modelling and occlusion-adaptive thresholds, yields a robust, scalable solution for cross-modal masked face recognition.

---


> [!TIP]
> 当前位于：**151-200**（第 4/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
