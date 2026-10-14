# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 101. [Decision Uncertainty-Oriented Watermarking (DUOW): Securing Multi-Agent Routing Against Policy Cloning](https://arxiv.org/abs/2610.14606)

**<font color=#1a73e8>作者：</font>** Ziming Zhang, Li Li, Guorui Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Routing policies in Multi-Agent Systems (MAS) represent valuable intellectual property, yet their exposure through execution logs creates significant risks of unauthorized policy cloning. Existing agent watermarking methods protect intellectual property by modifying internal generation processes, such as perturbing token sampling distributions or injecting structural mutations into action trajectories, which may compromise task fidelity or suffer from limited transferability across heterogeneous platforms. To address these limitations, we propose Decision Uncertainty-Oriented Watermarking (DUOW), a lightweight framework that operates at the external decision layer without modifying model parameters or generated outputs. DUOW introduces a plug-and-play scoring mechanism that evaluates candidate agents from semantic and operational perspectives, identifies functionally redundant routing decisions, and selectively redirects choices among equivalent alternatives to embed ownership signals. By coupling watermark behaviors with utility-preserving routing decisions, DUOW enables cloned policies to retain ownership signals during policy imitation while increasing the difficulty of watermark removal. A confidence-driven adaptive threshold dynamically determines embedding opportunities, balancing watermark capacity and task fidelity under diverse routing contexts. Extensive evaluations on four multi-agent routing benchmarks demonstrate that DUOW preserves high task utility, achieves reliable ownership verification under up to 90% log erasure, and introduces negligible computational overhead, with an average per-step latency of 0.043 ms and total embedding overhead below 0.54 ms.

---


### 102. [From Rainfall to Road-Network Functionality: Transferable Graph Forecasting for Flood-Disrupted Transportation Networks](https://arxiv.org/abs/2610.14622)

**<font color=#1a73e8>作者：</font>** Junyan Wang, Naiyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme rainfall can rapidly degrade road-network functionality (RNF), disrupting emergency mobility, accessibility, evacuation, logistics, and infrastructure restoration. Existing flood-transportation impact models are often difficult to deploy across regions because they rely on local calibration, intensive simulation workflows or target-region retraining. This study proposes G-R2R, a transferable spatiotemporal graph-learning framework that reframes rainfall-induced road-network disruption as a region-conditioned, topology-flexible graph forecasting problem for unseen transportation networks. The framework integrates ego-centered subgraph sampling, terrain-conditioned graph representation, region-conditioned dual-level static encoding, and dynamic rainfall-network feature learning. Static geographic and infrastructure attributes are fused with rainfall forcing and recent RNF states to forecast node-level RNF across heterogeneous road networks. G-R2R is evaluated using simulation-derived RNF sequences from ten flood-prone regions in Wenzhou, China, under unseen-region testing protocols. It outperforms representative forecasting baselines, achieving a stabilized MAPE of 2.33% and $R^2$ of 0.855 under the fixed unseen-region benchmark. Leave-one-area-out evaluation yields stabilized MAPE values of 2.30%-3.54%. Ablation analysis supports the contributions of the terrain-conditioned graph representation and dual-level static encoding. A historical-event replay of Typhoon Fitow further shows that G-R2R reproduces principal temporal trajectories and node-level spatial patterns of the simulation-derived RNF reference under observed rainfall forcing without target-region retraining. These results support rapid and transferable node-level RNF forecasting across the regional road-network domains represented in this study.

---


### 103. [EarthAlign: Learning Language-Aligned Representations of Earth System Data](https://arxiv.org/abs/2610.14624)

**<font color=#1a73e8>作者：</font>** Fadillah Adamsyah Maani, Numan Saeed, Jiaqi Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpreting Earth system conditions is central to understanding environmental risks and informing decisions across weather- and climate-sensitive sectors. Existing multimodal weather systems primarily target task-specific prediction, generation, or question answering, while general-purpose alignment between Earth system data and language remains underexplored due to the limited availability of diverse language supervision grounded in meteorological conditions. To fill this gap, we introduce EarthAlign, a large-scale dataset with broad geographic coverage spanning 2000-2024 that combines 10 expert-curated natural event and disaster data sources with climatology-derived normal-weather samples. Each sample includes temporal and geospatial information and four grounded caption styles aligned with 63-variable ERA5 meteorological data. Building on EarthAlign, we introduce MeteoLIP, a dual-encoder framework for learning aligned meteorology-language representations. MeteoLIP incorporates MetTok, which uses a geolocation- and time-conditioned query to aggregate variable-specific patch embeddings into a compact sequence of meteorology tokens. To comprehensively assess Earth system multimodal representations, we introduce three downstream tasks: cross-modal retrieval, weather-condition classification, and physical variable estimation. Our experiments show that MeteoLIP improves upon the corresponding CLIP and SigLIP baselines across these tasks. Further analyses highlight the importance of meteorological input, temporal and geospatial conditioning, and multi-style supervision for meteorology-language alignment. Thus, EarthAlign and MeteoLIP provide a foundation for learning and evaluating language-aligned representations of Earth system data. Our code, dataset, and weights are publicly available at this https URL.

---


### 104. [DuSRFlow: Dual-Lens Super-Resolution via Parallax-Aware Flow Estimation and Complementary Reference Warping](https://arxiv.org/abs/2610.14630)

**<font color=#1a73e8>作者：</font>** Fangpu Zhang, Huanjing Yue, Zifan Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-lens super-resolution (DuSR) aims to enhance a wide-angle low-resolution (LR) image by exploiting a telephoto reference (Ref) image. A central challenge in DuSR is reliable reference utilization under large parallax, occlusion, and cross-camera imaging discrepancies. Existing methods often employ off-the-shelf monocular optical flow models to provide geometric priors. However, their assumptions of photometric consistency and smooth motion are violated in dual-lens scenarios, leading to unreliable alignment and degraded reference-based reconstruction. To address these issues, we propose DuSRFlow, a dual-lens super-resolution framework that improves reference utilization from both correspondence learning and reference aggregation. First, we introduce DuFlowNet, a dedicated dual-lens flow estimator for robust cross-view alignment. To train DuFlowNet without ground-truth flow annotations, we develop a real--synthetic data fusion strategy that composites synthetic foreground objects onto real dual-lens image pairs, generating controllable large-parallax samples while preserving realistic cross-camera imaging characteristics. Second, we observe that reference reliability is highly spatially uneven in DuSR, where unreliable local reference responses may suppress the utilization of reliable cues. We therefore propose a Complementary Reference Warping strategy that coordinates patch-based warping and kernel-free-guided deformable warping according to local reference reliability, producing a more reliable reference representation before LR--Ref fusion. In addition, we construct DuSR-RealV2, a challenging real-world benchmark with complex depth variations, large parallax, and occlusion. Extensive experiments on multiple DuSR benchmarks demonstrate that DuSRFlow achieves state-of-the-art performance in reconstruction quality, perceptual quality, and cross-dataset generalization.

---


### 105. [Automatic assembly modeling through attention-based assembly feature mate prediction and assembly feature pattern recognition](https://arxiv.org/abs/2610.14633)

**<font color=#1a73e8>作者：</font>** Ziheng Dai, Wanbin Pan, Zhihong Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assembly modeling plays an important role in constructing product models, yet it is still mainly performed via interactive operations that are experience-dependent and labor-intensive. Data-driven strategies hold promise for automating this process; however, existing approaches either predict poses that cannot directly generate editable B-Rep assembly constraints or require prescribed part pairs or predefined assembly faces.
To reduce the large candidate space of constraint prediction without predefined assembly faces, we propose a data-driven framework based on assembly feature mate prediction. The framework performs automatic assembly modeling from unassembled B-Rep parts, using assembly features to group the geometric entities of local mating interfaces and restrict candidate formation. Given the lack of suitable assembly feature annotations in existing datasets, we construct a large-scale dataset through an automatic annotation pipeline. Using the annotated dataset, we train an attention-based network to predict assembly feature mates, with Engineering Compatibility Fusion (ECF) incorporating explicit engineering compatibility into learned matching scores. To improve the accuracy of automatic assembly modeling, we use assembly feature patterns (AFPs) to guide the matching process. Finally, a post-processing search selects assembly feature mate and AFP mate candidates, whose associated constraints are generated and solved to complete assembly modeling.
Experimental results show that the framework achieves assembly constraint accuracies of 74.79% on the six-assembly comparison set and 64.09% on the extended test set of 16 assemblies, which includes the comparison set. With ground-truth face labels supplied as additional input, the corresponding accuracies increase to 81.78% and 80.93%, respectively.

---


### 106. [PEARL: Process-Experience Aware Reinforcement Learning for Multi-Turn Agents](https://arxiv.org/abs/2610.14636)

**<font color=#1a73e8>作者：</font>** Jie Yang, Mianqiu Huang, Yiwei Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Terminal rewards make multi-turn agents trainable without step-level annotations, but group-relative advantages provide little guidance about which intermediate decisions to adjust. Failed trajectories also contain reasonable actions, while unfavorable decision patterns can recur as training proceeds. We introduce PEARL (Process-Experience Aware Reinforcement Learning), which improves local credit assignment without an additional critic. Given two continuations from the same history with different outcomes, PEARL locates their first divergence and builds a feature representation of each branch's local decision. It clusters these decision features in recent failure and success memories to identify recurring local patterns. Using this pattern memory, PEARL selectively strengthens negative advantages at lower-reward decisions, while leaving positive advantages and the base policy optimizer unchanged. On AppWorld, PEARL improves over ARPO on Normal and Challenge tasks at both 4B and 8B scales. On ALFWorld, it achieves 97.9% mean success at 4B, 2.7 points above the strongest baseline, while remaining competitive at 8B. Ablations of shaping location, success-bank filtering, and memory window support the value of selective, recurring-pattern-based updates.

---


### 107. [AegisVox: Factorized Privacy and Clinical Preservation for Long-Form Speech](https://arxiv.org/abs/2610.14643)

**<font color=#1a73e8>作者：</font>** Praphul Singh, Akshat Agarwal, Ratul Ghosh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical speech reveals identity through both spoken identifiers and voice, yet its pauses, delivery, and speaker roles can also carry useful clinical evidence. Protecting that speech therefore requires more than preserving its words. We present AegisVox, a factorized framework that assigns consistent surrogate voices and edits identifier-bearing turns using document-consistent replacements. Across 390 public simulated or non-patient conversations totaling 63.6 hours, a matched comparison of two speech renderers separates replacement realization from retained identifiers, speaker linkage, and clinical preservation. Text-to-speech rendering realizes 535/601 planned replacements versus 453/601 for the codec-based speech editor. However, similar aggregate clinical preservation conceals more model-labeled contradictions, and conversation-wide speaker scores conceal greater edited-speech linkage under a score-direction sensitivity analysis. Fresh transcription of original audio provides a reference for interpreting the clinical measurement chain; an independent judge tests sensitivity to model-based assessment. Better replacement realization can therefore coexist with worse clinical or speaker-linkage measurements. AegisVox supports use-specific evaluation of those tradeoffs, not a guarantee of identifier removal or clinical safety.

---


### 108. [Can Synthetic UAV Benchmarks Be Trusted? Real-Synthetic Validation for UAV Model Selection](https://arxiv.org/abs/2610.14647)

**<font color=#1a73e8>作者：</font>** Yuyi Zhi, Min Du, Bill Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic UAV imagery can expand pre-deployment test evidence when task-specific Real data are scarce, but visual plausibility or semantic label alignment alone does not establish validity for model selection. We study when Synthetic evaluation preserves the model-selection conclusions obtained from Real UAV data through two complementary cases under fixed evaluation protocols. In a requirement-specific road-debris benchmark, four language-conditioned perception systems obtain lower absolute F1 on Synthetic data, yet the point-estimate ordering and top-ranked model are preserved; bootstrap analysis yields no supported pairwise reversal, and size-matched resampling preserves the top-model decision. In contrast, a closed-set stress test on a separately materialized business corpus, using four VisDrone-compatible detectors over eight empirically supported classes, changes the point-estimate top-ranked detector and reverses three of six pairwise point-estimate preference directions. A complementary audit of five UAV business scenarios further reveals substantial Real-Synthetic mismatch in class composition, object density, and target scale, including systematic under-representation of small targets. These results show that Synthetic UAV benchmark trust is conditional: semantic coverage is insufficient, and validity must be established empirically for the task, operating regime, and model panel of interest.

---


### 109. [Prospective Forcing: Learning to Look Ahead for Autoregressive Long Video Diffusion](https://arxiv.org/abs/2610.14654)

**<font color=#1a73e8>作者：</font>** Yifan Shen, Yewei Xia, Gongxu Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generators synthesize long videos through chunk-wise rollouts, yet they are typically trained to predict only the immediate future. This limited prediction horizon makes it challenging to maintain video quality over extended rollouts. To address this problem, we introduce Prospective Forcing, a multi-head prediction framework that injects long-range predictive signals into autoregressive video representations. Built on a rolling-window generator, Prospective Forcing attaches lightweight, offset-specific heads that share the same conditioning information and independently predict chunks at different future temporal offsets. By extending supervision beyond the next chunk, these heads encourage the shared history representation to retain information useful for longer-horizon prediction, supporting temporally consistent generation. At inference time, we accelerate sampling by using accepted future-chunk predictions to skip full-window backbone executions. We equip the head with learnable embeddings to generate multiple candidates for the next chunk, and a learned verifier either selects a candidate or rejects all and falls back to standard autoregressive generation.

---


### 110. [TGuide: Faster Autoregressive Video Diffusion via Historical Trajectory Guidance](https://arxiv.org/abs/2610.14657)

**<font color=#1a73e8>作者：</font>** Zhuo Chen, Bin Zou, Fanyue Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can autoregressive video diffusion be accelerated further when only four denoising steps remain? Existing feature caching approaches struggle in this regime, as large feature changes between denoising timesteps undermine both direct reuse and lightweight predictors. We observe that features across video chunks remain strongly correlated at matching denoising timesteps, offering a complementary source of guidance. Building on this insight, we introduce TGuide, a framework that accelerates autoregressive video diffusion through a lightweight Anchor-Transport-Correct (ATC) predictor guided by historical sampling trajectories. Our ATC combines two complementary references: the current chunk's preceding-step features preserve its spatial structure, while the previous chunk's same-timestep features provide information at the target denoising stage. By integrating these references through spatial retrieval and adaptive correction, ATC improves velocity prediction accuracy despite the large gaps between denoising steps. To mitigate error accumulation across both denoising steps and video chunks, we train the predictor on its own autoregressive rollouts, allowing it to adapt to states shaped by its own earlier predictions. An optional confidence-aware scheduler further adjusts the quality-efficiency trade-off. Experiments on Self Forcing, Causal Forcing, and HY-WorldPlay show that TGuide preserves generation quality while achieving denoising speedups of up to $1.89\times$ over the original 4-step generators. On Self Forcing, TGuide generalizes from 81-frame training videos to 333-frame generation, approximately four times the training length, while exceeding the original model's VBench score.

---


### 111. [RASSG: Repair-Aware Semantic Survival Gating for Streaming Tool Execution](https://arxiv.org/abs/2610.14659)

**<font color=#1a73e8>作者：</font>** Daijin Hu, Xi Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Streaming speech assistants can launch tools before users finish speaking, overlapping execution with incoming speech to reduce user waiting time. However, subsequent self-corrections can invalidate apparently stable arguments, causing stale execution whose irreversible effects persist even after the final call is corrected. We propose Repair-Aware Semantic Survival Gating (RASSG) to jointly control tool launch and cancellation during streaming speech. RASSG launches a tool when three consecutive speech recognition results arrive with identical nonempty arguments, then combines calibrated argument invalidity risk with execution costs to decide cancellation at the last feasible opportunity before effects become irreversible. Evaluation on ReCAST, FDB-v3, and Audio2Tool uses a controlled execution clock with fixed tool runtimes and cancellation parameters. On ReCAST's prospective-repair subset, RASSG reduces the stale execution rate from LocalAgreement-2's 50.00% to 3.15%, with a mean delay of 3.676s across successful trajectories. The stale reduction also holds against every early-execution baseline on both public speech datasets. Ablations with identical initial launches support active cancellation, showing the value of controlling ongoing calls before their effects become irreversible. Code and data are available at this https URL.

---


### 112. [Impact of Expertise and Trust on AI-assisted Work](https://arxiv.org/abs/2610.14660)

**<font color=#1a73e8>作者：</font>** Qianou Ma, Pranav Khape, Rock Pang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) agents promise to extend what users can accomplish beyond their existing expertise, but they also raise the risk of producing plausible-looking work that users may struggle to evaluate. We ask how task-relevant expertise and trust in AI shape agent-assisted work. To isolate these factors, we conduct a think-aloud study in which 20 professionals with varying data-science expertise use the same agentic tool to complete the same data-science hiring assessment, used at a major U.S. company. We find that surface productivity can come at the expense of understanding: participants who delegated more completed more of the task, but were also more likely to produce invalid solutions. Experts more often resisted this tradeoff, sacrificing completion to decompose the task and scrutinize agent outputs. Our findings call for evaluating agentic assistance not only by how much it accomplishes, but by whether users remain able to evaluate the work they produce.

---


### 113. [TETRIS-4DGS: Efficient Post-Training Compression of 4D Gaussian Splatting](https://arxiv.org/abs/2610.14663)

**<font color=#1a73e8>作者：</font>** Chengzhen Wu, Kelei Liu, Sicheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D Gaussian Splatting (4DGS) has emerged as a powerful dynamic scene representation, supporting real-time high quality rendering but suffers from prohibitive storage overhead. Existing methods typically attempt to solve this by treating compression as a per-scene optimization problem, limiting generalizability and applicability where low-latency compression is required. In this work, we leverage existing image and video codecs and propose a generalized post-training compression framework for 4DGS to address these issues. Specifically, we apply importance-based adaptive quantization to Gaussians according to their importance levels, effectively refining bitrate allocation while remaining fully compatible with existing codecs. To further improve compression efficiency, we utilize the statistical properties of 4DGS and propose motion- and importance-aware packing to reorganize attributes into codec-friendly 2D maps. Our approach can achieve over 40x compression rate in seconds while maintaining high quality, facilitating the practical deployment of 4DGS.

---


### 114. [Ascent Conditions for Length-Normalized Single-Rollout Policy Updates](https://arxiv.org/abs/2610.14670)

**<font color=#1a73e8>作者：</font>** Levin David Schwab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dividing each trajectory's score contribution by its realized length can change the direction of a reward-centered policy update. In a finite trajectory model, we derive an exact ascent threshold for a three-outcome softmax policy and exhibit a binary-reward example in which the expected Euclidean update decreases task success. Natural-gradient ascent holds for fully controllable outcome distributions with deterministic binary labels, but can fail under a one-parameter restriction. A third-order U-statistic estimates the first-order return change without bias from independent current-policy trajectories, one per request. In the example, a same-sample plug-in estimator instead has the opposite sign in expectation for batch sizes two through forty-nine. Exact policy-grid enumeration confirms the local sign reversal. In a branching process, length-normalized learning initially loses return, then recovers and exceeds the unnormalized comparator. The analysis concerns the expected update field at the current policy.

---


### 115. [Competition Domains Matter: Selective Head Globalization for Training-Free Sparse Attention in Video Diffusion Transformers](https://arxiv.org/abs/2610.14672)

**<font color=#1a73e8>作者：</font>** Tiantian Liu, Meng Wan, Zhiqiang Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free sparse attention is a practical route to efficient video diffusion transformer inference, yet existing methods typically fix the competition domain at each query row for every attention head. Prior work primarily addresses how to estimate token-level importance within this fixed domain; whether the domain itself should adapt to head heterogeneity remains under-specified. We introduce EG-Sparse, a training-free framework that routes low-entropy heads to a grouped cross-head pool while retaining per-row local selection for high-entropy heads, using only scores already materialized by the sparse pipeline. A controlled diagnostic fixes the ranking score and varies only the competition rule: grouped cross-head selection reduces low-entropy-head reconstruction error by 9.8%, whereas forcing high-entropy heads into an all-head global pool increases it by 7.9%. Across four configurations, EG-Sparse achieves higher video quality while reducing attention density and GPU denoising latency compared with strong training-free sparse-attention baselines. Mechanism ablations further show that selective domain adaptation outperforms uniform, random, and fixed domain-assignment policies. These results support competition-domain adaptation as a distinct design axis within centroid-guided training-free sparse attention.

---


### 116. [CAST-ASD: Causal Attention over Speakers and Time for Online Active Speaker Detection](https://arxiv.org/abs/2610.14676)

**<font color=#1a73e8>作者：</font>** Pratham Gupta, Haotian Qi, Tushar Sandhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present CAST-ASD (Causal Attention over Speakers and Time), a causal joint model for active speaker detection (ASD). Recent ASD models improve performance by jointly processing all faces in a scene, but operate offline, with the full clip available before any frame is labelled. Low-latency causal detectors instead process each face independently. CAST-ASD combines joint face reasoning with fully causal inference. It applies scene-level attention across faces within the current frame and causal temporal attention over each face's history, enabling information sharing across speakers with zero lookahead. Its parameter count does not grow with the number of faces. On MSDWild, where most negative face-frames contain a visible competing speaker, CAST-ASD reduces competing-speaker false alarms by 32% relative to the causal per-face detector it extends, with larger gains as scene occupancy increases. It outperforms all causal baselines on both validation splits while using only one-tenth the inter-speaker parameters of a three-block fixed-roster convolution. Code and models are available at this https URL.

---


### 117. [A Hybrid Kinematic GCN and Elastic Transformer for Efficient Indian Sign Language Recognition](https://arxiv.org/abs/2610.14680)

**<font color=#1a73e8>作者：</font>** Pushp Garg, Himangshu Sarma, Mrinmoy Ghorai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sign Language Recognition (SLR) presents complex challenges due to variable signing speeds and spatial intricacies. Specifically, Indian Sign Language (ISL) requires precise modeling of its inherently bimanual nature and is bottlenecked by the scarcity of large-vocabulary benchmarks and the inability of standard models to handle irregular signing velocities. To address this, a structurally-aware hybrid framework for efficient, gloss ISL recognition is proposed. To minimize computational redundancy, an entropy-driven SVD sampler that dynamically extracts informative keyframes is used. Because this subsampling creates irregular physical time gaps, the proposed architecture employs a Continuous Dual Positional Encoding paired with a distance-aware Elastic Transformer to preserve natural signing rhythm. Spatially, a Kinematically-Conditioned Adaptive GCN explicitly models bimanual geometry using unified bone-joint features. To validate our framework, a 120-class, 9,453-video native ISL dataset is created. Augmented by Physical Node Dropout and ArcFace optimization to mitigate subject-specific memorization, our framework achieves a competitive 89.8% accuracy, establishing a strong baseline for complex sign language modeling.

---


### 118. [Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering](https://arxiv.org/abs/2610.14685)

**<font color=#1a73e8>作者：</font>** Hanxin Zhu, Jianqi Ma, Cong Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion enable novel-view video synthesis from a single input video, supporting world modeling, embodied intelligence, and robotic simulation. However, existing methods process camera trajectories independently, lacking the cross-trajectory consistency needed for coherent, navigable 4D worlds. We introduce Demiurge, an autoregressive video rerendering pipeline built on a dynamic 4D point-cloud memory cache. It promotes cross-trajectory consistency through four components: (1) an appearance video diffusion model that synthesizes photorealistic novel-view videos conditioned on the 4D memory; (2) a memory-consistent video depth completion model that aligns known-region depths with cached geometry and completes missing regions, mitigating scale ambiguity and discontinuities during memory updates; (3) memory-aware dual-stream warping that provides high-fidelity visual guidance and occlusion cues for novel-view synthesis; and (4) geometry-aware video refinement that enhances perceptual quality. Extensive experiments demonstrate state-of-the-art performance and three key capabilities: coherent spatiotemporal lattice construction over dense multi-view trajectories; large-parallax video rerendering under challenging camera motions, including 180-degree rotations with no input-view overlap; and geometry-faithful outputs that can be directly optimized into high-quality 3D Gaussian Splatting representations with minimal artifacts. Project page: this https URL.

---


### 119. [One-Way Coupling via Patchwise Adaptive Normalization in Transformer Surrogates](https://arxiv.org/abs/2610.14687)

**<font color=#1a73e8>作者：</font>** Emmanuel Gottlob, Hugo Thimonier, Ludovico Buizza 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many physical systems exhibit one-way coupling: exogenous fields such as medium density or obstacle geometry influence the dynamics without being affected by them. We investigate how explicitly representing these fields can improve the accuracy and computational efficiency of transformer-based PDE surrogates. Building on spatially adaptive normalization, we introduce Patchwise Adaptive Normalization (PAdaNorm), which partitions exogenous fields into patches aligned with the state tokenization. We evaluate PAdaNorm on datasets from three different domains, using a Walrus-inspired transformer architecture. Across the three PDE families, PAdaNorm is on par with or up to 16% better than parameter-matched baselines in mean long-horizon variance-scaled RMSE on 60-step autoregressive rollouts. We also find that PAdaNorm better maintains hard physical constraints over long rollouts, such as preventing flow into impenetrable solid regions in porous media. When the conditioning is static, PAdaNorm caches the conditioning embeddings once and reuses them across the entire rollout, reducing inference FLOPs per step by up to 36% compared with parameter-matched baselines. An ablation over eight conditioning variants shows that modulating a single attention axis (temporal or spatial) suffices and that a lightweight shared MLP across blocks remains competitive with per-block projections.

---


### 120. [AcrossVAM2.0: Conflict-Aware Point Supervision for Parameter-Efficient Video Diffusion Adaptation](https://arxiv.org/abs/2610.14693)

**<font color=#1a73e8>作者：</font>** Nan Wu, Yee Hung Hong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explicit point correspondence is attractive for adapting video generators: it describes how visible surfaces move, but can overwrite the appearance prior learned by a large pretrained model. We study this tension in a 5.01B-parameter text-to-video diffusion transformer. ACROSSVAM2.0 combines a confidence-weighted track-and-visibility head, zero-initialized residual feedback, and asymmetric PCGrad that removes only the auxiliary component opposing the primary flow-matching gradient on shared LoRA parameters. The design preserves the generator exactly at initialization and protects its primary update during adaptation. In a four-way ablation trained for 1,000 steps with three independent seeds, the full method lowers KLT forward-backward cycle error in all three seeds relative to a matched flow-only continuation (mean seed-level difference -0.00711, SD 0.00505), while robust sharpness remains positive in all three. An expanded 24-prompt evaluation (216 videos) yields 9.7% lower aggregate CoTracker3 cycle error than the matched control and near-matched performance on six VBench dimensions; however, the seed-level tracking effect is heterogeneous and I3D-FVD regresses from 0.1824 to 0.2022. These results support a bounded claim: conflict-aware adaptation improves correspondence consistency without broad perceptual degradation, but does not uniformly improve video quality. We release equations, pseudocode, matched outputs, source tables, and artifact provenance.

---


### 121. [Understanding Hidden Spatial Preferences in Bayesian Optimization](https://arxiv.org/abs/2610.14696)

**<font color=#1a73e8>作者：</font>** Maria Bånkestad, Jens Sjölund  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization uses posterior uncertainty to decide where to explore, but this uncertainty is not spatially neutral. On bounded domains, Gaussian-process posterior variance is typically larger near faces, edges, and corners, giving variance-based acquisition functions a systematic boundary bias. This spatial preference is usually inherited from the surrogate rather than chosen as part of the exploration strategy. We separate these roles by keeping the predictive model fixed and modifying the spatial preference of the exploration term. We control the preference with spatial weight fields and amortize their construction with neural surrogates. Controlled experiments show that the Gaussian process' default boundary bias changes which parts of the domain are explored and which optima are reached. We compare three alternative exploration principles and find, across standard benchmark functions and stochastic robot-pushing tasks, that they can often lower regret, particularly early in the optimization. The spatial structure of posterior uncertainty is therefore not a neutral default: it shapes the exploration strategy and can materially affect optimization performance.

---


### 122. [PURE: Refining Feed-forward 3D Reconstruction with Unlabeled Post-training](https://arxiv.org/abs/2610.14698)

**<font color=#1a73e8>作者：</font>** Yaolong Zhu, Peng Li, Jiahao Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models have achieved remarkable progress through large-scale training and strong learned priors. However, they remain fragile when applied to dynamic in-the-wild videos, where non-rigid motion, occlusions, and illumination changes are prevalent. A key limitation lies in their reliance on expensive depth and camera pose annotations, which hinders scaling to diverse real-world dynamic data and restricts generalization. To address this issue, we propose \textbf{PURE}, an unlabeled post-training refinement framework that improves depth and camera estimation without requiring ground-truth supervision. Instead of relying on annotations, PURE elegantly distills robust structural knowledge from state-of-the-art 2D priors into 4D feed-forward architectures. PURE leverages relative depth constraints, affine-invariant geometry distillation, and pose refinement based on feature correspondences to stabilize geometric predictions under challenging dynamic conditions. Extensive experiments on both synthetic and real-world dynamic benchmarks demonstrate that PURE delivers consistent improvements across multiple state-of-the-art architectures. Furthermore, our data-efficient paradigm effectively mitigates domain shifts, successfully unlocking the architectural limits of these base models in challenging, in-the-wild dynamic scenes.

---


### 123. [Joint Discrete and SE(3) Diffusion for Protein Interface Design](https://arxiv.org/abs/2610.14699)

**<font color=#1a73e8>作者：</font>** Zhenqiao Song, Jianwen Xie, Lei Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The design of high-affinity, target-specific protein binders is central to the development of modern therapeutics. However, existing protein-generation methods remain limited in this setting, as many generated designs fail to simultaneously achieve geometric and physicochemical complementarity at binding interfaces. To address this challenge, we introduce PIDiff, a physicochemically enhanced multimodal diffusion framework for protein-protein complex design. PIDiff jointly designs target-conditioned protein sequences and structures by coupling diffusion in discrete sequence space with diffusion on the continuous (SE(3)) structural manifold. At its core, PIDiff employs PIFormer, a novel architecture that interleaves geometry-aware invariant point attention with global sequence self-attention. We further curate PIBench, a protein-protein complex dataset with diverse target scaffolds derived from the Protein Data Bank (PDB). We first pretrain PIDiff on PIBench and subsequently fine-tune it for two therapeutically relevant applications: minibinder design and antibody design. PPFrame consistently outperforms baseline methods across sequence design success rate, structure binding energy, and sequence-structure co-designability on all tasks.

---


### 124. [DSABench: Benchmarking Source Discovery, Coordination, and Execution for Multi-Database Agents](https://arxiv.org/abs/2610.14700)

**<font color=#1a73e8>作者：</font>** Jinlong Luo, Haoran Wu, Bo Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most text-to-SQL benchmarks provide the target database. In a large data catalog, however, choosing the sources is part of the problem: an agent must find every database needed for a request, determine how their results fit together, and execute the resulting workflow. We present DSABench to evaluate these capabilities jointly. Its 815 human-reviewed tasks draw on Spider, BIRD, and LiveSQLBench; 618 require several databases to contribute, and 105 allow more than one interpretation of the required sources. Executable contracts define source participation, cross-source dependencies, and source-local execution, while RouteEnv lets agents inspect public catalog evidence without revealing the gold annotations. In our routing-only study across seven model backends, the highest RA-Set score is 60.55%, compared with a highest RA-Graph score of 34.66% when coordination requirements are included. The gap becomes more pronounced when execution is required. Across four backends, median non-privileged Route+Exec-Graph success ranges from 6.69% to 7.98% without clarification and from 11.44% to 13.25% with one clarification; the best observed clarified configuration reaches 16.99%. On ambiguous tasks, clarification improves exact branch-source recovery by 39.8-43.2 percentage points. These findings illustrate why retrieving plausible databases or producing correct local SQL is not enough: an agent must carry the right information through the entire multi-database workflow.

---


### 125. [Linear-Time Non-Local Codec Placement for Machine Learning Model Compression](https://arxiv.org/abs/2610.14703)

**<font color=#1a73e8>作者：</font>** Matteo Spallanzani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device inference imposes constraints on model storage and operand traffic and thus benefits from compressed operand representations, which mandate the use of encoding and decoding operators. However, na\"ıve placement of codec operators can cancel the operand traffic gains sought from compression. In this work, I present an algorithm to place codec operators into a source computational graph to make it compatible with target hardware. The edges of the graph are colored so that each induced subgraph is weakly connected and has a maximal node that both postdominates all subgraph inputs and dominates all subgraph outputs; this unique node - dubbed the $\textit{absolute dominator}$ - is the natural location to observe the traffic flowing through the subgraph and learn parametric codec operators. The algorithm's time complexity is linear in the source graph's size. With respect to na\"ıve local codec placement, the algorithm reduces modeled operand traffic by $24\%$-$44\%$ across four models, including $24\%$ on SigLIP and $34\%$ on SmolLM2.

---


### 126. [PixARG: Pixel-Asynchronous Retrieval-Augmented Diffusion for Fast and Realistic Image Generation](https://arxiv.org/abs/2610.14713)

**<font color=#1a73e8>作者：</font>** Zewei Xin, Qinya Li, Chaoyue Niu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion models achieve impressive image generation capabilities, they suffer from high computational costs, implausible artifacts, and limited adaptability to dynamic or private data due to static, centralized training. To address these, we propose PixARG, a novel retrieval-augmented generative framework that integrates dynamic real-world image retrieval into the diffusion pipeline to simultaneously enhance efficiency and visual realism. Specifically, PixARG constructs a pixel-level affinity map between the user's text prompt and the retrieved image to guide a heterogeneous noise initialization. By modulating noise intensity across spatial regions, this mechanism preserves semantically relevant structural priors while perturbing less relevant areas, thereby significantly accelerating convergence. To accommodate this spatially non-uniform noise and ensure synchronized generation, we introduce a pixel-wise asynchronous denoising scheduler and a spatiotemporal denoiser conditioned on the affinity map. Furthermore, we derive an affinity-adaptive training objective that elegantly balances deterministic restoration with stochastic regeneration across pixels. Experiments on LAION and COYO datasets across offline, online, and user-specific settings show PixARG enhances realism and semantic alignment while drastically reducing diffusion steps.

---


### 127. [Multi-Token Random-Walk Learning via Meeting-Triggered Information Exchange](https://arxiv.org/abs/2610.14716)

**<font color=#1a73e8>作者：</font>** Taichun Yeh, Xingran Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random walk (RW)-based algorithms are widely used in decentralized learning due to their low communication overhead and scalability. While most existing methods rely on a single token, multiple tokens can explore the network in parallel and exchange information upon meeting. However, the fundamental benefits of such meeting-triggered interactions remain unclear. In this work, we investigate multi-token RW learning under two information exchange policies: \textsc{Average-Gradient} and \textsc{Average-Model}, which average stochastic gradients and updated models, respectively, when tokens meet. We establish iteration complexity lower bounds for non-convex, convex, and strongly convex objectives on complete graphs, which apply to both exchange policies. Compared with single-token RW learning, the scaling factor in these bounds is reduced by a factor of $m^2$ for non-convex and convex objectives, and by an exponentially in $m$ for strongly convex objectives, where $m$ denotes the number of tokens. Numerical experiments reveal distinct behaviors of the two policies under two performance criteria: mean-token loss (the average loss across all tokens) and best-token loss (the minimum loss across all tokens). \textsc{Average-Model} achieves lower mean-token loss and is relatively insensitive to the network-to-token ratio $N/m$, where $N$ is the number of nodes. In contrast, \textsc{Average-Gradient} achieves lower best-token loss but exhibits a trade-off between parallel exploration and gradient interference as $N/m$ decreases.

---


### 128. [Integrating AIRL-Based Reward Estimation into a Control Method Using Fuzzy Inference and Policy Gradient](https://arxiv.org/abs/2610.14723)

**<font color=#1a73e8>作者：</font>** Seiji Ishihara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A method integrating policy gradient with fuzzy inference has been proposed. This method, hereafter referred to as the base model, has high flexibility with respect to the configuration of fuzzy inference rules and fuzzy representation. It can also automatically adjust the rule weights and the membership functions in the antecedent and consequent parts using the same framework for learning. In methods that integrate reinforcement learning with fuzzy inference, however, the reward function must be designed in advance. It is therefore useful to add learning-based reward estimation to the base model. This paper proposes a fuzzy control method that integrates a reward estimation mechanism based on the adversarial inverse reinforcement learning (AIRL) framework into the base model. The generative adversarial nets (GAN) framework adopted in AIRL, however, tends to suffer from unstable learning. To address this, the proposed method treats the policy of the base model as the generator and also uses the set of membership functions in the policy as the cost function of the discriminator. This configuration allows the discriminator update for reward estimation and the generator update for policy estimation to be performed simultaneously on the parameters shared by both, without estimating a value function. In simulations of an illustrative vehicle speed control task, the proposed method acquired policies with high generalization performance through stable and efficient learning.

---


### 129. [LightVAE: Towards Compact and Efficient Video Autoencoders](https://arxiv.org/abs/2610.14726)

**<font color=#1a73e8>作者：</font>** Shiqiao Gu, Yang Yong, Fengjun Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models enable high-quality video generation, but video VAE encoding and decoding remain computationally expensive. Existing methods use stage-specific lightweight operators, yet either constrain spatial and temporal computation jointly or remove temporal computation altogether, without distinguishing their compression sensitivities in pretrained Conv3D. To address these limitations, we present LightVAE, a compression framework that exploits redundancy in temporal modeling and network depth. LightVAE exactly reparameterizes eligible causal Conv3D layers into an aggregate spatial response and a difference-driven temporal correction. Based on their distinct compression sensitivities, temporal low-rank compression (TLR) keeps the aggregate spatial kernel dense and applies layer-specific low-rank approximation only to the temporal correction. An algebraically equivalent folded implementation converts the arithmetic savings into practical acceleration. LightVAE further uses width-preserving block pruning to reduce depth and probe-guided feature alignment, guided by feedback from a frozen teacher suffix, to recover quality after compression. The framework also extends to video encoders. Across three video VAE backbones and two GPU platforms, LightVAE consistently accelerates decoding. For the Wan VAE family, it achieves up to $2.24\times$ and $1.11\times$ the decoding throughput of state-of-the-art efficient VAE decoders on NVIDIA H100 and RTX~5090, respectively, with higher DAVIS PSNR and lower LPIPS. On MiniMax-H3, it achieves up to $2.97\times$ the original decoding throughput while retaining 99.51\% of the original model's overall VBench-2.0 score. Our code is available at this https URL.

---


### 130. [Align-VAE: Aligning Attention and Geometry in VecSet VAEs for 3D Reconstruction](https://arxiv.org/abs/2610.14734)

**<font color=#1a73e8>作者：</font>** Huaizhi Qu, Mingxin Yang, Xintong Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Set-based variational autoencoders (VecSet VAEs) represent 3D shapes as compact sets of latent tokens. Although each token originates from a query at a sampled surface location, whether these latents truly align with geometry remains unclear. We investigate this alignment and identify four issues: (i) attention-sink-like tokens that attract queries from across the shape; (ii) spatially periodic repetitions in decoder attention responses; (iii) mismatched normal information in encoder and decoder query features; and (iv) missing supervision of the intrinsic relation between signed distance fields and surface normals. To address these issues, we introduce Align-VAE with four corresponding modifications: (i) a shared bank of learnable decoder tokens provides a workspace for global computation; (ii) distance-biased cross-attention guides retrieval toward nearby predicted spatial anchors; (iii) normal-free encoder queries align the two stages' access to normal information while retaining normals in the encoder keys and values; and (iv) a screened Poisson-inspired regularizer supervises surface values and normal-direction derivatives. These changes align latent retrieval and field prediction with geometry without enlarging the per-shape code. On the ABO dataset, Align-VAE reduces Chamfer distance by 26.6% compared to the standard VecSet VAE.

---


### 131. [sGLP: Specifying Stochastic Agents that Simulate People](https://arxiv.org/abs/2610.14738)

**<font color=#1a73e8>作者：</font>** Ehud Shapiro  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Grassroots platforms are designed to be owned, operated and governed by their participants, and thus are constituted from person-to-person smartphone apps that run on participants' smartphones. A grassroots app is specified using a grassroots social contract, which is compiled through an abstraction cascade into a volition-guarded Grassroots Logic Program (vGLP), a multiagent concurrent logic programming language. A vGLP program in turn specifies a smartphone UI via which people express their volitions and thus control the app. Prudence dictates large-scale evaluation and testing of grassroots platforms prior to deployment, but using the many people needed to do that is a contradiction in terms. Hence another solution is needed.
Here, we present stochastic GLP (sGLP), designed to allow grassroots platforms to be simulated at scale from the vGLP programs that deploy them, with stochastic agents in place of people. sGLP is GLP with a rate extension for specifying stochastic behaviour. A stochastic agent is an sGLP program replacing both the vGLP UI and the person behind it. It is typed by the dual of the interactive type of the UI and specifies a stochastic profile of a person's behaviour.
We demonstrate sGLP on the grassroots social graph, with a population of men and women drawn from four stochastic profiles --- homophile or indifferent, wary or sociable --- and on grassroots currencies, with four profiles --- spenders or savers, cautious or generous --- and report what the mix of profiles does to the social graph that forms and to the currencies that circulate.
We prove that every run of a vGLP program in which sGLP agents replace the UI and the people behind it is a vGLP run. We implemented sGLP in GLP by Gillespie's method, and ran reproducible simulations with it.

---


### 132. [Japanese Handwriting Generation Based on Human Preference Feedback Using Direct Preference Optimization](https://arxiv.org/abs/2610.14743)

**<font color=#1a73e8>作者：</font>** Wakana Kuwata, Ryota Mibayashi, Masanori Tani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a Japanese handwriting generation framework that integrates human preference feedback using Direct Preference Optimization (DPO) to align generative models with human cognitive and stylistic preferences. While font generation technologies leveraging Generative Adversarial Networks and diffusion models have advanced significantly, applying these approaches to handwriting generation presents unique challenges. Font generation is a deterministic process yielding consistent styles. Handwriting generation, on the other hand, is inherently non-deterministic. In handwriting, glyph shapes never match exactly even when the same writer writes the same character. We define this shape difference as handwriting variability. Although this variability is essential for conveying the natural quality of human writing, it complicates model training and substantially increases data collection costs to capture diverse distribution patterns. To address these limitations, we incorporate human perceptual feedback into the training loop of handwriting generation. While collecting extensive handwritten data is costly, evaluating pairwise preferences between two generated samples remains very easy for humans. Applying DPO, an efficient RL-free preference optimization method, to our generation model enables high-quality handwriting generation without relying on large-scale dataset collection. Experimental results across four distinct Japanese handwriting styles demonstrate that DPO-based training enhances overall structural accuracy. However, in highly complex styles with significant variability, such as brush pen writing, the model fails to capture style-specific features. These findings highlight a critical challenge in extending DPO to complex handwriting styles.

---


### 133. [More Domains, No Gains? FLO: Fast-Slow Reciprocal Learning for Multi-Domain Graph Pre-training](https://arxiv.org/abs/2610.14748)

**<font color=#1a73e8>作者：</font>** Yupeng Tong, Lianze Shan, Jitao Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inspired by the great success of foundation models in the development of artificial general intelligence, Graph Foundation Models (GFMs) have recently attracted significant attention and have the potential to advance graph intelligence. Exhibiting such intelligence requires effectively learning knowledge from large-scale, multi-domain graph data during pre-training. Increasing domain diversity during pre-training is expected to yield richer and more generalizable knowledge. Most existing methods pursue this goal by designing domain alignment strategies that help a single graph model learn from multiple domains. However, we observe that existing methods struggle to benefit from increasing domain diversity. Through empirical and theoretical analysis, we reveal two key limitations. Firstly, pre-training in most GFMs is confined to a single message-passing paradigm. Since propagation flattens relations among neighboring nodes, the graph model can hardly perceive the knowledge beyond propagation, namely the attribute-predictable component of these relations. Secondly, domain alignment strategies often rely on randomly initialized parameters that are jointly updated with the graph model using immediate loss feedback, leaving early knowledge acquisition vulnerable to cross-domain interference. To address these issues, we propose FLO, a Fast--sLow reciprOcal approach for multi-domain graph pre-training. Specifically, a propagation-free attribute branch predicts the graph model's relations without message passing and returns these predictions to refine the model. We further stabilize knowledge acquisition by pairing a fast process that adapts to the current domain with a slow process that integrates knowledge across domains. On 12 datasets, FLO benefits from increasing domain diversity and achieves the best average performance in cross-domain and cross-task transfer.

---


### 134. [Equal-information evaluation of credit assignment in modular financial reinforcement learning](https://arxiv.org/abs/2610.14750)

**<font color=#1a73e8>作者：</font>** Gennadiy Chistiakov, Yury Yanovich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Credit assignment in modular financial reinforcement learning is difficult to evaluate because an attributed signal may improve a component loss without adding decision-relevant information or improving economic outcomes. We propose an evaluation framework combining equal-information reconstruction controls, fixed-utility comparisons and prespecified downstream guardrails. The framework is instantiated in an attribution-guided modular trading architecture and tested in three controlled studies covering update allocation, supervision-target representation and portfolio risk control. We find that residual-based allocation is exactly reproduced by an ordinary loss-budget control under the disclosed interface; direct shortfall supervision improves component prediction but fails decoded-outcome preservation; and component-wise critic supervision worsens risk-condition certainty equivalent and drawdown relative to scalar supervision under fixed utility. These results identify three distinct evaluation failures: redundant attribution signals, representation-induced prediction trade-offs, and misalignment between component supervision and downstream risk outcomes. A preserved historical engineering case further shows why module-level learning claims require run-level provenance. The contribution is a reusable methodology for evaluating credit assignment in expert systems operating under partial observability, delayed feedback and economic risk constraints.

---


### 135. [Random Fourier Features in Near-Linear Time](https://arxiv.org/abs/2610.14751)

**<font color=#1a73e8>作者：</font>** Sepideh Mahabadi, Sandeep Silwal, Tal Wagner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random Fourier features approximate a shift-invariant kernel in $\mathbb{R}^d$, such as the Gaussian kernel $\exp(-\tfrac12\|x-y\|_2^2)$, using independent samples from its spectral measure to construct an unbiased estimator for the kernel value with subgaussian concentration. However, generating $m$ such features requires $O(md)$ time. A long line of work on structured random features has accelerated this computation for the Gaussian kernel and other radial kernels, albeit with weaker concentration guarantees. We close this gap by showing a random feature map that can be computed in near-linear time $O((d+m)\log d)$ and yields near-subgaussian concentration. We obtain it through a new and tighter analysis of the Fastfood feature map of Le, Sarlós and Smola (ICML 2013), using Brascamp-Lieb inequalities and the Schoenberg representation of radial kernels.

---


### 136. [Amharic-English Cross-Language Question Answering Using Statistical Machine Translation, Named Entity Recognition, and Semantic Indexing](https://arxiv.org/abs/2610.14756)

**<font color=#1a73e8>作者：</font>** Emebet Bekele, Fekade Getahun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The predominance of English-language Web content creates an information-access barrier for speakers of low-resource languages such as Amharic. This paper presents the design, imple-mentation, and evaluation of a bidirectional Amharic-English cross-language question answering (CLQA) system that allows a user to formulate a natural-language question in either Amharic or English and retrieve an answer from documents written in the other language. The system integrates a statistical machine translation (SMT) component for query translation, a maximum-entropy named entity recognition (NER) component for Amharic text processing, semantic-based indexing, question analysis, passage retrieval, and answer extraction. A domain-diverse Amharic-English parallel corpus was used to train the SMT component, while monolingual cor-pora supported language modeling. Documents were normalized, tokenized, stemmed, indexed, and semantically enriched before retrieval. The original evaluation used precision and recall as the principal effectiveness measures. For Amharic-to-English retrieval, the system achieved 72% precision and 79% recall; for English-to-Amharic retrieval, it achieved 65% precision and 70% recall. These findings show that a modular translation-and-retrieval architecture can provide useful cross-language access even under low-resource conditions. This revised article preserves the original experimental claims while situating them in the context of subsequent multilingual transformer and Amharic QA research.

---


### 137. [Rethinking Opinion Measurement Interfaces for Human-in-the-Loop Optimization](https://arxiv.org/abs/2610.14757)

**<font color=#1a73e8>作者：</font>** Changkun Ou, Sven Mayer, Daniel Buschek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-in-the-loop optimization refers to systems that present choices to a human decision-maker and query their judgment to optimize system parameters iteratively. The user interface typically provides either an absolute rating scale or asks for a preferred option. However, these approaches can potentially suffer from calibration problems, inconsistencies, and completeness violations of user preferences in such a sequential evaluation. This paper revisits the design space of opinion measurement interfaces for human-in-the-loop optimization. We conducted a study (N=360) using text summarization and image color enhancement tasks to evaluate human sequential feedback in six representative opinion measurement interfaces. Based on our analysis, we recommend using a listwise approach to support sequential opinion measurement, which counterweighs individual rating and preferential choice limitations and conveys more information for subsequent use. We further discuss the trade-offs in different user interface designs and provide guidelines to inform future research.

---


### 138. [The Constitution Speaks Nheengatu: An Open MT System and Reproducible Corpus Pipeline for the Amazonian Língua Geral](https://arxiv.org/abs/2610.14760)

**<font color=#1a73e8>作者：</font>** Fabrício Carraro, Rodolfo Joel Zevallos, Rodrigo Gonçalves de Souza 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nheengatu (yrl), the Amazonian Língua Geral, has 6--10 thousand speakers and is co-official in São Gabriel da Cachoeira (Brazil), yet remains poorly served by evaluated Portuguese--Nheengatu MT resources. We present the largest parallel corpus assembled for the language (14.5k Portuguese--Nheengatu pairs), anchored by the 2023 official translation of the Brazilian Federal Constitution; the first MT evaluation set built from transcribed spontaneous speech; and, to our knowledge, the first open-weight MT models dedicated to bidirectional Portuguese--Nheengatu translation.
Three findings organize the paper. First, translation into Nheengatu on held-out constitutional articles plateaus on development data regardless of training length or model size, and much of the remaining error sits in conventional legal terms that the written sources do not attest consistently; a terminology success rate over a frozen lexicon shows that glossary mechanisms at training time and lexical constraints at decoding each raise term realization, the latter at a cost in repetitive output that chrF++ barely registers. Second, a corpus expansion that adds transcribed conversation raises speech chrF++ by 24--27 points while leaving written domains unchanged, a register gap that written-only benchmarks cannot see. Third, a larger NLLB model helps translation into Portuguese but not into Nheengatu on legal or speech text. For Portuguese-to-Nheengatu translation, our final systems reach 31.7--32.8 chrF++ on article-disjoint constitutional text, 64.1--64.5 on the near-domain set (62.1 after removing items with target-side content overlap), and 45.2--47.5 on speech.

---


### 139. [CrossMean: Model Merging by Pairing Merged and Expert Activations](https://arxiv.org/abs/2610.14762)

**<font color=#1a73e8>作者：</font>** Moshe Eliasof  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines fine-tuned experts into one network without retraining, and closed-form methods compute each merged layer from statistics of its input activations. However, these statistics are measured on a single expert, while in the merged model, each layer receives activations from the merged layers that precede it. Recent work re-measures these statistics in the merged model but still forms them from a single network. We formulate closed-form methods as a linear system and show that they use the same matrix on both sides. We then introduce CrossMean, which replaces this matrix on one side with a bilinear statistic that pairs merged and expert activations. From the same statistics, we also derive a label-free criterion that indicates the task sets in which accounting for the merged activations improves the merge more. Empirically, task sets with a lower criterion value show a larger improvement. On the eight-task benchmark of each vision backbone that we tested and on BERT encoders, CrossMean improves on merging with statistics measured on the experts, and with all linear layers merged, it also improves on re-measuring these statistics in the merged model. These results suggest that merging benefits from pairing merged and expert activations.

---


### 140. [When Does Trust Help? A Leakage-Free Evaluation of Representation- and Aggregation-Based Defenses Against Backdoors in Federated Intrusion Detection](https://arxiv.org/abs/2610.14767)

**<font color=#1a73e8>作者：</font>** Shiddarth Dey Tusar, Zawad Yalmie Sazid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) lets distributed intrusion-detection systems (IDS) train on private traffic, but exposes the global model to poisoning and backdoor attacks under non-IID client data. A popular defense family scores or filters clients using a small trusted "root" dataset and the similarity of client behaviour to a trusted reference. I re-examine these trust-based defenses under a protocol designed to remove common evaluation artifacts: train-only feature standardization, a server root set disjoint from client data, multi-seed (n=6) runs with paired significance tests, formal (varepsilon, delta) accounting for DP-SGD, and a defense-aware adaptive attacker. Across three NIDS datasets (CSE-CIC-IDS2018, NF-ToN-IoT, NF-UNSW-NB15-v2) I find: (1) a representation-similarity aggregator (RepGuard) significantly improves classification utility and seed-stability over FLTrust under heavy non-IID poisoning, and - under severe heterogeneity or many adversaries - also lowers backdoor ASR substantially (e.g., 0.48 vs FLTrust 0.86 at Dirichlet alpha=0.1); (2) at strong trigger magnitudes no defense reduces backdoor attack success rate (ASR approx 0.95); (3) a controlled trigger-magnitude sweep shows defenses help only for small triggers (ASR 0.10 for RepGuard at magnitude 0.5, vs. 0.40 undefended) and collapse to ASR approx 1.0 by magnitude 2; (4) a triggered-canary check that assumes knowledge of the attacker's trigger - the assumption behind much prior "success" - lowers ASR from 0.49 to 0.12, i.e., trigger knowledge, not representation scoring, suppresses the backdoor; (5) correctly-accounted DP-SGD (varepsilon in [0.3, 16]) costs little utility but does not mitigate the backdoor. I release the protocol so future FL-IDS defenses can be evaluated without the leakage and oracle assumptions that inflate reported robustness.

---


### 141. [Prior-Fitted and Frozen Scorers for Multimodal Contrastive Learning](https://arxiv.org/abs/2610.14770)

**<font color=#1a73e8>作者：</font>** Tillmann Rheude, Roland Eils, Benjamin Wild  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal contrastive learning typically relies on manually specified scoring functions, such as cosine similarity, to quantify the similarity between representations from different modalities. Several such functions have been recently proposed to extend contrastive learning beyond two modalities. In principle, however, any function that assigns high compatibility to matched samples and low compatibility to mismatched ones could serve as a scorer. Motivated by this broader view, we instantiate the scorer with a Transformer and find that even a randomly initialized model, when kept frozen, can outperform strong handcrafted multimodal contrastive baselines, whereas optimizing the scorer jointly with the encoders is less effective. Building on this observation, we introduce the Prior-Fitted Scorer (PFS): a Transformer scorer pre-trained on synthetic multimodal data generated from structural causal model (SCM) priors before transferring it to real-world data. The SCM exposes the scorer to diverse dependency structures, including shared, pairwise, and private information, providing a structured prior over higher-order cross-modal similarity. Across four real-world datasets, frozen Transformer scorers are competitive to contrastive baselines, and prior-fitting further improves the random initialization. More broadly, our results suggest that multimodal contrastive learning need not rely on manual similarity functions: Transformers can provide strong inductive biases, while causal pretraining can further shape these biases.

---


### 142. [How Should a Camera-First AI Agent Work?](https://arxiv.org/abs/2610.14772)

**<font color=#1a73e8>作者：</font>** Xiaofan Wu, Xi Zeng, Miaoxia Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Camera-first agents must act on the visual world as it unfolds. We argue that the central obstacle for future camera-first agents is not recognition ability - multimodal models (vision-language and live/streaming alike) generalize well through language and remain the right tool for semantic reasoning - but time. Many visual targets are ephemeral: they appear, are query-relevant, and leave within a short window. Binding memory to the same end-to-end path as reasoning means that by the time a monolithic pipeline completes, the evidence is gone. We formalize this as Ephemeral-Target Interaction (ETI) and a Perceptual Deadline Contract separating a hard memory deadline from a soft reasoning deadline, grounded in the bounded, passive nature of sensory and working memory. We propose a two-deadline architecture: an always-on, bounded, non-semantic fast path; an active remembering mechanism that commits a moment to durable memory before it is overwritten (event-driven in v1); and a deferred deliberation layer (multimodal model + tools). We instantiate the contract on real MOT17 track windows, a consistency check, and calibrate the single-path baseline from measured frontier-model latency: even a short answer takes 1.2-9.3 s, and an agentic identify-and-search longer. Answers can be late; evidence cannot be missed.

---


### 143. [Formalizing Forgetting: Theory of Forgetting for Online Continual Learning](https://arxiv.org/abs/2610.14787)

**<font color=#1a73e8>作者：</font>** Renjie Cao, Yifei Cheng, Li Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online continual learning (OCL) requires a learner to acquire a sequence of tasks in a single pass over the data, and catastrophic forgetting of earlier tasks remains its central challenge. Despite the many methods proposed to mitigate forgetting, the theoretical understanding of forgetting in OCL is still limited: existing analyses mostly focus on linear, overparameterized, or neural tangent kernel regimes, and it remains unclear which factors govern forgetting and how they affect it. To fill this gap, we analyze single-pass Shuffle SGD under strongly convex and general convex objectives and derive explicit upper bounds on the expected final forgetting. Further analysis of these bounds shows how the per-task data amount, task similarity, and task ordering enter them, and that their effects can differ across objective classes. Moreover, experiments with neural networks on Split-CIFAR-100 and PMNIST show that the trends suggested by our theory also appear in practice, indicating that these insights extend beyond the convex setting.

---


### 144. [GREAT-ESDD: Graph Edge Attention Network for Effectively Steered Delivery Decisions](https://arxiv.org/abs/2610.14792)

**<font color=#1a73e8>作者：</font>** Attila Lischka, Ze Zhou, Xuegang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online, same-day delivery requires operators to constantly update their routes, and the routing cost for deliveries increases with the number of customers. Out-of-home (OOH) delivery options can help companies handle increasing customer numbers while keeping delivery costs low. We develop a dynamic pricing-and-routing framework for this online ordering scenario with home and OOH delivery options. First, we develop a neural solver for the capacitated vehicle routing problem (CVRP) based on the Graph-Edge-Attention-Network (GREAT). We train it to solve CVRP with varying instance sizes and starting conditions, allowing it to reoptimize partially executed routes under changing conditions. It is fast while achieving solution quality competitive with traditional baselines. Our solver processes several CVRP instances in parallel in batches and we use it to solve the candidate routing problems that arise from an incoming customer's choice of home or OOH delivery. This provides an estimate of the delivery cost increase per option, which we use to set dynamic prices. Further, it directly provides the updated route once the customer decides. We trade off delivery fees against routing costs and steer customers toward OOH delivery when home delivery would be costly. However, effective steering requires us to know the customer preferences. To learn those online, we use Thompson sampling with a Laplace-approximated posterior. We call the resulting framework GREAT-ESDD (GREAT for Effectively Steered Delivery Decisions). Compared to a traditional routing solver, it increases profit by around 11% under a similar pricing decision time budget. Moreover, we show that we can estimate customer preferences successfully, outperforming a static pricing strategy after only 5 days of simulated operations.

---


### 145. [CESNET-TimeSeries26: A Multi-Year Network Traffic Time Series Dataset for Annual Seasonality, Concept Drift, and Long-Term Anomaly Detection](https://arxiv.org/abs/2610.14799)

**<font color=#1a73e8>作者：</font>** Josef Koumar, Karel Hynek, Kamil Jerabek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecast-based models are fundamental to network traffic management and anomaly detection. However, it is essential to evaluate these forecasting models over extended periods of time in order to assess their adaptability to unexpected phenomena and shifts in underlying patterns. This kind of long-term evaluation requires multi-year data to account for yearly seasonality and behavioral drift. Existing public datasets are too short to support such long-horizon forecasting tasks. We introduce CESNET-TimeSeries26, comprising 995 days of continuous traffic time series from the CESNET3 network, together with a single subnet spanning approximately 4.5 years. The dataset captures 278,466 IP addresses, 285 institutions, and 566 institutional subnets at three aggregation intervals. The dataset provides a definitive longitudinal benchmark for evaluating forecasting models in both operational management and security monitoring. We demonstrate that annual seasonality is the dominant periodic component. Moreover, we show that a forecasting model can exploit the annual component only when its training window covers at least one complete annual cycle, which no sub-year dataset provides.

---


### 146. [YOUDrive: Driving Style as a Composable Direction for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.14802)

**<font color=#1a73e8>作者：</font>** Guantian Zheng, Lidong Yu, Tianyu Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end driving policies can achieve strong task performance while offering limited control over their driving style. Driving style describes how a vehicle accelerates, brakes, and maintains distance. Policies trained without explicit preference conditioning lack a direct mechanism for adjusting these behaviors at inference. We propose YOUDrive, a vision--language--action planner for continuous and composable driving-style control. Each teacher's behavior is distilled into a task vector, a learned parameter update that induces a style direction in the planner's representation. These directions can be scaled and combined at inference without retraining the backbone. Conditioned on these directions, a flow-matching decoder models a multimodal trajectory distribution and generates kinematically feasible motion alternatives. We introduce the Style Alignment Score (SAS) to describe human-referenced kinematic behavior after safety and task gating. On NAVSIM navtest, a single coefficient monotonically controls assertiveness across six teacher-derived personas, while PDMS remains above 0.90 across the tested individual and blended configurations, reaching 0.954. Further analyses reveal systematic policy-specific kinematics after controlling for scene context, whereas the evaluated discrete style labels provide limited additional explanatory power. Code, checkpoints, and the metric will be released.

---


### 147. [ASIWorld: Benchmarking Autonomous Agents in a Persistent Survival Sandbox](https://arxiv.org/abs/2610.14807)

**<font color=#1a73e8>作者：</font>** Jianfeng Lin, Runze Wang, Haorong Hong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating autonomous agents requires examining whether they can translate goals into coherent action across extended interactions. In persistent environments, this requires coordinating interdependent actions under incomplete observations, accounting for delayed effects, and adapting as earlier decisions shape subsequent opportunities. We introduce ASIWorld, a survival sandbox that combines persistent world and character state with character-scoped observations and a programmable asynchronous interface to study sustained goal execution. Agents pursue interdependent production and exploration tasks through direct actions or agent-authored programs that continue running between model calls. The evaluation assesses task success, the attainment of development achievements, and survival costs, complemented by an analysis of execution behavior. In an exploratory study of nine agent configurations using a common harness, eight complete the production task and six complete both tasks. Analyses of execution trajectories and performance across difficulty levels reveal different preparation, combat, and recovery behaviors among configurations with similar task outcomes. Incomplete preparation is associated with stalled progression, while configurations that complete the tasks differ in survival costs and the fulfillment of additional achievement criteria. These findings illustrate the value of assessing sustained goal execution through both task outcomes and the behaviors and costs associated with achieving them.

---


### 148. [Groups Don't Move as One: A Bregman Clustering View of Linearized Group Influence](https://arxiv.org/abs/2610.14809)

**<font color=#1a73e8>作者：</font>** Hyunho Choi, Jaeseung Heo, Youngbin Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Influence functions provide an efficient alternative to retraining for assessing the effects of removing or reweighting training data. For groups, however, the standard first-order estimate reduces individual contributions to a sum that can conceal substantial differences among members, including opposing effects that cancel. We establish a Bregman centroid formulation of the linearized group influence objective, interpreting this aggregate as a single representative and using Bregman information (BI) to quantify the variation it omits. Extending this formulation to multiple clusters reveals distinct contributions whose sum recovers the original estimate. We further propose an estimator that jointly optimizes the weights of these cluster contributions, rather than simply summing them. Experiments uncover cluster-specific influence patterns and a positive association between target-specific BI and approximation error. The proposed estimator achieves higher $R^2$ than standard group influence in predicting target changes under the nonlinear proximal Bregman response function. Simplified clustering and correction variants reduce computational cost. The centroid view thus explains what additive group influence leaves out and provides a basis for using that information to improve estimation.

---


### 149. [Machine Learning-Based Prediction of Dengue Infection Using Clinical and Hematological Data from Bangladesh: A Comparative Analysis of Benchmark and Extended Prediction Models](https://arxiv.org/abs/2610.14813)

**<font color=#1a73e8>作者：</font>** Neesha Naimeen, Victor Miranda Soberanis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dengue is a viral infection caused by the dengue virus (DENV) and a major public health concern in Bangladesh, where symptom overlap with other febrile illnesses complicates early diagnosis. This study compares Logistic Regression, Random Forest and XGBoost to predict dengue from clinical and hematological data using two Bangladeshi hospital datasets (2024, n=1,511; 2025, n=1,283) with SMOTE. Extended models outperformed benchmarks within 2024 (Random Forest ROC-AUC 0.640 to 0.661), with RDW-CV the most consistently influential added predictor. 2025 benchmark performance was higher (ROC-AUC 0.904), unexplained by class imbalance and possibly reflecting data quality. External validation is needed.

---


### 150. [EvoCowork: A Benchmark for Real-World Office Tasks](https://arxiv.org/abs/2610.14828)

**<font color=#1a73e8>作者：</font>** Zhou Liu, Xingyan Chen, ZhaoYang Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Office workflows are a demanding testbed for self-improving agents because their deliverables must be correct, natively editable, and mutually consistent. A central question is whether gains on feedback tasks reflect reusable procedures rather than task-specific fixes. We introduce EvoCowork, a 240-task benchmark for evaluating harness-level recursive self-improvement across four office modalities, with model weights held fixed. The benchmark covers presentations, documents, spreadsheets, and cross-office workflows, and scores submitted artifacts for content, native structure, formulas, cross-file consistency, and visual quality where needed. Its protocol separates feedback, revision selection, and final testing: methods learn from single-modality tasks, then are evaluated on unseen single-modality tasks and cross-office workflows under a shared initial harness and explicit budgets. In static evaluations of two models and four harnesses, the best configuration scores 42.25 overall and 30.62 on cross-office tasks. Starting from the same MSA harness with GLM 5.3, ACE and AHE improve in-domain scores by 4.90 and 2.64 points, respectively, but change cross-office scores by only +0.03 and -1.72. Thus, gains on the file types that provide feedback do not necessarily transfer to coordinated workflows. EvoCowork makes this distinction explicit while recording the capability, transfer, and cost of harness evolution. Code and task packages: this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
