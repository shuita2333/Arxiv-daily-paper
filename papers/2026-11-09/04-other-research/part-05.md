# 📦 其他研究 | 2026年11月09日

> 本类共 **237** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-237**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-237**

---

### 201. [Scaling Neural Motor Decoding via Decoupled Behavioral Pretraining](https://arxiv.org/abs/2611.08263)

**<font color=#1a73e8>作者：</font>** Divyansha Lachi, Vinam Arora, Shivashriganesh P. Mahato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent neural decoding approaches achieve strong performance by training on large collections of paired neural-behavioral recordings, but such datasets are expensive, invasive, and difficult to scale. In contrast, behavioral data is abundant and easy to collect, raising the question of whether neural decoding can benefit from decoupling behavioral and neural representation learning. We introduce BEEMO, a flexible multi-session framework that enables training with arbitrary mixtures of paired neural-behavioral recordings and unpaired behavioral data. A behavior decoder learns movement dynamics directly from behavioral trajectories, while neural activity is incorporated through cross-attention layers when available, allowing behavioral and neural supervision to scale independently. Across multiple intracortical motor datasets and tasks in nonhuman primates, we show that incorporating unpaired behavioral data improves decoding performance, particularly when transferring to new tasks, and that adding even a small amount of behavioral data from the target task further improves transfer. By decoupling neural and behavioral data, we unlock a new dimension for scaling: unpaired behavioral data, which is substantially cheaper and easier to collect than paired neural recordings, can be used directly to improve decoding performance. We further show that behavior-only pretraining, without any neural pretraining, achieves performance comparable to models pretrained on substantially larger neural datasets. Together, our results suggest that scaling behavioral data offers a practical and cost-effective path toward neural decoding models that generalize across subjects and tasks. Code is available at this https URL.

---


### 202. [SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes](https://arxiv.org/abs/2611.08264)

**<font color=#1a73e8>作者：</font>** Hao Yu, Zhenwei Wang, Yongzhen Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We identify a key limitation of existing feed-forward 3DGS methods: Gaussian attributes are typically predicted in a radial-distance-normalized space that canonicalizes a global radial statistic of the reconstructed geometry, while the spacing between neighboring Gaussian centers can still vary substantially across scene scales and camera configurations. This mismatch induces systematic shifts in Gaussian-scale targets, leading to ambiguous supervision. To address this, we propose SplatAnything with Gaussian Spacing Normalization (GSNorm), which canonicalizes a robust scene-level statistic of Gaussian spacing to provide a more consistent spatial reference for Gaussian prediction. To rigorously assess our method, we further establish a systematic benchmark spanning diverse datasets, input sparsity levels, and challenging extrapolated viewpoints. Extensive experiments demonstrate that SplatAnything achieves state-of-the-art performance, with particularly strong gains under substantial variations in scene scale and viewpoint.

---


### 203. [DART: Domain-Agnostic Residual Transfer for Generalist Anomaly Detection](https://arxiv.org/abs/2611.08271)

**<font color=#1a73e8>作者：</font>** Muhammad Aqeel, Maham Nazir, Marco Cristani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalist Anomaly Detection (GAD) aims to detect anomalies in unseen domains using only a few reference samples. Recent normal-abnormal guided methods improve this setting by exploiting abnormal references, but their residuals often mix transferable anomaly cues with domain-specific appearance factors such as texture, geometry, and acquisition conditions. This residual domain entanglement limits cross-domain transfer and may produce spurious activations on novel domains. We propose DART, a plug-in framework for normal-abnormal guided GAD that learns to separate residuals into anomaly-relevant and domain-specific components. DART combines a Residual Disentanglement Module, which preserves anomaly-discriminative information while suppressing domain information, with Cross-Domain Meta-Training, which forms episodes across source domains to make the separation effective. The method is architecture-agnostic and can be inserted between residual computation and the detection head of existing GAD pipelines. Experiments on MVTec AD, VisA, and BraTS show consistent improvements over multiple base methods, with the largest gains under stronger domain shifts. this https URL

---


### 204. [Accelerating Safe Reinforcement Learning with Massive Parallelism](https://arxiv.org/abs/2611.08273)

**<font color=#1a73e8>作者：</font>** Joonyoung Lim, Younghwan Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the problem of scaling safe reinforcement learning (safe RL) to massively parallel training regimes, where a large number of environments are exe- cuted with short rollout horizons. Although this setting improves data throughput and wall-clock efficiency, it creates a mismatch with constrained Markov decision processes (CMDPs), whose safety constraints are defined over full-episode cost returns. We address this mismatch by analyzing staggered environment resets as a phase-mixture distribution over short trajectory segments. This analysis charac- terizes the bias induced by phase coverage and motivates a phase-aggregated cost estimator that reconstructs episode-level cost estimates from short rollout batches. We further incorporate finite-sample uncertainty and distribution mismatch into a constraint-tightening framework, yielding a scalable Safe RL method compatible with on-policy optimization. Using an MJX-based implementation of Safety Gym, our experiments show that the proposed method achieves performance comparable to non-massively parallel implementations while substantially reducing wall-clock training time.

---


### 205. [Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks](https://arxiv.org/abs/2611.08281)

**<font color=#1a73e8>作者：</font>** Zhitao He, Chi Him Zhang, Chengru Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchmark comprising 608 expert-designed tasks grounded in real-world fraud cases, covering 14 domains and 152 attack scenarios with prepared multimodal content. The tasks span four difficulty levels and reflect the distinct social and cultural contexts of Chinese and English environments. Agents inspect content, verify requests, and execute actions in simulated applications, with attack outcomes grounded in verifiable tool execution logs. To enable controlled red teaming of personal agents, we design a multimodal attack harness that integrates task information, attack progression control, and multimodal content construction to evaluate their intrinsic security against adaptive social engineering attacks in simulated environments. Evaluating seven widely used multimodal models across six dimensions reveals that all are vulnerable, with attack success rates of 7.1% to 34.5%. Adding multimodal content increases attack success from 19.9% to 29.2%, despite increased proactive verification coverage. Stronger safety instructions reduce attack success without improving recognition of deceptive multimodal content, while lower attack success rates for some models accompany excessive refusal of legitimate requests.

---


### 206. [Hierarchical Incremental Beta Splatting for Online Reconstruction](https://arxiv.org/abs/2611.08288)

**<font color=#1a73e8>作者：</font>** Linus Franke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online 3D Gaussian Splatting reconstructs a scene during capture: each keyframe spawns primitives once and refines them for only a few dozen iterations, leaving little chance to fix poor initialization or missing detail. Gaussians are also inherently soft, needing many overlaps for solid surfaces. We present Hierarchical Incremental Beta Splatting (HIBS), which brings beta kernels to incremental reconstruction. Their shape parameter interpolates between a soft, Gaussian-like profile and a flat-topped, near-opaque surfel, acting as a confidence dial for geometry. Our confidence-aware spawning uses geometric observability and multi-view depth agreement to initialize both opacity and shape, producing solid primitives where geometry is verifiable and soft, correctable primitives where it is not. As online densification, error-driven relocation recycles stale primitives into photometric-error hotspots. Bounded beta kernel support enables exact tile culling and faster rasterization, and a closed-form, shape-preserving merging formulation provides a level-of-detail (LOD) hierarchy for fast optimization and real-time rendering. On Mip-NeRF 360 in the on-the-fly protocol, HIBS improves PSNR by up to 0.8 dB while reducing optimization time by up to 40%. Project page: this https URL

---


### 207. [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294)

**<font color=#1a73e8>作者：</font>** Zhengyang Liang, Lizi Liao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manim supports precise, programmatic video generation, but a successfully rendered educational animation can still have visual defects, missing explanations, or incorrect content. Rendering does not directly identify the code changes needed to correct these visual failures, so feedback-driven revision is needed. Existing agentic frameworks use iterative rendering and revision but typically rely on large models, often proprietary. Existing Manim datasets primarily contain final programs and often lack quality verification and the trajectories of feedback and revisions needed to learn this refinement process. We introduce ManimData and ManimCode, a data and training framework for feedback-driven educational animation generation. We construct ManimData through a render-guided pipeline that iteratively generates, executes, reviews, and revises Manim programs with retrieved API documentation. Its 24,034 render-verified, quality-filtered records preserve intermediate programs, execution errors, visual critiques, and corrective revisions. We use role-conditioned supervised fine-tuning on these trajectories to train ManimCode, a single 4B model, to write, review, and revise animation programs. To improve correction of errors that differ from those in the collected trajectories, we then train the Reviser with reinforcement learning on self-generated states, using rendering outcomes and reference-free quality feedback. ManimCode achieves 96.6% and 97.0% render success on ManimData-test and ManimBench, compared with 52.6% and 82.0% for the untrained 4B model under the same inference setup, while also improving video quality scores from 2.48 to 2.94 and from 3.00 to 3.44. Integrating ManimCode into two long-form educational video generation systems increases completed videos from 19/117 to 107/117 and from 53/239 to 239/239, alongside improvements in educational effectiveness and visual quality.

---


### 208. [Dynamic Optimistic Constrained OCO with Memory via Delay Equivalence](https://arxiv.org/abs/2611.08302)

**<font color=#1a73e8>作者：</font>** Mohammed Abdullah, George Iosifidis, Salah Eddine Elayoubi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online Convex Optimization with memory and time-varying constraints (COCO-M) is a recently-introduced framework that captures the dynamics of stateful online learning and non-stochastic control with budget constraints. Despite its expressive power, COCO-M remains largely understudied. In this work, we tackle this problem in its full scale, providing an optimistic algorithm that incorporates untrusted predictions to tame universal dynamic regret and cumulative constraint violation. Our analysis leverages a potent reduction from memory to delay and treats state-dependent gradients as delayed feedback. We establish the first bounds that adapt to both environment non-stationarity (path length $P_T$) and prediction accuracy, while lifting previous restrictive assumptions such as functional separability. En route to these results, we derive findings of independent interest for the memory-to-delay reduction, and for delayed OCO with time-varying constraints. The proposed framework ensures sublinear worst-case guarantees that improve with prediction accuracy, reaching $\mathcal O(1)$ regret under perfect predictions, with cumulative constraint violation (CCV) $\mathcal O(\sqrt{T})$ for unknown $P_T$ and $\mathcal O(\log T)$ for known or online observable $P_T$ , while recovering the optimal COCO rates when memory disappears.

---


### 209. [First-Token Attraction in Mamba Dynamics](https://arxiv.org/abs/2611.08303)

**<font color=#1a73e8>作者：</font>** Trinh T. Nguyen, Minh-Khoi Nguyen-Nhat, Duy-Tung Pham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study token dynamics in deep Mamba models, with a particular focus on the attracting role of the first token. Unlike attention mechanisms, where token interactions are governed by positive scalar coefficients, Mamba dynamics involve full matrix-valued interaction coefficients with no positivity or definiteness guarantees. This structural difference makes Mamba dynamics substantially harder to analyze and prevents the direct application of existing techniques for attention-based models. To overcome this challenge, we introduce a new analytical framework based on a high-dimensional invariant box and a sharp exit-time argument, which together recover an effective form of sign-definiteness. Using this framework, we characterize the possible limit points of token trajectories and prove explicit exponential convergence rates. Our analysis reveals that the first token has privileged dynamics: its limiting direction attracts subsequent tokens, inducing token clustering and attention-sink phenomena in deep Mamba models. We further show that this attraction mechanism extends to broader sequence dynamics, including state-space models, causal attention, and classical time-series models. Experiments on Falcon-Mamba-7B validate our predictions, showing that concentration on the first token increases with depth and dominates in later layers.

---


### 210. [Interpretable many-body interaction laws for collective motion from few trajectories](https://arxiv.org/abs/2611.08314)

**<font color=#1a73e8>作者：</font>** Timon S. Gutleb  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models of collective motion usually reduce social interactions to pairwise forces, despite empirical evidence for many-body effects. We introduce the directional atomic cluster expansion (dACE), which adapts the atomic cluster expansion (ACE) of interatomic potentials to self-propelled agents. dACE provides a systematically improvable, exactly equivariant expansion of an agent's acceleration that splits uniquely into 1-, 2-, 3-body and higher contributions, along with a self term for the agent's own past motion that is fitted so that it does not absorb the interactions. On simulated collectives in two and three dimensions with known rules, dACE recovers the interaction law body order by body order from little data, while the neural model SocialNet, the current closest competitor, needs more data, has much larger errors on many-body or chiral rules and is restricted to 2D. On real data sets of tracked zebrafish and golden shiners, the laws learned by dACE agree better between disjoint halves of the data than SocialNet's. The learned laws are interpretable, and in the shiners the 3-body term opposes the pairwise response as neighbourhoods get dense. Finally, we show that next-step prediction accuracy mostly measures self-propulsion and noise rather than the interactions, and suggest more robust combinations of error measures for interaction learning.

---


### 211. [Polarity Classification with Multitask Learning Syntax Augmentation](https://arxiv.org/abs/2611.08323)

**<font color=#1a73e8>作者：</font>** Muhammad Imran, Carlos Gómez-Rodríguez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment Analysis (SA) is a fundamental NLP task concerned with the identification and categorization of subjective information in text. While lexicon-based methods offer transparency, they often struggle with linguistic phenomena such as negation and intensification. Syntactic parsing has been integrated into SA pipelines to address this, but conventional parsers introduce significant computational overhead. Recent work shows that reformulating dependency parsing as a Sequence Labeling (SEL) task can improve efficiency. We propose and compare two strategies for integrating syntactic knowledge into a neural sentiment analysis model under unified Multi-Task Learning (MTL). The first, Standard-MTL, jointly learns dependency parsing (via sequence labeling) and sentiment polarity classification using a shared encoder with two task-specific heads. The second, Contrastive-MTL, provides implicit syntactic guidance through a contrastive auxiliary objective and a syntax-biased attention pooling mechanism, without requiring explicit label prediction. Both rely on syntactic annotations during training and eliminate need for hand-crafted compositional rules or external parsing at inference. We evaluate eleven datasets spanning seven languages---the MARC corpus (English, Spanish, French, German) and seven datasets from SemEval-2022 Task 10 (English, Spanish, Norwegian, Basque, Catalan)---using four established SEL encodings. With the relative encoding, Contrastive-MTL outperforms a syntax-naive baseline on 10 of 11 datasets and surpasses the external rule-based pipeline (SELSP) that parses at inference on all six datasets where the latter applies, while being 1.5--9$\times$ faster at evaluation. Standard-MTL is more dataset- and encoding-dependent. These results show implicit syntactic supervision during training can match or exceed explicit parsing at inference without computational overhead.

---


### 212. [InstantHand: Feed-Forward 3D Gaussian Splatting for Animatable Hand Avatar Reconstruction from a Single Image](https://arxiv.org/abs/2611.08330)

**<font color=#1a73e8>作者：</font>** Chanho Kim, Muhammad Salman Ali, Kyeonghwan Gwak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand avatar reconstruction typically relies on multi-view capture or per-subject optimization, limiting its scalability. We introduce InstantHand, a feed-forward framework that constructs an animatable 3D Gaussian hand avatar from a single image using off-the-shelf MANO, camera, and mask estimates, without test-time optimization. Image-averaged losses provide insufficient supervision for alpha leakage, which thickens thin finger contours. To address this issue, we propose a Soft Alpha Band regularizer that concentrates supervision on silhouette boundaries. Furthermore, colors regressed from image features can drift toward a learned prior even in observed regions. Our Reliability-gated Appearance Transfer preserves observed appearance by transferring source colors according to each Gaussian's rendering contribution, while completing unobserved regions using the learned prior conditioned on global source identity. InstantHand constructs an avatar in 2.84 seconds and renders at 161 FPS, matching per-subject-optimized baselines on InterHand2.6M and remaining competitive in zero-shot evaluation on HanCo.

---


### 213. [Discovering Learning Rules that Shape Others](https://arxiv.org/abs/2611.08335)

**<font color=#1a73e8>作者：</font>** Hong Jun Lee, Ziyan Wang, Jun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In general-sum games, self-interested learners can reach outcomes that are poor for everyone, which has motivated methods that shape the opponent's learning. Methods like Learning with Opponent-Learning Awareness (LOLA), which differentiates through the opponent's learning process, and Model-Free Opponent Shaping (M-FOS), which uses model-free optimisation methods for long-horizon opponent shaping, have enabled mutual cooperation and exploitation of learners. However, these methods require access to the opponent's parameters, policy, rewards or learning rule during deployment. In single-agent reinforcement learning, update rules discovered by meta-learning have achieved state-of-the-art results (e.g. DiscoRL). These rules are separate from the policy they train and read only the agent's own experience. We hereby extend this framework to general-sum settings by introducing Discovered Update Rule for Opponent Shaping (DUOS). To the best of our knowledge, this is the first method to discover an update rule for an agent in general-sum games. DUOS meta-trains the rule to maximise the agent's expected return over its lifetime, and updates an inner network using the agent's own experience. We show that our discovered rule exhibits behaviour consistent with opponent shaping without reading opponent policies or parameters, and ranks 1st in normalised mean score and 1st in self-play among tournament entrants.

---


### 214. [4D Point Splatting for mmWave Radar Micro-Doppler Differentiable Rendering](https://arxiv.org/abs/2611.08342)

**<font color=#1a73e8>作者：</font>** Adnan Armouti, Guanyue Qian, Rajalakshmi Nandakumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave radar resolves the micrometer displacements of a moving body as micro-Doppler, enabling gait, gesture, activity, pose and vital-sign sensing. Each task relies on a downstream model trained on real data, yet radar datasets lag orders of magnitude behind vision and language. Brute-force collection will not close that gap, and existing synthesis methods (forward-only simulators, learned generators and static-scene inverse renderers) cannot fit a real capture of a moving body, leaving a sim2real gap. We present 4D Point Splatting (4DPS), a physics-based differentiable renderer that fits an explicit moving scene to a real capture. Using the synchronized camera to initialize the room and body, we represent the scene as oriented points carrying material, normal and velocity, and splat each point into range and Doppler bins. Our output is the raw complex return a real radar records, so we apply the same signal processing on the rendered data to obtain any representation for training any SOTA downstream model. We fit 235 sequences on HuPR and 100 on RT-Pose, two datasets with different radars. Our reconstructions set the state of the art, with median correlations of 0.940 and 0.830 on range-azimuth, 0.829 and 0.695 on range-Doppler, and 0.988 and 0.966 on micro-Doppler. Our renders also set the state of the art in downstream sim2real gap. On RT-Pose, a pose model trained on them reaches 21.9 cm MPJPE on real data, against 16.7 cm for real training and 127.6 cm for the RF-Genesis baseline, where both the rendered- and real-trained models learn nearly the same features. Our custom CUDA kernels fit a sequence in 5.7 minutes on HuPR and 12.9 on RT-Pose on one H100, making dataset-scale inverse rendering of mmWave radar possible for the first time. This work can enable synthetic data generation for any human-centered downstream task and model, and scene editing for data augmentation.

---


### 215. [USB Gym: A Gymnasium Testbed for Closed-Loop Ultrasound View Matching](https://arxiv.org/abs/2611.08352)

**<font color=#1a73e8>作者：</font>** Thanapong Intharah, Zhichao Gao, Yiliang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Our main goal is ultrasound guidance: moving a probe until its image matches a target view. Published methods for each part of a guide are evaluated in separate simulators. We asked whether these methods, combined into one guide, are good enough.
Methods: We built USB Gym, a testbed whose standard engine simulates ultrasound from public patient CT, with a network drawing organ textures from CT labels. Its guide has three replaceable parts (slots), an organ segmenter, a controller and a reward, which received 20 published methods, each run on the same 60 episodes of six held-out patients. In each slot, a published method replaced ours only if detectably better on these patients. The better of this combination and our original guide on 20 new CTs is the benchmark baseline. A pose oracle, reading the exact probe pose available only in simulation, set the reference. The results below are exploratory.
Results: On these CTs, the probe started on average 16.0 mm from the target view; the pose oracle brought it to 1.5 mm. Of the results known when the combination was fixed, only an image-similarity reward (SSIM) was slightly but detectably better, so the combination was our guide with that reward. This combination was the benchmark baseline, ending at 13.7 mm (16% of the oracle's progress).
Conclusions: Combining untuned published methods with ours did not guide the probe near the target view; the task remains under-explored. The testbed accepts new methods; no guide was tested on hardware.

---


### 216. [OraRefer: Segmentation-Guided Multi-Photograph Fusion for Oral Cancer Screening with Guaranteed Patient-Level Sensitivity](https://arxiv.org/abs/2611.08360)

**<font color=#1a73e8>作者：</font>** Rupam Mukherjee, Mehakdeep Singh, Shirin Dasgupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oral cancer and the oral potentially malignant disorders (OPMD) that can precede it are visible on the oral mucosa, which makes smartphone photographs a promising tool for screening. Deep learning models for this task classify individual photographs. However, screening refers patients, not photographs: a patient is usually photographed several times, and the referral decision must miss no more than a set share of patients with disease. We propose OraRefer, a patient-level screening model that reads each photograph with a segmentation-guided foundation model that conditions its class decision on the predicted lesion, combines all photographs of a patient with risk factors, and refers through a threshold with a finite-sample sensitivity guarantee. The model localizes the mouth itself, so inference needs no annotation. On 3000 photographs of 714 patients, patient-level fusion reaches an AUROC of 0.919 and outperforms attention-based multiple-instance learning. At a 90% sensitivity target, OraRefer detects 95% of patients with OPMD or cancer and misses 3 of 61 patients with cancer, at a specificity of 0.610. Because the threshold is calibrated without retraining, each clinic can set its own guaranteed operating point on a local calibration sample.

---


### 217. [NPCBench: A Clinical Apprenticeship Benchmark for Multimodal Care-Pathway Reasoning in Nasopharyngeal Carcinoma](https://arxiv.org/abs/2611.08369)

**<font color=#1a73e8>作者：</font>** Pengkai Wang, Wei-Wei Zhang, Yan Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current medical benchmarks typically break down clinical competence into isolated factual questions, single-image tasks, or static case vignettes. These tests score individual answers, but reveal less about whether a model can integrate subspecialty knowledge with multimodal evidence and track a patient's condition throughout a course of care. To close this gap, we introduce NPCBench, a clinical apprenticeship benchmark for nasopharyngeal carcinoma (NPC). NPCBench mirrors specialist training, from guideline and foundational knowledge to case planning, longitudinal review, CarePath integration, and open-ended consultation. It contains 4,777 component and consultation items and a 100-patient CarePath cohort with 417 scored diagnostic and care tasks. The episode-level evaluation tests whether diagnostic and care answers are jointly correct within a care pathway. By linking stepwise tasks to patient-level care trajectories, NPCBench evaluates whether models ground decisions in visual evidence, interpret changes in patient state, and meet clinical requirements in consultation. Across 30 evaluated models, we observe a composition gap: strong performance on individual tasks does not ensure jointly correct diagnostic and care answers for the same patient. Among 21 multimodal models, strict CarePath success reaches at most 23%. Paired controls and physician calibration further examine evidence grounding, longitudinal revision, and consultation judging. Overall, NPCBench broadens the evaluation of medical artificial intelligence beyond static question-answering paradigms to an apprenticeship-oriented assessment of clinical workflows, thereby offering a testbed for evidence-based and temporally coherent reasoning in oncology care.

---


### 218. [Module-Aware Optimization for Graph Neural Networks](https://arxiv.org/abs/2611.08379)

**<font color=#1a73e8>作者：</font>** Guy Hadad, Haggai Roitman, Moshe Eliasof 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Different optimizers impose different geometries on parameter updates. Adaptive methods such as Adam and AdamW use coordinate-wise updates, while matrix-aware optimizers such as Muon utilize weight-matrix structure through orthogonalized updates. For Graph Neural Networks (GNNs), however, the effective geometry of its weight matrices is shaped not only by its learned channel-mixing weights, but also by the graph-propagated representations it acts on. Thus, even if an update is well normalized as a matrix, its effect on the layer output can be amplified when applied to graph-propagated features. To address this gap, we introduce GraphMuon, a graph-aware optimizer that adapts Muon's matrix updates to the covariance structure of graph-propagated layer inputs. GraphMuon performs orthogonalization in a metric defined by these propagated representations and normalizes step sizes according to the update's induced effect on the layer representation. We show that theoretically, vanilla Muon can suffer from graph-induced update amplification, while our GraphMuon can mitigate this effect. As such, our GraphMuon yields a graph-metric analogue of Muon's polar update step. Empirically, GraphMuon achieves $1.32\times$-$2.42\times$ validation-loss time-to-target speedups over AdamW on three large-scale OGB benchmarks. Across 15 dataset-architecture configurations spanning node classification, inductive graph classification, and graph regression, it achieves lower time-to-target in 13 cases, while maintaining competitive or superior predictive performance. Code is available at this https URL.

---


### 219. [SensorGuard-RV: Sensor-to-Register Data Protection for Resource-Constrained RISC-V Devices](https://arxiv.org/abs/2611.08380)

**<font color=#1a73e8>作者：</font>** Hamid Noori, Carlton Shepherd  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Embedded systems rely on sensor measurements that traverse a complex hardware-firmware stack (e.g. peripheral interfaces, communication buses, memory, and drivers) before reaching the applications that use them. At worst, an attacker with access to this path may successfully intercept, overwrite, fabricate, or replay readings. This may cause systems that act on such data, such as flight controllers and industrial processes, to behave incorrectly or unsafely. Existing defences, such as trusted execution environments and trusted I/O paths, still depend on trusted driver software and correctly configured access control, which remain fragile in practice. In response, we present SensorGuard-RV, a hardware-first approach that delivers sensor samples into processor registers without trusting intermediate software, buses, or memory. After configuration, a write-once ownership switch hands the sensor to a fixed-function controller that performs hardware-level authenticated encryption on sensor samples under a key inaccessible to software. We develop a new RISC-V instruction then instructs the CPU to decrypt the sample and writes it to a register only after verifying its tag and rejecting replays, including across resets. We implement SensorGuard-RV on the NEORV32 core with an ADXL362 SPI accelerometer on an Artix-7 FPGA. At 100 MHz, a protected sample reaches a register in 5,191 cycles (51.9 $\mu$s), of which the two Ascon authenticated encryption engines account for 30. Because fixed-function acquisition removes per-byte software polling, the protected loop sustains 19,015 transactions/s, 5.3% above a software-driven SPI baseline. The added logic (3,155 LUTs and 2,215 registers; 5.0% and 1.7% of the device) is dominated by the Ascon engine and preserves the 100 MHz clock, while estimated power rises from 118 to 368 mW.

---


### 220. [Hybrid Machine Learning for Imbalanced Landing-Phase Safety Event Prediction from Flight Data](https://arxiv.org/abs/2611.08386)

**<font color=#1a73e8>作者：</font>** Taha Asghar, Bilal Mufti, Syed Qasim Zaheer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Landing-phase safety-event prediction requires the detection of rare abnormal approaches within strongly imbalanced multivariate flight data. Capturing coupled temporal behavior while distinguishing event-specific signatures across airport operating contexts remains a central modeling challenge. This study proposes an interpretable hybrid feature-fusion framework for multiclass landing-phase safety-event prediction. A long short-term memory (LSTM) autoencoder trained on nominal flight windows characterizes deviations from routine approach behavior. Its continuous reconstruction-error descriptor is fused with parameter-specific statistical flight-history features and supplied to a class-weighted XGBoost classifier to distinguish Normal, Speed High, Path High, and Flaps Late windows. The framework is evaluated using 53,750 NASA DASHlink approach windows from three arrival airports. Pooled and airport-specific learning strategies are compared alongside component-level benchmarks, repeated pipeline retraining, and feature-attribution analysis. The results demonstrate strong class-balanced detection, with mean macro recall above 0.90 across all airports under repeated partitioning and retraining. Component comparisons establish the importance of class weighting and show that continuous feature fusion outperforms reconstruction-error-only and hard-gate alternatives. Airport-level comparisons reveal benefits from local specialization at the two airports with larger datasets and from pooled training at the airport with the smallest dataset. Feature attributions associate predictions with operationally relevant vertical-path, configuration, speed, and approach-context variables. The framework provides an interpretable approach to rare-event detection and practical guidance for adapting flight-data monitoring models to airport-level data availability.

---


### 221. [Learning a patient world model for health system simulation in intensive care](https://arxiv.org/abs/2611.08392)

**<font color=#1a73e8>作者：</font>** Yingtai Li, Ruoyan Wang, Yu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing healthcare strategies requires anticipating their clinical and operational consequences before implementation, a task that often relies on health system simulation. Such a simulation necessitates modeling how patient states evolve and generate care demands. However, conventional approaches typically tailor compact state transitions to a single policy question and omit history-dependent dynamics, thus requiring the redefinition of states and transitions when there is a new question that entails different clinical information. We propose to learn a patient world model from longitudinal EHRs using a neural network to provide a shared clinical representation of patient trajectories that can serve simulation questions across scenarios. Taking ICU operations as an example, we train the model on MIMIC-IV, freeze it, and couple its time-queryable predictions to shared ICU calendars, resources, and queues via scenario-specific mappings, so that one model renders admission demand, care tasks, and discharge proposals across simulations evaluating ICU bed capacity, care dispatch, and post-ICU transfer capacity. Experiments show that our model matches Markov and semi-Markov comparators in aggregate occupancy and directional responses to capacity and dispatch policies. It also reproduces policy gains from replayed observed trajectories. For patients entering the same support state from different prior trajectories, the learned representation captures a 24-h recovery difference (-6.4 predicted versus -6.7 observed percentage points), a contrast missed by compact state models, which propagates into distinct simulated care demand, queue burden, and bed use. These results indicate that a learned world model of patient dynamics has the potential to replace question-specific state models, allowing new care policies to be evaluated by reconfiguring the scenario without model rebuilding.

---


### 222. [Adaptive Low-Light Enhancement for Road Anomaly Detection: A Multi-Architecture Benchmark and Edge Deployment Study](https://arxiv.org/abs/2611.08393)

**<font color=#1a73e8>作者：</font>** Obed Honour Eje, Oluwatosin Kolade, Glory Bagai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road anomaly detection systems on autonomous vehicles must function reliably under degraded visual conditions including darkness, rain, and Harmattan dust haze. This paper benchmarks four object detection architectures, YOLOv8n, YOLOv12n, RT-DETR, and Faster R-CNN, under physically grounded lighting and weather degradation, and shows that uniform application of the SCI low-light enhancement network is actively harmful at dusk-level lighting (-16.1% to -30.7% mAP@50). We propose a lightweight, training-free luminance-adaptive router that selects between no enhancement, moderate SCI, and denoising plus strong SCI based on per-frame Rec. 601 luminance, recovering most of the dusk penalty while preserving low-light gains, and we validate the full pipeline on NVIDIA Jetson Nano edge hardware.

---


### 223. [Synthesis of Ovarian Cancer Multi-Omics Datasets: A Biology-Informed Evaluation Framework](https://arxiv.org/abs/2611.08394)

**<font color=#1a73e8>作者：</font>** Déborah Boyenval, Alina Malyutina, Jaana Oikkonen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Paired multi-omic cancer cohorts are costly to assemble and difficult to share, motivating synthetic cohorts as a complementary resource. As generative model development accelerates, we shift the focus from proposing yet another architecture to defining evaluation criteria that determine whether synthetic data preserve biologically relevant structure. We introduce a biology-informed and patient-disjoint framework for evaluating the generation of paired RNA expression and copy-number variation (CNV) profiles, and apply it to the longitudinal DECIDER high-grade serous ovarian cancer cohort. The framework assesses modality-specific fidelity and coherence between RNA and CNV pairs using agreement between real training and held-out data as a reference, alongside complementary training-data proximity diagnostics. We adapt three multi-omic integration architectures based on variational autoencoders to generate paired profiles. The model leading several fidelity and coherence measures also shows the strongest training-data proximity. The protocol and case study offer the community a reference for comparing future multi-omic generators.

---


### 224. [Conformal Prediction for Time-Dependent PDEs](https://arxiv.org/abs/2611.08409)

**<font color=#1a73e8>作者：</font>** Joshua Stiller, Annika Schneider, Eyke Hüllermeier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification is crucial in scientific machine learning, where models inform safety-critical tasks such as flood forecasting, financial risk management, and thermal control in machines. Conformal prediction provides distribution-free coverage guarantees, but in time-dependent settings common to physics and engineering, these guarantees can break down, leading to systematic undercoverage. We study this problem in the context of surrogate models for time-dependent physical systems described by partial differential equations. We prove that in a function space setting, distributions at arbitrarily close times can be mutually singular, making exact coverage guarantees impossible. We further show that in discretized settings, the total variation distance between distributions often saturates exponentially fast with the grid resolution, mandating restrictions on the spatial discretization to ensure coverage. Finally, for certain settings, we show how to use principled weighted conformal prediction to obtain finite-sample coverage guarantees over growing time horizons.

---


### 225. [Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning](https://arxiv.org/abs/2611.08414)

**<font color=#1a73e8>作者：</font>** Chenruo Liu, Zihan Wang, Yijun Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) is commonly used in both supervised fine-tuning (SFT) and reinforcement learning (RL), often under similar optimizer settings. Yet, how the different dynamics of the two stages manifest in the low-rank increment that LoRA optimizes remains unclear. Tracking the singular spectrum and subspaces of LoRA updates on mathematical reasoning tasks, we find that RL concentrates the spectrum at every learning rate, while SFT expands it at moderate learning rates; moreover, RL rotates the singular subspaces much faster than SFT at small learning rates. Interpolating between SFT and RL one ingredient at a time, we pinpoint group-mean baseline subtraction as the source of both contrasts. A quadratic multi-index model updated via LoRA unveils the underlying mechanism: group-mean baseline subtraction tilts the balance between two competing forces, coherent fitting and gradient noise, toward spectral concentration and faster subspace rotation, while forcing the risk-favorable learning rate to be low. Guided by these dynamics, we tailor LoRA updates to each stage: in SFT, we flatten the spectrum of the full update to spread adaptation across singular directions, whereas in RL, we flatten the part of the update outside the current LoRA increment span to promote subspace rotation. Experiments on mathematical reasoning tasks across multiple models show that the respective configurations for SFT and RL yield the best performance among the compared methods in most evaluated settings.

---


### 226. [On the limitations of molecular representations](https://arxiv.org/abs/2611.08420)

**<font color=#1a73e8>作者：</font>** Acer Blake, Fergus Imrie, Charlotte M. Deane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular representations such as fingerprints and learned embeddings play a central role in cheminformatics and small-molecule machine learning. They serve as the primary input for a diverse array of tasks, including clustering, dataset splitting, and virtual screening, yet their evaluation is often limited to downstream model performance on narrow benchmark tasks. We carried out a systematic investigation of the quality of molecular representations, finding that none of the state-of-the-art molecular embedding models capture graph structure, 3D shape, or ADMET endpoint similarity better than fingerprints or physicochemical descriptors. However, classical fingerprints also revealed their own material limitations. For example, we show that depending on the representation, between 225M and $\sim$4B molecules have non-unique representations in the 10.8B Enamine REAL database, with implications for virtual screening. Our findings provide an insight into the current limitations of molecular representations, outlining future research directions for the development of more robust encodings of small molecules.

---


### 227. [Data-driven discovery of intrinsic Lie point symmetries of differential equation systems](https://arxiv.org/abs/2611.08421)

**<font color=#1a73e8>作者：</font>** Ilker Gurcan, Kadir Ustun, Ramazan Gokberk Cinbis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering continuous symmetries directly from differential-equation data can reveal geometric structure for model reduction and scientific machine learning without symbolic determining equations or a closed-form representation of the governing system. We formulate intrinsic Lie point-symmetry discovery as an operator-theoretic problem on sampled jet-space data. Admissible generators are identified from a sampled determining operator and separated from redundant, solution-dependent, and geometrically trivial directions. The framework combines prolongation, sequential subspace restrictions, and a fixed nonlinear dictionary linear in trainable coefficients. A rank-stabilization preflight test diagnoses systems whose represented intrinsic symmetry algebra does not stabilize under dictionary refinement. On a controlled differential-equation benchmark with an analytically known 11-dimensional represented intrinsic symmetry algebra, the method recovers the complete represented generator set, reproduces its Lie-bracket structure to numerical precision, and approximates a known generator beyond the training domain. Here we show that explicit intrinsic continuous-symmetry generators can be recovered from data obtained from exact or approximate differential systems.

---


### 228. [SM4RT: Cascaded Feed-forward Model for 4D Reconstruction](https://arxiv.org/abs/2611.08436)

**<font color=#1a73e8>作者：</font>** Pang-Chi Lo, Jhao-Syun Lai, Tsung-Wei Ke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SM4RT, a multi-task cascade feed-forward model for dynamic scene reconstruction from RGB videos. While existing feed-forward approaches typically address geometry reconstruction and motion estimation separately--and often predict motions in a single coordinate frame that must account for camera movement--SM4RT solves these tasks sequentially by first reconstructing 3D geometry and then bootstrapping motion estimation from the predicted structure. By expressing each pixel's 3D motion in its corresponding camera frame, SM4RT reduces ambiguity arising from camera motion. To address the sparsity of real-world motion labels, SM4RT further incorporates a weakly supervised loss that regularizes unlabeled point motions using labeled point positions at the other time step. We evaluate motion estimation on three dynamic-scene datasets--Kubric, Waymo, and Point Odyssey--and SM4RT achieves the best performance on most metrics compared with prior baselines. We additionally benchmark geometry reconstruction on five dynamic scene datasets and show that SM4RT achieves competitive performance with state-of-the-art methods. Overall, our unified framework demonstrates that combining geometry reconstruction and motion estimation in a cascade not only avoids performance trade-offs but also enhances motion estimation through improved geometric reasoning.

---


### 229. [Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety](https://arxiv.org/abs/2611.08438)

**<font color=#1a73e8>作者：</font>** Fazl Barez, Tung-Yu Wu, Hunar Batra 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural networks are likely to be among the most consequential artefacts in human history. As these systems become more capable and autonomous, their potential to cause societal harm also grows, making AI safety one of the defining challenges of our time. Yet we continue to build increasingly powerful systems without fully understanding how they work, how they will behave in unfamiliar situations, or how to reliably control them. Mechanistic interpretability offers a path towards understanding these systems by studying their internal representations and computations, with the aim of evaluating, predicting, and controlling behaviour. We survey mechanistic interpretability for AI safety in order to answer the question: Does understanding how models work actually make them safer? We place mechanistic interpretability in the broader context of interpretability research and compare its mechanistic evidence with behavioural evaluation. We introduce the foundations of mechanistic interpretability, including features, polysemanticity, transformer computation, and circuits, and survey methods for feature extraction and analysis, circuit discovery and causal verification, explaining intermediate representations in natural language, learning dynamics, and training-data attribution. Beyond surveying existing methods, we propose a unified framework for evaluating mechanistic interpretability claims and characterise six research orientations by their goals, assumptions, and trade-offs. Finally, we examine how mechanistic understanding can support AI safety, including knowledge editing, steering, and monitoring, and assess its limitations, failure modes, open problems, and relationship to behavioural safety measures. We also release a repository of code notebooks with worked examples that reproduce key findings from surveyed methods, allowing readers to build intuition through hands-on experimentation.

---


### 230. [Label-Wording Augmentation in a Typed-Decision Encoder: Gains on Unfamiliar Words, Not on Abbreviations or Codes](https://arxiv.org/abs/2611.08439)

**<font color=#1a73e8>作者：</font>** Vladimir Beskorovainyi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed-decision models score options that the caller supplies at request time, so their accuracy depends on label wording that the model's developer does not control. We compare two releases of a 307M-parameter multilingual cross-encoder, Ru-Jev, trained on thirteen Russian-language tasks; the later release adds an augmentation that presents labels in several surface forms. Holding questions fixed and varying only how eighteen routing labels are worded, we evaluate ten label vocabularies, produced by three separate processes and checked for overlap with the training data, with five candidates per question and, for eight of them, also with eighteen. On held-out vocabularies made of ordinary or borrowed words (English-derived jargon, office slang, department names), the augmented release is more accurate in every setting, by up to 0.24. Eleven of these fourteen gains survive a Holm correction (slang with eighteen candidates and descriptive sentences with five do not), and for jargon on all labels the label-level interval excludes zero in both settings. On abbreviations and opaque codes it gives no usable gain: on abbreviations it is not better, and worse on the clean slice, and on opaque codes both releases stay at or below chance once labels related to training options are removed. In most cells where accuracy rises, the risk-coverage area falls, but with eighteen candidates confident errors rise on jargon and slang. On two datasets neither release saw, accuracy moves by -8.4 and +5.6 points. We also report four evaluation hazards from comparing the two releases.

---


### 231. [Souffleur: A Glanceable Display for Mobile Voice Conversations](https://arxiv.org/abs/2611.08443)

**<font color=#1a73e8>作者：</font>** Anton Wolter, William Benjamin, Niklas Elmqvist  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The speech capabilities of mobile devices have grown, but their displays still rely on a text-based chat. When resuming a voice chat after a context switch, the last messages may not convey the key points of the conversation. Autobiographical use and sessions with external participants led to design goals for a mobile-first, speech-driven, glanceable display that helps users continue their reasoning from where they left off. We implement these goals in Souffleur and evaluate it in a between-subjects study with 48 participants. Compared with a conventional chat transcript, we found no reliable difference in how easily participants followed and resumed short voice conversations, nor in effort, attention or recall, although Souffleur reduces the conversation to a few short phrases.

---


### 232. [A Hidden Markov Preference Model for Online Prediction of Adversary Actions](https://arxiv.org/abs/2611.08445)

**<font color=#1a73e8>作者：</font>** Angel Daruna, Michael Cogswell, Tixiao Shan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A defender anticipating an attacker needs a probability distribution over the attacker's next action from information available before that action occurs. Two structures complicate this: the attacker's behavioral regime persists and can switch within an episode, and each action combines an operation with state-dependent arguments whose feasible values change over time. We capture both with a hidden Markov model whose latent state is the active regime and whose regime-conditioned action law is defined on a feasibility-masked tree of executable actions. The same likelihood forms the next-action distribution and updates the regime belief once the action is seen, and a partially observed prefix contributes its resolved local factors. Estimation separates into convex logistic fits that Baum-Welch reuses when regimes are unlabeled. We derive a reach-weighted nodewise KL expression for regime information, a sequence-wise log-loss bound for switching regime paths, and a uniform fallback guarantee. On the CAGE 2 cyber defense benchmark the filtered latent state is worth 0.8 nats per step, and after a controller switch the loss begins to fall in three steps against ten for a recurrent baseline.

---


### 233. [Adversarial Training with Large Step Sizes: Implicit Bias, Optimization, and Sharpness](https://arxiv.org/abs/2611.08457)

**<font color=#1a73e8>作者：</font>** Yi Feng, Andrea Paudice  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial Training (AT) is an important method for improving model robustness. We study the dynamics of deterministic Gradient Descent (GD) in AT. Most existing works in this direction focus on the small or vanishing step sizes regime, where GD resembles a continuous-time flow. However, such step sizes can make training inefficient and are rarely used in practice. In this paper, we study the AT dynamics of GD with large constant step sizes. We first study GD in adversarial linear logistic regression, focusing on two aspects: where the model parameters converge (implicit bias) and how quickly the losses decrease (optimization). We then turn to neural networks training and study how the sharpness of losses evolve during AT. Our results advance the understanding of the behaviors of GD with large step sizes in AT and highlight three key differences from its behavior in Standard Training (ST): (i) the implicit bias gap between AT and ST, previously established only for small step sizes, persists for arbitrarily large constant step sizes, (ii) different from ST, there is no uniform rate of convergence for the optimization error in AT, and (iii) sharpness can exhibit two-stage dynamics that differ from the Edge-of-Stability behavior observed in ST.

---


### 234. [Same Behavior, Different Mechanism: What Finite Experiments Can Certify About Integrated Information](https://arxiv.org/abs/2611.08469)

**<font color=#1a73e8>作者：</font>** Linqian Wu, Diaoxuan He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability, AI auditing and assessments of machine consciousness increasingly rest on mechanism-level quantities: functionals of a system's causal transition law that describe how it computes, not what it outputs. Experiments see that law only through finite, partial and noisy interventions. We ask when such a quantity is identifiable from an experiment's access, continuous in the mechanism and certifiable from finite data, and answer exactly for a deliberately demanding case - the integrated information $\varphi$ of integrated information theory - in stochastic networks of four and five units with known ground truth. Behavior can be silent: a recurrent and a feed-forward network with identical input-output laws at their response delay carry 0.28 and 0 bits, yet internal recordings separate them within 4-53 trials. Partial access can be just as blind: in our examples, units left out of a one-step recording impose precision floors of 0.30-1.02 bits that no sample size lowers, and in all-but-self parity networks, recordings of any length see several hidden units only through the product of their fidelities - a symmetry that one intervention broke in exact checks. The measure has sharp edges: because $\varphi$ selects a partition, and the cause and effect it specifies, by one criterion and reports another, infinitesimal changes of mechanism that cross an edge change it by 25-100% at 99% of the edges we found in random networks, and about 1% of surrogate models that fit interventional data almost perfectly misreport it by more than 20%. One-sided claims survive: the same data certify a lower bound on both sides of an edge, and we prove $\varphi>1.004$ bits throughout a 64-dimensional region of mechanisms and certify it from about $10^7$ controlled transitions with false-certificate probability at most $\alpha$. Measurability is thus a design question with computable answers.

---


### 235. [EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling](https://arxiv.org/abs/2611.08477)

**<font color=#1a73e8>作者：</font>** Yanlin Jin, Bowen Yang, Cheng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video models possess strong visual priors, yet do not natively represent human action in metric 3D space. We present EgoGeneralist, which adapts pretrained video generators to unify action-conditioned egocentric video generation, pose estimation, and joint action-video generation. Our role-adaptive action renderer provides video-native representations for multidirectional action-video learning, making metric motion usable as both a spatial control signal and a recoverable generation target. Cross-stream action-video coupling establishes close correspondence between metric motion and visual dynamics through lightweight adaptation while preserving the pretrained visual prior. Together, these designs establish a generalist framework spanning five action-video tasks. Despite adaptation only on controlled laboratory recordings, EgoGeneralist generalizes to diverse unseen scenes and interactions with effective action control and visual quality, bridging pretrained visual knowledge and metric 3D human motion.

---


### 236. [Scientist World: Grow a Research World for AI-Scientists](https://arxiv.org/abs/2611.08478)

**<font color=#1a73e8>作者：</font>** Taiming Lu, Sachin Konan, Zhuang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-Scientists arrived, but a world for them to grow in did not. Human scientists take theirs for granted $-$ centuries of open problems and shared ideas, waiting in the scientific literature. To AI-Scientists, that world is readable but not runnable, so we build Scientist World for them: every research paper becomes an executable environment. Our autonomous pipeline extracts each paper's open-ended research question and reproduces its proposed method as the baseline; an AI-Scientist entering the environment is evaluated against what the human authors achieved. We release the first 1,000 verified environments. With the world as an evaluation, we found that frontier AI-Scientists can already surpass the human researchers 74% of the time. As a record of how AI does science, it contains 6,400 hours of research traces, with every idea, experiment, failure, and success. As a training ground, we are able to raise (+158%) a small model to match frontier models in research ideation. At last, AI-Scientists' own world has arrived, grown from and growing with science itself.

---


### 237. [User Embeddings are Superpositions of Interpretable Behavioral Modes](https://arxiv.org/abs/2611.08487)

**<font color=#1a73e8>作者：</font>** Jonathan Kozaczuk, Zheng Dong, Noyan Evirgen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> User embeddings are central components of modern recommendation, personalization, and behavioral modeling systems. Though these embeddings can compactly encode rich behavioral information, they are inherently dense and opaque, limiting interpretability. To address this gap, we argue that user embeddings can be understood as sparse superpositions of interpretable behavioral modes. This structure is directly predicted by generative models of user behavior for linear embeddings and extends approximately to deep-learning representations by the superposition hypothesis. Superimposed modes can naturally be recovered by sparse dictionary learning methods, such as sparse autoencoders (SAEs), and recovered modes can be automatically named and queried in natural language. We validate mode recovery against known ground truth on synthetic data, where SAEs recover modes better than classical sparse baselines, including on transformer-encoded embeddings. We then apply the method to classical and transformer-based user embeddings from two real-world datasets. We also show how the corresponding natural-language labels enable zero-shot audience retrieval and characterization over embeddings never trained on text. The framework is post-hoc and model-agnostic, requiring no modification to the upstream embedding system.

---


> [!TIP]
> 当前位于：**201-237**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-237**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
