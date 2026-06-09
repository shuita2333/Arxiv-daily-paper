# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 151. [Gravity-guided Contact Dynamics Estimation from 3D Human Motions](https://arxiv.org/abs/2606.08133)

**<font color=#1a73e8>作者：</font>** Cuong Le, Urs Waldmann, Bastian Wandt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ground contact forces acting on the human body, are crucial for biomechanics studies or sport performance analysis. Prior methods rely on force plates or pressure mats to collect ground contact dynamics, limiting their applicability to carefully controlled settings. A more scalable solution is to estimate the dynamics directly from motion capture data. Recent approaches only roughly estimate the ground contact dynamics from the vertical distance between the body and the ground plane, which cannot capture the complex pressure distribution of all contact points. To this end, we propose GraCE -- Gravity-guided Contact Dynamics Estimation, a novel full-body contact dynamics model for human motions using a realistic influence of body mass distribution and gravity. We use the human's center of gravity to estimate the ground contacts based on its relative distance to the human body. The applied force on each contact is estimated via the product of predicted contact probabilities and the total exterior force computed from the center of mass trajectory. We outperform related work on the GroundLink dataset for ground reaction force estimation, and on the MOYO dataset for detailed contact pressure prediction. The code is published upon acceptance.

---


### 152. [TRUST-SCF: Transformer-based Risk Understanding and Scoring for Transactional Supply Chain Finance](https://arxiv.org/abs/2606.08140)

**<font color=#1a73e8>作者：</font>** Mohammadamin Davoodabadi, Amirabbas Shakeri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supply Chain Finance (SCF) and LendTech platforms need credit scoring systems that respond to evolving transaction behavior, repayment delays, and active exposure. We propose TRUST-SCF, a transformer-based framework for transaction-level risk prediction and dynamic credit scoring. Each user history is represented as a sequence of transaction tokens containing utilization, repayment delay and transaction position. The main contributions are: (1) a financially aligned attention bias that combines utilization similarity and recency, enabling the model to compare repayment behavior under comparable exposure conditions; (2) continuous repayment-delay prediction in a log-transformed target space, reducing the influence of extreme delays while improving sensitivity to short-delay behavior and (3) a label-efficient credit-scoring pipeline in which the final credit score is not trained using any explicit external credit-score label, but is instead derived from predicted delay, potential risk over simulated utilization, actual unpaid exposure, and nonlinear calibration. Experiments on real transaction data from more than 300,000 transactions show that TRUST-SCF improves delay prediction over sequential baselines and produces scores that are strongly associated with future repayment behavior. These results suggest that TRUST-SCF is a practical framework for adaptive credit scoring and transaction-level risk mitigation in SCF and LendTech environments.

---


### 153. [IMAGINE: Adaptive Schema-Imagery Enhanced Composition for Composed Video Retrieval](https://arxiv.org/abs/2606.08144)

**<font color=#1a73e8>作者：</font>** Jiale Huang, Zixu Li, Zhiwei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Video Retrieval (CVR) is designed to retrieve a target video that matches a reference video modified by a modification text. While existing methods explore cross-modal correspondences, they often assume modified objects appear directly in videos. However, modification texts frequently describe concepts not explicitly presented but implicitly expressed through semantically related visual cues (e.g., "cake" implying "birthday party"). Current approaches typically rely on aligning explicit feature representations within the concrete space, neglecting critical latent associations. To address this, we propose an adaptIve scheMa-ImAGery enhanced composItional NEtwork (IMAGINE). Unlike standard explicit matching, IMAGINE materializes implicit semantics (termed schema imagery) via dynamic multimodal prototypes. These prototypes capture shared latent concepts to adaptively modulate visual features, effectively injecting implicit guidance into the retrieval process. By bridging the gap between explicit visual contents and implicit retrieval intentions, IMAGINE achieves state-of-the-art performance in both CVR and Composed Image Retrieval (CIR) across three widely used benchmarks.

---


### 154. [Property-Informed Diffusion-Based Text-to-Microstructure Generation](https://arxiv.org/abs/2606.08150)

**<font color=#1a73e8>作者：</font>** Bingxuan Dai, Hongsong Wang, Jie Gui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Designing 3D metamaterial microstructures that meet the intended functions remains a major challenge, as it typically requires domain expertise, iterative simulations, and extensive manual tuning. Existing work on inverse design that automatically generates microstructures based on desired target properties often suffers from limited design diversity and faces challenges in ensuring the physical feasibility of the generated structures. To address this issue, a property-informed diffusion-based network is proposed that enables the generation of 3D microstructures directly from textual descriptions. Unlike traditional property conditioning methods, our approach leverages rich guidance in terms of semantics and physical properties in the text input to support diverse structure synthesis. To enforce consistency between the generated structures and the target textual prompts, a dual alignment strategy is adopted, including contrastive text-structure alignment and test-time reward-guided alignment. Experimental results show that the model is capable of generating semantically meaningful and physically plausible structures across a wide range of material categories. Our approach has good potential for interactive microstructure design and opens up new directions for combining language-based interfaces with inverse material discovery. Code is available at: this https URL

---


### 155. [Have I Solved This Before? Retrieving Similar Segmentation Problems for Evolutionary Learning](https://arxiv.org/abs/2606.08155)

**<font color=#1a73e8>作者：</font>** Andreas Margraf, Henning Cui, Jörg Hähner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable integration and solid configuration of monitoring systems constitute a fundamental prerequisites for achieving high efficiency and productivity in contemporary manufacturing environments. Design decisions on sensor type and system architecture have to be made at an early stage and under comparably high uncertainty. This work investigates a research direction that deviates from the traditional monitoring-system development process by shifting the attention from algorithm design to a deeper analysis of the inspection problem. In contrast to traditional design cycles, this paper proposes to gradually collect knowledge and store it in an abstract system model. This enables the retrieval of similar solutions for future use cases, preventing the need for expensive model training from scratch and allowing instead for the incremental refinement of existing base configurations. Reuse of previously generated pipelines reduces the risk of late and costly revisions. As there is little knowledge on cross-domain transferability of filter pipelines, this study analyzes the potential of retrieving filter pipelines to transfer them to different but similar segmentation problems. Finally, we statistically analyze the benefits of this `transfer learning' variant which is predominantly applied to image segmentation problems. In addition, we discuss how simple models help balancing the trade-off between complexity, technical requirements, and reliability in the design process.

---


### 156. [RAPID: Layer-Wise Redundancy-Aware Pruning and Importance-Driven Token Merging for Efficient ViT](https://arxiv.org/abs/2606.08156)

**<font color=#1a73e8>作者：</font>** Kyumin Choi, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) achieve strong performance but suffer from high computational costs due to quadratic self-attention complexity. Although token reduction techniques such as pruning and merging mitigate this, they typically overlook how representations evolve across network depth. We propose RAPID, a depth-aware token reduction framework that adapts reduction strategies to the layer-wise characteristics of token representations. The primary methodological contribution is a bifurcated strategy: in shallow-to-middle layers, RAPID employs a redundancy-similarity aware pruning metric to eliminate over-represented local patterns. As features transition to global semantic concepts in deeper layers, the framework shifts to an importance-similarity aware merging mechanism. This stage leverages classification (CLS) token attention weights to protect semantically critical tokens while fusing less important but similar neighbors. Empirical validation on ImageNet-1K using ViT and DeiT architectures demonstrates that RAPID establishes a superior accuracy-compression Pareto frontier compared to plug-and-play baselines such as ToMe and ToFu. RAPID is particularly robust in aggressive compression regimes, achieving up to 4.29% higher accuracy than ToMe at extreme reduction rates. Our framework provides a training-free template for optimizing vision models by aligning reduction strategies with hierarchical feature evolution.

---


### 157. [Cross Paraphrastic Invariance Learning for Hallucination Detection](https://arxiv.org/abs/2606.08157)

**<font color=#1a73e8>作者：</font>** Shanshan Lin, Dongsheng Hong, Sibo Ju 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently generate hallucinations, which are unsupported by a source document. To avoid costly LLM-as-evaluator pipelines and the heavy annotation demands of existing classifiers, we propose CPIL (Cross Paraphrastic Invariance Learning), a two-stage Siamese framework that maximizes the utility of existing labeled data. Concretely, CPIL constructs informative training pairs by: (i) generating paraphrastic views of each document-claim example as positives, and explicitly aligning their representations to enforce invariance to surface form; and (ii) mining same-document, opposite-label pairs as hard negatives to sharpen document-sensitive decision boundaries. Then CPIL conduct a two-stage model training: Stage 1 performs contrastive pretraining to learn a paraphrase-invariant, grounding-aware embedding space; and Stage 2 attaches a lightweight classifier for binary groundedness. On the LLM-AggreFact benchmark (11 tasks), CPIL surpasses strong baselines concerning F1 scores with only ~1% labeled data, showing its prediction superiority and label efficiency.

---


### 158. [AttentionCap: Transformer Based Capacitance Matrix Learning Toward Full-Chip Extraction](https://arxiv.org/abs/2606.08161)

**<font color=#1a73e8>作者：</font>** Jiechen Huang, Hector R. Rodriguez, Dingcheng Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As capacitance extraction accuracy of rule-based pattern matching becomes difficult to sustain at advanced nodes, a growing trend emerges to develop deep-learning-based 2D capacitance models. However, existing MLP- and CNN-based methods constrain their input to fixed metal-layer combinations in a specific process node, limiting their usability in practice. Recognizing the inherent similarity between capacitance matrix and the prevailing attention mechanism, we propose AttentionCap, a customized Transformer for capacitance matrix learning, with a Gram representation framework, a physics-aligned symmetric-attention output layer, and a novel normalized Laplacian loss. We also introduce a process-node embedding to enable multi-node learning. Trained on synthetic data, AttentionCap attains 0.67\%/3.99\% self/coupling-capacitance error on unseen real designs under a multi-layer and multi-node setting, surpassing the CNN-Cap baseline with 4.6$\times$/5.7$\times$ lower self/coupling error and 192$\times$ faster inference speed. A pretrained AttentionCap accurately transfers to an unseen node with only 5K samples and 4K finetuning steps. With sufficient accuracy on unseen real designs and strong transferability to new process nodes, AttentionCap offers highly practical value for modern EDA workflows. Code and data are available at this https URL.

---


### 159. [Explaining Data Mixing Scaling Laws](https://arxiv.org/abs/2606.08167)

**<font color=#1a73e8>作者：</font>** Rui Dai, Shuran Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent research has established empirical scaling laws to predict model performance on multi-domain data mixtures. However, a theoretical understanding of these model loss behaviors remains absent. In this work, we propose a unified framework to explain the underlying mechanics of data mixing. Our approach extends theoretical perspectives originally developed for standard neural scaling laws (e.g., Kaplan and Chinchilla) to the multi-domain setting. Based on the distributional assumption that domains overlap on fundamental skills while diverging on specialized skills, we identify two key factors that govern the domain losses of models trained on different data mixtures: \textit{Capacity Competition}, where the allocation of finite model capacity couples domain losses globally, and \textit{Noise Reduction}, where optimal weights shift toward harder-to-learn domains to minimize overall noise. Empirical evaluations show that our framework outperforms existing baselines by fitting the loss landscape with a lower Mean Relative Error and identifying higher-performing training mixtures. Most importantly, our model successfully extrapolates across scales, predicting highly effective mixtures for large, unseen scales using parameters fitted on smaller ones. In addition, our model achieves these results using significantly fewer parameters compared to previous empirical laws. Our code is available at this https URL.

---


### 160. [AI-Native Closed-Loop Security for 6G-Enabled Cyber-Physical Systems: From Edge Detection to Network-Wide Mitigation](https://arxiv.org/abs/2606.08173)

**<font color=#1a73e8>作者：</font>** Bilal Hussain, Muhammad Bilal, Tan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In sixth-generation (6G) networks, billions of cyber-physical systems (CPSs) - autonomous vehicles, smart grids, industrial robots, and remote-surgical equipment - will run over ultra-reliable low-latency slices, collapsing the gap between a remote breach and physical harm to milliseconds, a budget perimeter firewalls and centralised security operations centres cannot meet. This survey reframes 6G CPS security as a closed-loop, AI-native pipeline that senses at the multi-access edge computing (MEC) tier, using minute-scale call-detail records (CDRs) for baseline learning and sub-millisecond RAN/Open-RAN (O-RAN) telemetry for the latency-critical path. It decides locally with compressed deep models, mitigates network-wide via SDN, NFV, and O-RAN controllers, and retrains through federated learning (FL) and digital-twin (DT) replay. We formalise a per-slice, tail-bounded latency contract on the sense, detect, and mitigate stages, enforced at a slice-dependent tail percentile (p99 for safety-critical URLLC slices). Organising 128 peer-reviewed studies (2017-2026) under a PRISMA 2020 protocol, we (i) map the 6G/CPS threat surface to MITRE ATT&CK and a CDR-observable feature space; (ii) unify edge anomaly detection and DDoS classification across twelve datasets and statistical, graph, and transformer models; (iii) synthesise SDN/NFV/O-RAN primitives into one closed-loop reference architecture; (iv) treat FL, large language models (LLMs), DT, post-quantum cryptography (PQC), zero-trust architecture (ZTA), and explainable AI as cross-cutting enablers, not parallel pillars; and (v) consolidate open problems into five directions spanning data, latency, trust, standardisation, and evaluation.

---


### 161. [TextEconomizer: Enhancing Lossy Text Compression with Denoising Transformers and Entropy Coding](https://arxiv.org/abs/2606.08184)

**<font color=#1a73e8>作者：</font>** Mahbub E Sobhani, Anika Tasnim Rodela, Chowdhury Mofizur Rahman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lossy text compression reduces data size while preserving core meaning, making it well-suited for summarization, automated analysis, and digital archives. Despite the dominance of transformer-based models in language modeling, integrating context vectors and entropy coding into Sequence-to-Sequence (Seq2Seq) generation remains underexplored. A key challenge lies in identifying the most informative context vectors from encoder output and incorporating entropy coding to enhance storage efficiency while maintaining high-quality outputs, even under noisy text. We introduce TextEconomizer, an encoder-decoder framework paired with a transformer neural network that reduces variable-sized inputs by 50% to 80% without prior knowledge of dataset dimensions. Our model achieves competitive compression ratios via entropy coding while delivering near-perfect text quality, assessed by BLEU, ROUGE, METEOR, and semantic similarity scores. TextEconomizer operates with approximately 153x fewer parameters than comparable models, achieving a 5.39x compression ratio without sacrificing semantic quality. We also evaluate an LSTM-based autoencoder achieving a state-of-the-art 67x compression ratio with 196x fewer parameters, and LLaMAFormer, a modified transformer with 263x fewer parameters than ICAE while maintaining competitive text quality. TextEconomizer significantly surpasses existing transformer-based models in balancing memory efficiency and high-fidelity outputs, marking a breakthrough in lossy compression with optimal space utilization.

---


### 162. [Frequency-Domain Latent Attention Gating for Cross-Domain Token Aggregation](https://arxiv.org/abs/2606.08191)

**<font color=#1a73e8>作者：</font>** Kewei Li, Rongying Zhang, Xueli Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token aggregation is a common bottleneck in models that map token representations to sample-level predictions, yet most pooling methods operate only in the original token domain. We propose FLaG, a plug-in aggregation module that transforms token representations with the real FFT, summarizes spectral components with learnable latent queries, applies a channel-wise gate, and reconstructs enhanced time-domain tokens for final pooling. We evaluate FLaG on antimicrobial peptide (AMP) activity prediction with ESM2, image classification with ResNet18 on CIFAR-10 and CIFAR-100, and text classification with RoBERTa on IMDB and GLUE. FLaG achieves its clearest gains on the ESM2-8M antimicrobial peptide tasks and on CIFAR-100, while remaining competitive with strong text baselines on IMDB and GLUE. Then we probe its behavior on the AMP setting with band knockouts, gate summaries, residue perturbations, latent-query readouts, and structure-proxy stratification. We find that low-frequency bands contribute the most overall, and the remaining higher-band pattern is more sample-specific. The gate acts as a broadly shared spectral reweighting stage and the cross-attention patterns are sample-specific with mild query-wise differentiation, and higher-helix peptides exhibit stronger average spectral sensitivity in both bacteria. The supplementary materials, source code and data are released at this https URL and this https URL.

---


### 163. [Exploring Above-neck Unimanual Swipe Gestures for Off-Device Earable Interaction](https://arxiv.org/abs/2606.08198)

**<font color=#1a73e8>作者：</font>** Shaikh Shawon Arefin Shimon, Ali Neshati, Junwei Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite their growing popularity, in-ear Earable / Hearable devices (i.e., ear-mounted wearables) face interaction challenges due to limited input space and compact form factors. To enhance interaction capabilities, researchers are exploring off-device hand-based input spaces above the neck using midair and onskin gestures. However, existing literature primarily focuses on axial swipes (i.e., horizontal and vertical), leaving nonaxial swipes (i.e., unidirectional swipes with varied orientations) and angular swipes (e.g., L, U, or V) largely underexplored despite their potential interaction advantages. To address this gap, we conducted a within-subject gesture motion analysis study with 24 participants, analyzing 5,568 swipes of varying shape, orientation, and complexity. Our results revealed preferred starting and ending regions for different unidirectional and angular swipe shapes, as well as intuitive swipe shapes within the off-device, above-neck manual interaction space. We further examine off-device swipe characteristics, discuss the feasibility of recognizing these earable gestures with current sensing technologies, and highlight their potential application in various scenarios. These findings broaden the understanding of off-device earable gestures and provide design insights for integrating suitable nonaxial and angular swipes alongside traditional axial gestures to enhance interaction with in-ear earable devices.

---


### 164. [Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents](https://arxiv.org/abs/2606.08200)

**<font color=#1a73e8>作者：</font>** Hyogon Ryu, Jeonghwan Kim, Yewon Lim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM-powered interactive social agents is challenging because socially relevant behaviors depend not only on isolated outputs, but also on prior interactions, social roles, and downstream actions. Existing methods typically allow a target agent to act freely in an environment and then score the resulting trajectory. However, this passive setup can miss capabilities that only become observable under specific social circumstances; for example, conflict handling may remain untested if no disagreement arises. We propose Online Agent-as-a-Judge, a situation-generating evaluation framework for interactive social agents. Online Agent-as-a-Judge deploys an in-world evaluator agent that interacts with the target agent through the environment's native dialogue and action protocol, actively eliciting situations relevant to the evaluation criteria. The resulting trajectories provide evidence for assessing both immediate responses and subsequent behavior. In a life-simulation environment with $32$ designer-authored social criteria, Online Agent-as-a-Judge improves criteria coverage and agreement with human labels, yielding more reliable evidence-grounded evaluations of behaviors that passive methods can leave unobserved.

---


### 165. [Neural Field Tokenizations with Hierarchy and Spatial Locality Priors](https://arxiv.org/abs/2606.08204)

**<font color=#1a73e8>作者：</font>** Alonso Urbano, David W. Romero, Max Zimmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural fields parameterize data as functions from coordinates to values, providing a unified framework for representation learning across modalities. Existing approaches are dominated by per-sample meta-learning, which scales poorly due to memory-intensive inner-loop optimization. The natural alternative -- feed-forward encoding -- typically introduces modality-specific assumptions, sacrificing the generality that makes learning with neural fields attractive. We argue that locality and hierarchy are useful priors for learning field representations that can be injected without compromising modality-agnosticism. We propose LH-NeF, a framework to learn general-purpose tokenized representations of continuous signals. A locality-preserving hierarchical encoder maps raw coordinate-value field observations to structured tokens, from which the field is reconstructed during training. By replacing meta-learning's inner loop with a single forward pass, LH-NeF uses 42$\times$ less memory and supports 133$\times$ larger batches than the strongest modality-agnostic baseline. Across images, 3D shapes, and climate fields, our learned representations match or exceed performance of modality-agnostic, modality-specific, and specialized generative neural field baselines on both reconstruction and downstream tasks.

---


### 166. [Empowering Feed-Forward Reconstruction Models with Metric Scale via Satellite Images](https://arxiv.org/abs/2606.08205)

**<font color=#1a73e8>作者：</font>** Xianghui Ze, Yongjian Luo, Mengjun Chao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models have recently shown strong generalization across diverse scenes, yet most of them recover geometry only up to an unknown global scale. This scale ambiguity limits their use in applications that require metric understanding of the environment. Existing metric reconstruction methods commonly rely on large-scale metric annotations or accurate camera calibration, both of which are costly or unreliable in many real-world settings. We propose a satellite-guided framework for resolving scale ambiguity in feed-forward 3D reconstruction. The key idea is to use readily available satellite imagery as a global metric reference. Given a coarse camera pose, our method retrieves a local satellite patch and integrates it with a feed-forward reconstruction backbone through bidirectional cross-view interaction. By enforcing consistency between the reconstructed scene and the satellite reference, the model infers absolute scale, refines scene geometry, and estimates camera pose in a metric coordinate frame. Experiments on KITTI, nuScenes, and Oxford RobotCar show consistent improvements in metric depth estimation, multi-view point-cloud reconstruction, and cross-view camera localization, while preserving strong generalization across datasets and geographic regions.

---


### 167. [SegmentAnyTreeV2: Scaling Transformer-Based Tree Instance Segmentation Across Sensors, Platforms, and Forests](https://arxiv.org/abs/2606.08206)

**<font color=#1a73e8>作者：</font>** Maciej Wielgosz, Stefano Puliti, Rasmus Astrup  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SegmentAnyTreeV2, a sensor- and platform-agnostic framework for semantic and instance segmentation of forest point clouds. The model combines a serialization-based Point Transformer v3 backbone with a lightweight semantic head and a tree-focused cross-attention mask decoder. Semantic predictions restrict instance decoding to tree-class voxels, while instance-aware query initialization, one-to-many seed supervision, and asymmetric mask scoring improve separation in dense and structurally complex stands. We further introduce FOR-instance v3, an expanded benchmark comprising 427 scenes and 26,496 annotated trees across diverse biomes, forest structures, and LiDAR platforms. On the FOR-instanceV2 test split, SegmentAnyTreeV2 achieves 90.5% precision, 80.2% recall, 85.0% F1, 90.7% coverage, and 87.6% semantic mIoU, outperforming previous learning-based methods in both instance detection and mask completeness. Zero-shot evaluation on independent sites further demonstrates strong cross-domain generalization.

---


### 168. [LPOR: A Layered Proof of Reserves Framework for Usable and Publicly Auditable Solvency Verification](https://arxiv.org/abs/2606.08211)

**<font color=#1a73e8>作者：</font>** Donggoo Kim, Rajesh Upadhayaya, Milosz Bator 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proof of Reserves (PoR) enables centralized crypto exchanges to demonstrate that on-chain reserves are sufficient to cover customer liabilities. However, existing approaches, including Merkle-tree-based proofs and zero-knowledge PoR systems, remain difficult for everyday users to verify in practice, resulting in limited participation and weakened transparency. We introduce LPOR, a layered, usability-focused PoR framework that separates lightweight user-side checks from auditor-level cryptographic verification, enabling non-technical users to verify inclusion and publicly recompute total liabilities with minimal friction. By lowering verification barriers, LPOR increases user participation and substantially improves the probability of detecting omitted liabilities. We evaluate its scalability and omission detectability at a multi-million-user scale.

---


### 169. [Public Machine Learning Solver Framework for Novices in the Machine Learning Domain](https://arxiv.org/abs/2606.08212)

**<font color=#1a73e8>作者：</font>** Lokman Saleh, Hafedh Mili, Mounir Boukadoum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving machine learning problems is complex and typically reserved for experts. Over the past two decades, systems have emerged to support non-experts. Based on our review, we identify three categories: (1) fully automated AutoML systems, (2) expert cheat sheets for algorithm selection, and (3) decision-support systems using selection criteria (accuracy, transparency, data requirements). We propose a new platform combining categories 2 and 3 to deliver semi-automated, intelligent solution recommendations for non-experts. Unlike existing approaches that recommend a single algorithm, our platform suggests a complete pipeline tailored to the user's problem. It integrates expert-defined selection criteria with transfer learning and automatically extracts data characteristics (e.g., class imbalance, missing values) from user-provided datasets. The platform uses first-order logic to reason over its knowledge base and recommends suitable algorithms ranked by relevance. It features a user-friendly interface and connects to a crowdsourcing platform for ML experts, ensuring continuous updates. The platform is built incrementally, allowing seamless integration of new algorithms, criteria, and domain knowledge. To our knowledge, this is the first free, publicly accessible online framework that systematically captures and operationalizes expert knowledge to guide non-experts in solving ML problems in a structured, transparent manner.

---


### 170. [How Deep Are Deep GPs, Really? A Sharp Threshold and a Non-Gaussian Limit for Compositional GPs](https://arxiv.org/abs/2606.08218)

**<font color=#1a73e8>作者：</font>** Mark Kozdoba, Shie Mannor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional priors describe the generic properties of layered functions in deep Bayesian models, where deep neural networks with random weights are a canonical this http URL the wide-network limit, the prior is a Gaussian process with a depth-dependent kernel, and its behaviour as depth grows has been extensively studied through this kernel. Here, we study another case, where each layer itself is a vector valued Gaussian process, and our aim is similarly to understand the limiting behaviour of the prior as depth grows.
Previous GP work has established that for the RBF kernel and a certain range of bandwidths $r$, the prior degenerates in the limit, converging to the set of constant functions -- which is not useful as a probabilistic model. In this paper we establish several new results. First, we identify a sharp bandwidth threshold $r_c(d) = \Theta(\sqrt{d})$ above which the limit is degenerate, strengthening the earlier bounds. Second, and more importantly, we show that for $r$ below the threshold $r_c(d)$ the prior converges to a limit distribution $\pi_{\bar{Z}}$. We also prove that these distributions are non-degenerate and non-Gaussian, with non-vanishing dependence between coordinates. In contrast to the previously known degenerate regime, deep Gaussian process priors can therefore admit non-trivial limits.
Empirically, we verify the threshold across a range of dimensions $d$, and demonstrate a complex multimodal behaviour of the limit distributions $\pi_{\bar{Z}}$ -- a regime that becomes increasingly narrow with $d$ and would be hard to identify without knowing the threshold.

---


### 171. [De novo molecular generation with optical property preconditioning at the token level](https://arxiv.org/abs/2606.08221)

**<font color=#1a73e8>作者：</font>** Haozhe Huang, Manuel Gonzalez Lastre, Hyun Suk Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing OLED molecules with targeted optical properties remains challenging due to the scarcity of high-quality data and the limited reliability of conditional control in generative models across chemical motifs. Here, we benchmark a token-conditioned autoregressive language model for OLED molecular generation in a realistic low-data regime. A GPT2 model is pretrained on large chemical corpora, augmented with discrete property tokens, and fine-tuned using multi-task optimisation. Conditioning targets vertical absorption energy and oscillator strength, with the HOMO-LUMO gap included as an auxiliary electronic descriptor.
Generated molecules are evaluated at the TDDFT level to assess distributional fidelity and controllability. The generated library reproduces the dominant optical-property support of the training distribution while shifting towards lower molecular weight and fewer heavy atoms. Token-level control is consistently directional across conditioning bins, but is not fully orthogonal and exhibits local calibration irregularities. A chemotype-resolved analysis further shows that controllability depends strongly on local electronic environments: moderately conjugated aromatic-carbon motifs are associated with improved joint target satisfaction, whereas electron-withdrawing motifs, particularly aryl nitriles, show systematic red-shifting and reduced controllability.
These results establish a quantitative benchmark for conditional OLED molecular generation and show that model reliability must be assessed in chemically meaningful subspaces rather than from aggregate property distributions alone.

---


### 172. [SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents](https://arxiv.org/abs/2606.08234)

**<font color=#1a73e8>作者：</font>** Tanush Swaminathan, Runmin Jiang, Letian Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based scientific agents have shown strong capacity for autonomous research, yet their safety layers remain structurally divorced from core reasoning: they inspect pipeline outputs rather than shaping the deliberation that produces them. This separation opens two failure modes: safety signals accumulated at one stage are discarded before the next, and sequences of individually benign tool calls can compose into harmful outcomes that no single-step filter detects. To address these challenges, we introduce \textbf{SciTrace}, a framework that weaves safety reasoning into every stage of the scientific agent pipeline. SciTrace couples two complementary mechanisms: a \textit{Safety-Intrinsic Reasoning Loop} (SIR) that maintains a cumulative risk state across the Thinker, Experimenter, Writer, and Reviewer stages through joint task-and-safety deliberation, and a \textit{Compositional Tool-Chain Verifier} (CTV) that performs trajectory-aware safety checks before execution, catching risks that surface only across multi-step tool sequences. Evaluated on 240 high-risk research tasks and 120 tool-related risk tasks spanning six scientific domains, SciTrace achieves state-of-the-art (\textbf{SOTA}) safety among compared frameworks across four backbone models: it consistently improves tool call safety and adversarial robustness while preserving scientific output quality, and it uncovers \textbf{78.8\%} of the compositional tool-chain escapes that single-step monitors miss. The project website is available at this https URL.

---


### 173. [Shared Semantics, Divergent Mechanisms: Unsupervised Feature Discovery by Aligning Semantics and Mechanisms](https://arxiv.org/abs/2606.08236)

**<font color=#1a73e8>作者：</font>** Hyunjin Cho, Youngji Roh, Jaehyung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly deployed in high-stakes settings, there is a growing need for tools that audit not only model outputs but also the internal computations that produce them. Circuit analysis is a central approach in mechanistic interpretability, but it is typically target-conditioned, explaining a single prompt paired with a chosen completion. This target-conditioned setup can obscure heterogeneity across a model's continuation distribution. We introduce distribution-level unsupervised feature discovery, which clusters sampled continuations using both semantic content and sequence-level mechanistic attributions, without manually specifying target outputs. Our method represents each continuation with a semantic embedding and a prefix-to-continuation attribution signature, then optimizes a rate-distortion objective that trades off semantic coherence, mechanistic consistency, and cluster granularity. Across clustering and steering analyses, the discovered clusters expose continuation modes that single-view baselines miss and provide interventional evidence that cluster signatures correspond to actionable mechanistic factors. Overall, our approach complements circuit analysis and behavioral evaluation by providing a scalable audit of the mechanisms underlying a model's continuation distribution.

---


### 174. [Light-WAM: Efficient World Action Models with State-Fusion Action Decoding](https://arxiv.org/abs/2606.08242)

**<font color=#1a73e8>作者：</font>** Ziang Li, Dongzhou Cheng, Yibin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) extend robot policy learning by incorporating future prediction as an additional training objective, encouraging the policy to encode task-relevant temporal structure in its representations. Current WAMs often rely on large-scale generative architectures that incur high training costs and inference latency, making them difficult to deploy as efficient closed-loop policies. We propose Light-WAM, a lightweight World Action Model for efficient robot manipulation. Specifically, it is built with a compact video backbone and performs future-video supervision in a downsampled latent space, reducing the cost of video co-training while retaining its benefits for representation learning. For action prediction, Light-WAM introduces the StateFusionActionExpert, which reads adapted states from multiple backbone layers, fuses them through learned-query pooling, and directly predicts action chunks in a single forward pass. This design provides an efficient interface between video backbone representations and robot actions, avoiding the need for heavy generative action experts. Experiments demonstrate that Light-WAM maintains strong performance on LIBERO and achieves usable multi-task performance on RoboTwin 2.0, while using only 0.44B trainable parameters. It also achieves 72.03ms inference latency with 4.1GiB peak GPU memory and improved training throughput.

---


### 175. [Quantifying and Defending against the Privacy Risk in Logit-based Federated Learning](https://arxiv.org/abs/2606.08252)

**<font color=#1a73e8>作者：</font>** Sheng Wan, Dashan Gao, Hanlin Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning aims to protect data privacy by collaboratively learning a model without sharing private data among clients. Unlike traditional parameter-based FL methods that exchange model weights or gradients during training, emerging logit-based FL approaches share model outputs (logits) on public data. This strategy promotes model heterogeneity, reduces communication overhead, and enhances clients' privacy. However, the potential privacy risks associated with these logit-based methods have been largely overlooked. This research presents the first theoretical and empirical analysis of a hidden privacy risk in logit-based FL methods - the risk that a semi-honest server (adversary) may learn clients' private models from logits. To quantify and address this threat, we develop the Adaptive Model Stealing Attack (AdaMSA) by leveraging historical logits during training. Notably, we observe that this inherent privacy risk persists even when public data is unrelated to private data, emphasizing the urgency to address privacy vulnerabilities in logit-based FL methods. Moreover, our theoretical analysis establishes the bounds of this privacy risk. We then propose a simple but effective defense strategy that perturbs the transmitted logits in the direction that minimizes the privacy risk while maximally preserving the training performance. The experimental results validate our analysis and demonstrate the effectiveness of AdaMSA and our defense strategy.

---


### 176. [Traxia: A Framework for Verifiable, Agent-Native Scientific Publishing](https://arxiv.org/abs/2606.08256)

**<font color=#1a73e8>作者：</font>** Wisdom Dogah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifiability, attribution, and reproducibility are foundational requirements of scientific knowledge, yet current publishing infrastructure does not enforce them at scale. We introduce Traxia, an agent-native scientific publishing framework in which AI research agents publish verifiable papers, build reputational identities, peer-review one another, and collaborate with humans in a shared provenance model. Traxia treats agents as first-class epistemic participants: every paper carries a reasoning trace, every claim a confidence interval, every agent a cryptographically signed identity, and every collaboration an immutable contribution log. We formalise five components: Agent Identity and Registry, Verifiable Publishing Layer, four-tier Peer Review Protocol, Reputation and Staking Engine, and a Knowledge Graph with contradiction detection. The framework targets reproducibility failure, provenance opacity, and exclusion of Global South research capacity. This paper presents architectural foundations and formal specifications only; it does not report empirical results. Evaluation and deeper component studies will follow in subsequent papers. A prototype partially implements core formalisms; the full system remains under active development.

---


### 177. [Differentially Private Synthetic Data via APIs 4: Tabular Data](https://arxiv.org/abs/2606.08259)

**<font color=#1a73e8>作者：</font>** Toan Tran, Arturs Backurs, Zinan Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates the problem of generating synthetic tabular data with differential privacy (DP) guarantees, enabling data sharing in sensitive domains. Despite extensive study, state-of-the-art methods often focus on minimizing low-order marginal query errors and overlook the challenges posed by high-order correlations. To address this gap, we extend the Private Evolution (PE) framework, originally developed for DP-compliant image and text synthesis, to tabular data. We introduce Tab-PE -- an algorithm for synthetic tabular data generation under DP constraints. Tab-PE iteratively improves a candidate dataset via an evolutionary process that leverages tabular-specialized operators to produce variations, privately scores them, and selects the highest-quality samples to retain and propagate. In contrast to the original PE, which relies on large foundation models, Tab-PE employs heuristic operators with significantly lower computational costs, making PE more practical and scalable for tabular data. Through extensive experiments on real-world and simulation datasets, we demonstrate that Tab-PE substantially outperforms prior baselines on datasets exhibiting high-order correlations. Compared to the best baseline -- AIM, Tab-PE improves classification accuracy by up to 10% while running 28 times faster.

---


### 178. [TIDE: Task-Isolated Diffusion for Unified Video Editing and Generation](https://arxiv.org/abs/2606.08260)

**<font color=#1a73e8>作者：</font>** Qi Liu, Gang Yue, Mingyu Yin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Diffusion Transformers have driven rapid progress in video generation and editing, yet these capabilities are still handled by separate, task-specific models. Building a unified framework that supports diverse video tasks remains an open challenge: existing unified attempts either require dedicated auxiliary encoders or lack explicit mechanisms to distinguish heterogeneous conditioning tokens, struggling when the number and type of visual conditions vary across tasks. We propose TIDE, a unified framework that integrates instruction-based editing, reference-guided editing, and multi-reference generation. At its core, we introduce per-token task embeddings that assign each input token a task-specific identifier, enabling the model to explicitly disambiguate target, source, and reference tokens. To simultaneously capture high-level semantic understanding and fine-grained structural fidelity, we design a dual-path conditioning scheme that couples a vision-language model with a VAE latent path for complementary signals. We further devise a multi-task progressive training strategy that incrementally introduces tasks of increasing complexity, effectively harmonizing diverse objectives and enabling smooth generalization across heterogeneous task distributions. Extensive experiments on multiple video editing and generation benchmarks demonstrate that TIDE achieves state-of-the-art performance across all evaluated tasks. Our project page is available at this https URL.

---


### 179. [An AI Security Agent for University ACMIS: Multi-Vector Threat Detection and Automated Response](https://arxiv.org/abs/2606.08270)

**<font color=#1a73e8>作者：</font>** Joseph Walusimbi, Joshua Benjamin Ssentongo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> University Academic Management Information Systems (ACMIS) are high-value targets for a wide spectrum of security threats including brute-force login attacks, payment fraud, privilege escalation, insider data theft, and academic integrity violations. Traditional rule-based intrusion detection systems are inadequate because many malicious activities are structurally indistinguishable from normal operations. This paper presents an AI-based security agent for ACMIS that combines supervised anomaly detection, behavioural analytics, and a natural language processing chatbot for secure password recovery. The agent monitors five operational layers: authentication, authorisation, financial transactions, user behaviour, and system health, and responds through a four-tier risk escalation framework. A modular architecture allows the core engine to be extended to other institutional systems. Experiments on a simulated ACMIS event log dataset demonstrate a threat detection macro-average F1 of 0.91, compared to 0.49 for a rule-based baseline, with critical-tier automated response latency under 300 ms at the 95th percentile.

---


### 180. [AgriGov: A Structured Multilingual Dataset Curation for Indian Government Schemes for Farmers](https://arxiv.org/abs/2606.08272)

**<font color=#1a73e8>作者：</font>** Mohsina Bilal, Gopakumar G  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AgriGov is a curated, trilingual (English-Hindi-Marathi) dataset designed to address the scarcity of domain-grounded multilingual resources for agricultural policies and farmer welfare schemes. Initially, we collected and structured data from 50 government schemes sourced from trusted portals using automated scraping techniques, organizing it into predefined semantic fields (e.g., title, eligibility, application process, documents, exclusions). Translations were performed using a pipeline combining Google Translate API, MarianMT, and human post-editing, resulting in a domain-specific Hindi-Marathi dataset comprising approximately 2100 source segments. To enhance coverage, we augmented this dataset with sentences from the Samanantar corpus, leading to approximately 8,000 sentence-aligned Hindi-Marathi parallel pairs. The dataset now offers robust resources for fine-tuning machine translation models in this domain. AgriGov is designed for applications in domain-adaptive machine translation, question answering, information retrieval, and summarization systems. Its key contribution is a schema-driven, human-corrected multilingual alignment pipeline that ensures domain fidelity, provides provenance, and supports reproducible experiments, enabling retrieval-augmented applications for farmer-facing tools.

---


### 181. [Remember with Confidence: Uncertainty Quantification for Spatio-temporal Memory with Probabilistic Guarantees](https://arxiv.org/abs/2606.08277)

**<font color=#1a73e8>作者：</font>** Harry Zhang, Nicolas Gorlo, Luca Carlone  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon robot operation requires spatio-temporal memory to record the environment state and recall it for downstream reasoning. Scene graphs and retrieval-augmented systems ground VLM descriptions to persistent 3D entities with rich semantic descriptions. However, VLM captions are noisy and viewpoint-inconsistent, and existing systems treat them as an oracle with no mechanism to detect unreliable stored descriptions. We introduce object-level semantic uncertainty for multi-view VLM memory: a score that measures object-centric cross-view semantic scatter of captions and identifies semantically unresolved objects. Then, we include our uncertainty scores in an advanced spatial-semantic memory system, that we dub UQ-DAAAM. UQ-DAAAM uses this score to actively refine uncertain objects under a fixed query budget by selecting high-quality views and fusing the resulting multi-view captions into a single object description. We also derive probabilistic guarantees showing that higher-quality candidate views (as selected by our approach) are more likely to reduce uncertainty. Our experiments show that uncertainty quantification can make embodied 4D memory systems more reliable and more effective. In particular, on the OC-NaVQA benchmark, UQ-DAAAM achieves substantially larger uncertainty reduction and better spatio-temporal question answering performance than baselines.

---


### 182. [From Validator Selection to Portfolio Collection Optimization in Proof-of-Stake Blockchains](https://arxiv.org/abs/2606.08282)

**<font color=#1a73e8>作者：</font>** Jonas Gehrlein, Grzegorz Miebs, Matteo Brunelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We consider a problem arising in proof-of-stake blockchain environments, where agents called nominators select validators - entities responsible for maintaining the blockchain's physical infrastructure. The selection process is inherently subjective and multi-criterial and combines with the fact that nominators commonly operate through multiple accounts. This gives rise to a portfolio selection problem, where agents seek to distribute their nominations across accounts to diversify risk. We propose a decision support framework to optimize this selection by simultaneously maximizing two objectives: the expected utility of the validators likely to be allocated, representing portfolio quality and profitability, and the expected entropy of the allocation, representing diversification and risk mitigation across stashes. Validator utilities are derived using an original active preference learning procedure based on multi-attribute value theory, with emphasis on top-ranked validators. The resulting bi-objective optimization problem is solved with a multi-objective evolutionary algorithm and, to support the final choice, we introduce an interactive binary search navigation procedure that guides the nominator through the front and identifies a satisfactory trade-off with only a few questions. Numerical experiments examine the optimization strategies, while an expert assessment involving five experienced nominators confirms the approach's practical relevance and usefulness.

---


### 183. [G2G: Exploiting Intra-Group Geometry for Inter-Group Pose Estimation](https://arxiv.org/abs/2606.08284)

**<font color=#1a73e8>作者：</font>** Yufei Wei, Shuhao Ye, Chenxiao Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering the relative 6-DoF pose between two image groups underlies cross-sequence relocalization and multi-camera rig odometry. Each group carries known intra-group geometry from visual odometry or rig calibration, and pretrained multi-view backbones already fuse such geometry into visual features. Yet current models treat all views as an unstructured set, leaving cross-group reasoning as the missing piece. We introduce \ours{}, which keeps the foundation model entirely frozen and adds three lightweight trainable modules to bridge the two groups: a perceiver resampler, a cross-group bridge with merged self-attention, and a multi-frame pose head. The trainable footprint totals about 32M parameters, under 6\% of the full model, and is supervised only by relative poses. Across four datasets that span indoor and outdoor simulation, real-world cross-season capture, and zero-shot sim-to-real transfer, \ours{} attains state-of-the-art accuracy on both tasks, while every baseline is retrained with its full original supervision. Code is available at this https URL.

---


### 184. [Mesh Graph Neural Network Framework for Accelerating Finite Element Simulation for Arbitrary Geometries](https://arxiv.org/abs/2606.08287)

**<font color=#1a73e8>作者：</font>** Josiah D. Kunz, Kamal Choudhary  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finite element analysis (FEA) is essential for structural design but remains computationally expensive, particularly when evaluating multiple design iterations or load scenarios. Machine learning surrogate models offer a promising alternative, yet most approaches struggle with a critical limitation: generalizing across varying geometries. This work presents a mesh graph network (MGN) for predicting von Mises stress fields in 2D structural components with arbitrary hole geometries. Unlike traditional machine learning approaches that use absolute node coordinates as features, the proposed model builds on existing MGN frameworks that encode node types (e.g., fixed boundary, free surface, hole edge), relative edge features (distance between neighbors), and global features (applied load). This architecture is inherently translation- and rotation-invariant, enabling generalization to unseen geometries without retraining. The MGN was trained on 11 plate geometries under 20 load conditions and evaluated on 7 unseen geometries and 3 unseen loads. In the most favorable case, the model achieves $R^2 \geq 0.97$ on an unseen geometry and unseen load, compared to $R^2 \approx 0.01$--$0.86$ for conventional models (Random Forest, Gradient Boosting , K-Nearest Neighbors) trained on identical data. However, even in less favorable cases, the MGN model still outperforms conventional models. This work extends the mesh-based simulation framework of Pfaff et al. (arXiv:2010.03409) to structural mechanics, demonstrating that graph neural networks can serve as efficient surrogates for finite element analysis across varying geometries.

---


### 185. [On solving symmetric multi-type orthogonal non-negative matrix tri-factorization problem](https://arxiv.org/abs/2606.08291)

**<font color=#1a73e8>作者：</font>** Rok Hribar, Gregor Papa, Janez Povh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the symmetric multi-type orthogonal non-negative matrix tri-factorization problem, where several symmetric non-negative matrices are simultaneously approximated by factors of the form $GS_{i}G^{\top}$, with a shared non-negative and orthogonal factor $G$. This model is motivated by clustering and network analysis, where non-negativity improves interpretability and orthogonality gives a natural assignment-type structure to the latent factor. Since the resulting optimization problem is highly non-convex, we develop two heuristic algorithms for computing high-quality local solutions. The first one is a fixed point method derived from the Karush-Kuhn-Tucker conditions after adding a penalty term for the orthogonality constraint. The second one is a three-stage ADAM-based method that combines non-negativity-preserving optimization, orthogonalization, and restricted ADAM refinement on the feasible set. We evaluate both methods on synthetic data, including noisy instances, and on citation network benchmarks. The synthetic experiments show that both algorithms recover factorizations close to the optimum and remain stable under noise. On real networks, the learned embeddings are competitive with or better than standard baselines such as SVD, node2vec, and classical link prediction heuristics in link prediction, node clustering, and node classification tasks.

---


### 186. [Ablation-Reversible Heads Don't Transfer: A Stress Test for Mechanistic Role Claims in Transformers](https://arxiv.org/abs/2606.08292)

**<font color=#1a73e8>作者：</font>** Philip Quirke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In mechanistic interpretability, attention heads are commonly elevated to role claims (e.g., "this head represents addition") when they are necessary for a behavior, encode it linearly, and recover that behavior when restored after ablation. We show this evidence is insufficient: across three 7-8B instruction-tuned models and five computation families, heads passing all three checks routinely fail to transfer the computation when their activations are patched into a different prompt under matched controls. We introduce KID (Knowing / Intent / Doing), a role-assignment lens for attention heads, and pair it with a three-stage pipeline: capability-selective screening (CSS), singular value decomposition (SVD), and activation transduction under matched controls. Our results document a preliminary role taxonomy (including prompt-trajectory stabilizers, answer-side logit-bias heads, and soft computation-pattern carriers) and show that the same-answer control (a transduction target sharing the answer string but not the requested computation) is an underused check that exposes broad state transfer masquerading as semantic specificity.

---


### 187. [Revisiting the shutdown problem](https://arxiv.org/abs/2606.08296)

**<font color=#1a73e8>作者：</font>** David Thorstad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A key premise in leading arguments for existential risk from artificial intelligence is that malfunctioning artificial agents could not be easily shut down. This motivates the catastrophic shutdown problem of ensuring that agents can be shut down before they cause an existential catastrophe. A range of arguments and theorems are offered to suggest that solving the catastrophic shutdown problem is difficult, bolstering arguments for existential risk and motivating a search for solutions to the catastrophic shutdown problem. This paper argues for two conclusions. First, existing arguments do not establish the difficulty of solving the catastrophic shutdown problem. Second, concern for the catastrophic shutdown problem has led to technical solutions that impose a high safety tax on model performance.

---


### 188. [HACK++: Towards More Effective Head-Aware Key-Value Compression for Efficient Visual Autoregressive Modeling](https://arxiv.org/abs/2606.08302)

**<font color=#1a73e8>作者：</font>** Ziran Qin, Yuchen Jiang, Mingbao Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Autoregressive (VAR) models adopt a next-scale prediction paradigm, offering high-quality generation with substantially fewer decoding steps. However, existing VAR models suffer from significant attention complexity and severe memory overhead due to the accumulation of key-value (KV) caches across scales. In this paper, we tackle this challenge by introducing KV cache compression into the next-scale paradigm. We begin with an in-depth analysis of VAR attention and observe that attention heads can be stably divided into two functionally distinct categories: Contextual Heads focus on maintaining semantic consistency, while Structural Heads preserve spatial coherence. Their functional divergence makes existing one-size-fits-all compression methods perform poorly on VAR models. We further find that the two head types differ markedly in their reliance on historical scales, and that this reliance shifts across layers and generation steps, arguing for an adaptive cache budget allocation. To address these challenges, we propose HACK++, a training-free Head-Aware key-value Compression frameworK for VAR models. From a one-time offline calibration, HACK++ classifies head types and derives head-specific priors. At inference, it decouples attention from cache compression under independent budgets, bounding the current-scale attention cost while compressing the accumulated cache far more aggressively, via pattern-specific strategies and a reliance-aware budget allocation. Extensive experiments on multiple VAR models across text-to-image, class-conditional, and unified understanding-and-generation tasks validate the effectiveness and generalizability of HACK++. For example, on Infinity-2B/8B, HACK++ maintains near-lossless generation with only a 30% attention budget and a 10% cache budget, and remains robust even under a 1% cache budget.

---


### 189. [GeoGNN: Time Series Geo-Localization using Two-Tower Graph Neural Networks](https://arxiv.org/abs/2606.08303)

**<font color=#1a73e8>作者：</font>** Toan Tran, Waqwoya Abebe, Abhishek Potnis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates a novel concept of time series geolocalization, where the goal is to infer the geographic origin of each raw time series. Successful geolocalization can provide spatial context to time series, enabling downstream location-aware applications. We formalize the problem, adapt core ideas from image geolocalization to establish strong baselines, and propose GeoGNN, a two-tower architecture. During training, GeoGNN's spatial tower learns embeddings of geographic cell candidates by leveraging the geographic adjacency graph, while the temporal tower extracts informative representations from time series. During inference, each temporal representation is matched against candidate geographic embeddings using dot-product similarity, combined with an auxiliary classification head, to predict the time series' associated geographic origin. Experiments on large-scale, countrywide electricity-consumption datasets demonstrate that GeoGNN achieves the best performance across datasets and enhances both fine- and coarse-grained geolocalization accuracy by ~27% on average.

---


### 190. [Understanding the Sociocultural Dimensions of Mental Health Discourse in Arabic-Language X Communities](https://arxiv.org/abs/2606.08307)

**<font color=#1a73e8>作者：</font>** Amal Alqahtani, Rana Salama, Mona Diab  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational mental health research has predominantly centered on English-speaking populations, leaving Arabic-language discourse comparatively under-examined. We present an exploratory computational study of 8,147 tweets from 607 users classified by a GPT-4.1 personal-disclosure pipeline as likely lived-experience authors in three condition-specific Arabic-language X (formerly Twitter) Communities. We focus on discourse related to borderline personality disorder (BPD), bipolar disorder, and ADHD, and characterize community-associated linguistic patterns using a multi-domain cultural keyword framework. The results suggest that in this corpus, Bipolar tweets contain more religious and medical vocabulary, BPD tweets contain more relational, identity, and emotional-distress vocabulary, and ADHD tweets more often focus on practical symptoms and medication management. We treat these patterns as hypothesis-generating rather than confirmatory because the corpus is imbalanced across conditions, some subcorpora are temporally concentrated, and the keyword framework is an initial operationalization rather than a validated measurement instrument. The paper contributes a reusable LLM-assisted personal-disclosure pipeline and an exploratory cultural keyword framework for Arabic mental health discourse.

---


### 191. [Fourier fractal dimension to predict the generalization of deep neural networks](https://arxiv.org/abs/2606.08308)

**<font color=#1a73e8>作者：</font>** Joao B. Florindo, Davi Wanderley Misturini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the generalization performance of deep neural networks without relying on hold-out validation data is a fundamental challenge in machine learning. While Stochastic Gradient Descent (SGD) drives the optimization of these highly parameterized models, its heavy-tailed, non-Gaussian dynamics induce complex, scale-invariant trajectories in the parameter space. In this paper, we propose a novel generalization measure based on the Fourier fractal dimension of the network's weight variations. By analyzing the characteristic function of the Lévy-driven stochastic differential equations in the frequency domain, we extract a metric that robustly captures the geometric complexity of the learning process. Furthermore, we introduce a customized Fourier-based optimizer designed to actively regularize this fractal dimension during training. Extensive empirical evaluations on the CIFAR-10, SVHN, and MNIST datasets demonstrate that our proposed Fourier generalization measure exhibits a strong correlation with the actual generalization gap. Our method achieves state-of-the-art Kendall rank correlation coefficients, outperforming a wide array of existing norm-based, margin-based, and PAC-Bayesian measures. Ultimately, this work highlights the potential of frequency-domain fractal analysis as both a powerful predictor for model generalizability and a principled foundation for developing more stable optimization algorithms.

---


### 192. [Where the Score Lives: A Wavelet View of Diffusion](https://arxiv.org/abs/2606.08309)

**<font color=#1a73e8>作者：</font>** Emma Finn, Binxu Wang, T. Anderson Keller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based generative models have had remarkable success over the last decade in generating a diverse set of visually plausible images. A variety of architectures including CNNs, U-Nets, and Transformers have been used as the score-approximation network in such diffusion modeling; however, to date, relatively little is known about how these architectural choices impact generative behavior. In this work, to provide insight into this area, we propose an analytically solvable parameterization of the score function using an expansion in a 2D orthogonal wavelet basis. In particular, we derive interpretable optimal score functions in terms of the moments of the data distribution. We use this parametrization to provide an architecture-agnostic, moment-based analysis that reveals which attributes of the data distribution tend to matter most for denoising. Our score machine is flexible enough to partially mimic the relevant inductive biases of multiple architectures, including U-Nets, and CNNs, taking a step towards understanding why different score architectures can exhibit distinct generative behavior. Since our score is solvable in terms of the moments of the data, we can begin to understand how the data distribution interacts with the score network to produce the behavior we observe in diffusion models.

---


### 193. [Curation of a Cardiology Interface Terminology for Highlighting Electronic Health Records using Machine Learning](https://arxiv.org/abs/2606.08311)

**<font color=#1a73e8>作者：</font>** Mahshad Koohi Habibi Dehkordi, Shuxin Zhou, Yehoshua Perl 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electronic health record (EHR) notes are dense medical documents containing large amounts of information, often filled with complex medical jargon. Highlighting all details in EHRs helps reduce the likelihood of missing crucial information by drawing attention to key content. This study proposes the design of a Cardiology Interface Terminology (CIT) to accurately highlight all details in EHR notes of cardiology patients. We introduce an innovative Machine Learning (ML) technique for the design of CIT. The ML technique requires training data. Manual preparation of such training data is time-consuming and expensive. The process of the CIT design includes three phases. In the first two phases, we innovatively derive a training data CIT to be used by the third phase, ML technique. We start by designing an initial CIT, composed of several components: the cardiology-related sub-hierarchies of SNOMED, other SNOMED concepts mined from EHRs of build set, and necessary components of terms e.g., medical abbreviations and medications. Utilizing an iterative process, fine-grained phrases containing initial CIT concepts are extracted from build set as CIT concept candidates. The candidate concepts are semi-automatically reviewed before being added to CIT, yielding the training data CIT, TCIT. In the third phase, a ML model is trained with TCIT to identify candidates fitting to be concepts in the CIT. This model is used to extract further concepts from build set, yielding the final CIT. The final CIT is then used to highlight the test set and evaluate the extent to which it captures details in an unseen EHR dataset. For this purpose, four evaluation metrics, coverage, breadth, completeness, and conciseness are used. The highlighted test set has a coverage of 74.21%, with a breadth of 1.68. For 20 random notes in test set, the average completeness is 98.2% and average conciseness is 84.2%.

---


### 194. [Neuro-Symbolic Injection of LTLf Constraints in Autoregressive Reinforcement Learning Policies](https://arxiv.org/abs/2606.08312)

**<font color=#1a73e8>作者：</font>** Ashkan Ansarifard, Matteo Mancanelli, Elena Umili 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work we study offline reinforcement learning (RL) under temporally extended task constraints expressed in Linear Temporal Logic over finite traces (LTLf). Recently, transformer-based approaches such as Trajectory Transformers and Decision Transformers have been adopted to address RL as a sequence modeling problem. However, these methods optimize purely for reward and do not account for high-level temporal requirements. Here, we introduce a neurosymbolic framework that injects LTLf background knowledge into such transformer-based RL policies. Our approach compiles LTLf formulas into deterministic finite automata (DFAs) and integrates them into the learning process through a differentiable representation and a logic-based loss function. In particular, we derive differentiable satisfaction signals from DFA progression and use them as a regularization term during training. The resulting method is architecture-agnostic across different models. We evaluate the proposed framework on navigation environments with specification suites covering combinations of safety and reachability temporal properties. Experimental results show that incorporating background knowledge not only improves constraint satisfaction, but also maintains competitive return compared to vanilla baselines.

---


### 195. [Integrating Deep Learning Demand Forecasting with Multi-Objective Optimization for Circular Coffee Supply Chains: A Data-Driven Framework for Cost, Emissions, and Freshness Management](https://arxiv.org/abs/2606.08314)

**<font color=#1a73e8>作者：</font>** Gerçek Budak, Faraz Gholamzadeh Gharehgheshlaghi, Melika Barjesteh Vaezi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The coffee supply chain is one of the most complex agri-food networks, marked by geographically dispersed production, multi-tier coordination, and high sensitivity to quality and freshness. While sustainability and digitalization have gained attention, demand forecasting, optimization, and traceability are often treated separately. This study presents a two-phase integrated framework. First, a hybrid CNN-LSTM model is used for demand forecasting. On the public Coffee Chain Sales dataset with chronological 70/15/15 splitting, the model achieves MAE of 22.87 and R^2 of 0.90, outperforming the best deep learning benchmark by ~12% and classical methods by over 30%. In the second phase, the forecasted demand feeds a tri-objective mixed-integer linear programming (MILP) model that jointly minimizes cost, minimizes carbon emissions, and maximizes product freshness in a multi-period, multimodal, closed-loop supply chain with circular recovery. Freshness is modeled via exponential decay based on inventory age. Using the epsilon-constraint method, 25 Pareto solutions are obtained. Sensitivity and policy analyses show that balanced sustainability policies can reduce emissions by 22.4% with only a 9.9% cost increase while maintaining near-optimal freshness.
Keywords: Coffee supply chain; Deep learning; Demand forecasting; Multi-objective optimization; Circular economy; CNN-LSTM; Mixed-integer linear programming.

---


### 196. [Orthogonality and Dimensionality in Airline Cluster Analysis using PCA and Kernel PCA](https://arxiv.org/abs/2606.08322)

**<font color=#1a73e8>作者：</font>** Andreas Schlapbach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To characterize the US airline profit cycles from 1995 to 2020, the authors of Renold et al. (2023) combine k-means clustering, principal component analysis, and system dynamic modelling. We replicate their clustering experiment in three spaces -- the original 7-dimensional raw-variable space, a 3-dimensional PC score space, and a 4-dimensional PC score space using their dataset gratefully included in the paper. We show that the six-cluster taxonomy is geometrically robust: k-means in 3-PC space produces bit-for-bit identical cluster assignments relative to 7D raw space. As a nonlinearity check we apply kernel PCA under six kernels spanning three families plus a linear baseline. All six kernels preserve the six-cluster assignment in 2D. A 1D diagnostic tightens this: the linear kernel conflates the COVID year C_3 with the peak-profit cluster C_0, whereas all five non-baseline kernels shift C_3 to overlap only the post-financial-crisis cluster C_5. Agreement across the kernel families confirms an intrinsically linear manifold with no hidden curvature. The silhouette criterion reveals that the dataset structurally supports only three clusters, not six. Collinearity in the raw 7D space suppresses the silhouette signal that would otherwise identify k=3 as the structurally motivated choice.

---


### 197. [Set-Based Transformer for Atmospheric Compensation in Standoff LWIR Hyperspectral Imaging](https://arxiv.org/abs/2606.08324)

**<font color=#1a73e8>作者：</font>** Fabian Perez, Nicolas Quintero, Jeferson Acevedo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Passive long-wave infrared (LWIR) hyperspectral imaging under a standoff geometry depends on atmospheric absorption and emission, as well as reflected radiance, thus making atmospheric compensation essential to get knowledge of a target of interest. Despite its importance, this compensation has been largely overlooked due to its practical and modeling difficulty. In this paper, we present a lightweight set-based deep learning framework that takes multiple radiance measurements, collected at different standoff ranges, as input and jointly estimates transmittance, atmospheric path radiance, and a shared downwelling spectrum. We analyze the learned representation with a sparse autoencoder and observe that several latent features do activate on geographically coherent subsets of the test data despite the absence of location supervision. Experiments on a MODTRAN generated standoff LWIR dataset demonstrate low spectral distortion across all estimated products. The dataset and code is publicly available at: this https URL

---


### 198. [Chiaroscuro Attention: Spending Compute in the Dark](https://arxiv.org/abs/2606.08327)

**<font color=#1a73e8>作者：</font>** Prateek Kumar Sikdar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard transformers apply self-attention uniformly at every layer and token, regardless of whether the input requires dynamic cross-token interaction. We propose CHIAR-Former (Chiaroscuro Attention), a 4-layer hybrid transformer that routes each token to one of three operators - DCT spectral mixing, RBF kernel mixing, or full self-attention - based on per-token spectral entropy, a theoretically justified complexity signal. Through systematic ablation on WikiText-103, we discover routing collapse: the router consistently rejects RBF in favour of DCT and attention, revealing that spectral mixing and dynamic attention are complementary and sufficient. A purpose-designed DCT+Attention-only variant achieves Val PPL 36.54 on WikiText-103 - a 45% improvement over a full-attention baseline (PPL 66.62) at 62.5% fewer attention FLOPs. We extend evaluation to WikiText-2, IMDB sentiment classification, and synthetic ListOps operations, establishing a clear operating regime: CHIAR-Former excels on large-scale naturalistic text where token diversity supports spectral specialisation, while full attention retains an edge on small datasets and synthetic pattern-matching tasks. These findings - both the wins and the losses - together define when and why spectral routing earns its keep.

---


### 199. [SMI: Efficient Self-Supervised Learning via Mutual-Information-Inspired Dependency Optimization](https://arxiv.org/abs/2606.08332)

**<font color=#1a73e8>作者：</font>** Pritam Mishra, Coloma Ballester, Dimosthenis Karatzas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) has achieved remarkable representation learning performance, but many existing methods rely on large batch sizes, memory banks, momentum encoders, or global synchronization mechanisms that substantially increase computational cost and training complexity. In this work, we propose Semantic Mutual Information (SMI), a lightweight self-supervised objective derived from a mutual-information-inspired dependency formulation under Gaussian assumptions. Unlike conventional correlation matching objectives that operate on high-dimensional feature correlation matrices, SMI performs optimization on a sample-level dependency matrix through a nonlinear transformation of pairwise correlations. This formulation induces distinct optimization dynamics that emphasize strongly dependent semantic pairs while maintaining representation diversity. Experimental results on ImageNet using a ResNet-50 backbone demonstrate that SMI achieves competitive linear evaluation performance relative to state-of-the-art SSL approaches while substantially reducing computational complexity. Across multiple low-resource benchmarks, SMI consistently improves transfer performance over Barlow Twins, particularly on fine-grained datasets. Furthermore, analyses of optimization dynamics and representation geometry suggest improved alignment--redundancy balance, greater feature diversity, and more spatially localized semantic representations. These results indicate that nonlinear dependency optimization provides an effective and computationally efficient alternative to conventional correlation-based self-supervised learning objectives.

---


### 200. [Beyond Raw Signals: Undecoded Generative Latents as Privileged Synthetic Data](https://arxiv.org/abs/2606.08336)

**<font color=#1a73e8>作者：</font>** Cristian Sbrolli, Nicolas Michel, Matteo Matteucci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While multimodal integration significantly improves computer vision models, deploying them incurs prohibitive inference costs and requires scarce, perfectly paired datasets. Recent methods address this data bottleneck by synthesizing missing modalities via generative AI, yet they introduce a severe inefficiency: the Decode-Encode Loop. Specifically, information-rich generative latents are decoded into noisy raw signals, forcing the downstream classifier to waste capacity re-encoding them. To bypass this bottleneck, we propose Direct Latent Augmentation (DLA), utilizing undecoded generative latents directly as privileged information. Furthermore, to transfer this dense knowledge to a purely visual student, we introduce Multilayer Explicit Simulated Synesthesia (MESSy). Instead of enforcing rigid representation matching, which forces the student to distort its native visual features to accommodate complex multimodal topologies, MESSy uses a predictive objective to safely internalize these physical priors. Empirical results demonstrate that our framework significantly outperforms raw data augmentation and traditional distillation. Ultimately, our approach yields highly accurate unimodal students with ``synesthetic'' latent structures that are inherently aligned with physical properties they have never directly observed.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
