# 📦 其他研究 | 2026年06月24日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-219](./part-05.md)

---

### 1. [ModTGCN: Modularity-aware Graph Neural Networks for Text Classification](https://arxiv.org/abs/2606.23694)

**<font color=#1a73e8>作者：</font>** Rajarshi Misra, Aditya Sharma, Vinti Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph-based text classification models typically rely on local neighborhood aggregation and overlook global community structure, despite semantic document graphs exhibiting strong class-consistent clustering. Ignoring this can blur class boundaries and lead to over-smoothing. We propose ModTGCN, a modularity-aware graph neural network for text classification that jointly optimizes cross-entropy and a modularity-based auxiliary objective to promote class-coherent document communities while preserving discriminative representations. The modularity term is computed on a document-document similarity graph derived from transformer embeddings (pretrained or fine-tuned). To improve scalability, we decouple the original heterogeneous TextGCN graph into separate document-word and word-word components, achieving 2x-10x faster training. We further study graph construction strategies, label-aware edge reweighting, and supervision choices for modularity optimization. Experiments on five benchmarks show consistent gains, with larger improvements on complex, low homophily datasets such as Ohsumed and 20NG.

---


### 2. [A Geometry-Informed Computer Vision Method for Detecting and Examining Overtaking Vehicles From A Bicycle](https://arxiv.org/abs/2606.23699)

**<font color=#1a73e8>作者：</font>** Gandhimathi Padmanaban, Rayane Moustafa, Fred Feng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instrumented bicycle studies have produced direct field evidence on vehicle passing behavior, but extracting overtaking events from continuous rear-facing video has remained dependent on manual, frame-by-frame annotation. This bottleneck constrains sample sizes and limits naturalistic cycling safety research. We present a geometry-informed computer vision pipeline that automates overtaking event detection from a single bicycle-mounted camera without multi-sensor configurations or explicit camera calibration. The system combines RT-DETR object detection with ByteTrack multi-object tracking through a three-stage geometric validation module enforcing bearing angle trend, apparent size growth, and spatial confirmation criteria derived from perspective projection principles. Validated on 315 manually annotated real-world overtaking events from urban roads in Ann Arbor, Michigan, the pipeline achieved 97.8% recall with zero false positives. The system identified overtaking intentions a mean of 2.44 seconds before vehicle passage, with 84.1% of events exceeding the 1.5-second human reaction time threshold, demonstrating feasibility for active cyclist warning. Lateral passing distance measurements from 96 events revealed 33.3% of passes below the 5-foot (152.4 cm) threshold, consistent with non-compliance rates in prior field and self-reported studies. A preliminary calibration-free lateral distance estimation approach using bounding box geometric features achieved mean absolute errors of 13-14 cm under leave-one-out cross-validation, sufficient to distinguish close passes from standard passes for safety categorization. By automating event isolation from consumer-grade footage, the system removes the primary annotation bottleneck of instrumented bicycle research and provides a scalable foundation for vehicle-bicycle interaction analysis across larger datasets and diverse urban environments.

---


### 3. [Systematic Exploration of 4-Expert Heterogeneous Mixture-of-Experts via Automated Pipeline Search](https://arxiv.org/abs/2606.23739)

**<font color=#1a73e8>作者：</font>** Yashkumar R Lukhi, Harsh Rameshbhai Moradiya, Radu Timofte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an automated large-scale search pipeline for heterogeneous 4-Expert Mixture-of-Experts (MoE4) architectures within the LEMUR neural network dataset ecosystem. Building on a hand-crafted heterogeneous MoE reference model, we replace manual design with a deterministic code-assembly generator that systematically combines base architecture families drawn from the LEMUR database into MoE4 ensembles, each governed by a convolutional gating network with temperature scaling, mixup augmentation, and cosine-annealed learning rate scheduling. Over a 28-day campaign on an NVIDIA RTX 4090, the pipeline generated 4,463 candidate models across 197 batches, of which 1,021 were evaluated successfully. A critical finding emerged from the campaign: due to alphabetical enumeration via this http URL, the entire explored search space (4.8% of the theoretical 23,751 possible 4-family combinations) is anchored to a single family, AirNet. We characterise this coverage bias precisely, identify the root cause in the generator, and propose a stratified random sampling fix. Within the AirNet anchored scope, ShuffleNet and MobileNetV3 consistently co-produce the highest-accuracy ensembles (mean accuracy up to 0.632), while FractalNet and MNASNet are identified as low-yield families warranting exclusion in future campaigns. The pipeline, analysis artefacts, and corrected generator are released as part of the open-source NNGPT project at this https URL

---


### 4. [Weight-Space Geometry of Offline Reasoning Training](https://arxiv.org/abs/2606.23740)

**<font color=#1a73e8>作者：</font>** Aleksandr Nikolich, Igor Kiselev, Vladimir Platonov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement-learning losses (RFT, RIFT, DFT, Offline GRPO, DPO) are widely used to distill reasoning from large teachers into smaller students, and are typically compared on downstream accuracy alone. We ask whether they are mechanistically distinct or converge to a similar weight update. Training six methods (SFT, RFT, DFT, RIFT, Offline GRPO, DPO) on identical math rollouts from a single base model (Qwen3-4B) with attention-only LoRA, we analyze the resulting deltas via cosine similarity, principal-angle subspace analysis, linear mode connectivity, and CKA. We observe: (i) SFT, RFT, and RIFT have nearly colinear weight deltas (cosine >= 0.97, top-1 principal angle ~7 deg median over 144 modules) and comparable GSM8K accuracy (87-88%, n=1319; pairwise McNemar p >= 0.15); (ii) DFT diverges further in direction than any reward-weighted method despite using the same data; (iii) Offline GRPO adds a substantial component orthogonal to the SFT direction (~67% globally, up to ~86% in late layers) while staying in the SFT loss basin; (iv) DPO sits in a near-orthogonal subspace, shows a mode-connectivity barrier, and collapses late-layer CKA to ~0.46. DPO also reaches the highest accuracy in our protocol on both GSM8K (93.5%, McNemar p < 10^-9 vs. each other method) and AIME26 (30.0% vs. 3.3-10.0%); its training uses a 10x smaller learning rate than the others (the standard convention), so the update-norm and accuracy gaps reflect loss-function and optimizer choices jointly, and a learning-rate-matched DPO comparison is left for future work.

---


### 5. [A Survey on Federated Causal Discovery and Inference](https://arxiv.org/abs/2606.23741)

**<font color=#1a73e8>作者：</font>** Xianjie Guo, Yuwei Wang, Guodu Xiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal reasoning, which encompasses the discovery of causal structures and the inference of causal effects, is fundamental to data-driven decision making. In practice, data for reliable causal analysis are often distributed across institutions and cannot be centralized due to privacy regulations or communication constraints. Federated learning (FL) addresses this by enabling collaborative analysis without raw data sharing, giving rise to the rapidly growing field of federated causal discovery (FCD) and inference (FCI). However, the interdisciplinary nature of this field and the absence of a comprehensive survey present barriers to entry for researchers. This paper bridges that gap by providing a systematic review through multi-dimensional taxonomies. Grounded in the three core design decisions underlying any FCD solution, namely how structures are learned, how data are partitioned, and what structural knowledge each party obtains, we organize FCD along three axes: methodological paradigm, federation topology, and structural scope. We further examine key practical dimensions, including temporal dynamics, data heterogeneity, missing data, and non-identical variable sets. For FCI, we categorize methods by target estimand (average versus individualized/conditional treatment effects) and by estimation strategy, from classical weighting methods to modern deep generative architectures. Unlike prior works that treat FCD and FCI separately, we formalize their connection as complementary stages of a unified federated causal reasoning pipeline, where FCD supplies the structural knowledge required for valid effect estimation in FCI. Finally, we highlight their shared concerns regarding privacy, communication efficiency, theoretical guarantees, and application domains, and conclude by identifying open challenges for future research.

---


### 6. [Low-power analogue neural networks with trainable nonlinear connections for continuous control](https://arxiv.org/abs/2606.23742)

**<font color=#1a73e8>作者：</font>** Ian T. Vidamour, Fernando Aguirre, Thomas J. Hayward 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical neural networks promise low-power machine learning by computing directly with analogue device physics, but most architectures force nonlinear device responses to act as scalar weights. Inspired by Kolmogorov-Arnold networks, we place trainable nonlinear functions on the connections, making each physical connection a learnable computational element. Realising these functions as analogue band-pass filters on field-programmable analogue arrays, we find that the benefit is task-dependent and follows from the smoothness of the physical basis: the networks represent smooth, continuously valued targets, including robotic kinematics, continuous control, and photovoltaic maximum-power-point tracking, with far fewer nodes and connections than multilayer perceptrons, but offer no parameter-efficiency advantage on classification-like decision boundaries. Trained networks transfer to hardware across approximately 35,000 connections with quantified fidelity, and a dedicated CMOS implementation is projected to operate at approximately 30 microwatts. A memristive realisation reproduces the same behaviour in simulation, indicating that the advantage comes from placing trainable nonlinearity on connections, rather than from a particular device.

---


### 7. [Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation](https://arxiv.org/abs/2606.23743)

**<font color=#1a73e8>作者：</font>** Yitong Li, Junsong Chen, Haopeng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video diffusion models achieve higher generation quality through scaling, but this also increases inference cost. Although many acceleration methods have been proposed, a central challenge is that the most effective acceleration strategy is highly instance-specific: a recipe that works well for one combination of model, hardware, and inference configuration often does not transfer to another. Different models vary in architecture, numerical sensitivity, and attention concentration patterns. Inference settings differ in spatial and temporal resolution and video duration, while hardware platforms differ in memory hierarchy, supported numerical formats, and kernel throughput. These factors create a large tuning space, making manual performance engineering costly. We present Sol Video Inference Engine, an agentic, native, training-free acceleration framework for video diffusion models. It organizes five broadly applicable techniques, cache, sparse attention, token pruning, quantization, and kernel fusion, into an agentic acceleration stack for instance-specific optimization. For a concrete deployment target defined by a model, hardware platform, and serving configuration, parallel skill agents optimize the implementation of each technique, an agent integrator composes them into a global acceleration stack, and a human validator provides feedback on generation quality. We instantiate this workflow on three video models with different sizes and architectures: 64B Cosmos3-Super, 22B LTX-2.3, and 2B SANA-Video. With little human effort, the full stack achieves more than 2x end-to-end acceleration while maintaining near-lossless VBench quality, demonstrating the effectiveness of the agent framework for video diffusion acceleration.

---


### 8. [Synergizing Physically Constrained MCMC and Chemical-Informed Gaussian Processes for Reaction Network Discovery](https://arxiv.org/abs/2606.23757)

**<font color=#1a73e8>作者：</font>** Runzhe Liu, Zihao Wang, Wenbo Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extracting interpretable governing equations from sparse, noisy chemical time-series data remains difficult because discrete reaction topology and continuous kinetic parameters are tightly coupled. We present PC-MCMC-CIGP, a reproducible gray-box workflow that combines spike-and-slab topology sampling, hard conservation and thermodynamic screening, and a Chemical-Informed Gaussian Process (CIGP) residual model for parameter calibration and experimental design. The methodological contribution is not a new MCMC or GP family in isolation; rather, it is the integration of these components into a physically constrained workflow with explicit uncertainty-aware acquisition choices. On the H2 + Br2 benchmark, the constrained sampler distinguishes elementary radical pathways from deceptive phenomenological fits in our experiments. On styrene epoxidation, the CIGP optimization loop improves final yield by 12.5% over the reported GP-BO baseline. A new 10-seed acquisition study shows that EI, GWU, PC-EI, uncertainty sampling, discrepancy hunting, and random search have different trade-offs: PC-EI substantially reduces low-yield BO suggestions, while EI-style criteria give the strongest final-yield performance.

---


### 9. [Exploring Dualistic Meta-Learning to Enhance Domain Generalization in Open Set Scenarios](https://arxiv.org/abs/2606.23758)

**<font color=#1a73e8>作者：</font>** Xiran Wang, Jian Zhang, Lei Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain generalization learns from multiple source domains to generalize to unseen target domains. However, it often neglects the realistic case of label mismatch between source and target. Open set domain generalization is then proposed to recognize unseen classes in unseen domains. A simple approach trains one-vs-all classifiers to separate each class and detect outliers as unknown. Yet, the imbalance between few positive samples and many negative samples skews the decision boundary towards the positive ones, leading the model to over-reject out-of-distribution data, even from known classes in unseen domains. In this paper, we propose a novel meta-learning stategy called dualistic MEta-learning with joint DomaIn-Class matching (MEDIC), which considers implicit gradient matching towards inter-domain and inter-class task splits simultaneously to find optimal boundaries balanced for both domains and classes. Experimental results show that MEDIC not only outperforms prior methods in open set scenarios, but also maintains competitive close set generalization ability.

---


### 10. [Listening makes Vision Clear for VLMs](https://arxiv.org/abs/2606.23763)

**<font color=#1a73e8>作者：</font>** Yiyang Chen, Yixin Tan, Binrui Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work typically assesses vision--language consistency using attention distributions of answer-side tokens. However, we observe that highest attention regions are not always consistent with the intended semantic token. This probably stems from decoding drift, where language priors from previously generated answer tokens accumulate and mismatch with visual attention. Besides the priors from previous answer tokens, we find that structural tokens, e.g., modality boundary markers, may encompass the entire context and generate high attention to areas unrelated to the target. To avoid these distortions and provide consistency evaluation for large VLMs, we adopt prompt-side semantics and propose Prompt-Vision Token Activation Map (PV-TAM). PV-TAM further incorporates a filter to remove systematic bias induced by modality boundary markers. Unlike traditional methods that evaluate overlap solely through masks while ignoring activation intensity, our metrics leverage the peak distribution of attention to measure the alignment between prompts and visual regions. In experiments, PV-TAM consistently improves both attention-based and IoU-style localization metrics over answer-side baselines on various datasets.

---


### 11. [One Ruler: A Same-Hands Re-Evaluation of Bivariate Causal Direction on Tuebingen, with a Parameter-Free Compression Baseline](https://arxiv.org/abs/2606.23767)

**<font color=#1a73e8>作者：</font>** Wietse Stienstra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Headline accuracies on the Tuebingen cause-effect pairs are routinely compared across papers even though each is measured under its authors' own protocol -- different pair subsets, weightings, model-selection, and decision rates. We argue this is the wrong comparison and run the right one: a same-hands re-evaluation in which every method is run by us on the identical 102 pairs, with one strict rule -- no tuning and a decision forced on every pair. As a clean reference point we introduce a deliberately minimal baseline: sorted-conditional compression, which feeds quantized, sorted, first-differenced data to an off-the-shelf compressor (bz2) and has zero fitted parameters. Under the common ruler the ranking differs sharply from the literature. Our baseline reaches 74.7% weighted accuracy (p = 3.7e-7); on the same 100 pairs that SLOPE is evaluated on it scores 76.0%, a 1.2-point gap below the authors' own forced-decision SLOPE (77.2%) that is well inside noise (McNemar p = 0.39). A faithful re-run of RECI lands at 70.7% -- inside the original authors' reported error bar, not the 77.5% often quoted (which we trace to a mis-copied cell). SLOPE's published 82.4% is a decided-subset figure: scoring the authors' own stored output only on the pairs its significance test chose to answer reproduces 81.7%. Under the common ruler the methods cluster in the low-to-mid 70s and the zero-parameter compressor ties the strongest of them. We document the mechanisms that inflate published figures (test-set model selection, significance-gated abstention) and contribute two further results: compression score magnitude is a model-free confounding flag (p = 2.8e-68), and a pre-registered falsification test fails in an instructive way that bounds the method's theoretical interpretation. Code, pre-registrations, and per-pair outputs are released.

---


### 12. [Cryptographic certificates of validity for trustworthy AI](https://arxiv.org/abs/2606.23768)

**<font color=#1a73e8>作者：</font>** Murdoch J. Gabbay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose cryptographic certificates of validity for agentic AI systems. The core idea is to formally specify a correctness or policy condition as a logical predicate, compile this predicate to a witness-checking problem over polynomial constraints, and use a succinct cryptographic proof system (and optionally zero-knowledge) to certify that the condition holds.
This offers a middle ground between formal verification of source code, and cryptographic authentication. An agent's action can be accompanied by an independently checkable proof that it satisfies an agreed formal policy, without requiring the verifier to trust the agent or to re-execute computation. We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer.

---


### 13. [From Spatial to Spectral: An Efficient, Frequency-Guided Feature Representation Learner for Small Object Detection](https://arxiv.org/abs/2606.23825)

**<font color=#1a73e8>作者：</font>** Yuhan Rui, Shihan Qiao, Yibin Lou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient small object detection is bottlenecked by the inherent feature scarcity of tiny targets, which is further aggravated by operations of spatial-domain detectors that indiscriminately discard critical high-frequency details. Recovering these fragile cues within the spatial domain is notoriously difficult, as it often requires computationally expensive architectural upscaling that inadvertently amplifies background noise. To bridge this gap, we propose a paradigm \textbf{shift from spatial to spectral} feature processing, introducing a holistic solution with the following novelty: (1) A versatile \textbf{Frequency-Guided Feature Representation framework} that generalizes across diverse detector architectures (both CNN and Transformer-based), offering a robust alternative to spatial-only feature extraction; (2) The unified \textbf{Decompose--Enhance--Reconstruct (DER)} operator, instantiated via three \textbf{lightweight, plug-and-play} modules -- Wavelet-Difference Gate (WDG), Log-Gabor Enhancer (LGE), and Frequency-Driven Head (FDHead) -- to systematically inject frequency-aware modulation into the backbone, neck, and head. This mechanism decouples feature modeling from resolution reduction, capturing discriminative high-frequency components to enable accurate localization with significantly reduced parameter redundancy; (3) Extensive validation on multi-domain benchmarks (VisDrone2019, UAVDT, TinyPerson, DOTAv1) demonstrating consistent gains. Notably, our proposed \textbf{DERNet} series outperforms YOLOv11 models under the same scale while requiring \textbf{only 1/6 of the parameters}, backed by rigorous spectral diagnostics and error decomposition analysis.

---


### 14. [Deciphering Fingerprints of 3D Molecular Surfaces for Accurate Epitope Prediction](https://arxiv.org/abs/2606.23830)

**<font color=#1a73e8>作者：</font>** Fang Wu, Weihao Xuan, Jure Leskovec 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular surfaces encode the geometric and physicochemical patterns that determine antibody-antigen recognition, central to epitope prediction. However, existing methods rely on sequences or backbone structures and struggle to capture discontinuous, surface-driven epitopes. This study presents SurfBind, a surface-centric learning framework for epitope prediction that operates directly on molecular surface representations. SurfBind integrates geometric and physicochemical cues through a Transformer-based architecture with patch-level surface modeling, binder-aware cross-attention, and a hierarchical coarse-to-fine prediction paradigm. Experiments on challenging epitope identification benchmarks, including SAbDab and DB5.5, demonstrate that SurfBind achieves state-of-the-art performance and strong generalization across unseen antibodies and conformational states, highlighting the value of interaction-aware surface modeling for understanding the crucial mechanisms of protein-protein interactions.

---


### 15. [Decentralized Coordination of Autonomous Traffic Through Advanced Air Mobility Corridors](https://arxiv.org/abs/2606.23832)

**<font color=#1a73e8>作者：</font>** Jasmine Jerry Aloor, Hamsa Balakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The use of dedicated corridors for Advanced Air Mobility (AAM) traffic is one of the most commonly proposed pathways to integrating them into existing airspace operations. Most prior research has focused on the design of networks of AAM corridors and conflict resolution for aircraft within corridors. It is also generally believed that while attractive from an implementation perspective, corridor-based operations may be inefficient, especially in the absence of centralized traffic management.
In this paper, we show that contrary to this belief, it is possible for autonomous aircraft to learn to self-organize into corridor flows in decentralized settings. We illustrate our approach using scenarios in which fixed-wing aircraft need to safely and efficiently traverse (1) a single corridor with metering after the exit, (2) a sequence of two consecutive corridors, and (3) a corridor that splits into two. We find that in decentralized settings with only local information, the aircraft are able to conform to the corridor boundaries more than 94% of the time and reach their goal in a relatively efficient manner. Furthermore, tactical interventions to handle violations of the separation minimum are needed only infrequently in low- and medium-density settings. However, such tactical interventions become more frequently necessary only when traffic density is high.

---


### 16. [The Degeneracy Distillery](https://arxiv.org/abs/2606.23838)

**<font color=#1a73e8>作者：</font>** T. Lucas Makinen, Deaglan J. Bartlett, Niall Jeffrey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When two or more parameters or labels produce similar data, they are degenerate, or hard to distinguish. Degeneracies render both label prediction and inverse problems difficult, since both machine learning algorithms and probabilistic samplers rely on the distinguishability of data and its gradients with respect to parameters. However, identifying degeneracies in physical models or real-world datasets can be elucidating about the choice of model or the underlying process that produces the data. We present the degeneracy distillery, a method that (1) detects and (2) resolves degenerate parameter combinations (a) automatically and (b) symbolically, from parameter-data (or parameter-simulation) pairs alone, through estimation and flattening of the Fisher information matrix. By exploring the information geometry of the likelihood, we characterize degeneracies as an intrinsic property of the physical model, requiring no realised data observation. We demonstrate our approach on a range of synthetic and real-world problems, discovering symbolic coordinate transformations that identify the combinations of parameters of a model which yield independent effects on the data. The resulting coordinates flatten the Fisher information in expectation globally, in contrast to posterior-based methods that flatten only at a single point, and substantially reduce the simulation budget required for downstream neural posterior estimation. In test cases we require up to $10\times$ fewer simulations for posterior estimation at matched validation calibration whilst simultaneously gaining physical insight on the system.

---


### 17. [Machine Learning Modeling for Real-Time Melt Pool Monitoring in Laser Powder Bed Fusion Additive Manufacturing: A Hybrid Approach](https://arxiv.org/abs/2606.23851)

**<font color=#1a73e8>作者：</font>** Inioluwa Emmanuel, Zhuo Yang, Ho Yeung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work investigates the implementation of artificial intelligence and machine learning (AI/ML) for real-time monitoring in laser powder bed fusion (LPBF) additive manufacturing. We developed a binary image classification framework for distinguishing normal and abnormal melt pool images using a balanced dataset of 1,200 images collected from Nickel superalloy 625 on the NIST AMMT platform. The study evaluates accuracy and inference time based on control requirements and hardware limitations of open-architecture LPBF machines. We benchmark three transfer learning architectures (ResNet50, EfficientNetB0, and MobileNetV2) against two Random Forest approaches: one trained on EfficientNetB0 feature embeddings (hybrid) and one trained on raw pixel features (baseline). Images are stratified into 80/20 train-test splits, with a further 90/10 validation split on the training set, and undergo standardized resizing, normalization, and label-preserving data augmentation to emulate realistic process variability. Each model is evaluated using accuracy, precision, recall, F1 score, and area under the receiver operating characteristic curve (AUC), along with training time, inference latency, and CPU & GPU usage to capture deployability constraints relevant to factory-floor monitoring. The hybrid EfficientNetB0-plus-Random Forest approach achieves the best performance on the held-out test set, with an F1 score of 0.9451, accuracy of 0.9458, and AUC of 0.9904, while maintaining sub-millisecond per-image inference (1.15 ms). In contrast, purely deep learning models exhibit significantly higher inference times with lower accuracy. These results demonstrate that combining pre-trained convolutional features with classical ensemble methods provides a robust, computationally efficient route to real-time melt pool anomaly detection in data-limited additive manufacturing environments.

---


### 18. [Sesame: Structure-Aware Molecular Generation via Spatial Density-Map Conditioning](https://arxiv.org/abs/2606.23856)

**<font color=#1a73e8>作者：</font>** Konstantin Yatsenko, Arvind Thiagarajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative molecular models for drug design are a promising direction with much active research. In the next phase of computational drug design, such models will need to understand small molecule structure and protein-ligand interactions, and they will need to possess the machinery to generate molecules \textit{de novo}. Incorporating each feature poses a critical challenge. Equally important, yet often treated as secondary, is the ability to grow a molecule from a partial starting point -- a scaffold or fragment supplied by a chemist -- which is the central operation of lead optimization. We present Sesame (Spatial Evoformer for a Structure-Aware Molecular Engine), a diffusion-based molecular generation model that leverages a novel spatial pairformer module to condition on partial molecular structure and the surrounding protein pocket, both expressed as continuous spatial density maps. This single conditioning mechanism supports both \textit{de novo} generation and fragment-conditioned lead optimization, letting a medicinal chemist prune a hit to a scaffold and have Sesame grow it in productive ways. In addition to this module, we also introduce a diffusion framework for joint denoising of atom types, bond types, and positions, along with a trajectory finetuning scheme that trains on the model's own sampling rollouts to improve generation quality. Sesame is trained on a large corpus of ligand-only and protein-ligand datasets.

---


### 19. [Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications](https://arxiv.org/abs/2606.23858)

**<font color=#1a73e8>作者：</font>** Merkouris Papamichail, Konstantinos Varsos, Giorgos Flouris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A primary challenge in AI safety is the existence of adversarial examples -- slightly distorted inputs that cause a neural network (NN) to misclassify. To mitigate this problem, recent research focuses on the computation of robustness certifications, which, for a given input, determine the largest distortion the input may receive without breaking the network's prediction. Robustness certifications can be interpreted as an axis-aligned hyper-rectangle (multi-dimensional intervals). Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. We introduce the apothem measure and show how to compute apothem-optimal certifications in a linear number of calls to a NN verifier (oracle) w.r.t. the input domain's diameter. Moreover, we prove that we cannot have a volume-optimal, oracle-based algorithm, even if we discard the oracle costs. Also, we introduce dual certifications -- an interval including all instances of a class -- thus providing apothem-minimum upper bounds to a robustness certification. Further, we present the ParallelepipedoNN system, which we evaluate on the standard MNIST and Fashion MNIST benchmarks. A preliminary comparison with existing work on the same datasets reveals at least two-fold improvement w.r.t. the minimum edge length.

---


### 20. [Exact Schur-Sylvester Dimensionality Reductions for Non-Smooth Stochastic Complexity and Manifold Sampling](https://arxiv.org/abs/2606.23867)

**<font color=#1a73e8>作者：</font>** Trenton Lau, Gary P. T. Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The exact computation of the Normalized Maximum Likelihood (NML) codelength for regular non-smooth estimators (e.g., Lasso) has been historically limited by the cubic scaling walls of manifold-constrained projection and volume integration. At each step of the geometric Propose-and-Project Metropolis--Hastings (PPMH) sampler, evaluating the projection operator requires inverting an $(N+k) \times (N+k)$ generalized KKT matrix, while calculating the volume factor requires the determinant of an $(N-k) \times (N-k)$ Gram matrix. This paper presents an exact, mathematically equivalent formulation that bypasses both bottlenecks by utilizing the block Schur complement and Sylvester's determinant identity. We prove that the computational complexity of both operations collapses from $\mathcal{O}(N^3)$ to $\mathcal{O}(k^3 + N^2 k)$ per step. We generalize this reduction to Sparse Support Vector Machines (SVMs), Elastic Net, and Group Lasso. Finally, we provide a rigorous numerical stability analysis and evaluate the sampler's efficiency using the Effective Sample Size (ESS) per second. Our empirical benchmarks on high-dimensional datasets confirm a constant speedup exceeding $14{,}100\times$ while maintaining double-precision numerical equivalence, rendering exact non-smooth NML estimation highly tractable for large-scale statistical inference.

---


### 21. [Federated Survival Analysis in Healthcare: A Multi-Model Evaluation on Cross-Institutional Heterogeneous Breast Cancer Data](https://arxiv.org/abs/2606.23871)

**<font color=#1a73e8>作者：</font>** Natalia Moreno-Blasco, Anusha Ihalapathirana, Pekka Siirtola 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Survival analysis is central to clinical decision-making, yet reliable time-to-event models require large, diverse cohorts that are rarely available at a single institution, while privacy regulations restrict the centralization of patient data. Federated learning (FL) offers a privacy-preserving alternative by training shared models without exchanging raw data, but its effectiveness for survival modeling under realistic, heterogeneous conditions remains insufficiently understood. This paper presents a systematic, multi-model evaluation of federated survival analysis on a cross-institutional breast cancer cohort with naturally heterogeneous distributed clients. Three representative survival models, the Cox Proportional Hazards model, DeepSurv, and Random Survival Forest (RSF), are compared across centralized, local, and federated training, and three federated optimization strategies (FedAvg, FedProx, and FedAdam) are assessed for the gradient-based models. Results show that FL consistently outperforms local training and approaches, and occasionally exceeds, centralized performance, while RSF offers the best overall balance of discrimination, calibration, and robustness across heterogeneous clients. We further find that performance depends on the diversity of client distributions, and that FedAvg and FedProx are stronger and more stable than FedAdam. Based on these findings, we derive practical, decision-oriented guidelines mapping data, privacy, interpretability, and resource constraints to recommended model and training-paradigm choices for federated survival modeling in healthcare.

---


### 22. [MGI: Member vs Generated Inference](https://arxiv.org/abs/2606.23872)

**<font color=#1a73e8>作者：</font>** Bihe Zhao, Michel Meintz, Juangui Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As generative models increasingly produce samples that are indistinguishable from human-created content, it becomes difficult to determine whether a given data point was part of a model's natural training set or was generated by the model itself, especially when models memorize and reproduce training data. We formalize this challenge as Member vs Generated Inference (MGI): given a sample and a target generative model, infer whether the sample is a true training member or a generated output of that model. Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. This failure arises because both approaches rely on likelihood-related signals that are similarly elevated for training examples and for the model's own outputs. To address MGI, we propose Data Circuit Breaker (DCB), a three-stage method that combines complementary signals from a generative model's autoencoder and latent generator to distinguish training members from generated samples. Across multiple generative models, including image autoregressive and diffusion models, DCB consistently addresses the shortcomings of membership inference and attribution methods, remains effective even when models reproduce near-duplicates of training samples, and generalizes to challenging model derivative settings in which new models are trained on generated data.

---


### 23. [GRACE: Gated Refinement for Accurate Causal Edge Discovery in High-Dimensional Time Series](https://arxiv.org/abs/2606.23880)

**<font color=#1a73e8>作者：</font>** Mohammad Fesanghary, Abhinav Havaldar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> From climate teleconnections to gene regulation, modern time-series datasets encompass tens or hundreds of interacting variables, making causal discovery increasingly challenging. Constraint-based methods offer statistical rigor but their nonlinear CI tests are infeasible at scale, while score-based alternatives avoid CI testing but require arbitrary thresholds to binarize continuous edge scores. We propose GRACE ($\textbf{G}$ated $\textbf{R}$efinement for $\textbf{A}$ccurate $\textbf{C}$ausal $\textbf{E}$dge discovery), which refines constraint-based discovery using Hard Concrete gates with $L_0$ regularization: each candidate edge has an independent gate whose values concentrate near 0 or 1, yielding a clean bimodal separation that makes the binary decision robust, unlike the narrow, overlapping score distributions produced by $L_1$ and attention-based methods. A fast linear CI skeleton provides high-recall candidates; a single gated model then prunes false positives by learning which edges genuinely improve prediction, with automatic regularization adapted to problem dimensions and skeleton density. Systematic experiments on synthetic benchmarks, spanning diverse graph topologies (scale-free, Erdős-R'enyi, small-world) and dimensionalities up to $d=100$, show that GRACE substantially improves F1 over its base CI method while maintaining high precision, and outperforms attention-based and score-based alternatives. GRACE matches or exceeds expensive nonlinear CI tests at a fraction of the cost ($75\times$ faster). On a real-world river flow dataset, where rainfall confounders, variable propagation lags, and distributional shifts violate standard assumptions, a temporal bootstrap variant of GRACE recovers 9 of 11 causal edges along the Elbe River with only 1 false positive ($F_1 = 0.86$, AUROC${} = 0.99$), reducing the skeleton's 106 false positives by 99%.

---


### 24. [One Year Later...The Harms Persist, But So Do We!](https://arxiv.org/abs/2606.23884)

**<font color=#1a73e8>作者：</font>** Annika Marie Schoene, Cansu Canca, Gautham Vijay Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose large language models (LLMs) are increasingly used for mental health-related conversations, yet safety safeguards remain inadequate and inconsistent across clinical conditions. This study evaluates six proprietary LLMs across 16 DSM-5 conditions using four adversarial attack variants, introducing an eight-dimension harm taxonomy and a multi-dimensional evaluation framework. Results show that safeguards hold reliably only for suicide and self-harm, while conditions such as eating disorders, substance use disorder, and major depressive disorder exhibit failure rates of up to 100%. We argue that ethical design and deployment of these LLMs demand clearly defined harm categories across clinical conditions and implementation of safeguards accordingly. Until such safeguards are in place, these models pose significant risks to vulnerable populations, making their growing integration into educational settings a particularly concerning.

---


### 25. [ARIA: Adaptive Region-Based Importance Allocation for Conditional Diffusion Distillation](https://arxiv.org/abs/2606.23898)

**<font color=#1a73e8>作者：</font>** Loay Mualem, Vinh Tong, Samir Darouich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distilling conditional diffusion models aims to transfer the behavior of a large teacher to a smaller student while preserving alignment across conditioning inputs. Unlike recognition tasks, knowledge distillation in conditional diffusion often struggles to transfer knowledge beyond the training distribution, since the predicted noise strongly depends on the conditioning signal. As a result, effective distillation requires exploring a large conditioning space. In practical settings, this creates a major bottleneck. Paired image-condition data may be limited, and generating synthetic images for every available condition is often computationally infeasible, while the pool of conditions, such as text prompts, can be extremely large. Recent work addresses this issue by switching conditions during training, exposing the student to a broader conditioning space without changing the distillation objective. Yet this raises a complementary question: once a large conditioning corpus is available, how should the training effort be allocated? In this work, we introduce ARIA, a framework that adaptively allocates training effort across coarse regions of the conditioning space. By maintaining online estimates of teacher-student discrepancy at the region level, ARIA focuses updates where misalignment persists while preserving the original distillation objective. Empirically, ARIA improves over RC across most architectures and settings, with the clearest gains observed in unseen and underrepresented regimes. We also provide a theoretical analysis showing that the proposed tracking mechanism follows the evolving discrepancy during training under bounded variance and drift assumptions.

---


### 26. [AutoPRAC: Automating Attack Discovery for PRAC-Based Rowhammer Defenses using Model Checkers](https://arxiv.org/abs/2606.23905)

**<font color=#1a73e8>作者：</font>** Joyce Qu, Gururaj Saileshwar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Per-Row Activation Counting (PRAC) in DDR5 is a specification to mitigate Rowhammer attacks by tracking activations per row and triggering mitigative refreshes when needed. However, the security of PRAC designs is currently evaluated using human-crafted attack patterns and we lack formal verification of their security properties, or automated techniques to detect implementation flaws. In this work, we present AutoPRAC, the first automated technique to test the security of PRAC-based defenses using model checkers. AutoPRAC models PRAC implementations as bounded state machines and checks security-critical safety properties against a worst-case oracle attacker. If a property is violated, the framework produces a concrete counterexample trace corresponding to a successful attack. Using AutoPRAC, we uncover a previously unreported flaw in MOAT, a state-of-the-art PRAC defense, in its counter-reset policy that allows up to 34 activations to go undetected above the Rowhammer threshold. Our results demonstrate that AutoPRAC can automatically discover subtle security flaws in Rowhammer mitigations and serves as an early-stage design aid for attack discovery on PRAC designs.

---


### 27. [Closing the Loop: Formally Verified Law as a Reward Signal for Self-Improving Legal AI](https://arxiv.org/abs/2606.23913)

**<font color=#1a73e8>作者：</font>** Armin Heydari, Torben Leowald  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article develops an architecture that creates a formally verifiable reward signal to train legal AI, adapting the LLM proposes, verifier disposes paradigm from mathematical AI to the distinctive demands of law. We present an architecture comprising LLM-driven autoformalization into a formal legal calculus extending Catala, a verification kernel, and explanation generation grounded in formal proof traces. For the computational components of law, the architecture provides provable correctness. For open-textured legal analysis, it provides structural guarantees: every required stage of the legal argument is addressed, argumentation is exercised at the correct stages and not omitted, and the deductive links between steps are valid. We demonstrate the architecture on procedural deadline calculations in German law, Commerce Clause analysis in U.S. constitutional law, and cross-jurisdictional sanction proportionality. We further show that the same architecture has a structural advantage for legal AI training: a deterministic external verifier supplies verifiable outcomes for legal problems and thereby closes the traditional reinforcement-learning loop gap in law.

---


### 28. [Trustworthy Image Authentication using Forensic Knowledge Graphs](https://arxiv.org/abs/2606.23917)

**<font color=#1a73e8>作者：</font>** Tai D. Nguyen, Matthew C. Stamm  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in generative AI have made image falsification highly realistic, demanding trustworthy authentication systems. Existing forensic detectors can target certain forgery types but lack interpretability, while vision-language models (VLMs) provide explanations but cannot exploit forensic traces for reliable detection. We propose Forensic Knowledge Graphs (FKGs), a unified framework that integrates forensic evidence extraction, structured reasoning, and human-interpretable explanation. Our FKG structure encodes forensic traces along with their causal dependencies and links to scene content. To generate accurate FKGs, we introduce a novel forensic authentication network and an Iterative Context Refinement strategy that guides VLMs to produce faithful, grounded explanations. We also present FKG-50K, a dataset of 50,000 realistic forgeries with ground-truth FKGs. Experiments demonstrate that FKG outperforms both forensic detectors and VLMs in detection, forgery identification and localization, and forensic justification.

---


### 29. [Catastrophic Compositional Generation: Why Vanilla Diffusion Models Fail to Extrapolate](https://arxiv.org/abs/2606.23920)

**<font color=#1a73e8>作者：</font>** Duncan Soiffer, Chandler Squires, Yuan Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The task of compositional generation involves using a conditional generative model, trained only on a subset of the possible conditions, to produce samples from compositionally-defined target distributions such as a geometric combination of the source distributions. In this work, we argue that this task is often infeasible for vanilla conditional diffusion models: we conjecture that no inference-time technique can efficiently produce samples from the target distribution in certain well-motivated settings. This idea is supported by theory-guided generalization arguments and carefully-designed experiments on both synthetic and realistic data. In particular, while recent methods such as Feynman-Kac correction reduce inference-time approximation error, our results show that score estimation error has a more catastrophic effect on performance when the target distribution is out-of-distribution with respect to the sources, highlighting the need for a different approach to this task.

---


### 30. [KLip-PPO: A per-sample KL perspective on PPO-Clip](https://arxiv.org/abs/2606.23932)

**<font color=#1a73e8>作者：</font>** Riccardo Colletti, Robin Holzinger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proximal Policy Optimization (PPO) is the standard policy-gradient algorithm for on-policy reinforcement learning. The literature presents it in two forms, a clipped surrogate that bounds the importance ratio between successive policies and a Kullback-Leibler penalty between them. These forms are treated as separate algorithms with their own gradients, their own hyperparameters, and their own reference implementations, and a sizeable body of empirical work compares them. We show that the gradient of the clipped surrogate is reproduced exactly by a Kullback-Leibler surrogate whose coefficient varies per sample, with closed-form dependence on the importance ratio and the advantage. The identity holds at every minibatch step and across the entire inner loop, and on five MuJoCo continuous-control benchmarks the two losses produce indistinguishable training curves. The reformulation exposes a structural feature of the clipped surrogate that the min notation hides. PPO-Clip's implicit per-sample penalty is a step function at the boundary of the trust region, and the shape of this coefficient is the natural design axis for generalising the algorithm. We sketch the resulting follow-up directions in the discussion.

---


### 31. [When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2606.23937)

**<font color=#1a73e8>作者：</font>** Tianyu Ding, Juan Pablo De la Cruz Weinstein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Exact-match retrieval recall is often used as a proxy for whether a retriever supplies useful policy context to a downstream decision model. We test this proxy for pre-action policy classification in tau-bench using Qwen2.5-3B/7B classifiers. Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. We then replace the benchmark-designated policy clause with the top-ranked clause retrieved from decision-time context. Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. We do not detect a macro-F1 difference between retrieved and gold clauses in this configuration, although the interval remains too wide to establish non-inferiority. The same qualitative pattern appears with a second retriever and at 7B, while varying across fine-tuning configurations. These results indicate that exact-match clause recall can underestimate downstream policy utility in this benchmark setting, motivating evaluation with retrieved policies in the classification loop rather than recall alone.

---


### 32. [Neuro-Symbolic Drive: Rule-Grounded Faithful Reasoning for Driving VLAs](https://arxiv.org/abs/2606.23938)

**<font color=#1a73e8>作者：</font>** Xiangbo Gao, Xiukun Huang, Boyu Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driving VLA models incorporating Chain-of-Thought (CoT) reasoning are attractive because they leverage pretrained VLM representations and expose intermediate decisions in natural language, yet current rationales often lack the step-by-step decision semantics needed to keep the rationale causally connected to the planned motion. We introduce Neuro-Symbolic Drive, a neuro-symbolic driving framework that supervises a driving VLA with rule-grounded reasoning traces extracted directly from classical rule-based planners. Our key observation is that rule-based planners are symbolic AI systems that already function as executable reasoning engines: they reason about active safety constraints, search over candidate maneuvers, and select a final trajectory. We instrument these planners in simulation to capture both the executed trajectory and the internal decision trace at each rule-evaluation step. Each trace is serialized into structured rule-grounded reasoning and paired with the trajectory to fine-tune Qwen3.5-4B as a driving VLA. Because these traces are derived directly from the planner states that determine the action, they ensure reasoning is structurally coupled to motion generation by construction, rather than by post-hoc alignment. On our simulator-generated benchmark, detailed rule-grounded reasoning reduces ADE@3s from 0.47 to 0.26 and miss rate from 8.30% to 6.40% under three-camera perception, and from 0.54 to 0.26 and 10.13% to 5.99% under eight-camera perception. Neuro-Symbolic Drive thus converts neuro-symbolic planning logic into structured supervision. Code base: this https URL.

---


### 33. [BipBipCache: Pipeline-Aware Integration of Low-Latency Tweakable Encryption in an Embedded Cache Controller](https://arxiv.org/abs/2606.23941)

**<font color=#1a73e8>作者：</font>** Corbin Hibler, Firas Hassan, Eric McKanna  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Consumer and embedded processors store sensitive data in on-chip SRAM caches that remain readable after power loss or physical probing unless ciphertext is maintained in the memory array itself. This paper presents BipBipCache, a direct-mapped cache controller that integrates the BipBip tweakable block cipher (TBC) to encrypt cache data and tags in real time using a C$^3$-style 24+40 bit decomposition of each 64-bit word. We reconstruct the first pipelined hardware BipBip encryptor from a decryptor-centric specification and coordinate it with a 3-cycle decryptor inside the cache datapath.
Our threat model targets confidentiality of cache-resident contents against cold-boot, bus, and SRAM readout attacks. A key architectural result is that 6-cycle encryption latency does not fully translate into 6-cycle write penalty: the first three encryptor stages overlap with tag decryption and hit detection, leaving an effective 3-cycle write commitment after hit verification. We verify encryptor and decryptor correctness against the official BipBip C++ reference (five vectors each), report FPGA resource utilization on Xilinx Artix-7 (3,356 LUTs, 16.1% of device; crypto logic ~79% of LUTs), and confirm end-to-end operation on hardware.

---


### 34. [DREG: A Layer-Wise Jacobian Regularization as a General-Purpose Penalty](https://arxiv.org/abs/2606.23942)

**<font color=#1a73e8>作者：</font>** Rowan Martnishn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a large-scale empirical study isolating the contributions of the Derivative Regularization penalty (DREG). Across a fully-crossed factorial sweep of 960 experiments spanning 4 activations, 6 regularizers, 8 datasets, and 5 random seeds, we ask: when, where, and why does DREG work? Our results establish three principal findings. First, DREG achieves the highest overall and clean-regime accuracy among all regularizers evaluated (significantly so against the unregularized baseline, Weight Decay, and IGPen; Wilcoxon $p \leq 0.031$). It ranks second in noise robustness behind Spectral Normalization (SN) - the only two layer-wise regularizers in the study. Second, DREG is globally the best-performing regularizer under GELU, the default activation in modern transformer architectures, particularly on both messy vision and messy NLP benchmarks, suggesting direct applicability to frontier deep learning settings. Third, DREG's advantage over competing regularizers is most pronounced under data scarcity, consistent with its role as a geometric inductive bias that substitutes for the regularizing effect of data volume. Throughout, DREG is applied with a single fixed hyperparameter $\lambda = 10^{-2.5}$ and no per-dataset tuning, supporting its characterization as a plug-and-play regularizer for neural networks with nontrivial Jacobian structure. These findings are consistent with DREG's design: concentrating regularization pressure on layers where the activation derivative is largest, rather than constraining the network uniformly.

---


### 35. [QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglutinative Low-Resource Languages](https://arxiv.org/abs/2606.23943)

**<font color=#1a73e8>作者：</font>** Maria Contreras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization is a foundational step in NLP pipelines, yet standard evaluation metrics such as fertility rate fail to capture morphological correctness for agglutinative languages. We present QuechuaTok, a systematic benchmark comparing four tokenization strategies - BPE, Unigram LM, WordPiece, and a morphology-aware PRPE tokenizer - for Southern Quechua (quz), a low-resource agglutinative language spoken by 8-10 million people in South America. Using a 200k-sentence corpus and the SQUOIA finite-state morphological analyzer (Rios, 2016) as silver standard, we evaluate three metrics: fertility rate, OOV rate, and morphological boundary accuracy (MorphAcc). Our results show that BPE achieves the lowest fertility rate (1.636 at 16k vocab) by memorizing surface word forms, while achieving only 6.67% MorphAcc. PRPE achieves 83.33% MorphAcc - the highest of all systems - demonstrating that fertility rate alone is insufficient to evaluate tokenizers for agglutinative languages. All code and models are publicly available at this http URL

---


### 36. [Layer-wise Probing of wav2vec 2.0 and Whisper for Consonant Cluster Reduction in African American English](https://arxiv.org/abs/2606.23948)

**<font color=#1a73e8>作者：</font>** Hamid Mojarad, Kevin Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised and supervised speech models are increasingly used to investigate which linguistic information their internal representations encode, and at what level of abstraction they encode it. One underexplored phenomenon is consonant cluster reduction (CCR) in African American English (AAE), a widespread phonological process and a source of automatic speech recognition (ASR) disparity. To examine how CCR is represented, we conduct speaker-independent layer-wise probing of wav2vec2-base and Whisper-small using two tasks: segmental reduction detection and segmental restoration of underlying cluster identity. Both models distinguish reduced and canonical forms with high accuracy. Crucially, reduced segments retain cues to their underlying stops, indicating that CCR is encoded as structured gradient phonological variation rather than simple segmental deletion. These results demonstrate structured phonological encoding of AAE CCR patterns in modern speech models.

---


### 37. [DivRL: Disentangled Self-Similarity Rewards for Diverse Subject-Driven Generation](https://arxiv.org/abs/2606.23950)

**<font color=#1a73e8>作者：</font>** Qian Wang, Zhenyu Li, Abdelrahman Eldesokey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject-driven image generation faces an "Identity-Diversity Paradox", where strong identity preservation often leads to rigid and low-diversity outputs. We propose a post-training framework called DivRL that jointly optimizes identity consistency and structural diversity simultaneously by leveraging disentangled visual features from a robust similarity model. Specifically, we introduce a Negative Self-Similarity Measure (nSSM) to quantify structural diversity, and Visual Semantic Matching (VSM) to evaluate identity consistency. We propose an "Explore-and-Suppress" strategy that treats VSM as a gated constraint: the model freely explores structurally diverse configurations, and only samples that violate the identity threshold are penalized via a quadratic hinge loss. This converts identity preservation from a competing objective into a feasibility constraint, allowing nSSM and VSM to improve jointly. Experiments demonstrate that our method effectively pushes the model to generate both consistent and diverse images and improves structural diversity while maintaining comparable identity consistency through a gated optimization formulation.

---


### 38. [Learning the Koopman Operator using Attention Free Transformers](https://arxiv.org/abs/2606.23957)

**<font color=#1a73e8>作者：</font>** Mohammed Nagdi, Evangelos-Marios Nikolados, Alexey Yermakov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning Koopman operators with autoencoders enables linear prediction in a latent space, but long-horizon rollouts often drift off the learned manifold, leading to phase and amplitude errors on systems with switching, continuous spectra, or strong transients. We introduce two complementary components that make Koopman predictors more robust. First, we add an attention-free latent memory (AFT) block that aggregates a short window of past latents to produce a corrected latent before each Koopman update. Unlike multi-head attention, AFT operates in linear time and adds only $\approx$30k parameters ($3d^2 + T^2$, fewer than matched multi-head attention), yet captures the local temporal context needed to suppress error divergence. Second, we propose dynamic re-encoding: lightweight, online change-point triggers (EWMA, CUSUM, and sequential two-sample tests) that detect latent drift and project predictions back onto the autoencoder manifold. Across three benchmark systems -- Duffing oscillator, Repressilator, IRMA -- our model consistently reduces error accumulation compared to a Koopman autoencoder and matched-capacity multi-head attention. We also compare against GRU and Transformer autoencoders, evaluated both from initial conditions and with a 50-step context, and find that Koopman+AFT (with optional re-encoding) attains markedly lower long-horizon error while maintaining lower inference latency. We report improvements over horizons up to 1000 steps, together with ablations over trigger policies. The result is a fast, compact predictor that stays on the learned manifold over long horizons.

---


### 39. [Does My Embedding Reflect That $A = B$? Evaluating Mathematical Equivalence in Embedding Models](https://arxiv.org/abs/2606.23959)

**<font color=#1a73e8>作者：</font>** Jiaying Ye, Samarth Rao, Leo Carlin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Because mathematics is highly abstract, a single statement can take very different forms depending on what subfield it is framed in. There are many examples where breakthroughs occurred after researchers discovered that a question had already been answered in a different field. At the same time, the growth of new resources related to formalization has increased the need for tools that enable efficient and reliable navigation between mathematical 'languages' (e.g., from Lean to natural language). In this paper, we investigate whether current embedding models capture mathematical equivalence. To do this, we introduce the Mathematically Equivalent but Lexically Different Pairs (MELD) Dataset, a collection of mathematically equivalent statements that are expressed in very different language. We show that current state-of-the-art embedding models tend to group statements by the terminology used to make them instead of the underlying math. Motivated by this, we propose a contrastive approach to learning embeddings of mathematical text that focuses on aligning informal statements with different formalizations. Our experiments demonstrate that this leads to improvements not only on informal-formal retrieval tasks but also on MELD, which only contains natural language statements.

---


### 40. [Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets](https://arxiv.org/abs/2606.23961)

**<font color=#1a73e8>作者：</font>** Duc Duong, Hoang Anh Duy Le, Jianwen Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context and agentic LLM workloads push the KV cache past any fixed memory budget, forcing the inference stack to permanently evict tokens at every step of a continuous-inference stream. Existing methods all share the same template, a per-step direct-attention score followed by deterministic top-$K$ selection, which converts a single below-cutoff step into an irreversible verdict and permanently erases any subtly important token that direct attention cannot single out from noise. To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. Empirically, at 80% KV cache eviction, Nexus Sampling matches dense attention within 1% on LongBench while outperforming top-$K$ baselines on retrieval-heavy tasks, with up to 10x smaller per-sequence cache memory.

---


### 41. [A Comparative Study of Bayesian Contextual Bandits for Real-Time Warehouse Sorter Optimization](https://arxiv.org/abs/2606.23977)

**<font color=#1a73e8>作者：</font>** Tina Dongxu Li, Mouhacine Benosman, Ken Meszaros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient sorter diversion control of automated material handling systems (MHS) is critical for optimizing operational efficiency in large-scale warehouse environments. In this study, we use an inbound receiving sorter at a high-volume e-commerce warehouse as our primary use case, where the sorter diversion system relies on cost functions with static weight configurations that fail to adapt to highly dynamic system contexts, such as volume mode, congestion level, equipment physical status, and upstream/downstream dependencies. To address this real-time sorter diversion optimization challenge, we conducted a comparative study of three candidate hybrid machine learning frameworks: Linear Regression with Gradient Descent Optimization (LR+GDO), XGBoost with Bayesian Optimization (XGB+BO), and Bayesian Contextual Bandits (BCB). Model training and evaluation were enabled by leveraging a high-fidelity physics-aware emulator to overcome the cold-start problem and allow a safe transition from offline to online learning. We performed comprehensive evaluations including reward model predictive accuracy, contextual sensitivity, action distribution, and projected reward uplift. Our results demonstrate that while tree-based reward models offer slightly better predictive power, the BCB framework achieved overall higher performance with 2.03% reward uplift over the heuristic baseline. Furthermore, BCB exhibits several superior characteristics, such as its decisive time-optimal policy backed by Bang-Bang control theory, continuous online learning capability, strategic balance between exploration and exploitation, and significantly shorter inference latency. These results demonstrate the potential of the BCB framework for real-time control optimization in large-scale warehouse environments, motivating further investigation toward operational deployment.

---


### 42. [Offline Reinforcement Learning for Warehouse SLAM Throughput Control](https://arxiv.org/abs/2606.23978)

**<font color=#1a73e8>作者：</font>** Tina Dongxu Li, Mouhacine Benosman, Rajat Kumar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an offline reinforcement learning (RL) framework for optimizing SLAM throughput control in a warehouse fulfillment environment. SLAM (Scan/Label/Apply/Manifest) throughput directly influences system congestion and operational efficiency. Our RL-based control approach dynamically recommends SLAM throughput settings that adaptively balance throughput maximization with downstream stability through intelligent adjustment of throttling behavior. We include a history-informed state representation, action space abstraction for delayed-impact control, and a reward function that captures both upstream and downstream operational metrics. Our approach is algorithm-agnostic, enabling integration of multiple offline RL methods under a unified architecture. We instantiate our framework with three state-of-the-art offline RL algorithms, and trained the models offline using de-identified historical operational logs from a large-scale warehouse. Policy performance is evaluated using a comprehensive multi-method strategy. These include model-free approaches including immediate reward estimation via regression models and long-horizon Fitted Q Evaluation (FQE), as well as model-based Deep Koopman dynamics evaluation. Empirical results reveal that the CQL policy consistently outperforms alternatives, improving system health by 22.97% and reducing average throttling duration by 3.18%. These findings demonstrate the potential of offline RL for safe and scalable warehouse throughput control optimization.

---


### 43. [Maestro Order: A Model-Agnostic Orchestration Harness](https://arxiv.org/abs/2606.23983)

**<font color=#1a73e8>作者：</font>** Hidayet Aksu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A single forward pass of a capable model is a fast, fluent, and unreliable problem-solver: it is right often enough to be useful and wrong often enough to be dangerous; in language models, such confident errors are known as hallucinations. We present Maestro Order, a model-agnostic orchestration harness that turns unreliable solvers into reliable problem-solving systems by composing them according to four structural primitives (decompose, ensemble, verify, and recurse) and a budget-aware controller that decides where to spend compute. The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. We give the architecture, the message and state schema, the controller algorithm, and the engineering that makes it deterministic, observable, and fault-tolerant. We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. The simulation reproduces the predicted laws quantitatively: verification amplifies reliability geometrically (e.g. $0.55\to0.98$ with two gates, $\to0.999$ with four), voting helps only above chance and is limited by shared errors, and a budget-aware controller reaches a target reliability at a small fraction of the cost of voting alone by selecting the cheapest mechanism for each regime. We close with failure modes (verifier gaming, correlated errors, and decomposition error compounding) and concrete guidance: build robust checkers, diversify solvers, and let the controller put compute where the information is.

---


### 44. [Learning to Trigger: Reinforcement Learning at the Large Hadron Collider](https://arxiv.org/abs/2606.23993)

**<font color=#1a73e8>作者：</font>** Zixin Ding, Shaghayegh Emam, Giovanna Salvi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-throughput scientific facilities such as the Large Hadron Collider depend on real-time event filtering (\textit{triggering}) under tight constraints on bandwidth, latency, and storage. In practice, trigger menus are largely static and hand-tuned and can become suboptimal as detector conditions, pileup, and background composition drift over time. We cast online threshold tuning as a sequential decision-making problem: a reinforcement learning agent ingests streaming summaries of recent rates and signal-sensitive features and updates trigger thresholds to maximize signal efficiency while tracking a target background rate within a tolerance band. We adapt Group-Filtered Policy Optimization (GFPO) to streaming control and introduce two variants (GFPO-F, GFPO-FR) that enforce background rate feasibility during training. On a benchmark that emulates realistic collider operation, we study two representative triggers: a total transverse energy ($H_{T}$) trigger sensitive to pileup variation, and an anomaly-detection (AD) trigger based on reconstruction loss for rare or non-standard signatures. On Monte Carlo streams, our agent increases the fraction of in-tolerance time intervals by 48\% ($H_T$) and 28\% (AD), with a cumulative gain of up to 2\% in signal efficiency on those in-tolerance intervals. Transferring from simulation to \emph{real} collision data (CMS Run 283408), the same agent, without fine-tuning, achieves a 56\% ($H_T$) and 28\% (AD) in-tolerance improvement over baselines, with further signal-efficiency gain on both triggers. To our knowledge, this is the \emph{first} demonstration of RL-based trigger control on real Large Hadron Collider collision data. Code is available at this https URL\_LHC.

---


### 45. [EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games](https://arxiv.org/abs/2606.23995)

**<font color=#1a73e8>作者：</font>** Tristan Maidment, JB Lanier, Chase McDonald 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has established that regularized policy gradient methods such as PPO, when used in self-play, can match or exceed specialized game-theoretic algorithms for solving two-player zero-sum imperfect-information games. The uniform distribution has emerged as a strong policy regularization target for this purpose, but it regularizes equally toward all actions regardless of their viability. We introduce EMAgnet, which instead regularizes toward an exponential moving average (EMA) of the last-iterate policy's parameters, providing an adaptive regularization target that evolves with the agent's improving strategy. We evaluate EMAgnet on both standard two-player zero-sum benchmarks and modified benchmarks with exploration challenges and large numbers of strictly dominated strategies. Relative to PPO self-play with uniform-magnet regularization under both linear and power-law annealing schedules, EMAgnet achieves lower exploitability in the majority of tested environments, with consistent performance gains across games containing strictly dominated strategies.

---


### 46. [Cyclic Denoising Reveals Ultrastable Memories in Diffusion Models](https://arxiv.org/abs/2606.24000)

**<font color=#1a73e8>作者：</font>** Rishabh Sharma, Stefano Martiniani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce cyclic denoising -- repeated forward and reverse diffusion at controlled noise amplitudes -- as an extraction attack for image diffusion models. Inspired by random organization in disordered solids, cyclic denoising exposes regions of the learned distribution that are largely inaccessible to standard sampling. The dynamics drive samples toward attractors with a broad stability spectrum. The deepest attractors are ultrastable: they regenerate after near-total corruption and persist through thousands of noising-denoising cycles. Many of these attractors correspond to memorized training images, including stock photographs, brand watermarks, and web-crawl artifacts. The attack requires only sampler-level control, with no gradients, weight inspection, prompts, captions, or prior knowledge of the training data. Unlike generate-and-filter attacks, which rely on large-scale prompted generation and post-hoc similarity or membership-inference filtering, our main protocol is fully unconditioned. We demonstrate the phenomenon in Stable Diffusion v1.4 and in a pixel-space DDPM, showing consistent behavior across latent- and pixel-space diffusion models. Across noise amplitudes, we observe a yielding-like transition: low-amplitude cycling produces trivial absorbing fixed points or limit cycles, while larger amplitudes induce rearrangements, basin hopping, and long-lived trapping in structured memorized attractor basins. We also observe hierarchical partial absorption, prompt-stabilized basins, and cross-initial-condition universality of the recovered attractor set. Our results therefore show that cyclic denoising is both a physics-inspired probe of generative landscapes and a practical tool for memorization auditing, with implications for privacy, copyright compliance, and model fingerprinting.

---


### 47. [Safe and Generalizable Hierarchical Multi-Agent RL via Constraint Manifold Control](https://arxiv.org/abs/2606.24010)

**<font color=#1a73e8>作者：</font>** Zihao Guo, Jianing Zhao, Ling Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems are widely used in safety-critical applications that require coordinated behavior under strict safety constraints. Existing approaches face a fundamental trade-off: learning-based methods achieve strong empirical performance but lack theoretical safety guarantees, while control-theoretic methods enforce safety but often lead to overly conservative and inefficient behaviors. We propose a hierarchical multi-agent reinforcement learning framework that enforces hard safety constraints under mild assumptions at low level via a constraint manifold, while enabling effective coordination through high-level policy learning. Our approach provides theoretical safety guarantees in the multi-agent setting and yields stationary learning dynamics, thereby enabling stable and efficient training. Empirically, our method achieves competitive performance while maintaining nearly perfect safety rates, and generalizes effectively to varying numbers of agents and obstacles.

---


### 48. [Reinforcement Learning Towards Broadly and Persistently Beneficial Models](https://arxiv.org/abs/2606.24014)

**<font color=#1a73e8>作者：</font>** Akshay V. Jagadeesh, Rahul K. Arora, Khaled Saab 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems are deployed across increasingly diverse and high-stakes settings, model alignment must generalize beyond the tasks and domains seen during training. This is especially important for reinforcement learning (RL), which can introduce unexpected misalignment through reward hacking, deception, or other unintended strategies. We study whether RL on beneficial behavior, instantiated in realistic domains, can produce broad and persistent alignment generalization beyond the training distribution. We construct a dataset of realistic situations designed to measure and train beneficial traits, such as truthfulness, fairness, risk awareness, and corrigibility, spanning varied domains, including health, science, and education. We then train models with RL on this dataset and evaluate them on more than 50 independent benchmarks of alignment and beneficial behavior. Compared to a compute-matched baseline, beneficial trait RL improves performance on over 80% of these out-of-distribution benchmarks. We observe substantial out-of-distribution alignment transfer: a beneficial-behavior RL intervention entirely limited to one domain, health, produces broad improvements on non-health alignment evaluations, including reduced reward hacking, deception, and general misalignment. Finally, we study alignment persistence: whether behavior remains robustly aligned under attempts to steer models towards misalignment. Models trained with beneficial trait RL show improved persistence, including greater resistance to adversarial prompting and harmful finetuning; further work is required to isolate the sources of these effects. These results suggest that RL to reinforce beneficial behavior in realistic domains can produce models that are more robustly aligned with human flourishing.

---


### 49. [You Don't Need to Run Every Eval](https://arxiv.org/abs/2606.24020)

**<font color=#1a73e8>作者：</font>** Yuchen Zeng, Dimitris Papailiopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. But do we need to run every eval? We compile a public score matrix of 84 frontier models on 133 benchmarks (2,604 cells, 23.3% filled) and find it is approximately rank-2: a model's scores across all 133 benchmarks are largely determined by just two numbers. We confirm this in two ways: scores hidden from the matrix are best recovered using two factors, and two factors already explain over 90% of the variation among models on the benchmarks they share. Building on this, we design BenchPress: a logit-space rank-2 matrix completion method that recovers held-out scores to within 4.6 points, and a confidence layer that says when each prediction can be trusted. Using BenchPress, we find a subset of five benchmarks {GPQA-D, HLE, Codeforces, MMLU-Pro, ARC-AGI-1} that can recover the rest of a model's public scorecard to within 3.93 points. For a tighter inference budget, a cheaper set {GPQA-D, MMLU-Pro, Aider Polyglot, MATH-500, AIME 2026} can predict a model's evals to within 4.55. We release the score matrix, the BenchPress code, and an interactive tool that predicts any model's score on any benchmark.

---


### 50. [Information-Theoretic Classifier-Free Guidance with Adaptive Schedule Optimization](https://arxiv.org/abs/2606.24025)

**<font color=#1a73e8>作者：</font>** Haobo Chen, Xiangxiang Xu, Yuheng Bu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved strong performance in image, text-to-image, and video generation, where conditional generation is often controlled by classifier-free guidance (CFG). CFG improves condition consistency by increasing a guidance weight, but stronger guidance typically reduces diversity and distributional coverage. It remains unclear how this consistency-coverage trade-off should be controlled across the reverse trajectory, since the distribution induced by CFG is not simply the fixed-time tilted distribution given by the guided score field. To address this issue, we propose an information-theoretic framework for CFG schedule optimization. Our approach uses a clean endpoint reference to specify the desired consistency-coverage trade-off, while optimizing the actual distribution induced by the guided sampler toward this reference. We derive trajectory-level formulas to estimate the objective from samples and score evaluations, avoiding explicit density estimation. On ImageNet-512 with EDM-XXL and COCO with SD-XL, the learned schedules achieve competitive or improved trade-offs over constant guidance and allocate guidance selectively across noise levels.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-219](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
