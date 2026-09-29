# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**601-650**（第 13/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 601. [Dexterous Tactile World Model](https://arxiv.org/abs/2609.34286)

**<font color=#1a73e8>作者：</font>** Ziyao Zeng, Xiatao Sun, Hao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models for manipulation are typically trained from video, yet the events that determine how manipulation unfolds, such as making and releasing contact, are difficult to observe visually and are often easier to sense through touch. We present the Dexterous Tactile World Model (DTWM), a video world model for future-frame prediction of egocentric manipulation from both observed video and tactile signals from a glove worn on each hand. We condition a pretrained video diffusion transformer on each hand's tactile signal through a zero-initialized residual at the corresponding hand location in the video tokens, while a causal mask prevents predicted frames from accessing future information. Compared with a vision-only model matched in architecture, parameters, and training, DTWM reduces the underestimation of hand motion from 23% to 9%, while reducing the perceptual error in the hand region by 7.4% across three training runs per model. The benefit also increases over the prediction horizon, with the improvement in the later predicted chunks being about 4.1x larger than in the first. DTWM also outperforms other visual-tactile world models under the same setting, and training with touch improves future-frame prediction even when no touch is available at inference. Ablations show that the model benefits from both the magnitude and spatial location of force: replacing the tactile signal with binary contact states, either per hand or per location, increases prediction error. The observed course of the force indicates whether the interaction will persist or change.

---


### 602. [Semantic Modality Compensation for Unsupervised Visible-Infrared Person Re-identification under Unpaired Settings](https://arxiv.org/abs/2609.34294)

**<font color=#1a73e8>作者：</font>** Duanning Chen, Ke He, Bin Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised visible-infrared person re-identification (USL-VI-ReID) learns person representations that can be compared across modalities without identity annotations. In the unpaired setting, however, identity correspondences between modalities are often incomplete, leaving many identities without an observed counterpart in the other modality. Existing unpaired methods bridge this gap by generating or mapping features for the other modality, mainly by exploiting the statistics of visual features without explicitly separating content that is discriminative for identity from style that is specific to modality. Consequently, the generated features may distort identity cues or inherit bias from the source modality, undermining the reliability of supervision across modalities. We formulate unpaired learning across modalities as a semantic compensation problem and propose Semantic Modality Compensation (SMC), a framework based on prompt composition that decouples identity semantics from modality style within a shared visual semantic space. SMC first constructs a discriminative ReID space through augmented dual contrastive learning, yielding pseudo labels, cluster prototypes, and memory banks for each modality. It then learns visible and infrared modality prompts in the CLIP semantic space and maps clusters obtained from pseudo labels to identity semantic tokens. For each cluster lacking a reliable match in the other modality, SMC combines its identity token with the prompt for the target modality to synthesize a semantic counterpart in the missing modality. The synthesized counterpart is then projected back into the ReID space and injected into a compensation memory through confidence gating. Extensive experiments under both paired and unpaired settings demonstrate that SMC consistently outperforms state-of-the-art methods, with particularly large gains when identity mismatch is severe.

---


### 603. [PSM: Dataset Distillation Based on Precise Statistical Matching by Difficulty](https://arxiv.org/abs/2609.34299)

**<font color=#1a73e8>作者：</font>** Hongxu Ma, Guang Li, Shijie Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation (DD) condenses a large original dataset into a small distilled dataset with high training utility. Decoupled statistical matching methods substantially reduce distillation time and memory overhead while achieving strong performance. However, they typically supervise all distilled samples using running statistics estimated from the entire original dataset. These statistics mainly capture the average feature distribution while overlooking differences in sample difficulty, limiting their ability to characterize the difficulty structure of the original data. To address this issue, we propose Precise Statistical Matching (PSM) by difficulty. After pretraining, PSM uses the Global Precision Score (GPS) to estimate image difficulty, ranks the samples within each class, and partitions each class into IPC (images per class) difficulty groups. During distillation, Statistics Updated Again (SUA) updates the teacher's batch normalization (BN) running statistics through forward passes on original samples from each group, providing difficulty-specific supervision for the corresponding distilled batch. Meanwhile, Initial Sample Screening (ISS) initializes distilled samples using original images from the corresponding difficulty group, providing an effective starting point for precise matching. Experiments across multiple datasets and model architectures demonstrate that PSM broadens the difficulty range of distilled samples and improves downstream performance in most evaluated settings. Code will be released.

---


### 604. [CAT-Free: Multi-View Pedestrian Localization without Calibration, Annotations, or Target-Scene Training via Adaptive Geometric Filtering](https://arxiv.org/abs/2609.34302)

**<font color=#1a73e8>作者：</font>** Taigo Sakai, Hiroki Kouno, Naoki Kato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-camera pedestrian localization is useful for wide-area monitoring in public and commercial spaces. However, deploying these systems often requires considerable setup for each new environment. Existing methods typically require camera calibration, position annotations, or target-scene training. CAT-Free removes all three requirements. It uses synchronized RGB video as its only scene-specific input. Camera configuration is estimated directly from the video. Pedestrian locations are then estimated by combining observations from multiple cameras. Automatic camera estimation is not always accurate. This can produce unreliable pedestrian locations. CAT-Free therefore introduces two adaptive geometric filters. They remove unreliable position estimates. Their thresholds are estimated from each input sequence. CAT-Free achieves 82.5, 84.5, and 65.7 MODA on WildTrack, MultiviewX, and GMVD. It uses no supplied calibration, position annotations, or target-scene training. Published methods using such scene-specific information report 88.2--95.0 MODA on WildTrack and 83.9--96.5 on MultiviewX under their respective protocols. CAT-Free also transfers without retuning. It reaches 74.9 MODA on four additional sequences and 78.6 on an unseen 8-camera installation. Finally, localization uncertainty predicts MODA with $r=-0.98$. This provides a label-free estimate of localization reliability.

---


### 605. [Riemannian Difference-of-Convex Optimization for K-Means Clustering](https://arxiv.org/abs/2609.34310)

**<font color=#1a73e8>作者：</font>** Meng Xu, Bo Jiang, Hanfu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> K-means is a widely adopted clustering approach in signal processing and machine learning. In this paper, we study K-means clustering through a cardinality-constrained formulation on a compact embedded submanifold. We replace the cardinality constraint with a difference-of-convex (DC) penalty and establish a global error bound to prove that the penalized and constrained formulations share the same global minimizers whenever the penalty parameter exceeds a finite threshold. To solve the resulting nonsmooth Riemannian DC problem, we reformulate it as a minimax problem and propose RADA-DC, a Riemannian alternating descent ascent method combining dual regularization with DC linearization. Under standard assumptions and suitable parameter choices, RADA-DC finds an $\epsilon$-Riemannian critical point within $O(\epsilon^{-3})$ iterations. We conduct experiments on synthetic and real-world datasets to demonstrate that the proposed method outperforms the tested baselines, including K-means++, in solution quality at competitive computational cost when the number of clusters is large.

---


### 606. [DORA: Dynamic Online Reinforcement Agent for Token Pruning in Vision Transformers](https://arxiv.org/abs/2609.34325)

**<font color=#1a73e8>作者：</font>** Kaixuan He, Song Chen, Yi Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) incur quadratic self-attention cost in the number of tokens. Most token-reduction methods adapt token identities within a prescribed layer-wise compression schedule, or search a static mask offline, and thus limit online adaptation of when and how much to prune. We propose DORA (Dynamic Online Reinforcement Agent), which learns an input-adaptive pruning policy itself for frozen ViTs. At each eligible block, a hierarchical actor decides whether to prune, how many tokens to remove, and which tokens to remove from each image's evolving representation. Because early deletions change the states observed by later decisions, DORA formulates pruning as a finite-horizon Markov decision process. Complete-prefix shadow evaluations convert final-prediction fidelity into localized per-step credit, while closed-loop accuracy feedback adjusts the fidelity penalty toward a shared accuracy-drop target. A privileged critic and all shadow computations are training-only. Deployment retains the frozen backbone and a lightweight actor that applies hard deletion and packed variable-length FlashAttention, converting token reduction into measured speedups. On ImageNet-1K with DeiT-Base, DORA reduces FLOPs by 38.4% relative to the uncompressed backbone within one percentage point of accuracy loss. Averaged across four ViT-type backbones at matched accuracy, DORA uses 13.2% fewer FLOPs and achieves 32.4% higher throughput than the corresponding per-backbone baseline means. Under zero-shot transfer to ImageNet-A, these gains widen to 20.3% and 45.6%, respectively.

---


### 607. [SkillPE: Creativity-Oriented Cinematic Skill Evolution for Text-to-Video Prompt Engineering](https://arxiv.org/abs/2609.34335)

**<font color=#1a73e8>作者：</font>** Yanwei Huang, Mingxuan Zhu, Shujie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving high-quality, cinematic results in text-to-video generation remains challenging for non-experts, whose prompts often lack professional narrative and creative design. We propose SkillPE, a prompt engineering (PE) framework that evolves reusable cinematic skills from expert-authored seeds. SkillPE represents shot logic, composition, lighting, sound design, and other filmmaking cues in a fine-grained format, and retrieves movie references categorized as resonators (good matches), dissonants (weak matches), and divergents (creatively useful near-misses). The first two refine when and how a skill should be applied, while divergents inspire alternative cinematic realizations at different degrees of modification while preserving the user intent. Candidate skills are assessed through generated videos along prompt fidelity, cinematic quality, narrative appeal, and creativity to construct the final skill libraries. Experiments on StoryEval and VBench show improvements of up to 1.40 points over the strongest external baseline and 0.51 points over seed skills on 7-point four-dimensional evaluation, while remaining competitive on benchmark-native metrics. Overall, SkillPE offers a practical approach to balancing fidelity and creativity in cinematic text-to-video generation. Code is available at this https URL .

---


### 608. [The Composition Gap in Dataset Distillation](https://arxiv.org/abs/2609.34343)

**<font color=#1a73e8>作者：</font>** Guang Li, Takahiro Ogawa, Miki Haseyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dataset distillation compresses a training set into a small synthetic set, usually evaluated one at a time. In federated and data-governance settings, several parties distill their own data and a user trains on their union. We ask whether the union of separately distilled sets reproduces training on the union of the real data composability and show that it can fail even when every source is distilled exactly and the total budget admits an exact joint distillate. Compressing a training trajectory into fewer steps transforms the source statistics nonlinearly, so averaging compressed sources differs from compressing their average. For quadratic objectives we derive the exact composition error for two-to-one step compression in terms of the source-Hessian variance and the linear terms of the losses, and on a smooth network at small step sizes this prediction captures the local endpoint discrepancy in magnitude and direction. For learned synthetic sets, however, the composed error decomposes exactly into this local discrepancy and an aggregate source residual. Under endpoint matching the residual exceeds the structural term by more than an order of magnitude, and under distribution matching the two terms partly cancel. Joint distillation also retains an accuracy advantage when both sets are distilled from the same dataset, where the local discrepancy is exactly zero. Training fidelity and downstream accuracy are therefore distinct requirements, neither established by evaluating each set on its own.

---


### 609. [E-WAVE: Event-based Continuous Optical Flow via Warping-Aligned Visual Encoding](https://arxiv.org/abs/2609.34346)

**<font color=#1a73e8>作者：</font>** Jiale Wu, Xiaoyang Bai, Haoming Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporally dense optical flow is essential for dynamic perception in immersive VR/AR systems, where rapid head, hand, and object motion must be continuously captured and tracked. Existing frame-based optical flow estimation methods are constrained by the tradeoff between temporal resolution and computational cost; while event cameras, with their high temporal resolution and energy efficiency, serve as a natural solution to the dilemma. However, event-based approaches commonly rely on correlation volumes to capture pairwise voxel correspondences, which incur substantial memory and computation overhead. We present E-WAVE, a correlation-free framework for high-temporal-resolution (HTR) optical flow estimation from event streams. Instead of constructing all-pairs correlation volumes, E-WAVE employs global attention mechanism to model long-range feature dependencies and performs trajectory guided feature warping using Bézier curve. Through iterative updates, it predicts trajectories that allow for querying at arbitrary timestamps without repeated inference. Experiments on MultiFlow and DSEC-Flow demonstrate a 25% lower trajectory error and comparable endpoint flow estimation accuracy relative to state-of-the art baselines. Additional evaluations on self-captured data using a head-mounted prototype validate that E-WAVE remains robust under challenging real-world conditions.

---


### 610. [Fuzzy Distribution Modeling for Synthetic Tabular Data Generation with Causality Preservation](https://arxiv.org/abs/2609.34349)

**<font color=#1a73e8>作者：</font>** Michael Vasilakakis, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthetic tabular data generation provides an effective alternative for the training of machine learning models when real-world data is limited or inaccessible. However, the heterogeneous, non-smooth, and incomplete nature of tabular data poses fundamental challenges to conventional probabilistic and deep generative models, where their interpretability remains limited. This paper proposes a novel fuzzy distribution modeling methodology for synthetic tabular data generation based on fuzzy sets theory. Feature distributions are represented using fuzzy sets and feature dependencies are modeled through Fuzzy Cognitive Maps, resulting in a low-parameter, and an interpretable data representation. Synthetic samples are generated by sampling fuzzy concepts rather than raw values, enabling native support for mixed data types, missing values, and domain constraints. The methodology further supports linguistic queries and IF-THEN reasoning, facilitating transparent simulation of decision-making processes. Experimental results on benchmark datasets demonstrate competitive performance with respect to utility, fidelity and privacy compared to state-of-the-art methods, while offering substantially improved interpretability. These results establish fuzzy distribution modeling as a principled and effective approach for synthetic tabular data generation in fuzzy systems and decision support applications.

---


### 611. [SemRD-V2X: Closure-Guided Communication with Bounded Inference for Cooperative Perception](https://arxiv.org/abs/2609.34353)

**<font color=#1a73e8>作者：</font>** Hu Xu, Chun Li, Siyuan Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vehicle-to-Everything (V2X) cooperative perception improves 3-D detection by sharing intermediate features, but dense remote features may repeat context that the ego agent can infer locally. Most communication-efficient designs optimize masks or codes empirically, leaving a more basic question open: which remote evidence is indispensable given the receiver's own observation? We introduce a closure-fidelity perspective on ego conditioned remote perception. Under a finite deductive abstraction and explicit conditions, its rate--distortion function decomposes over an irredundant core, and the exact zero-distortion rate becomes $P_A H(\pi_A)$. This analysis suggests a concrete design principle: transmit compact evidence and recover derivable context with bounded receiver-side inference. Guided by this principle, SemRD-V2X is an operational neural proxy that combines exact-budget BEV support selection, pointwise channel compression, and masked shared-weight reconstruction before standard fusion. Experiments on simulated V2XSet and real-world DAIR-V2X validate the resulting design. In a controlled five-run V2XSet comparison against a locally reproduced V2X-ViT-v1 baseline on one Tesla V100, SemRD-V2X reduces the analytical feature payload by $26.6\times$ while improving AP@0.5/AP@0.7 by 4.13/8.57 points, with 3.81\% additional mean compute latency. These results position closure fidelity as both an analytical lens and an actionable design principle for communication-efficient cooperative perception.

---


### 612. [FAST-Brain: A Flow-Aligned Spatio-Temporal Surrogate Brain Model](https://arxiv.org/abs/2609.34354)

**<font color=#1a73e8>作者：</font>** Shucheng Liu, Changchun Shi, Kai Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling resting-state functional magnetic resonance imaging (rs-fMRI) data is crucial for understanding brain-wide neural activity. However, traditional methods struggle to capture complex temporal dynamics over long horizons, to account for the brain's anatomical spatial structure, and to model high-dimensional ambient signals that lie on a low-dimensional intrinsic subspace. We propose FAST-Brain, a unified flow-aligned spatio-temporal surrogate brain model that addresses all three challenges. At its core is a flow-aligned generative framework that directly predicts the clean blood-oxygen-level-dependent (BOLD) signal, paired with a graph convolutional network that captures spatial structural constraints and a Transformer that models long-range temporal dependencies. Theoretically, we show that under a low-dimensional subspace assumption, the approximation error of our model scales with the intrinsic dimension rather than the ambient dimension, which justifies our direct modeling of the BOLD signal. Extensive experiments on synthetic and Human Connectome Project datasets demonstrate that FAST-Brain achieves state-of-the-art performance in recovering functional connectivity, effective connectivity, and the implicit low-dimensional signal subspace.

---


### 613. [CoeF-SFL: Preserving Collaborative Server-Client Learning with Enhanced Communication Efficiency](https://arxiv.org/abs/2609.34360)

**<font color=#1a73e8>作者：</font>** Junwoo Bae, Jin-Hyun Ahn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Split Federated Learning (SFL) enables resource-constrained clients to participate in collaborative training, but vanilla SFL exchanges smashed data and gradients at every batch, which incurs significant communication overhead. Recent methods reduce this overhead with an auxiliary network at the client-side cut layer. However, we identify that this approach makes the client optimize a local objective that differs from the end-to-end objective, which fundamentally limits the collaborative training between the client and the server. We propose Compensated Feedback based SFL (CoeF-SFL), a communication-efficient framework that retains the end-to-end objective without any auxiliary network. In CoeF-SFL, the client and the server exchange the smashed data and the gradients once per round and reuse them during local training. Since this reuse makes the gradients stale on the client side, we compensate them with a curvature-based correction in the activation space and develop two variants. CoeF-D approximates the Hessian with a diagonal gradient outer product, while CoeF-J exploits the tractable Jacobian-based Hessian of a surrogate loss that upper-bounds the true loss. We provide the theoretical background of each method, characterizing its compensation. Across vision and language tasks, model capacities, cut layers, and data distributions, CoeF-SFL significantly outperforms auxiliary-network-based methods under the same communication frequency, and the improvement is most substantial on vision tasks. Code is available at this https URL

---


### 614. [SyncRA: Learning Temporal Correspondence in Omni-Modal Models](https://arxiv.org/abs/2609.34363)

**<font color=#1a73e8>作者：</font>** Zelong Xu, Yan Li, Wenhe Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent omni-modal models demonstrate strong perception of audio and visual inputs, yet often struggle to connect what they hear with what they see at the same moment. This weakness in temporal correspondence can cause models to associate spoken cues with the wrong visual scenes, producing plausible answers grounded in incorrect audio-visual pairings. We diagnose this problem through controlled temporal swaps, revealing that model answers do not reliably follow changes in these pairings. To address it, we propose Synchrony-Guided Representation Alignment (SyncRA), a lightweight method for strengthening temporal correspondence between audio and vision. Specifically, SyncRA contrasts intermediate audio-visual representations within each video, aligning matching moments while separating mismatched ones to capture local temporal correspondence within a shared global context. The objective derives supervision directly from existing input timing, requiring no additional annotations and leaving inference unchanged. We evaluate SyncRA across four open omni-modal models spanning different sizes and architectures on five public video benchmarks. SyncRA consistently outperforms answer-only fine-tuning across all model-benchmark combinations, while substantially improving the ability to track changing audio-visual pairings in controlled evaluations. These results demonstrate that lightweight, targeted supervision can effectively strengthen temporal correspondence and translate into broad improvements in audio-visual question answering.

---


### 615. [When Harness Beats Scale, and When Reading Beats Both](https://arxiv.org/abs/2609.34366)

**<font color=#1a73e8>作者：</font>** Ivan Bondarenko, Nikolay O. Nikitin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe our system for DocSem, the document-grounded quantitative reasoning shared task at DocInsights 2026, and analyze why it succeeded on labeled data and failed on the test set. The pipeline pairs hybrid block retrieval with Program-of-Thoughts (PoT) generation executed in a sandboxed interpreter, self-consistency sampling, and entity enrichment from chunk-level knowledge graphs. On our held-out split, application architecture moved the metrics far more than model scale did: PoT added 0.282 joint accuracy to a compact 7B model but at most 0.005 to a 72B model, and a 27B model with the full harness matched the 72B (0.884 vs.\ 0.873) at roughly 2.7$\times$ fewer parameters and a quarter of the CO$_2$. We read this through a distinction between world knowledge, which scales steeply with parameters, and language knowledge, which scales gently, and show that structured-output training makes a compact model harness-ready rather than merely small. On the raster, watermarked test PDFs the same system collapsed to 13.58\% joint (rank 149 of 163); a controlled re-rendering of the validation set reproduces the OCR half of the collapse while bounding what the simulation misses. Auditing the physical nature of evaluation inputs precedes architecture, and the leaderboard's bimodality is consistent with reading quality, not reasoning, having separated the field.

---


### 616. [Rate-Distortion Adaptive Primitive Selection for Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2609.34367)

**<font color=#1a73e8>作者：</font>** Yulong Cheng, Youneng Bao, Junfeng Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned image codecs (LICs) achieve high reconstruction quality, but their decoding speed is often insufficient for immersive virtual reality (VR). Gaussian splatting (GS) codecs render much faster, yet still lag in reconstruction quality and typically decide primitive allocation without considering the coding cost of each primitive. We introduce OIC-GS, an omnidirectional GS codec with a new hierarchical HEALPix primitive grid representation. Gaussian primitives are anchored at predefined spherical locations, eliminating explicit coordinate coding. Finer levels refine their coarser ancestors, naturally supporting coarse-to-fine reconstruction and layered transmission. The predefined grid also enables efficient viewport decoding by selecting only view-relevant primitives. We further introduce a lightweight entropy model for quantized primitives and optimize the codec under a spherical rate-distortion objective. Primitives with insufficient rate-distortion benefit are automatically removed when their quantized opacity becomes zero, allowing OIC-GS to adapt both primitive density and level of detail without a fixed primitive budget. A single bitstream supports full-sphere, viewport-dependent, and progressive decoding. The first viewport reaches final quality after decoding only 52% of the bitstream, and is then rendered at 1,270 FPS. On a 100-image omnidirectional benchmark, OIC-GS outperforms all evaluated GS codecs, reducing WS-PSNR BD-rate by 49.6% over GaussianImage++ and 68.6% over SGI, which uses a learned entropy model.

---


### 617. [Emergence, Not Bandwidth: Physical Coupling and the Limits of Learned Multi-Agent Communication](https://arxiv.org/abs/2609.34373)

**<font color=#1a73e8>作者：</font>** Mihir Chauhan, Aniket Bera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rate-limited multi-agent teams raise three questions the emergent-communication literature has answered only empirically: what an optimal message should encode, what compression costs over a horizon, and when a learned protocol is unique enough for a teammate to read. We answer them for rate-limited Dec-POMDPs, then measure how far reinforcement learning falls short of the optimum. Our theorems fix what is achievable independently of any learner, so a gap between an engineered and a learned sender at the same bit budget is an optimization fact, not an information-theoretic one. We instantiate this on three MuJoCo arenas spanning zero, partial and rigid physical coupling, charging every condition exactly 2 bits per decision, and create the discriminating regime by closing a physical side channel within one arena, holding bodies, task and reward fixed. Communication value is governed by coupling: under rigid coupling through a shared object, no channel beats silence (+0.001 +/- 0.001, p = 0.982, n = 25), since proprioception already carries that information; without coupling, every condition solves the task; under partial coupling, the engineered 2-bit sender reaches an interquartile mean of 1.000 but the learned one reaches 0.482, indistinguishable from silence (p = 0.400, n = 25). With a shared alphabet, bandwidth cannot explain the gap. Warm-starting from an engineered receiver localizes the failure: the same channel reaches 0.857 versus 0.562 cold-started (p < 0.001), so it is neither representational nor one of maintenance; reinforcement learning fails to discover the protocol. Cross-play shows learned protocols are individually meaningful but mutually unintelligible: self-play 0.980 collapses to 0.144 across seeds, and our best constructed alignment leaves at least 77% of that gap. All headline results use 25 seeds per arena and seven published baselines at matched rate.

---


### 618. [LRC-JEPA: Disentangling Dynamics and Residual Context for Efficient World Models](https://arxiv.org/abs/2609.34375)

**<font color=#1a73e8>作者：</font>** Luzhe Huang, Lei Chu, Jingyi Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compact JEPA world models enable efficient latent-space planning, but low-dimensional representation trained under reward-free self-supervision must encode both action-conditioned dynamics and predictable visual context. This competition can entangle controllable state with high-rank nuisance appearance and degrade planning as scenes become more complex. We introduce LRC-JEPA, a lightweight end-to-end world model that routes information into a compact predictive latent $\mathbf{z}$ and learned-query residual-context embeddings $\mathbf{u}$. Only $\mathbf{z}$ is propagated by the dynamics model and used for planning, while $\mathbf{u}$ captures temporally persistent information for cross-attention reconstruction; a differentiable residual connection encourages the latent to retain complementary dynamic content. Under explicit assumptions, we show that the resulting representation is sufficient, minimal, nuisance-invariant, and disentangled. Across four simulated control environments, LRC-JEPA improves average planning success over a parameter-matched JEPA baseline by 9 percentage points and matches or exceeds substantially larger pretrained models. On the real-world Bridge-v2 set, its 5.5M-parameter active encoder outperforms DINO-WM (22.1M) and V-JEPA2 (303.9M) encoders while also enabling faster planning. Physical-state probes, reconstruction interventions, and ablations confirm the effectiveness of LRC-JEPA's representation disentanglement.

---


### 619. [Marathoner: Ultra-Long-Horizon Autonomous Intelligence](https://arxiv.org/abs/2609.34378)

**<font color=#1a73e8>作者：</font>** Zhang Ruiyang, Ou Jinpeng, Xie Yifan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans naturally possess the ability to work persistently toward long-term goals. Given a challenging task, humans can continuously work for months or even years to accomplish a specific objective. In this paper, we propose Marathoner, an autonomous agentic model possessing the ability of ultra-long-horizon execution. Specifically, we propose a comprehensive post-training pipeline to instill this critical capability into base model. For Ultra-Long-Horizon Task Synthesis, we leverage major release PRs containing 1000+ lines of new code from diverse GitHub repositories as the primary source for synthesizing challenging task-level data. Additionally, we introduce Multi-Task Chaining, which chains multiple generated tasks into a single more challenging task, enabling the synthesis of tasks with frontier-level difficulty. For rejection sampling finetuning, we combine strong teacher model with diverse harnesses to generate trajectories on our synthesized tasks and conduct supervised finetuning on base model with rejection sampled trajectories. For reinforcement learning, cold-started model performs real-world execution through harnesses in independent sandboxes during rollout process, effectively facilitating the acquisition of genuine ultra-long-horizon execution capability. We further propose a novel reward strategy, Later Stage Bonus Reward, which explicitly encourages model to perform meaningful maneuvers during later stages of execution. Through extensive evaluation on 5 benchmarks containing ultra-long-horizon tasks, Marathoner achieves consistent and substantial performance improvements over base model and even surpasses performance of strong proprietary model. Further analysis shows that Marathoner can consistently work for 10+ hours and conduct 1000+ tool calls on highly challenging tasks.

---


### 620. [Joint and Cross-Modal Video-Audio Generation and Editing: A Unified Formulation and Design Taxonomy](https://arxiv.org/abs/2609.34381)

**<font color=#1a73e8>作者：</font>** Abhinav Sharma, Sai Karthik Navuluru, Wang Wei 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video and audio are perceived together, yet most generative models treat them in isolation. We examine methods that model the two modalities jointly, generate one from the other, or edit them in a coupled manner, organized around a single question: how is the output kept coherent across modalities in time and semantics? A unified formulation casts joint generation, cross-modal generation, and joint editing as three problems defined on a single distribution over audio-visual pairs, and a taxonomy compares methods along five design axes. To our knowledge, this is the first overview to systematically taxonomize joint audio-visual editing, which we map as nine edit categories spanning 28 edit types. We describe methods, datasets, and metrics for each setting and close with the open problems we view as most consequential.

---


### 621. [VastMAT: A Large-Scale Multi-Category Benchmark for Multi-Animal Tracking](https://arxiv.org/abs/2609.34390)

**<font color=#1a73e8>作者：</font>** Zhizhen Li, Zan Wang, Huidong Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-animal tracking (MAT) supports the study of animal movement, behavior, and group interactions. However, general multi-object tracking (MOT) benchmarks primarily focus on pedestrians and vehicles, whereas dedicated MAT benchmarks remain limited in jointly supporting broad animal coverage, large-scale video data, and extensive within-video multi-instance association. To address this gap, we introduce VastMAT, which has four key characteristics: (1) Large scale. It comprises 2,947 videos with 1,002,562 annotated frames, totaling 27.85 hours. (2) Broad category coverage. These videos cover 337 animal categories with diverse morphologies and motion patterns. (3) Extensive instance annotations. It provides 3,663,248 bounding boxes and 22,883 identity trajectories---to our knowledge, the largest numbers of both among dedicated MAT benchmarks. (4) High-quality annotations. To ensure reliability, annotations undergo iterative expert review and correction, and quality is assessed through an independent reannotation audit. To systematically assess tracking performance and cross-category generalization, we establish Seen-category and category-disjoint Unseen-category protocols, and evaluate eight representative MOT methods under both protocols. Under these protocols, the highest baseline HOTA scores are 66.37\% and 52.90\%, respectively, highlighting the challenge of tracking unseen animals. To address the low-overlap association challenge revealed by our analysis, we propose Center-Distance-Augmented Association (CDA), a lightweight module that adaptively combines IoU with center similarity normalized by the boxes' own scales. Without additional training, CDA improves TrackTrack's HOTA by 1.58 and 1.31 percentage points under the two protocols, respectively. To facilitate further MAT research, we will publicly release our benchmark and code.

---


### 622. [HyperDAM: Hyperspectral Distractor-Aware Memory with Amodal Expansion for SAM 3 Tracking](https://arxiv.org/abs/2609.34396)

**<font color=#1a73e8>作者：</font>** Ryoga Yuzawa, Tasuku Takagi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral video provides material cues that can disambiguate targets with similar false-color appearance, yet foundation-model trackers update memory primarily from spatial and appearance evidence. We present HyperDAM, a DAM4SAM3-based hyperspectral tracker with three principal contributions. First, HOTC2026-Modal adds human-verified frame-wise modal masks and mask-tight boxes to all 481 organizer-provided HOTC 2026 videos. Second, a frame-zero-calibrated HSI gate rejects spectrally inconsistent updates to the distractor-resolving memory (DRM) without altering the current prediction. Third, a causal spatiotemporal expander adds outward-only amodal corrections from frozen SAM features. Static-scene recovery and empty-mask RTS smoothing address target switches and full occlusion. Model selection prioritizes cross-domain robustness over leaderboard-specific optimization. The final system ranked second in HOTC 2026, achieving 68.0093% AUC and 87.7703% DP@20 in the organizer's private evaluation.

---


### 623. [GeoCFM: Positive-Only Conditional Flow Matching for Mineral Occurrence Sampling](https://arxiv.org/abs/2609.34398)

**<font color=#1a73e8>作者：</font>** Moshe Eliasof, Eldad Haber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Critical mineral discovery is a positive-only problem: deposits are observed as sparse locations, while unlabeled regions are not reliable negatives, and similar geophysical signatures can arise from different subsurface states. We therefore model mineral targeting as learning a conditional spatial distribution over occurrence locations, $\pi(p\mid d)$, given geo-images $d$, rather than predicting a deterministic per-pixel score map. We introduce GeoCFM, a conditional flow-matching model that generates mineral occurrence point sets conditioned on multi-channel geo-images; GeoCFM learns a point-wise transport field in $\mathbb{R}^2$, using UNet features with point-conditioned velocity prediction to bridge dense rasters and sparse supervision without pseudo-negatives. On a synthetic magnetics--geochemistry benchmark with latent activation and on USGS Earth MRI data with a spatially disjoint tile split, GeoCFM improves geometric agreement with observed occurrences over score-map and non-conditional baselines, while representing epistemic uncertainty through conditional sampling.

---


### 624. [Unlocking Few-Step Diffusion for Faithful Previews](https://arxiv.org/abs/2609.34406)

**<font color=#1a73e8>作者：</font>** Jing Jia, Sifan Liu, Guanyang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling latency compounds in diffusion workflows, where users generate and discard many candidates before keeping one. Surprisingly, the poor outputs of standard few-step samplers do not reflect a lack of reconstruction capacity: by optimizing only the initial noise, frozen 3-4-step samplers can closely reproduce their corresponding full-step outputs. Building on this finding, we learn corrections to the initial noise and denoising updates using endpoint supervision, improving correspondence with full-step outputs generated from the same noise and prompt. The resulting previews allow users to screen candidates cheaply and reserve full-step generation for promising ones. Input correction also transfers across sampling budgets without retraining. Experiments show substantial improvements in reference fidelity, including 53-78% lower reconstruction MSE than retrained LD3 on unconditional benchmarks, alongside improved ranking preservation and candidate selection on SD1.5, SDXL, and FLUX.1-dev.

---


### 625. [MASCIT: A Mask-Aware State Space Classifier for Naturally Irregular Time Series](https://arxiv.org/abs/2609.34409)

**<font color=#1a73e8>作者：</font>** Yoo-Min Jung, Hyeon-Gi Kim, Jonghun Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Naturally irregular time series combine asynchronous observations, missing values, unequal lengths, and nonuniform sampling, while dense adapters can discard temporal structure. We propose a mask-aware state space classifier for irregular time series (MASCIT), which supplies observation masks to the encoder and excludes invalid steps from gated temporal aggregation. Across 34 irregular time series datasets, MASCIT yielded the strongest aggregate point estimate and was the only evaluated neural model with three-seed results on every dataset. MASCIT retained the lowest point rank across six overlapping irregularity indicators, while factorial ablations favored partial over full selectivity. These results support selective state space models as effective, executable backbones for naturally irregular time series classification.

---


### 626. [Mathematics for and by human cognition: A resource-rational search for bottlenecks in problem-solving](https://arxiv.org/abs/2609.34410)

**<font color=#1a73e8>作者：</font>** Sneha Aenugu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human cognitive constraints are generally viewed as limiting factors in problem-solving. We argue that these constraints can instead play a critical role in driving advances in mathematics and beyond. We propose a theory of mathematical abstraction as a resource-rational search for bottlenecks in problem-solving. Bottlenecks arising from cognitive constraints create pressure to restructure existing knowledge, potentially giving rise to novel formalisms with applications beyond the problems that originally motivated them. Drawing on episodes from the history of mathematics, we illustrate how such bottlenecks can drive the development of novel abstractions and examine how cognitive constraints and affective responses shape this process. Finally, we discuss the implications of this account for machine mathematical discovery and argue that incorporating human-like constraints may facilitate the discovery of useful mathematical abstractions.

---


### 627. [Beyond End-to-End Black Box Mapping: An Intentional Agent Framework for Cognitive-driven Facial Reaction Generation](https://arxiv.org/abs/2609.34419)

**<font color=#1a73e8>作者：</font>** Hanzhong Zhang, Jindong Wang, Siyang Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic human-like facial reaction generation (FRG) is essential for building intelligent systems that can engage in human-computer interaction (HCI). While diverse and context-appropriate facial reactions can reflect latent appraisal and affective processes in human interaction, most existing FRG methods rely on end-to-end architectures that directly map speaker behaviours to listener expressions without an explicit intermediate internal state. We reformulate FRG as generation mediated by a structured internal-state process and propose the \textbf{Intentional Agent}, which shifts FRG from direct stimulus-response mapping to stimulus-grounded generation through explicit intermediate states. To represent temporal internal-state evolution, we propose an internal dynamics model that integrates emotional drives with an iterative Inner Thought Flow (ITF) within a structured intermediate state used for subsequent generation. This state can continue to update during conversational silences. Furthermore, to bridge abstract internal states with physiological actions, we formulate FRG as a downstream affective mapping from this latent thought flow to facial expressions. Experiments on the REACT 2025 dataset show an FRDist of 72.39 and an FRDiv of 0.5057; perceptual plausibility is evaluated separately through blinded human ratings. A blinded human evaluation of 96 reactions found no significant difference in mean score between Full and ground truth ($5.527$ vs.\ $5.195$, $p_{\mathrm{Holm}}=.076$), while Full significantly outperformed Event-Triggered and Heuristic-Only (both $p_{\mathrm{Holm}}<.001$). The Reaction Quality Scorer (RQS) correlated strongly with human judgements (Pearson $r=.855$; Spearman $\rho=.821$, both $p<.05$), supporting its use as an automatic metric. These results underscore the immense potential of endogenous dynamics in building highly autonomous, human-like agents.

---


### 628. [MegaGraph: Towards Efficient Training of Large-Scale Graph Transformers with Automated Hybrid Parallelism](https://arxiv.org/abs/2609.34420)

**<font color=#1a73e8>作者：</font>** Tong Qiao, Ao Zhou, Yingjie Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Transformers (GTs) offer superior representation capabilities by overcoming the depth limitations and over-smoothing issues of traditional Graph Neural Networks (GNNs). However, scaling GTs to large graphs poses critical bottlenecks. Specifically, the attention score matrix and its associated topology-aware bias matrix jointly incur significant per-layer memory overhead, and heavy graph embedding layers result in severe workload imbalances. These characteristics are unique to GT training and are not addressed by parallelism techniques designed for either conventional GNNs or Transformers, making a dedicated solution necessary. This paper introduces MegaGraph, the first automated hybrid parallelism framework designed for efficient GT training. MegaGraph designs three specialized strategies, namely graph-aware context parallelism, heterogeneous pipeline parallelism, and hybrid data parallelism, to support efficient training on large-scale graphs. However, coordinating these three parallelism strategies yields an exponentially large configuration space. To address this complexity, an automatic search engine leverages precise cost models via a Profile - Model - Search workflow to identify the optimal parallelism configuration. Evaluations demonstrate that MegaGraph enables training on large-scale graphs where state-of-the-art baselines fail due to out-of-memory (OOM) errors. The framework reduces per-device peak memory by up to 77.8\% and achieves up to 4.51$\times$ training speedup while maintaining model accuracy.

---


### 629. [On the Relation Between Interval Regret and Dynamic Regret](https://arxiv.org/abs/2609.34423)

**<font color=#1a73e8>作者：</font>** Yi-Han Wang, Peng Zhao, Zhi-Hua Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-stationary online learning has attracted much attention in recent years, as static regret is insufficient to guide algorithm design in changing environments. To address this limitation, interval regret and dynamic regret have been introduced as two representative performance metrics that strengthen static regret in complementary directions. Interval regret requires an online algorithm to achieve competitive static regret over every local time interval, whereas dynamic regret evaluates performance against an arbitrary sequence of time-varying comparators. Despite their importance, the relation between these metrics has long remained unclear. Prior work has often regarded interval regret as the stronger notion, based on the intuition that local guarantees should naturally induce global guarantees. Consequently, it is widely conjectured that an algorithm with optimal interval regret should automatically attain optimal dynamic regret. In this paper, we first establish a negative result that refutes this intuition of a metric-level implication. Specifically, for both convex and curved functions (including exp-concave and strongly convex functions), we show that there exist instances in which an algorithm with optimal interval regret nevertheless fails to achieve optimal dynamic regret. We then show how to leverage local adaptivity to obtain optimal dynamic regret. In particular, optimal dynamic regret can be attained by invoking an interval regret minimization process over an enlarged Euclidean ball containing the original convex feasible domain and using a suitable domain-converted surrogate loss. This reduction applies to both convex and curved functions. As a byproduct, we obtain the first proper and efficient algorithm with optimal dynamic regret for exp-concave functions, improving prior results while significantly simplifying the analysis.

---


### 630. [Q-learning Penalized Transformer for Safe Offline Reinforcement Learning](https://arxiv.org/abs/2609.34426)

**<font color=#1a73e8>作者：</font>** Shengchao Hu, Peng Wang, Jifeng Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of safe offline reinforcement learning, which involves training a policy to satisfy safety constraints using an offline dataset. This problem is inherently challenging as it requires balancing three highly interconnected and competing objectives: satisfying safety constraints, maximizing rewards, and adhering to the behavior regularization imposed by the offline dataset. To tackle this trilogy challenge, we propose Q-learning Penalized Transformer policy (QPT), a \emph{training--inference consistent} framework that bridges conditional sequence modeling with constraint-aware value estimation. QPT trains a Transformer policy that generates actions conditioned on trajectory context and target return/cost, retaining strong behavior regularization. To inject explicit safety semantics during learning, we augment sequence-model training with a Q-shaped penalty using learned reward and cost Q-functions to favor high return under low constraint violation. At inference, the same Q-functions enforce the cost threshold and choose the highest-reward feasible action, closing the loop between training and deployment. We provide a principled analysis under stylized near-deterministic CMDPs, characterizing how Q-penalized conditional generation improve safety and performance. Empirically, QPT consistently outperforms strong safe offline RL baselines across 38 tasks on the DSRL benchmark, and exhibits robust zero-shot adaptation to different constraint thresholds.

---


### 631. [HUMAN-TCI: Hierarchical Multi-Stream Motion-Aware Network with Torso-Centered Interaction for Text-to-Motion Retrieval](https://arxiv.org/abs/2609.34430)

**<font color=#1a73e8>作者：</font>** Muhammad Islam, Euijoon Ahn, Usman Naseem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate retrieval of human motions is a crucial first step in text-guided human motion modeling and synthesis, as it selects semantically relevant sequences from large datasets and provides grounded references for downstream tasks. Retrieving motions from natural language descriptions remains challenging because sentences can describe multiple actions, overlapping movements, and intricate dependencies between body parts. Existing methods often focus on simple, single-action descriptions and typically process body parts independently or by merely concatenating features, without explicitly modeling how torso movements influence other parts. In addition, their processing pipelines often rely on computationally heavy models, introducing considerable overhead, particularly when modeling longer or more complex motion sequences. This limits learning discriminative motion-pattern representations, reducing retrieval accuracy, interpretability, and efficiency in practical applications. To address these limitations, we propose HUMAN-TCI, a Hierarchical Multi-Stream Motion-Aware Network for text-guided human motion retrieval. HUMAN-TCI employs a three-stream architecture that separately models upper-body, lower-body, and torso motions while explicitly capturing their interactions, allowing torso-related movements to influence the positioning and dynamics of other body parts. By incorporating tailored torso attention, our model effectively recognizes complex human motion patterns, captures fine-grained motion relationships and handles complex multi-action descriptions. Our framework supports retrieval for both simple, single-action sentences and long, compositional descriptions containing sequential or overlapping actions without relying on complex models.

---


### 632. [Harmonizing Spectral Evolution in Conditional Flow Matching for TTS](https://arxiv.org/abs/2609.34431)

**<font color=#1a73e8>作者：</font>** Isha Pandey Varad Deshpande Abhijat Bharadwaj Ganesh Ramakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional Flow Matching (CFM) models for text-to-speech (TTS) suffer from incoherent frequency evolution during inference. While similar spectral imbalances are addressed in diffusion models for other domains, those generic solutions fail to generalize to the inherently uncoordinated acoustic dynamics of CFM. We demonstrate that this issue can be effectively mitigated by introducing a novel training-free frequency-selective boosting strategy. Using the Discrete Wavelet Transform (DWT), our method dynamically modulates mel-spectrogram sub-bands during ODE integration, synchronizing spectral development by penalizing aggressive low-frequency growth and boosting lagging high-frequency details. Validated across diverse architectures (Matcha-TTS, F5-TTS, IndicF5), our approach reduces the required Number of Function Evaluations (NFE) from 32 to 26 and improves Frechet Audio Distance (FAD) by up to 61%, all without compromising mean opinion scores, speaker similarity, and speech intelligibility.

---


### 633. [Admissible Diffusion for Multimodal Interventional Trajectories](https://arxiv.org/abs/2609.34433)

**<font color=#1a73e8>作者：</font>** Xing Han, Shravan Chaudhari, Jiarui Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating a plausible clinical trajectory does not establish what would happen under a different treatment. We present ADMIT, a framework combining irregular multimodal representations, treatment-conditioned latent diffusion and explicit constraints on generated states or actions. We formulate its interventional target through sequential g-computation and distinguish causal assumptions from constraint satisfaction. Its admissibility mechanism translates physiological prior knowledge into explicit constraints on generated states and proposed actions. Treatment-exposure dynamics condition latent transitions, while state projection or action gating applies the constraints during rollout so that they influence subsequent trajectory generation. In our preliminary experiments, multimodal inputs improved supervised hidden-state recovery and reduced treatment-contrast error. In a simulated dosing-schedule experiment with leak-free history encoding, ADMIT predicted most of the tumor-volume change caused by redistributing a fixed total dose. An exposure input improved these predictions around a temporary dose reduction whether or not the assumed clearance rate was correct, but reduced the predicted size of a dose effect, and a deterministic recurrent baseline matched ADMIT's average predictions. Exposure projection reduced constraint violations, although enforcement remained incomplete. Semi-synthetic experiments using eICU context illustrated treatment-response generation under fixed and adaptive policies. Observational examples further characterize model treatment sensitivity. ADMIT provides a framework for testing whether complementary observations and physiological restrictions improve intervention trajectories, with representation recovery, effect accuracy and rule enforcement assessed separately.

---


### 634. [When the Score Becomes the Target: Rethinking Metric Validity in Autonomous Driving](https://arxiv.org/abs/2609.34440)

**<font color=#1a73e8>作者：</font>** Morui Zhu, Deyuan Qu, Qi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving benchmark scores are increasingly used not only for evaluation but also as optimization targets. This raises a fundamental question: do score gains remain reliable evidence of driving improvement once the score itself is optimized? We address this question by examining how the scoring process responds to changes in driving behavior and whether the resulting gains persist under repeated execution and replanning. We decompose the process into execution, measurement, subscore mapping, and aggregation. Controlled interventions reveal substantial behavioral changes that receive little score response because distinctions are omitted, thresholded, or attenuated between requested and executed motion. Closed-loop comparisons further show that optimization gains can reverse when the execution interface changes, demonstrating their dependence on how requests are executed and returned as feedback. Together, these findings connect the behavioral distinctions preserved by a metric to the conditions under which its gains transfer. Metric validity under optimization therefore requires examining both what the scoring process measures and how the optimized behavior is executed.

---


### 635. [Livin' on a Prior: Likelihood Score Approximation for Inverse Problems](https://arxiv.org/abs/2609.34446)

**<font color=#1a73e8>作者：</font>** Rostislav Makarov, Tal Peer, Danilo de Oliveira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models have found great success as data-driven methods of solving inverse problems. Two popular approaches work either by combining a pretrained generative prior with a known degradation model, or by training a conditional generative model directly from paired data. We target a setting that spans both regimes: unknown degradations can be learned from few paired examples, while known degradations can be learned from self-generated samples. We introduce Likelihood Score Approximation (LSA), a generative framework that keeps a pretrained unconditional model fixed and learns an observation-conditioned model that approximates the likelihood score from paired samples. Within a conditional stochastic-interpolant framework, LSA can be trained in either score or velocity coordinates, independently of the unconditional model's native parameterization, and supports both deterministic and stochastic sampling. We further show empirically that the prior model can be swapped post-training while keeping the same LSA model. Across speech and image inverse problems, LSA operates effectively even at roughly 0.01% of the full training dataset. On the ImageNet-256 benchmark it achieves competitive or better restoration quality than strong posterior-sampling baselines while requiring up to several orders of magnitude fewer network evaluations.

---


### 636. [Modeling Whole-Slide Images as Dynamic Tumor Microenvironment Fields](https://arxiv.org/abs/2609.34451)

**<font color=#1a73e8>作者：</font>** Lei Wu, Jiashuai Liu, Di Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the gigapixel-scale nature of whole-slide images (WSIs), weakly supervised WSI analysis is commonly formulated as a multiple instance learning (MIL) problem, where patch-level features are aggregated into slide-level representations. However, diagnostic and prognostic evidence often arises from spatially coherent tumor microenvironment regions and their interactions, rather than isolated patches alone. Existing patch-level or static region-based methods usually overlook how tissue regions should be adaptively formed and subsequently evolved through microenvironment interactions across heterogeneous boundaries. In this paper, we propose Concept-Guided Tumor Microenvironment Evolution (TMEvolve), a reaction-diffusion-inspired framework that models WSIs as latent tumor microenvironment fields over discrete patch graphs. TMEvolve instantiates this view as a learnable graph-discretized evolution process over patch neighborhoods. It first forms adaptive soft tissue regions as coherent microenvironment units, then performs pseudo-time evolution through two complementary local dynamics: intra-region diffusion, which stabilizes latent states within coherent tissue compartments, and concept-guided boundary flux, which propagates visual feature signals and language-derived concept signals across heterogeneous region interfaces. The evolved microenvironment regions are finally aggregated for slide-level prediction. We evaluate TMEvolve on six datasets across three weakly supervised WSI tasks: survival prediction, gene expression prediction, and histological subtype classification. TMEvolve consistently improves over representative MIL methods, pathology foundation models, and concept-guided baselines. Ablation studies and visualizations further support the effectiveness and interpretability of TMEvolve, highlighting the value of dynamic region modeling and boundary interaction.

---


### 637. [SPACE-LoRA: Allocating Activation-Subspace Protection for Continual Learning](https://arxiv.org/abs/2609.34453)

**<font color=#1a73e8>作者：</font>** Seunghyun Yoo, Kiseok Kim, Hyeontae Joo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study addresses the catastrophic forgetting problem that occurs when sequentially learning successive tasks using Low-Rank Adaptation (LoRA) from a lifelong learning perspective. While existing approaches have primarily constrained parameter updates or learning subspaces to reduce interference with past knowledge, they have not fully considered additive interference. This occurs when a newly added residual adapter on top of a fixed past model generates non-zero responses along input directions important for old tasks, thereby altering previous predictions. To this end, we propose Subspace Protection with Allocated Capacity for Efficient Continual Adaptation (SPACE-LoRA). SPACE-LoRA directly suppresses the responses of the new residual branch along input activation directions that are important for old tasks and adaptively determines the protection coverage for each module based on past-task sensitivity estimated via a common Fisher sensitivity-based coverage target. Under a fixed LoRA rank, this approach adaptively adjusts module-specific protection coverage while suppressing interference along input directions sensitive to old tasks. We assess the effectiveness of activation-subspace protection in mitigating catastrophic forgetting and examine the role of sensitivity-guided protection in continual learning across diverse tasks. Code is available at this https URL.

---


### 638. [Breaking Windows Malware Detection: A Comprehensive Evaluation of Problem-Space Adversarial Robustness](https://arxiv.org/abs/2609.34456)

**<font color=#1a73e8>作者：</font>** Mashal Zainab, Salijona Dyrmishi, Hamid Bostani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Problem-space evasion attacks have exposed critical weaknesses in machine learning-based malware detectors; yet, their evaluation remains fragmented across models, datasets, and attack methodologies, often neglecting domain-specific requirements such as executability and functionality preservation. We address this gap with a unified, large-scale evaluation of nine state-of-the-art evasion attacks against eight Windows malware detectors, including seven open-source models and one commercial detector, under executability-preserving conditions. Our study analyzes attack effectiveness, complementarity, transferability, and adversarial hardening to evaluate robustness along complementary dimensions. We show that detector vulnerability depends strongly on both model representation and attack type: raw-byte detectors are particularly susceptible to several classes of problem-space manipulation, but no detector family is uniformly robust across all attacks. Importantly, effectiveness is not explained by transformation-space size alone: the strongest attacks can achieve substantially higher success while using fewer distinct transformations and concentrating on a small set of high-impact manipulations. We further show that two complementary attacks are sufficient to cover approximately 99% of the adversarial examples produced by the remaining evaluated attacks. Transferability exhibits a different pattern from direct attack success: attacks with low direct success can produce highly transferable evasions. Finally, adversarial hardening is highly attack- and model-dependent: robustness gains often fail to transfer across attacks and can even increase susceptibility to unseen attacks. These findings highlight limitations in current malware robustness evaluations, establish a comprehensive empirical baseline, and clarify relationships between effectiveness, transferability, and defense robustness.

---


### 639. [Escaping Local Views: Discovering Latent Concepts for Interpretable Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.34459)

**<font color=#1a73e8>作者：</font>** Yijie Sun, Sanquan Sun, Yanda Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient cooperation is challenging due to the usual partial observability of each agent in multi-agent reinforcement learning. Recurrent networks encode local interaction histories, but their hidden representations provide limited insight into the information underlying individual decisions. To address these challenges, we propose a novel interpretable framework, called escaping local views (ELV), which introduces semantically structured latent concepts to render policy decisions transparent. Specifically, each agent extracts low-dimensional semantic concepts from its local observation and action-observation trajectory. These concepts are jointly encoded into a contextual latent variable via a variational autoencoder (VAE), which builds a bridge between local views and global semantics. To explicitly model the decision of each agent, we employ a dual-path attention mechanism in which one module estimates the salience of individual concepts relative to the global context, while the other captures higher-order cooperative patterns with pairwise concept interactions. Furthermore, we incorporate a concept prediction module that derives an intrinsic reward from next-concept prediction errors, which incentivizes agents to explore regions of semantic novelty. Experiments in multiple environments verify that ELV not only achieves competitive performance but also explicitly provides how agents reason about their decisions.

---


### 640. [Precise Editing and Flexible Referencing for Interactable Worlds](https://arxiv.org/abs/2609.34470)

**<font color=#1a73e8>作者：</font>** Xinyao Liao, Xianfang Zeng, Zhu Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present EditWorld, a video world model for precise editing and flexible referencing in interactable worlds. Existing video world models primarily focus on navigation, letting users explore generated worlds but offering limited control over how existing world content is modified. EditWorld extends world modeling from exploration to precise modification by streaming editing instructions and reference images during autoregressive generation. To support these capabilities, EditWorld introduces Gated Causal Attention for temporally varying editing conditions and reference images, together with a Sparse Context mechanism that maintains a bounded historical context for long-horizon inference. We further adopt joint autoregressive and bidirectional training with annealed self-resampling, and construct a dedicated data synthesis and annotation pipeline that provides supervision for world editing. We also present WBench-Editing to systematically evaluate streaming world editing capabilities. EditWorld achieves the best overall performance on WBench-Editing with an overall score of 73.8 and an editing score of 80.0, substantially outperforming existing methods on editing-related metrics. this https URL

---


### 641. [VL-AcneSeg: A Vision-Language Framework for Region-Aware Acne Lesion Segmentation](https://arxiv.org/abs/2609.34472)

**<font color=#1a73e8>作者：</font>** Sukju Oh, Soo Ick Cho, Dae Hun Suh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acne assessment is crucial for clinical decision-making, yet traditional grading and counting are subjective and fail to account for lesion size. While area-based assessment has emerged as a promising alternative, acne segmentation has continued to rely on general-purpose architectures. To address this gap, we propose VL-AcneSeg, a multimodal framework for acne lesion segmentation that leverages CLIP and region-level text prompts to incorporate spatial priors, enabling lesions to be localized across the whole face. Because region-level prompts indicate which facial areas contain lesions, we report a single global prompt, which requires no such information, as our primary setting. On our internal clinical dataset, VL-AcneSeg achieves a Dice score of 0.5082 and an IoU of 0.3407 under this protocol, the highest among all compared methods, including recent vision-language segmentation methods that are themselves given region-level prompts; region-level prompting raises these to 0.5296 and 0.3602. Moreover, lesion area measurements derived from our segmentation correlate with IGA scores at a level comparable to expert annotations (Pearson r = 0.719 versus 0.658). Notably, our framework maintains consistent performance across external validation datasets, performing reliably even on uncontrolled smartphone images without requiring additional training or fine-tuning. By pairing a protocol that requires no lesion-location information with area-based severity estimation, this work provides a foundation for objective acne assessment outside the clinic. Our implementation is publicly available at: this https URL

---


### 642. [Deep kernel hedging](https://arxiv.org/abs/2609.34474)

**<font color=#1a73e8>作者：</font>** Jean-Loup Dupret, Donatien Hainaut, Edouard Motte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a deep kernel hedging framework that combines the flexibility of deep learning with the structural inductive bias of kernel methods. The hedging functional is restricted to a reproducing kernel Hilbert space whose kernel is parameterized through a neural network embedding of the input features. The framework minimizes a regularized empirical risk under convex loss functions and can accommodate path-dependent information through truncated time-augmented signature features. We derive a generalized representer theorem for the joint hedging problem, reducing the empirical optimization to a finite-dimensional problem. To further reduce the computational cost associated with large kernel matrices, we develop a scalable random Fourier feature approximation and establish convergence guarantees. The random Fourier parameters are sampled once and remain fixed throughout training, while the deep kernel adapts to market data through the learned neural representation. We evaluate the performance of the proposed deep kernel approach on both synthetic and real data and compare it with standard kernel methods and classical deep hedging architectures. Numerical results indicate competitive and robust hedging performance, particularly in low-data regimes, which highlights the benefits of combining expressive neural representations with the inductive bias of kernel methods.

---


### 643. [When Does an Image Determine the Answer? Benchmarking Visual Answerability across Charts and Scenes](https://arxiv.org/abs/2609.34480)

**<font color=#1a73e8>作者：</font>** Sungguk Cha, Mintae Kim, Youngsub Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable visual question answering requires correct answers when evidence is sufficient and abstention when it is not. We introduce a benchmark that connects complete-question evaluation with explicit evidence for its labels across PlotQA charts, CLEVR rendered scenes, and GQA photographs. Each question groups original and edited images, presented independently; success requires every supported answer and every required abstention to be correct. For chart missing-information labels, executable witnesses establish that admissible complete charts give different answers but identical pixels after masking. Scene labels follow source programs and edits, with a residual-cue analysis for photographs. Across 72,000 responses from six model configurations, the highest observed complete task success rates are 57.0%, 43.5%, and 33.7%, respectively. On charts, the strongest configuration achieves 96.2% per-view decision accuracy, yet 265 of its 835 groups with every decision correct still contain incorrect answers. Evaluating supported answers and necessary abstentions together exposes failures that answerability decisions alone conceal.

---


### 644. [CARDAMOM: A Micro-Dialectal Arabic Speech Dataset for ASR](https://arxiv.org/abs/2609.34481)

**<font color=#1a73e8>作者：</font>** Bashar Talafha, Samar M. Magdy, Aisha Alansari 等 39 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Cardamom, a micro-dialectal Arabic speech dataset designed to support fine-grained evaluation and adaptation of automatic speech recognition (ASR) systems. Community-curated by native speakers familiar with the represented varieties, Cardamom contains approximately 40 hours of transcribed YouTube speech spanning 21 micro-dialects across Egypt, Jordan, Lebanon, Mauritania, Palestine, and Saudi Arabia. Each segment is annotated with one or more operational micro-dialect labels, code-switching information, and utterance-level perceived gender, enabling analysis of sub-country variation that is obscured by conventional country-level labels. We describe the collection and annotation process, motivate the micro-dialect inventory linguistically, and benchmark four multilingual ASR systems in zero-shot and adapted settings. The strongest zero-shot system obtains 43.47% aggregate WER, with particularly high error rates on Mauritanian and Lebanese varieties; adaptation on Cardamom reduces its WER to 35.21%. Audio-based identification experiments further show that the annotations provide a learnable prediction target, with a dedicated classifier reaching 85.57% accuracy on 21-way micro-dialect identification. Cardamom provides a resource for studying localized dialectal variation and developing Arabic speech systems with broader regional coverage.

---


### 645. [FlexLoop: Depth-Elastic Looped Policies for Adaptive Test-Time Computation in Deep RL](https://arxiv.org/abs/2609.34488)

**<font color=#1a73e8>作者：</font>** Xun Wang, Ruishuo Chen, Yu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped architectures scale computation by reusing the same parameters across recurrent steps, and recent work shows that they substantially improve deep reinforcement learning policies on long-horizon tasks. Since recurrent depth directly controls computation, one may expect looped policies to naturally support elastic inference across recurrent depths. Surprisingly, we find that pretrained looped policies exhibit severe recurrent-depth specialization: reliable decisions are concentrated near the full trained depth, tying deployment computation to this depth even when less computation may suffice. Achieving depth elasticity, i.e., reliable decisions across recurrent depths with adaptive computation at deployment, therefore remains a key challenge. To address this, we propose FlexLoop, a novel post-training framework that converts pretrained fixed-depth looped policies into depth-elastic policies. FlexLoop keeps training on the original RL objective to preserve full-depth capability while performing adjacent-depth policy distillation to progressively transfer decision quality from deeper to shallower recurrent steps. The resulting policy supports reliable inference across recurrent depths and enables state-wise adaptive inference through recurrent-depth consistency. Experiments on $30$ online and offline long-horizon goal-conditioned environments show that FlexLoop preserves full-depth performance while making shallower depths effective. Keeping competitive performance, FlexLoop reduces average recurrent depth by up to $\bf{43\%}$ and achieves up to $\bf{1.34\times}$ wall-clock speedup in a stress test.

---


### 646. [When Less Data Favors Smaller Teachers: Rethinking Teacher Capacity and Data Selection for Knowledge Distillation](https://arxiv.org/abs/2609.34489)

**<font color=#1a73e8>作者：</font>** Minjae Park, Taesun Yeom, Jaeho Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data pruning reduces the training cost of knowledge distillation (KD). However, the preferred teacher capacity changes with the data budget: smaller teachers can outperform larger ones when limited training data are available. Understanding what drives this shift is important not only for teacher choice but also for identifying which samples are useful for distillation. We analyze teacher supervision by decomposing it into relational ordering---the ranking of classes---and score geometry---the magnitudes and margins of class probabilities---and show that the small-teacher advantage in the low-data regime arises not only from score geometry but also from relational ordering. Beyond understanding teacher capacity, our analysis reveals two properties of effective subsets: samples should match the difficulty appropriate for the available budget, and their relational signals should be diverse rather than redundant. Based on these findings, we propose DVA (Difficulty- and Volume-Aware data selection for KD), a training-dynamics-free method, which uses a small teacher as a proxy for budget-aware difficulty filtering and class-conditional relational volume maximization. Despite requiring no training dynamics statistics, our method remains competitive with training-dynamics-based methods while consistently outperforming training-dynamics-free baselines.

---


### 647. [HPMD: A Historical Persian Manuscript Dataset for Word Spotting with Line-Level Annotation](https://arxiv.org/abs/2609.34490)

**<font color=#1a73e8>作者：</font>** Saeid Firouzi Daghigh, Majid Iranpour Mobarakeh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large collections of historical Persian manuscripts have been digitized, but searching them is still slow and mostly manual. Historians usually want to find where a specific name, date, event, or topic appears, which is a word spotting problem. Progress on this task is limited by two things. First, there is almost no public dataset of historical Persian handwriting; the only notable resource, OpenITI MAKHZAN, contains a relatively small Persian portion. Second, word spotting models usually need word-level bounding boxes, which are very expensive to annotate. In this paper we introduce a new dataset of 223 pages, 3,678 lines, 37,631 words, and 130,630 characters, collected from diverse historical Persian books of poetry and prose and annotated at the region, line, and text level. We also propose a baseline that is trained only with line-level annotations but returns word-level locations. A fine-tuned line detector finds text lines, and a fine-tuned CRNN recognizer trained with CTC produces a frame-by-character posterior matrix for each line. Instead of decoding the most probable character at each frame, the query is scored directly against this matrix, so visually similar characters in Persian such as be and pe no longer cause hard failures. The frame alignment also gives the horizontal position of the word inside the line. On the test set, the fine-tuned line detector reaches an F1 of 0.892, and posterior-based search raises the word spotting F1 from 0.487 to 0.558 compared with exact matching on the decoded text, with the decision threshold selected on a held-out validation set. A PHOC attribute-embedding baseline that additionally receives oracle word boundaries at test time reaches an F1 of 0.449, below the proposed method. We also report a distributional analysis of the dataset, a taxonomy of retrieval errors, and a per-conditionbreakdown of performance.

---


### 648. [LLN: Learnable Lens Networks for Parameter-Efficient Long-Horizon Dynamical Prediction](https://arxiv.org/abs/2609.34493)

**<font color=#1a73e8>作者：</font>** Binbin Yong, Zhao Su, Lan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explicit residual connections of the form (x+f(x)), often combined with normalization layers, have become a standard strategy for training very deep neural networks. However, residual addition primarily provides an algebraic shortcut for gradient propagation, while leaving the evolution of feature geometry across layers largely unconstrained. We introduce Learnable Lens Networks (LLN), a physics-inspired architecture that replaces direct feature-space residual accumulation with learnable optical transport in an augmented position-angle phase space. Each layer alternates between free propagation, which provides an implicit transport path, and a learnable lens field that performs nonlinear trajectory transformation and focusing. Theoretically, we establish that LLN transport is globally invertible and volume-preserving for any differentiable lens field, with the implemented coordinate-wise Gaussian transport further satisfying symplecticity. Importantly, these structural constraints do not limit expressivity: with unrestricted embeddings and readouts, LLN retain universal approximation of continuous end-to-end maps. Experiments across diverse dynamical systems demonstrate that LLN improves long-horizon prediction while using substantially fewer parameters than same-depth comparators. Further analysis reveals stable depth-wise gradient transport and interpretable learned dynamics under the coupled propagation and refraction design.

---


### 649. [QAMM: Adjoint MeanFlow Matching for Few-Step Offline Reinforcement Learning](https://arxiv.org/abs/2609.34497)

**<font color=#1a73e8>作者：</font>** Yuehu Gong, Shutong Ding, Mokai Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow policies can model rich action distributions, but their iterative sampling limits decision speed. Adjoint matching uses the critic's action gradient to improve a flow policy without backpropagating through its sampling trajectory, yet its supervision is defined for instantaneous velocities. We propose QAMM, a method that turns the critic-derived adjoint signal into supervision for MeanFlow's average velocity. The resulting policy learns finite-interval transport directly and generates actions with few network evaluations. We derive the adjoint MeanFlow target, specify its gradient boundaries, and train it with an offline actor-critic. On ten HumanoidMaze tasks, QAMM produces effective two-call policies and achieves competitive performance against strong flow-policy baselines. These results show that adjoint-based Q optimization can be combined with average-velocity learning to obtain expressive offline policies with few-step action generation.

---


### 650. [Scalable GNN-based Knowledge Graph Representation Learning with Efficient Message Passing](https://arxiv.org/abs/2609.34499)

**<font color=#1a73e8>作者：</font>** Huu Tan Mai, Cuong Xuan Chu, Heiko Paulheim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) excel at representation learning on Knowledge Graphs (KGs), achieving stateof-the-art performance on tasks like link prediction or entity classification. However, their high computational complexity, inherent to their user-defined message passing (MP) algorithm, still prohibits their widespread adoption, especially for large KGs. Current efforts to mitigate the scalability bottlenecks of GNNs on KGs, such as subgraph sampling, are often task- and model-specific, and do not reliably guarantee lossless (if applicable) runtime/space reductions. To address this, we extend Relational Sparse Matrix Multiplication (RSPMM), originally designed to losslessly lower the space complexity of composition-based MP with pointwise composition functions, to support more expressive functions (e.g., 2x2 block-diagonal matrix multiplication, Givens rotation, circular correlation). Our method delivers significant task-independent reductions in runtime and space for current GNNs on KGs and facilitates efficient re-implementations of GNNs that maintain near state-of-the-art performance on challenging KG tasks, for a fraction of computational costs.

---


> [!TIP]
> 当前位于：**601-650**（第 13/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
