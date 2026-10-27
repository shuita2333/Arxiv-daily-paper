# 📦 其他研究 | 2026年10月28日

> 本类共 **446** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

---

### 151. [Securing Edge & Physical AI: Post-Quantum IoT Blockchain for Mission-Critical Cyber-Physical Agents](https://arxiv.org/abs/2610.33862)

**<font color=#1a73e8>作者：</font>** Kürşat Çakal, Suat Özdemir  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed Cyber-Physical Systems (CPS) and Edge AI networks increasingly depend on public-key authentication and key-establishment mechanisms that are vulnerable to cryptographically relevant Quantum Computers (QC). Shor's algorithm threatens widely deployed asymmetric primitives, while Grover's algorithm reduces the effective security margins of symmetric and hash-based mechanisms. Although Post-Quantum Cryptography (PQC) provides a migration path, its larger public keys, ciphertexts, and signatures introduce additional computation, memory, communication, storage, and packet-fragmentation costs that can constrain dynamic multi-agent systems. In this article, we introduce rotational secrecy, an architectural objective that limits temporal key exposure through authenticated transitions between cryptographic epochs. We present Private Authentication for Rotational Secrecy (PARS), a reference mechanism that coordinates policy-triggered key establishment, rotation, and reconciliation among authorized Physical AI agents. For deployments that need distributed agreement on security state, we further develop the PARS-Enabled Edge Security Ledger (PARS-ESL), an optional permissioned architecture maintained by authorized validators or capable edge gateways. PARS-ESL does not store high-volume operational transactions. Instead, it records authenticated state for key epochs, group membership, revocation, algorithm-suite policies, challenge validation, and recovery checkpoints. As a result, resource-constrained agents can take part as lightweight clients, and low-latency operational traffic stays outside the ledger consensus path, protected by the currently active symmetric epoch keys. Our results show that ledger-assisted post-quantum key-epoch management is feasible for selected Edge AI and CPS security-control workloads under the stated trust, compromise, connectivity, and resource assumptions.

---


### 152. [RelateGS: Reliable Semantic and Relational Evidence for 3D Scene Understanding with Gaussian Splatting](https://arxiv.org/abs/2610.33868)

**<font color=#1a73e8>作者：</font>** Seongjun Choi, Sangyoun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-aware 3D Gaussian Splatting (3DGS) has advanced language-driven 3D scene understanding by incorporating semantic and relational cues into reconstructed scenes. However, relation-aware grounding depends not only on representing such information, but also on whether the underlying scene-side evidence is reliable and sufficient. Multi-view semantic aggregation can incorporate weak observations, while object relations can remain under-observed along the available camera trajectory, leading to ambiguous evidence for target disambiguation. We present RelateGS, a structured language-aware Gaussian representation that selectively refines semantic and relational evidence for 3D visual grounding. RelateGS suppresses unreliable observations during semantic feature uplifting and consolidates multi-view object observations into a persistent 3D graph. The graph further identifies under-observed object relations and guides targeted re-querying of informative existing frames to complement their evidence. Experiments on Sr3D+ and Nr3D demonstrate competitive 3D grounding performance, improving the previous best by 7.9 and 1.7 percentage points at Acc@0.25, respectively.

---


### 153. [Stable Dimensionality Reduction via Isometric Centroid-Encoder](https://arxiv.org/abs/2610.33872)

**<font color=#1a73e8>作者：</font>** Tomojit Ghosh, Siva Rama Krishna Prasad Changala, Prathyusha Kanakamalla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many supervised dimensionality reduction methods promote intra-class compactness and inter-class separation but do not explicitly constrain class geometry, leading to variability in the relative arrangement of classes across independent runs. Such variability limits the reproducibility and interpretability of low-dimensional embeddings. We propose the Isometric Centroid-Encoder (ICE), a supervised dimensionality reduction framework in which class centroids are learned directly in the latent space while preserving a prescribed pairwise class-centroid geometry. Unlike existing centroid- or prototype-based methods that primarily encourage intra-class compactness, ICE explicitly regularizes the relative arrangement of latent class centroids. Unlike multidimensional scaling and many metric-learning approaches that preserve sample-level relationships, ICE operates on class centroids, preserving inter-class geometry without requiring large numbers of sample-pair or triplet constraints. We further show that the intrinsic dimensionality required to represent the centroid-distance configuration of $M$ classes is at most $M-1$, explaining the observed saturation of distance-preservation measures as the latent dimensionality increases. To quantify embedding reproducibility, we introduce the Centroid Neighborhood Stability (CNS) metric, which measures the consistency of class-level neighborhood topology across independent runs and complements existing embedding quality measures. Experiments on image and biological datasets demonstrate that ICE produces stable embeddings with improved preservation of class-centroid geometry while remaining computationally efficient. Additional analyses of optimization dynamics, sensitivity, and preprocessing further provide practical insights into latent dimensionality and explicit geometry modeling for supervised dimensionality reduction.

---


### 154. [Semantic Concept Steering Breaks the Explanation Drift Loop in Continual Learning](https://arxiv.org/abs/2610.33877)

**<font color=#1a73e8>作者：</font>** Yehonatan Elisha, Oren Barkan, Noam Koenigstein  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting in continual learning (CL) manifests not only as accuracy degradation but also as \emph{explanation drift}: models maintain predictive accuracy while silently shifting attention from diagnostic features to spurious correlations. This work identifies and resolves a previously overlooked structural flaw in explanation-aware CL: pixel-level saliency regularization derives supervision targets from the model's own frozen saliency maps, creating a \emph{self-referential drift loop} that actively reinforces spurious attention across tasks. We introduce \textbf{C$^3$L} (Concept-Consistent Continual Learning), which breaks this loop by anchoring regularization to class-consistent semantic concepts (e.g., ``curved beak'', ``striped pattern'') discovered offline, independent of model state, providing (i) target independence from model drift, and (ii) cross-instance semantic consistency across every instance of a class. We identify that our concept-based objective, combined with approximate LRP relevance conservation, induces a \emph{crowding-out effect}: since concept and background regions compete for the relevance of the same prediction, enforcing high relevance within concept regions implicitly suppresses spurious background correlations without explicit penalization. \method does not require human-annotated concept sets, as it employs a fully automated concept discovery and spatial grounding. Extensive evaluation across five benchmarks and over 20 baselines demonstrates state-of-the-art performance in accuracy, forgetting, explanation quality, spurious correlation mitigation, and out-of-distribution robustness.

---


### 155. [Min-Marginal Power Indices for Multi-Objective Feature Selection](https://arxiv.org/abs/2610.33885)

**<font color=#1a73e8>作者：</font>** Wenjie Shi, Chi Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Game-theoretic feature selection scores each feature by its average marginal contribution across coalitions. An average shows whether a feature helps overall, but not whether, in some coalition, adding it turns an acceptable model into an unacceptable one. Building on minimum marginal aggregation, we define the Min-Marginal Power Index (MinPI) on a binary utility-threshold game. For a fixed quota, MinPI takes the value -1, 0, or +1 and labels each feature harmful, neutral, or decisive. A harmful label carries its own evidence, an evaluated coalition in which adding the feature drops utility below the quota, so no score cutoff is needed; finite-budget estimators keep this property but may miss harmful features. We use MinPI to propose feature removals, which are accepted only if they pass a validation gate, and to prefilter multi-objective search. On six benchmark datasets over five seeds, MinPI removed 12.5% of analyzed features with almost no loss of held-out utility. On Madelon and Abalone, where it removed the most, its removals cost far less held-out utility than random removals of the same size. Prefiltering increased the dataset-averaged hypervolume of multi-objective search in all five seeds. MinPI is therefore a conservative feature-deletion step whose gains are largest where the data contain many removable features.

---


### 156. [WMEval: Evaluating Interactive World Models Grounded on Physical Simulations](https://arxiv.org/abs/2610.33894)

**<font color=#1a73e8>作者：</font>** Lanxiang Hu, Yixin Huang, Abhilash Shankarampeta 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models hold immense potential for high-stakes applications in robotics, game engines, and immersive digital twins, yet existing benchmarks primarily focus on perceptual similarity rather than the physical-causal coherence essential for real-world utility. We introduce WMEval, a comprehensive benchmark that evaluates interactive world models against Unity-based physical simulations. By leveraging Unity as a high-fidelity ground-truth oracle, we shift evaluation beyond perceptual visual assessment toward the objective state-based verification required for downstream applications. Spanning 9 diverse scenes, WMEval assesses action controllability, scene and character consistency, prompt adherence, kinematics, fluid mechanics, physical causality, and lighting. By executing matched action sequences in both the simulator and the world model, WMEval enables evaluation at both the perceptual level and the physical-causal level, using simulator-derived states as reference. Experiments on state-of-the-art models reveal significant room for improvement in dimensions that remain hidden by standard perceptual metrics but are vital for real-world deployments. Our code is available at: this https URL.

---


### 157. [OS-Wizard: Scaling Computer-Using Agents to Specialized Software via Knowledge-Guided Exploration](https://arxiv.org/abs/2610.33907)

**<font color=#1a73e8>作者：</font>** Zhoumianze Liu, Zichen Ding, Bowen Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-using agents are increasingly capable of performing complex tasks in the digital world. However, high-quality interaction trajectories remain scarce for specialized desktop applications, where limited application knowledge, cumbersome GUI workflows, and incomplete exploration hinder automated collection. We introduce OS-Wizard, an automated trajectory collection framework. It combines tutorial-guided exploration with a hybrid GUI--Code action space, providing application-specific knowledge and simplifying GUI workflows through direct execution of application-native commands. The framework also checkpoints and revisits pivotal states during tree exploration to explore alternative workflows, complementing linear rollouts for broader coverage. We collect 10.9K trajectories comprising 54.9K state--action samples. Fine-tuning open-source base models on this corpus yields a best-performing model that improves performance on a benchmark of specialized desktop workflows by 58.2 percentage points to 64.1\%, surpassing reported human performance of 59.8\% and establishing a new state of the art. The fine-tuned model also improves performance on general desktop workflows using GUI actions only, suggesting that the collected supervision benefits general desktop tasks as well. Comparative experiments and ablations demonstrate the efficiency of trajectory collection and the importance of code actions.

---


### 158. [Rank-1 Weight-Corrected Trainable Weight Averaging for Out-of-Distribution Detection](https://arxiv.org/abs/2610.33909)

**<font color=#1a73e8>作者：</font>** Akito Shinohara, Hiroaki Aizawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection identifies inputs outside the training distribution. Rank-based analyses such as RankFeat and RankWeight suggest that OOD overconfidence is closely related to dominant low-rank components in feature and weight spaces. Since weight averaging operates directly in parameter space and improves model generalization, we consider it for OOD detection from a dominant-component perspective. Trainable Weight Averaging (TWA) assigns a single coefficient to each checkpoint, limiting independent control of dominant weight components. We extend TWA with leading rank-one weight components extracted by Singular Value Decomposition as correction directions, whose contributions are learned through the in-distribution classification objective. On ResNet50, our method improves over fine-tuning and standard TWA across the evaluated datasets with MSP and RankWeight, both with and without Outlier Exposure. Mahalanobis-based evaluation yields mixed results, indicating that the benefit depends on the OOD scoring protocol. Target-layer analyses with MSP and Energy favor correction near the classifier.

---


### 159. [Texture-Aware Strategies for Subregion Style Transfer Augmentation](https://arxiv.org/abs/2610.33910)

**<font color=#1a73e8>作者：</font>** Cheng Ji, Yu Zhao, Xiaochong Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A common strategy for data augmentation is to apply style transfer on training images to enrich appearance variations. Recent approaches have combined style augmentation with random erasing by selectively replacing image subregions with style-transferred patches. However, existing methods rely on uniformly random region selection or fixed geometric constraints, which may fail to cover informative texture patterns and limit augmentation diversity. To address these limitations, we propose a texture-aware subregion style augmentation framework that prioritizes regions with strong texture responses for style replacement. Furthermore, we extend this framework with a hybrid region strategy that combines a texture-driven region with an auxiliary random region, implicitly enabling more diverse style perturbations. Experiments demonstrate that our approach achieves higher classification accuracy and improves robustness compared with existing style-based augmentation methods.

---


### 160. [Human-Aware Agentic Driving: Rethinking Driver State, Trust, and Intervention](https://arxiv.org/abs/2610.33915)

**<font color=#1a73e8>作者：</font>** Lu Feng  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic driving brings goal-directed reasoning, memory, tools, and adaptive interaction into automated vehicles. A vehicle can clarify a request, explain a maneuver, or prepare a driver to take control, then adapt its next action to the response. These capabilities make the vehicle an active participant in shaping the human behavior it observes. We examine how agentic interaction affects driver-state inference, trust and reliance, and human intervention in conditional automation. Established findings on attention, takeover prediction, trust-aware planning, and adaptive warnings provide useful foundations, but their applicability depends on how observations are elicited and how assistance changes the driving task. We distinguish what remains applicable, what changes under flexible interaction, and what remains unresolved across these three areas. The analysis identifies three research priorities: establishing the effects of interventions, jointly designing interaction and driving policies, and maintaining useful adaptation across repeated use and system changes. Progress should be measured through driver comprehension, appropriate reliance, and the ability to perform the required driving action in time.

---


### 161. [Learning Population Dynamics with Variational Doob-Wasserstein Flow](https://arxiv.org/abs/2610.33922)

**<font color=#1a73e8>作者：</font>** Weizhu Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces a novel simulation-free framework for learning unbalanced population dynamics on the Riemannian Wasserstein-Fisher-Rao (WFR) manifold, termed Variational Doob-Wasserstein Flow (VDWF), built upon the theory of the unbalanced mean-field Schrödinger bridge (MFSB). First, by independently learning a geometry model equipped with a data-dependent metric, our model captures the intrinsic geometric structure of population dynamics. Furthermore, leveraging Doob's h-transform, the proposed method incorporates boundary information to improve flow-based trajectory inference. For unbalanced transport, a growth model is employed to learn the dynamics while constructing intermediate mass samples in the WFR space without simulation. Additionally, we analyze the convergence rate of the proposed framework using a uniform Log-Sobolev inequality (LSI). Finally, we validate the proposed approach on multiple real-world datasets, demonstrating competitive performance in learning both balanced and unbalanced population dynamics compared with state-of-the-art methods.

---


### 162. [Multitask Interactions in Recurrent Dynamics across 100 Cognitive Tasks](https://arxiv.org/abs/2610.33926)

**<font color=#1a73e8>作者：</font>** Sílvia García-Hernández, Leema Hamid, Manuel Brenner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The brain continually learns tasks with very different computational demands. Recurrent neural networks (RNNs) have been used as dynamical surrogates for studying task solutions, with recent work extending this approach to joint training on multitask batteries. However, it remains unclear how tasks interact as these batteries grow in scale and heterogeneity: under what conditions do they transfer or interfere with one another, and how do these effects relate to task complexity and model structure? We study this question by simultaneously training hierarchical Almost-Linear RNNs (AL-RNNs) on 100 tasks spanning a wide range of cognitive demands. AL-RNNs allow us to vary the amount of nonlinearity in the recurrence, while hierarchical task features provide a low-dimensional interface for task-specific adaptation within shared dynamics. On this task battery, performance improves with both nonlinear capacity and task-feature dimensionality, with the joint hierarchical model outperforming both individually trained models and a single unstructured joint model. Many tasks are individually solvable with linear dynamics, yet cannot be solved together by a shared linear model. Through hierarchical task features, task-specific linear region usage, and task geometry, the trained model provides several related but distinct measures of task similarity that capture how computations are separated and combined within the shared backbone. Across a series of experiments, we relate these representations to individual task complexity, joint solvability, pairwise transfer learning, and leave-one-out adaptation. Together, our experiments characterize task interactions in multitask recurrent learning while demonstrating both the potential and the challenges of reusable dynamical backbones for cognitive computation.

---


### 163. [EnerGNN: Learning Optimization-Compatible Energy Functions for Exact Constrained Combinatorial Inference](https://arxiv.org/abs/2610.33930)

**<font color=#1a73e8>作者：</font>** Niki Triantafyllou, Maria M. Papathanasiou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-based approaches to combinatorial optimization often predict solutions directly or use predictions to restrict search, while expressive energy-based models typically rely on approximate inference. We introduce EnerGNN, a framework that learns energy functions over complete binary configurations and minimizes them under explicit hard constraints through mixed integer programming (MIP). EnerGNN combines a graph neural network encoder with an optimization-compatible readout and a nonlinear energy head, enabling exact constrained inference over the learned energy. An optimality-aware contrastive loss trains the energy to reflect solution quality and constraint violations. Across Quadratic Knapsack, Combinatorial Auctions, and a personalized cell therapy supply chain problem, EnerGNN achieves near-optimal solutions with 100% feasibility. On the supply chain problem, it achieves a 0.05% mean primal gap and a 17.4$\times$ speedup over the monolithic MIP. The learned energy also generalizes to larger instances and supports zero-shot constraint injection, adapting to changing constraints without retraining while preserving feasibility.

---


### 164. [Stable and Calibrated Latent Force ODE Filters](https://arxiv.org/abs/2610.33939)

**<font color=#1a73e8>作者：</font>** Paul Fischer, Jonathan Schmidt, Philipp Hennig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating unobserved forces in mechanistic systems is a central task of scientific machine learning. Approximate Gaussian filtering methods that synthesize mechanistic and empirical information have shown remarkable capacity in jointly identifying latent processes together with the system state in a single forward-backward pass. The resulting latent force ODE filter framework channels information from observational data specifically into the unknown parts of the system. This work addresses open questions about calibration and stability of the method. We show that the joint posterior over state and force is the reweighted conventional latent force posterior. This uncovers a crucial dependence of the stability of the method on the prior variance of the system state, which effectively controls the flow of information from observations to the latent force through the mechanistic system. From this insight, we construct an improved algorithm that provides stable and calibrated plug-and-play inference. We demonstrate the improved framework on several simulated experimental settings.

---


### 165. [TurboWAM: Learning What Matters for Fast World Action Models](https://arxiv.org/abs/2610.33941)

**<font color=#1a73e8>作者：</font>** Guile Wu, Shuangzhi Li, Xingxin Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models have demonstrated promising performance in robot policy learning, yet their high inference latency remains a critical bottleneck for real-world deployment. Recent approaches have sought to improve inference efficiency by reducing test-time future-frame imagination or accelerating action prediction. However, these methods often leverage representations from all video world model layers without explicitly considering their varying relevance to action prediction, leading to redundant computation and suboptimal representation utilization. In this work, we propose TurboWAM, a fast world action model that efficiently aggregates structured world representations conditioned on action predictions. Specifically, TurboWAM introduces a structured world representation aggregation module that adaptively fuses representations from different world model layers according to their relevance to the evolving action denoising state. Furthermore, TurboWAM employs a structured action supervision mechanism that adaptively modulates gradients from action supervision across different world model layers during backward propagation, facilitating world representation learning. During inference, by reducing the number of world model layers executed and caching relevant representations across action denoising steps, TurboWAM substantially reduces computational overhead. Extensive experiments on multiple robot manipulation benchmarks demonstrate that TurboWAM achieves low inference latency while maintaining competitive task success rates compared with state-of-the-art methods.

---


### 166. [Schema-Free Text-to-SQL: Learning Enterprise Database Structure from Query Logs](https://arxiv.org/abs/2610.33946)

**<font color=#1a73e8>作者：</font>** Ömer Faruk Akgül, Nikhil Kapahi, Prajit Reddy Muppidi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems achieve remarkable accuracy on academic benchmarks, yet performance drops dramatically in enterprise deployments. This gap stems from a fundamental assumption: existing approaches require complete schema documentation, but enterprise databases typically lack comprehensive documentation, featuring cryptic naming and implicit relationships. We present the first text-to-SQL framework that operates without schema documentation, instead learning database structure from historical query logs. Query logs encode implicit structural knowledge: which tables are queried together, how they join, and what columns map to business concepts. We construct a knowledge graph from parsed query patterns and introduce entity-driven GraphRAG retrieval that grounds user questions in domain terminology rather than relying solely on embedding similarity. Validated on both an industrial deployment with expert evaluation and the Beaver benchmark, our approach substantially outperforms similarity-based retrieval methods, the dominant industry approach, in both executability and answer quality. On Beaver, we achieve 95.7% execution validity compared to 60.8% for embedding-based retrieval, with expert data engineers preferring our system 70% to 10% on internal deployment. Our work demonstrates that text-to-SQL can operate effectively in schema-ambiguous enterprise environments, enabling natural language database interfaces "in the wild".

---


### 167. [Accuracy Is Not Enough: An Efficiency- and Statistics-Aware Benchmark of ResNet50 and Vision Transformer for Explainable Multi-Class Gastrointestinal Diseases Classification](https://arxiv.org/abs/2610.33965)

**<font color=#1a73e8>作者：</font>** Akwasi Asare  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated classification of gastrointestinal (GI) findings in endoscopic images could support early diagnosis, but architectures are often chosen on accuracy alone. We present a controlled, reproducible benchmark of ResNet50 and ViT-B/16 for eight-class GI classification on the public Kvasir dataset (4,000 images), using a stratified split (400 test images) and stratified group 5-fold cross-validation over all images. In cross-validation, ResNet50 and ViT-B/16 reached 92.12% and 91.70% accuracy, and a two one-sided tests (TOST) procedure showed equivalence within a +/-3 percentage-point margin (difference +0.43 points, 90% CI -0.33 to +1.18; p < 0.001). The architectures differed mainly in cost: ResNet50 had 3.6 times fewer parameters and 4.3 times fewer operations, 2.5-fold lower single-image CPU latency (69 vs. 177 ms) and 3.8-fold higher GPU throughput. Cross-validated calibration was similar (expected calibration error 0.021 vs. 0.023). An edge-oriented transformer, MobileViT-S, was most accurate on the test split (95.5%) but lost 9.4 points when an acquisition artefact present in some classes (the ScopeGuide inset) was occluded, whereas ResNet50 was not significantly affected. On 500 unseen polyp images with expert masks, both models' Grad-CAM maps focused on the lesion (3.6 times chance). On a de-duplicated external subset of GastroVision (1,998 images), accuracy fell to 78-80% for all three models and differences between them remained small. Accuracy differences between architectures were thus small relative to the effects of shortcut learning and domain shift, whereas efficiency differences were large. An efficient CNN is a defensible default for resource-constrained screening, but no model is deployment-ready without local validation.

---


### 168. [Performance of Neural Operator Baselines on 'The Well' Dataset](https://arxiv.org/abs/2610.33967)

**<font color=#1a73e8>作者：</font>** Yash Pincha, Andy Dimnaku, Andrew Chiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Well, a 15-terabyte dataset spanning 16 physical simulation domains, provides an extensive benchmark for developing and evaluating machine learning surrogate models for complex physical systems. The baselines released with the benchmark were presented by their authors as illustrative examples obtained at small computational cost, trained with zero to very limited hyperparameter tuning and under a highly constraining 12-hour per-run wall-clock limit. These results have subsequently been treated as fully tuned benchmarks, and in some cases effectively interpreted as unconstrained performance baselines. We perform a short non-exhaustive hyperparameter search for the Tucker-factorized Fourier Neural Operator (TFNO) under the same 12-hour per-run wall-clock limit, while using only a single input timestep rather than the history of up to four used by the published baselines. Despite this more restrictive setup, tuning alone reduces VRMSE below both published FNO and TFNO baselines on 15 of 17 tasks, sometimes by several orders of magnitude. This sensitivity to a modest tuning effort underscores that the released neural operator baselines should not be treated as architectural benchmarks.

---


### 169. [Hierarchical Cooperative GFlowNets](https://arxiv.org/abs/2610.33968)

**<font color=#1a73e8>作者：</font>** Pedro Dall'Antonia, Juan Belieni, Ana Carolina Erthal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Flow Networks (GFlowNets) are trained to sample objects from compositional spaces with probability proportional to a reward function, but ineffective exploration can cause learned samplers to concentrate on a few high-reward regions. An intuitive remedy is to train multiple GFlowNets independently in parallel and combine their samples. However, this does not prevent multiple models from collapsing onto the same high-reward areas, leaving large regions of the state space unexplored. With this in mind, we propose Hierarchical Cooperative GFlowNets (HCG), an approach that dynamically partitions the search space to coordinate discovery without relying on hand-crafted boundaries. HCG imposes an ordering in which the highest-ranked model may explore the entire space, while lower-ranked models are progressively pushed toward regions not covered by higher-ranked ones. We provide a theoretical characterization of how specific learning objectives can shift probability mass away from designated areas, instantiating this mechanism within our architecture. A shared classifier coordinates the hierarchy by partitioning the search space, keeping the GFlowNets independently parameterized and enabling asynchronous training. Furthermore, we derive a normalizer-weighted aggregation rule for the ensemble and prove that it recovers the target reward-proportional distribution under the stated assumptions. Finally, experiments across multimodal distributions, sequence generation, combinatorial optimization, and biological sequence design show that HCG improves mode coverage and target approximation, translating increases in the number of coordinated samplers into broader, complementary exploration.

---


### 170. [A spinal-inspired spiking neural network for continuous finger-joint kinematics estimation from high-density surface EMG](https://arxiv.org/abs/2610.33979)

**<font color=#1a73e8>作者：</font>** Cristian David Guerrero-Mendez, Leonardo Abdala Elias  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Decoding simultaneous and proportional finger kinematics from high-density surface electromyography (HD sEMG) remains challenging. Although data-driven methods have shown promising performance for finger movement decoding, their limited physiological interpretability remains a relevant limitation. This study proposes and evaluates a spiking neural network (SNN) that incorporates spinal-inspired structures and mechanisms to predict multi-joint finger kinematics from HD sEMG signals. The spinal-inspired SNN includes a spike-encoding computational model with input-noise variability, a phenomenological representation of Henneman's size principle, and excitation/inhibition (E/I) balance. HD sEMG and kinematic data were collected from 23 healthy participants performing grasping tasks under different elbow and wrist postures. Performance was assessed using six prediction metrics and compared against six baseline machine learning and deep learning methods. The proposed method showed a large and significant ($p<0.05$, rank-biserial correlation $r_{rb}>0.7$) improvement over all baseline methods across all accuracy metrics. Performance improved significantly with increasing spike encoder firing rates up to approximately 128 Hz, and with more regular input spike trains compared with a Poisson-like encoder. In contrast, the E/I balance did not significantly affect the decoding performance of the algorithm. The firing rate and inter-spike interval statistics of the SNN differed significantly across motor tasks. These results demonstrate that incorporating neurophysiological principles into SNNs improves prediction performance while providing additional physiological interpretability for simultaneous and proportional finger-kinematics decoding. This approach represents a promising step toward physiology-informed neural networks, with potential applications in motor rehabilitation.

---


### 171. [Constrained Gradient Equilibrium: Approachability under Locally Constrained Adversaries](https://arxiv.org/abs/2610.33985)

**<font color=#1a73e8>作者：</font>** Kaicheng Zhang, Lujing Zhang, Yifei Pang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient equilibrium (GEQ) is a recent framework in online learning that requires the time-averaged gradients along the learner's trajectory to vanish. We study GEQ when the learner is constrained and ask when such an equilibrium remains achievable in an adversarial environment. We first show that constrained GEQ (CGEQ) can be impossible even under simple and slowly varying constraints, motivating imposing local temporal structure on the adversary. We then develop an approachability framework for CGEQ under locally constrained adversaries, and obtain necessary and sufficient characterizations in the spirit of classical Blackwell approachability. Beyond these theoretical characterizations, we provide an algorithmic principle that converts window-wise no-regret learners into CGEQ algorithms under a local feasibility condition with margin. Experiments on synthetic and real data demonstrate that the resulting algorithms perform strongly in both achieving GEQ and respecting the constraints.

---


### 172. [Hybrid Mamba-Transformer Network for Single-Shot 3D Reconstruction from Fringe Patterns](https://arxiv.org/abs/2610.33988)

**<font color=#1a73e8>作者：</font>** Xinjie Zhou, XiaoLei Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning facilitates rapid single shot three dimensional (3D) reconstruction using fringe projection profilometry (FPP), but recovering accurate surface height from a single high frequency fringe image remains challenging because both long-range spatial consistency and fine geometric details must be preserved. Convolutional networks are limited in modeling long range dependencies, whereas window-based Transformers establish global interactions only progressively with increasing depth. To address these limitations, a hybrid Mamba Transformer network is proposed for fringe to height regression. The network adopts a Swin based U shaped architecture and introduces visual state space modeling at the intermediate resolution encoder stage. An axial and dilated vision state space (ADVSS) block is further developed to enhance prescan feature encoding through local, dilated, and axial depthwise convolutions while retaining four directional selective scanning. This design combines linear complexity long range modeling with direction aware preservation of local fringe structures. Experiments on a publicly available FPP dataset show that the proposed method outperforms hNet, SwinConvUNet, UHRNet, and HiDNet in mean absolute error(MAE), root mean square error (RMSE), absolute relative error, and structural similarity index measure (SSIM). Using only one deformed fringe image, the proposed method achieves an RMSE of 0.548 mm and an SSIM of 0.9985, reducing RMSE by 65.2% and 59.6% relative to UHRNet and HiDNet, respectively. These results demonstrate the effectiveness of combining selective state space modeling with hierarchical window based attention for accurate single-shot FPP reconstruction.

---


### 173. [Resolving the Mobility-Equity-Emissions Trilemma: A Causal Machine Learning Framework for Dynamic Tolling Policy](https://arxiv.org/abs/2610.33994)

**<font color=#1a73e8>作者：</font>** Christian Mulomba Mukendi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a causal machine learning framework to integrate dynamic tolling for mobility, equity, and climate objectives, resolving a long-standing policy trilemma. Using Double Machine Learning, we estimate zone-type-specific treatment effects, showing that commercial zones yield nearly twice the delay reduction of residential zones. Our adaptive quota mechanism expands residential coverage 34-fold while preserving 93% of total delay savings and sustaining high return on investment. The framework delivers climate co-benefits, reducing emissions by 743.5 metric tons of CO2 (valued at 141 USD) via congestion-sensitive pricing under moderate traffic conditions with sensitivity bounds from 557.6 to 929.3 tons. Crucially, we uncover a policy-invariant toll range where performance remains robust across demand scenarios, simplifying implementation. This study reveals critical, previously unidentified insights, such as a policy-invariant toll range, that can significantly simplify real-world implementation. Validated on synthetic data mirroring real-world networks, our methodological advances lay the foundation for future public deployment.

---


### 174. [Steering the Teacher: Improving On-Policy Self-Distillation for Thinking Models](https://arxiv.org/abs/2610.34005)

**<font color=#1a73e8>作者：</font>** Tiejin Chen, Xiaoou Liu, Hanyang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains a student on its own reasoning trajectories using token-level supervision from a reference-conditioned teacher initialized from the same model. However, access to the reference can induce teacher behaviors that undermine independent reasoning in thinking models, leading to reference hallucinations, where the student cites an unavailable reference to justify reasoning steps, and reconsideration suppression, where the teacher discourages verification and revision at uncertain steps. We introduce Steered-Teacher OPSD (ST-OPSD) to jointly address these failure modes through activation steering. ST-OPSD extracts two directions from model-generated reasoning trajectories and applies them to the teacher's hidden states during distillation target computation, suppressing reference-invoking behavior and encouraging reconsideration with marker-family calibration. The student learns from the resulting teacher distributions without being steered. Experiments on AIME and HMMT show that ST-OPSD improves accuracy over vanilla OPSD and other interventions while restoring reconsideration and reference-hallucination rates to base-model levels.

---


### 175. [Cross-User Adaptation for sEMG Gesture Recognition via Continual Learning](https://arxiv.org/abs/2610.34011)

**<font color=#1a73e8>作者：</font>** Aran Ramakrishnan, Shubhi Mishra, Tyler Ham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prosthetic and assistive interfaces increasingly depend on decoding hand gestures from surface electromyography (sEMG). Because the signal is shaped by person-specific factors, the recurrent neural networks (RNNs) commonly used to model these temporal streams must adapt to new wearers and new gesture classes after deployment. Continual learning (CL) enables this adaptation without retraining from scratch, yet applying it to recurrent sEMG models is not straightforward. Standard recurrent training practices can destabilize learning, and which CL strategy holds up under realistic cross-user drift is unestablished. We evaluate three representative CL strategies under domain- and class-incremental drift on NinaPro DB1, and find experience replay to outperform elastic weight consolidation (EWC) and naive fine-tuning. It reaches 83.3% final accuracy for class-incremental drift while limiting forgetting to 1.8-5.8% accuracy drop, as against 16.2-28.5% for EWC and naive training. We further show these models must be trained on shuffled, independently-windowed segments. Streaming windows in temporal order collapses the network into predicting a single dominant gesture, while a shuffled, stateless regime trains stably. Finally, hand-crafted time-domain features raise per-task accuracy by up to about 40% over raw signals, but only replay preserves that gain under class-incremental drift.

---


### 176. [The Patient Is Always Right? Evaluating Sycophancy in Medical Diagnosis with Graded Patient Beliefs](https://arxiv.org/abs/2610.34013)

**<font color=#1a73e8>作者：</font>** Viswonathan Manoranjan, Andrea Mock, Myra Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> More people are seeking out general-purpose AI models for medical advice, including diagnosis. Yet, AI models are susceptible to sycophancy, like validating users' beliefs even when they are untrue, which could lead to false positive diagnoses. Here, we evaluate how nine AI models change their diagnostic decision when a patient presents a belief that they have a specific (but incorrect) medical condition. We vary how close the user belief is to the clinical evidence presented. Models sycophantically adopt the patient's belief on average 23.2\% of the time---sometimes even when the patient proposes a fictional, made-up condition. We also varied different personas, including a Rare Disease Claimer that got models to accept their belief 43.0\% of the time. Additional analyses find that medical fine-tuning and model scale makes models less susceptible to changing their diagnoses. Sycophantic bias in medical diagnosis raises implications for safety, especially as more people are using AI for health support.

---


### 177. [The Information Geometry of Representation Formation](https://arxiv.org/abs/2610.34015)

**<font color=#1a73e8>作者：</font>** Sanjukta Krishnagopal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most analyses of neural representations focus on trained endpoints, leaving the process by which internal structure forms comparatively unmeasured. We instead treat representation formation itself as an object of study, asking whether the path a representation takes through training reveals information that its endpoint does not. We formalize this idea by viewing representation learning as a geometric trajectory, using Bures geometry to measure movement through representation space and quantum Fisher information to characterize local sensitivity to input factors. We find that learning concentrates local sensitivity on task-relevant factors, and that changing only the prediction target reorganizes this geometry around the corresponding visual factor. More strikingly, representation trajectories become systematically less direct as the learned computation requires higher-order interactions among input factors. This effect persists under matched-performance and training-duration controls and transfers from synthetic vector inputs to residual CNNs on rendered and natural images. Importantly, formation history contains predictive information about the stability of the learned representation: controlling for interaction order, path tortuosity predicts its subsequent drift under continued training and sensitivity to parameter perturbations, whereas endpoint displacement does not. Finally, representation-aware optimization lets us actively shape these trajectories, showing that formation geometry is not only measurable but actionable. Together, these results establish representation formation as a new source of information about learning: its geometry reveals properties of the computation being constructed, predicts subsequent representational stability, and provides a target for intervention during optimization.

---


### 178. [The Symmetry of Differential Neural Tangent Kernel under the Orthogonal Group](https://arxiv.org/abs/2610.34023)

**<font color=#1a73e8>作者：</font>** Bangti Jin, Longjun Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The differential neural tangent kernel (DNTK) is a tool for analyzing the training dynamics of overparameterized physics informed neural networks. In this work, we investigate the symmetry of the infinite DNTK under an orthogonal group, for two layer and deep neural networks separately, based on the explicit expression of the DNTK and recursive formula, respectively. The results are for all activations with or without a bias term, and shed insight into the structure of the infinite width DNTK. Then we prove that the integral operators over the unit sphere induced by operators from the same group orbit share the spectrum, and their reproducing kernel Hilbert spaces differ only by an orthogonal transformation, and that the operator fixed DNTK exhibits zonal symmetry on the unit sphere for symmetric operators. Thus the eigenvalue decay rate of the associated integral operator can be derived for shallow networks with RePU activation and zero bias initialization.

---


### 179. [Holding a Steady Course: Knowledge Evolution from Expertise and Lessons for Continual Agent Learning](https://arxiv.org/abs/2610.34043)

**<font color=#1a73e8>作者：</font>** Wenzhe Fan, Benjamin Steenhoek, Gaurav Mittal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are increasingly deployed across sequences of related tasks, yet they often fail to retain and improve their knowledge over time. Existing approaches convert interaction trajectories into memories or reusable skills, but experience is not automatically reliable knowledge. Automatically collected skills and memories can propagate errors, mislead, and corrupt useful knowledge. To address this gap, we introduce Knowledge Evolution from Expertise and Lessons (KEEL), an agent-agnostic framework that uses verifier evidence to transform successful behavior into reusable skills and failures into corrective lessons. As new evidence accumulates, individual skill claims can be supported, contradicted, replaced, or retired. On SkillFlow benchmark, KEEL improves task success by 4.2 to 21.7 percentage points over the no-knowledge baseline, compared with gains of 2.4 to 9.6 points from SkillFlow's default method. Ablations show that skills and lessons are complementary. These results show that reliable continual agent learning depends not simply on accumulating experience, but on continually validating and evolving the knowledge derived from it. Our code is available at: this https URL.

---


### 180. [Minimax Regret for Sobolev Kernel-Based Reinforcement Learning](https://arxiv.org/abs/2610.34045)

**<font color=#1a73e8>作者：</font>** Haichen Hu, David Simchi-Levi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the minimax regret rate for episodic kernel-based reinforcement learning, where the expected reward and transition density belong to a Sobolev reproducing kernel Hilbert space, with continuous state and action spaces, and adversarial initial states. For Sobolev smoothness parameter $\nu>0$, state dimension $d_S$, and action dimension $d_A$, we prove that the minimax expected regret over $T$ episodes is $\widetilde\Theta(T^{\max\{e_A,e_B\}})$, where $e_A=\frac{\nu+d_A}{2\nu+d_A}$, $e_B=\frac{\nu+d_A+3d_S/2}{2\nu+d_A+2d_S}$ with the other model parameters fixed. The two exponents reflect the distinct difficulties of action selection and learning across states. We introduce Sobolev Optimal Value Iteration (SOVI), which attains this rate from observed rewards and transitions. For fixed smoothness and reference-kernel lengthscale, its regret bound has a prefactor polynomial in the state-action dimension $d=d_S+d_A$, horizon $H$, transition and reward RKHS norm bounds $u,B_r$, and kernel norm-comparison factor $\Lambda$, up to logarithmic factors. The algorithm separates initial action selection from continuation-value estimation and combines local polynomial approximation with the shared RKHS structure of the approximation errors. Our matching upper and lower bounds determine the optimal dependence on the number of episodes for Sobolev kernel-based reinforcement learning. Thus, we partially address the open problem in Vakili(2024) under the condition of the Sobolev kernel setup.

---


### 181. [Leveraging Dale's Principle as an Inductive Bias in Recurrent Neural Networks](https://arxiv.org/abs/2610.34052)

**<font color=#1a73e8>作者：</font>** Jiyi Wang, Chenxiao Yang, Yujia Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the fundamental differences between biological neural networks and artificial neural networks (ANNs) is that biological neurons obey Dale's principle: each neuron projects either exclusively excitatory or exclusively inhibitory outputs. While this constraint is central to biological circuits, previous attempts to impose Dale's principle in ANNs have often led to training instability or degraded performance. In this work, we introduce EISep RNN, a recurrent neural network architecture that implements Dale's principle through a learnable excitatory-inhibitory separation. Across a series of learning settings, including multi-task learning, continual learning, and reinforcement learning, EISep achieves more stable training dynamics, competitive or improved performance, and sparser, more modular connectivity than vanilla RNNs and previous Dale-constrained models. EISep also exhibits stable and informative latent dynamics. These results establish Dale's principle as a biologically grounded and computationally effective inductive bias for recurrent neural networks.

---


### 182. [Back to Basics: Formal Analysis Hints Improve Weak-to-Strong Monitoring](https://arxiv.org/abs/2610.34064)

**<font color=#1a73e8>作者：</font>** Daniel Ben-Levi, Judah Goldfeder, Mateusz Dziemian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Frontier agentic systems are capable of taking misaligned actions that may cause significant harm. Monitoring techniques are developed to oversee these systems in order to detect and prevent dangerous actions. However, current state-of-the-art monitors suffer from four persistent failure modes: complete detection failures, partial detections, accepting false benign framings, and suspicion score calibration errors. These failure cases can be efficiently combated by augmenting transcripts with supplementary hints, spanning command provenance, security-sensitive action flags, and task-disallowed effect markers. Provenance links allow for the recognition of diffuse attacks, while security and authorization flags simultaneously enable subtle attack recognition and provide an explicit reason for monitors to doubt the false benign framings they encounter, reducing rationalization and improving calibration. We find that augmenting weak extract-and-evaluate monitors with these hints significantly boosts performance with minimal computational cost. Furthermore, a failure mode analysis confirms that hints can remediate all four failure modes, notably almost entirely eliminating detection failures. A series of ablation studies emphasizes the efficiency and potential of the augmented extract-and-evaluate approach. Synthesizing our findings, we propose a tractable two-pronged approach toward enabling weak-to-strong monitoring.

---


### 183. [Learning the Autoregressive: Direct Score-Difference Estimation with Amortized Future Credit for Video Distillation](https://arxiv.org/abs/2610.34092)

**<font color=#1a73e8>作者：</font>** Zixuan Duan, Yabo Chen, Xunzhi Xiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distillation for autoregressive (AR) video generation commonly first initializes an AR student and then refines it with distribution matching distillation (DMD). This refinement process faces two challenges. First, although initialization already yields a reasonably capable student, DMD obtains the refinement direction indirectly by estimating the full student score before forming the teacher-student correction. Second, detached-history training prevents the generator from assigning credit to a current chunk for its influence on subsequent chunks. We introduce Leta, a few-step distillation framework that addresses these challenges with ScoreDelta and FutureCredit. ScoreDelta directly estimates the teacher-student correction from denoising residuals, while FutureCredit learns an auxiliary cross-chunk update signal from vector-Jacobian products (VJPs) of next-chunk teacher residuals. Leta combines these signals into a joint teacher-guided update field in a single forward pass during generator updates. Teacher evaluations and credit VJPs are used only for estimator training. For ScoreDelta, we establish population equivalence to score-difference estimation and a conditional approximation advantage under limited capacity in a fixed-feature linear model. In our controlled experiments, Leta improves over DMD by 0.9 points on VBench and 0.66 on VideoAlign. This advantage persists at a higher generator update frequency (a generator-to-estimator update ratio of G:E=1:1), where Leta improves over DMD by 1.6 on VBench and 0.35 on VideoAlign. Project page: this https URL.

---


### 184. [LegoOcc++: Towards Consistent Open-Vocabulary 3D Occupancy Prediction](https://arxiv.org/abs/2610.34093)

**<font color=#1a73e8>作者：</font>** Changqing Zhou, Yueru Luo, Han Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D occupancy prediction is important for embodied agents operating in complex environments whose semantic categories extend beyond fixed taxonomies. While recent studies have explored open-vocabulary occupancy in outdoor driving scenarios, indoor environments remain challenging due to dense occlusions, complex geometry, and fine-grained long-tailed semantics. To reduce the need for expensive voxel-level semantic annotations, we study a geometry-only supervision setting requiring only binary occupancy labels. We build upon Language-Embedded Gaussians as a unified representation coupling 3D geometry with language-aligned semantics. For geometry learning, we introduce an opacity-aware Poisson-based Gaussian-to-Occupancy formulation that enables stable volumetric aggregation under binary occupancy supervision. For semantic learning, we render Gaussian features into images and align them with a frozen open-vocabulary model, together with Progressive Temperature Decay to reduce feature mixing during Gaussian splatting. Building on this framework, we further introduce Instance-Level Semantic Consistency to alleviate fragmented object predictions, and Covisibility-Aware Support-View Selection to provide informative and less redundant multi-view semantic supervision. We also extend our framework to outdoor driving scenarios to evaluate its generality across substantially different environments. Extensive experiments on indoor and outdoor benchmarks demonstrate that our method achieves strong open-vocabulary occupancy performance, validating the effectiveness and generality of our framework. Code will be available at this https URL.

---


### 185. [BE-CTDE: Blockchain-Enabled Multi-Agent Reinforcement Learning with Anomaly Detection and Token Economics](https://arxiv.org/abs/2610.34121)

**<font color=#1a73e8>作者：</font>** Chih-Wei Huang, Hsin-Chieh Lee, Yun-Chen Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning supports cooperative decision-making in Internet of Things systems, but strategic deviations can disrupt coordination and undermine confidence in the training process. This paper proposes Blockchain-Enabled Centralized Training and Decentralized Execution (BE-CTDE), which uses blockchain as an active training-management layer. A behavioral verifier compares executed trajectories with shared-policy recommendations; its flags drive a token mechanism combining slashing, burning, rewards, and compensation. Retained balances determine each agent's contribution to the global policy update, connecting auditable behavior to learning influence. We derive a one-round incentive condition that accounts for action-dependent compensation and the payoff from deviation, and a finite expected exclusion-time bound under explicit conditional detection and accounting assumptions, showing perfect detection is unnecessary. An exact finite-population capacity bound characterizes the limits of the population-relative detector. In multi-agent path finding experiments, BE-CTDE outperforms a state-of-the-art learning-based path planner with substantially higher success rates under attack, even when adversaries form the majority. It also outperforms partially defended baselines in all configurations, with collision rates up to 35% lower than under detection without economic consequences and up to 43% lower than under conventional stake slashing. Together, these results characterize how behavioral verification and token feedback can support accountable cooperative learning.

---


### 186. [Enhancing Type 2 Diabetes Diagnosis with Evolutionary Algorithms and Machine Learning](https://arxiv.org/abs/2610.34123)

**<font color=#1a73e8>作者：</font>** Parisa Rezaei, Mohsen Saffar, Hamid Reza Naji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Type 2 diabetes is a widespread chronic disease that requires early and accurate diagnosis to prevent serious complications. Traditional diagnostic methods often lack sufficient accuracy, which highlights the need for more reliable computational solutions. In this study, we propose a model that integrates the Random Forest classifier with the Bat Optimization Algorithm for simultaneous feature selection and hyperparameter tuning. The SMOTE-ENN method was first applied to the Pima Indians Diabetes Database to correct class imbalance and remove noisy or ambiguous samples, producing a more balanced and cleaner dataset. The optimized model trained on this refined dataset achieved 89% accuracy, 88% precision, 90% recall, and an F1-score of 89%, clearly outperforming the baseline Random Forest and other existing approaches. These results demonstrate the potential of combining evolutionary algorithms with ensemble learning to provide a practical and cost-effective tool for early detection of type 2 diabetes in clinical practice.

---


### 187. [StickFigure: Enabling Pose-Only IoT Cameras for Privacy-Preserving Edge Vision](https://arxiv.org/abs/2610.34130)

**<font color=#1a73e8>作者：</font>** Aveline Xiaoyuan Han, Chenshu Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor IoT cameras can support assisted living and activity-aware spaces, but exporting raw RGB frames raises privacy concerns by exposing facial, clothing, and household details that body-motion tasks often do not require. We present StickFigure, a pose-only IoT camera system that, during real-time monitoring, keeps raw frames local and ephemeral while exporting only compact skeleton streams sufficient for downstream human activity recognition (HAR). While pose estimation has matured on GPUs, extracting accurate pose streams on resource-constrained IoT cameras remains difficult. To overcome these challenges and enable on-device pose streams on (almost) any IoT camera, we present two core designs in StickFigure: an activation-aware pose backbone that allocates channel capacity after spatial downsampling and a lightweight hierarchical MLP refiner that selectively corrects elbow and wrist coordinates using intermediate visual features and kinematic context. We fully implement StickFigure and evaluate it on public benchmarks and real-world deployment. Compared with state-of-the-art MCU pose models, StickFigure achieves the highest pose accuracy and downstream HAR utility on both NTU RGB+D and Penn Action, while using 96.5% fewer parameters and 99.3% fewer MACs per frame than RTMPose-S-based baselines, achieving 0.107 s p95 latency on a representative STM32H753 MCU. We believe StickFigure establishes a new operating point for privacy-aware edge vision on massive IoT cameras.

---


### 188. [Decoupled Prune-and-Reconstruct: Training on a Compact Core with Double-Layer Sparsification](https://arxiv.org/abs/2610.34140)

**<font color=#1a73e8>作者：</font>** Siqi Gu, Gaozhen Ma, Liheng Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On million-node graphs, the memory wall arrives before the compute wall: a GNN that never fits in VRAM cannot deliver the all-node inference its accuracy promises. The standard remedy, pruning, has always been an accuracy tax - paid once and never refunded. DPR refuses this framing. Its central insight is that the mask that shrinks training can also scaffold recovery: one compact node set bounds both computations of graph learning, serving as the encoder's training graph and, at inference, as the anchor from which a sparse structure-aware decoder rebuilds every pruned node (double-layer sparsification). The order is inverted - prune for efficiency, then reconstruct for accuracy - and the tax is repaid: the deployed 30%-budget model trains in 1,450 MiB of peak memory on one 6 GB GPU and recovers 96.9% of its dense-reconstruction reference, beating a same-GPU rerun of the edge-sparsification baseline DSpar by +1.36 pp at 50.1% lower peak training memory; against the same-protocol full-batch no-prune encoder the deployed point pays a measured 2.64 pp accuracy tax for a 2.8x smaller training footprint. Pruning without reconstruction leaves the encoder at 0.378 within the same 40-epoch window (Fig. 4), and all-node serving runs 46x faster than sampling-based GraphSAGE, giving up approx. 5.4 pp of test accuracy. The framework scales to a 2.45M-node production graph at 6,285 MiB of peak training memory; extended variants (long-range context, external text features, a CAN-bus application) are reported as extensions and do not compete with the deployed method, and the 41.8%-budget M4 point, scored on a coarsened super-node graph with its own split, is reported separately rather than compared with the original-node baselines. DPR thus turns aggressive node pruning from an accuracy tax into a safe training accelerator for VRAM-limited all-node inference.

---


### 189. [Reversion, Retention, and Semantic Intervention: Measuring Functional Content in CLIP Fine-Tuning Deltas](https://arxiv.org/abs/2610.34144)

**<font color=#1a73e8>作者：</font>** Chih-Ting Liao, Kezhen Bao, Xin Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning adapts pretrained models to new tasks, but identifying which weight changes support the resulting behavior remains difficult. Weight-space interpretability assigns semantic descriptions to these changes, called fine-tuning deltas. Such descriptions leave open how much task performance depends on the identified updates, particularly when other updates can support the same predictions. We address this gap by pairing reversion, which restores selected parameters to their pretrained values, with retention, which keeps only selected fine-tuning updates. We evaluate Contrastive Language-Image Pretraining (CLIP) models on synthetic financial charts, Flowers102, EuroSAT, and FGVCAircraft with ViT-L/14, and on Flowers102 with ViT-B/16, using a shared recipe that tunes the final six visual blocks. Our contributions are threefold. First, attention value-output (VO) updates alone recover 43-87% of the accuracy improvement, although reverting them leaves chart accuracy unchanged. Cross-entropy loss preserves this contrast on Charts and EuroSAT, while correct-class score margins reveal additional contributions. Second, VO weights recover more loss improvement than all ten equally sized, layer-matched random subsets in each setting. VO and multilayer perceptron (MLP) retentions jointly correct 25-81% of pretrained errors, demonstrating overlapping recovered behavior, which we call operational redundancy. Third, removing semantically selected directions reduces VO-retained recovery more than matched-random removal in all five settings. Together, these results distinguish semantic alignment, removal cost, and retained recovery as complementary evidence about the functional role of fine-tuning updates within the evaluated CLIP recipe.

---


### 190. [MuSTEL: A Large-Scale Multilingual Synthetic Text-Line Image Dataset for OCR](https://arxiv.org/abs/2610.34148)

**<font color=#1a73e8>作者：</font>** Majid Adibian, Hossein Saberi, Hossein Zeinali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical character recognition (OCR) systems depend strongly on the scale and diversity of their training data. One approach to document OCR first analyzes the page layout and extracts text-line images, which are then transcribed by a recognition model. Multilingual line-level recognition involving Persian, Arabic, and English presents additional challenges because different writing directions, fonts, and styles may coexist within a single line. This paper introduces MuSTEL, a large-scale synthetic multilingual OCR dataset containing more than 14.5 million annotated text-line images, organized into a training partition and predefined small and large test sets. Samples are generated from natural-language corpora, including multilingual content already present in the source texts. The generation framework incorporates capability-aware font selection, within-line font and style changes, mixed-direction text rendering, highlighting, and underlining. A validated repository of 2,009 font files from 711 families supports broad typographic coverage, while varied backgrounds, blur, geometric distortion, skew, stroke width, and image save quality provide diverse document-like appearances. Statistical analysis characterizes the dataset's language composition, transcription lengths, lexical and character-sequence diversity, image dimensions, typography, and rendering conditions. MuSTEL provides a resource for training and evaluating multilingual line-level OCR systems and investigating recognition robustness across languages, writing directions, and visual conditions.

---


### 191. [Edge-Centric Adaptive Neural Activation via Parametric Tanh Functions](https://arxiv.org/abs/2610.34154)

**<font color=#1a73e8>作者：</font>** Andreas Falkenberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Within the broader landscape of artificial intelligence architectures, this paper introduces a compact, edge-centric neural framework that resolves the computational bottlenecks of modern edge-activated paradigms like Kolmogorov-Arnold Networks (KANs) while retaining their expressiveness over traditional Multi-Layer Perceptrons (MLPs). While KANs demonstrate remarkable representational capacity by placing learnable univariate functions on connection edges rather than hidden nodes, their reliance on non-local B-splines introduces severe optimization hurdles, high memory overhead, and poor hardware scaling. To bridge this gap, we propose the Parametric Tanh Connection Function, a smooth, bounded architectural primitive defined as $a_{\tanh}(x;\delta,\alpha,\beta,\gamma) = \delta + \alpha \tanh(\beta x + \gamma)$. This formulation unifies offset, amplitude, local slope, and horizontal displacement into a lightweight, 4-parameter differentiable mapping optimized edge-by-edge via backpropagation. Evaluated on dense architectures using MNIST and CIFAR-10, our parametric tanh connection model achieves significant absolute accuracy gains over traditional affine baselines-reaching 95.63% $\pm$ 0.08% on MNIST and 44.74% $\pm$ 0.18% on CIFAR-10. Crucially, it matches or exceeds the expressiveness of unconstrained 7-parameter exponential connection baselines while requiring up to 85% less training runtime. By replacing complex splines or hyper-flexible exponents with a bounded, analytically smooth hyperbolic tangent kernel, this work delivers a highly scalable, hardware-friendly compromise for heterogeneous connection-level deep learning.

---


### 192. [Single-Cycle Battery Remaining Useful Life Prediction with Compressed Continuous Wavelet Features and Deep Neural Networks](https://arxiv.org/abs/2610.34159)

**<font color=#1a73e8>作者：</font>** Sungeun Kim, Mingyu Jung, Yuri Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lithium-ion batteries are widely used in industrial applications, but their performance gradually degrades over time, making accurate lifetime prediction important for safety and reliability. However, reliable lifetime assessment generally requires extensive degradation testing, which is both costly and time-consuming. To reduce this burden, recent data-driven approaches have sought to predict the end-of-life cycle of batteries from only the initial few cycles. Nevertheless, identifying reliable degradation patterns from such limited early-cycle data remains challenging because early aging dynamics are often subtle and nonlinear. To address this issue, we adopt the continuous wavelet transform to convert cycle-wise voltage, current, and capacity signals into time-frequency representations, enabling multi-resolution characterization of degradation behavior. Building on this representation, we apply scale compression to reduce redundancy while preserving structural information in the scalograms. We evaluate the proposed framework on eight benchmark datasets derived from seven public battery datasets covering diverse electrode chemistries, cell form factors, and cycling protocols. Experimental results show that the proposed framework consistently outperforms prior approaches in single-cycle remaining useful life prediction and remains robust as the number of input cycles increases from 1 to 100. In addition, redundancy-fidelity analysis characterizes the trade-off introduced by scale compression, and gradient-based visual explanations indicate that the model focuses on localized time-frequency regions associated with structured signal transitions during charge-discharge operation. These results demonstrate the effectiveness and interpretability of the proposed framework for early-cycle battery remaining useful life prediction.

---


### 193. [Reinforcement Learning for Adaptive Crowd Flow Control Using Dynamic Barriers](https://arxiv.org/abs/2610.34163)

**<font color=#1a73e8>作者：</font>** Alhanof Alolyan, He Wang, Amani Alonayzan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crowd barriers are widely used to regulate pedestrian movement during large public events such as pilgrimages. However, fixed barrier layouts often create unnecessary stopping and local congestion even when they successfully control the overall crowd flow. Finding better barrier configurations is difficult because there is no dataset that provides the best barrier placement for a given crowd scene. We address this challenge by introducing a simulation-driven reinforcement learning framework that learns barrier configurations without requiring labelled training data. Starting from a segmented crowd scene, we construct a realistic simulation environment that reproduces the observed pedestrian distribution. This environment is then used to train a Soft Actor-Critic (SAC) agent that continuously adjusts barrier positions to improve pedestrian movement. Unlike supervised approaches the proposed framework allows the agent to explore barrier configurations that have never been observed in real data. We evaluate the learned policy under unseen numbers of pedestrians. The learned policy consistently outperforms the existing manually designed barrier configuration by reducing pedestrian stops while maintaining effective flow regulation. These results demonstrate that combining computer vision crowd simulation and reinforcement learning provides an effective framework for optimizing crowd control infrastructure.

---


### 194. [Reasoning or Just Prompting? Probing the Mechanism of Latent Chemical Reasoning](https://arxiv.org/abs/2610.34173)

**<font color=#1a73e8>作者：</font>** Kaiyuan Lu, Jiatong Li, Yatao Bian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent reasoning performs intermediate computation in continuous space rather than through explicit tokens, which is particularly appealing in chemistry, where errors in explicit reasoning can propagate to the final answer. Yet if latent states truly constitute an implicit reasoning chain, they should be causally important. We find otherwise: swapping or moderately perturbing intermediate latent states has little effect on performance, while removing them entirely sometimes causes a substantial score drop. Thus, the latent states matter, but their molecule-specific content appears to matter far less. This points to a simpler interpretation. Rather than encoding a step-by-step reasoning chain, latent states may primarily steer subsequent model computation, much like soft prompts. Indeed, a single fixed prefix shared across molecules reproduces LatentChem's performance, and a learned static soft prompt performs comparably to per-input latent generation in controlled models. The tolerance of latent sequences to substitution and moderate perturbation further supports this connection. We therefore suggest that latent chemical reasoning may be better viewed as soft prompting than as a reasoning chain hidden in continuous space.

---


### 195. [Write What Matters: Disentangling Token Selection from Slot Allocation in Recurrent Memory](https://arxiv.org/abs/2610.34180)

**<font color=#1a73e8>作者：</font>** Chen Chen, Rui Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-sequence models must retain earlier information. Full attention keeps all past tokens but grows expensive, and recurrent-memory models compress history into fixed slots for linear-time processing. Limited capacity makes writes consequential: distractors can interfere with useful content, while skipped evidence cannot be recalled. Existing multi-slot memories write every token to the same number of slots, merging whether to store it with how many slots to update. We introduce Factorized Write Routing (FWR), which first keeps or skips each token and then chooses a fixed or token-adaptive number of slots. Queries still read all slots. Across ten seeds on two synthetic tasks that query facts after long contexts, we observe a density-dependent reversal. With four slots per write, long-context accuracy favors always writing on dense Feature Recall (0.472 vs 0.337), but learned selective writing on sparse-fact Passkey (0.222 vs 0.048). The tested adaptive rule underperforms fixed allocation under the learned gate on both tasks. A diagnostic oracle given fact labels unavailable at deployment reaches 0.372 on Passkey, showing headroom in filtering distractors. The results suggest avoiding missed writes in information-dense contexts and filtering distractors when they dominate.

---


### 196. [GeoPrompt: Geometry-Conditioned Prompt Learning for Underwater Open-Vocabulary Instance Segmentation](https://arxiv.org/abs/2610.34190)

**<font color=#1a73e8>作者：</font>** Shanshan Han, Yuxi Wang, Can Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary instance segmentation (OVIS) provides a promising solution for marine perception by recognizing and segmenting categories beyond predefined label spaces. Existing OVIS methods usually rely on vision-language alignment, where visual region features are matched with textual category embeddings to recognize both seen and unseen classes. However, this alignment assumption becomes fragile in underwater environments. Color attenuation, scattering, turbidity, and low contrast distort visual appearance, causing region features to deviate from their corresponding semantic concepts. As a result, the similarity between degraded visual features and textual classifiers becomes unreliable, which particularly weakens the recognition of unseen underwater categories that cannot be corrected by category-specific supervision. To address these issues, we propose GeoPrompt, a geometry-conditioned prompt learning framework for underwater open-vocabulary instance segmentation. Our key insight is that geometric structure is more stable than visual appearance in degraded underwater scenes. Specifically, GeoPrompt introduces a geometry-guided visual adaptation module (GVAM) to extract depth-derived structural priors and inject them into multi-scale visual features. It further develops a geometry-conditioned prompt learning (GCPL) that generates geometry-aware textual classifiers from structural representations. These geometry-aware classifiers are integrated with fixed and image-conditioned textual classifiers to improve open-vocabulary semantic alignment. Experiments on the MARIS-OpenIS benchmark show that GeoPrompt achieves state-of-the-art performance and brings consistent improvements on underwater open-vocabulary instance segmentation.

---


### 197. [CORMA: Constraint-Routed Decision Mamba for Generalizable Multi-Constraint Offline Safe Reinforcement Learning](https://arxiv.org/abs/2610.34208)

**<font color=#1a73e8>作者：</font>** Changxu Ni, Feiran You, Yongan Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline safe reinforcement learning (RL) learns safety-aware policies from static datasets while satisfying safety constraints during deployment. Motivated by the strong trajectorymodeling capabilities of Transformers, recent Decision Transformer (DT)-based methods formulate offline safe RL as conditional sequence modeling by conditioning action generation on return-to-go (RTG) and cost-to-go (CTG) tokens, thereby enabling adaptation to varying safety budgets. However, existing DT-based methods are developed for single-constraint tasks. For tasks with multiple constraints, generalizing learned policies to unseen combinations of safety budgets remains challenging due to the conflicting requirements imposed by heterogeneous constraints. Moreover, the quadratic complexity of Transformer architectures significantly increases the computational overhead in multi-constraint tasks, as representing additional constraints requires more CTG tokens. Recently, Mamba has emerged as an efficient sequence-modeling backbone, offering linear computational complexity and strong generalization capabilities. In this paper, we propose CORMA, a constraint-routed decision Mamba framework for generalizable multi-constraint offline safe RL. CORMA decomposes policy inference into constraint-aware RTG estimation and adaptive action generation, where constraint-specific experts model feasible RTG distributions and a router-guided product-of-experts mechanism fuses these distributions to provide safety-aware guidance for a Mamba-based action decoder. A three-stage optimization strategy is designed to improve training stability. Extensive experiments on OSRL benchmarks demonstrate that CORMA achieves superior reward-safety trade-offs, reduces inference latency by 37% compared with DT-based methods, and exhibits stronger zero-shot generalization to unseen safety-budget combinations than offline safe RL baselines.

---


### 198. [StaX-Net: Stackelberg Interleaved Asymmetric Network for Cross-Modality Medical Image Translation](https://arxiv.org/abs/2610.34214)

**<font color=#1a73e8>作者：</font>** Amin Golnari, Saeid Sanei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modality medical image translation is challenged by anatomically inconsistent synthesis that can compromise clinical diagnosis. We propose StaX-Net, a Stackelberg interleaved asymmetric network that incorporates a partially coupled encoder-discriminator structure, and a 2D feature aggregation and spatial transformation (FAST) layer that distills target-supervised priors under the learning using privileged information paradigm. The shared blocks between the generator and discriminator enhance architectural feature alignment. To stabilize the leader-follower training, a Stackelberg-inspired asymmetric optimization scheme employs explicit shared-parameter freezing and asymmetric learning rates. The FAST layer distills target-domain priors during training and applies a source-only transform at inference. This constrains the synthesis process through target-informed feature representations relative to standard generative architectures. The code is available on GitHub for public use.

---


### 199. [Synthetic linguistic data](https://arxiv.org/abs/2610.34215)

**<font color=#1a73e8>作者：</font>** Giuseppe Samo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic linguistic data have become increasingly prominent in linguistic research, from the analysis of large collections of AI-generated texts to controlled experiments investigating grammatical and lexical preferences. This glossary entry extends Bresnan's (2016) distinction between the linguistic garden and the bush by introducing an artificial plant nursery as a metaphor for synthetic data. We distinguish between synthetic bush data, consisting primarily of corpus-like collections of model-generated language, and synthetic garden data, in which model outputs are elicited under controlled conditions to investigate specific linguistic hypotheses. We argue that synthetic data constitute a distinct object of linguistic investigation: comparing them with natural language data can reveal both shared patterns and divergences, but their interpretation requires careful consideration of the conditions under which they are generated.

---


### 200. [Interpretable and Steerable Molecular Graph Generation using Concept Bottlenecks](https://arxiv.org/abs/2610.34227)

**<font color=#1a73e8>作者：</font>** Sarabeshwar Balaji, Ritesh Kumar, Lav R. Varshney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep graph generators (DGGs) largely lack interpretability, which is a significant limitation for one of their most crucial applications, drug discovery, where interpretable and transparent generation could provide greater control over the desirability of generated molecules, thereby reducing trial-and-error in candidate selection. Common approaches to interpretability, such as disentanglement, cannot guarantee that the learned representations are human-interpretable. To address this, we propose incorporating concept bottlenecks into DGGs, allowing users to interpret, debug, and steer the generation process. We show that this consistently improves distributional fidelity (lower FCD), with only modest, non-systematic effects on validity and uniqueness. We further explore Concept Controller, an optimization-based steering approach that has proven to be effective for steerable image generation. We evaluate our approach on a one-shot molecular graph generation framework, though the underlying ideas can be transferred to sequential graph generation as well.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
