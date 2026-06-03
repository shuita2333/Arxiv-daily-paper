# 📦 其他研究 | 2026年06月04日

> 本类共 **312** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-312**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-312**

---

### 301. [A Pocket Offline Model for Simultaneous Speech Translation as CUNI Submission to IWSLT 2026](https://arxiv.org/abs/2606.03948)

**<font color=#1a73e8>作者：</font>** Aziz Sharipov Ortega, Dominik Macháček  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We implement simultaneous translation capability with the offline direct speech-to-text translation model Canary, using the state-of-the-art policy AlignAtt, and submit it to IWSLT 2026 Simultaneous Speech Translation Shared task for Czech to English and English to German and Italian.
The strengths of our system are: (1) high translation quality, outperforming similarly sized baselines both in low- and high-latency regimes in computationally unaware simulations; (2) low computational requirements, as the model has only 1B parameters; (3) multilinguality -- support of 25 source and 25 target languages.

---


### 302. [VLESA: Vision-Language Embodied Safety Agent for Human Activity Monitoring](https://arxiv.org/abs/2606.03954)

**<font color=#1a73e8>作者：</font>** Hanjiang Hu, Yiyuan Pan, Jiaxing Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI systems increasingly assist humans in physical tasks, ensuring safety becomes paramount -- physical actions carry immediate and irreversible consequences that digital errors do not. We introduce the Vision-Language Embodied Safety Agent (VLESA), a framework that monitors human activities from egocentric video and triggers real-time safety interventions when dangerous actions are predicted. VLESA addresses intent-dependent safety where identical actions can be safe or dangerous depending on context. A dataset pairing egocentric frames with goal-conditioned safety annotations is introduced, enabling a goal-conditioned safety Q-filter trained via GRPO that evaluates actions with respect to inferred intent without retraining. On top of that, an intent-action prediction agent is proposed to jointly infer goals and predict future actions from video. On the ASIMOV-2.0 benchmark, VLESA achieves higher intervention accuracy at the exact ground-truth frame compared to baselines, while the GRPO-trained Q-filter improves action safety by over 41 percentage points through goal-conditioned constrained decoding. Code is available at this https URL.

---


### 303. [Efficient ASR Training with Conversations that Never Happened](https://arxiv.org/abs/2606.03957)

**<font color=#1a73e8>作者：</font>** Máté Gedeon, Péter Mihajlik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational ASR for lower-resource languages and niche domains is limited by the scarcity of domain-matched multi-speaker training data. We propose an augmentation pipeline that generates scenario-level dialogues with participant metadata, maps speaker attributes to TTS voice profiles, and assembles synthesized utterances into speaker-aware simulated conversations. We evaluated five LLM families under single-generator, fixed-budget mixture, and scale-up settings using the same FastConformer-Large training recipe for each one. We ran comprehensive evaluations on the Hungarian BEA-Dialogue benchmark corpus, with the method itself being applicable to any language given the resources for each component. The results show that synthetic conversations consistently improve speech recognition performance, but generator choice and data composition strongly affect the gains. Our largest training configuration, using only 67 hours of real conversations and 636 hours of simulated data, achieves better performance on the evaluation benchmark than a zero-shot model trained on 2700 hours of Hungarian speech. These findings indicate that LLM-generated conversational data synthesized with TTS is a practical complement to real conversational corpora for speech model training.

---


### 304. [Using Reward Uncertainty to Induce Diverse Behaviour in Reinforcement Learning](https://arxiv.org/abs/2606.03962)

**<font color=#1a73e8>作者：</font>** Anthony GX-Chen, Ankit Anand, Gheorghe Comanici 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical reinforcement learning (RL) typically seeks a deterministic policy that maximizes the expected sum of a scalar reward. Yet, modern applications such as language model fine-tuning or scientific discovery demand diversity. Existing remedies such as entropy regularization or diversity bonuses often require fragile trade-offs that sacrifice performance for stochasticity or rely on heuristic metrics that can misalign policy rankings. We argue that diversity is more naturally understood as the rational response to uncertainty in the reward. When the reward function is not perfectly known--as is the case with ambiguous preferences or imperfect reward models--committing to a single action can be sub-optimal. Building on this, we propose a fundamental reformulation of the RL objective by replacing the scalar reward with a distribution over reward functions, and applying a non-linear objective over sets of actions. The result is a framework in which calibrated behavioural diversity emerges naturally, remains controllable through the reward function distribution, and is obtained without sacrificing expected reward. Focusing on the contextual bandit setting, we derive a principled gradient estimator for this objective and prove that our formulation naturally generalizes both vanilla policy gradient and more recently developed action-set approaches. Our empirical results demonstrate that this framework offers a robust and theoretically grounded alternative for complex RL tasks where the traditional formulation of the problem fails to induce the desired breadth of agent behaviour.

---


### 305. [QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards](https://arxiv.org/abs/2606.03968)

**<font color=#1a73e8>作者：</font>** Rongzhi Zhang, Rui Feng, Zhihan Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based RL is a promising route for extending reinforcement learning beyond verifiable rewards, yet existing methods optimize rubrics while treating the query distribution as fixed. We identify a structural bottleneck: rubric quality is constrained by query structure. Open-ended queries yield vague rubrics; naively narrowing them introduces fabricated references that no model can verify, so all responses fail and training receives no reward signal. We present QUBRIC, a framework that co-designs queries and rubrics. Teacher-derived key points ground the rewriting of open-ended queries into scenario-based, evaluable questions. Contrastive rubric generation then turns teacher-policy gaps into query-level criteria, and learnability filtering retains only informative query-rubric pairs for GRPO training. QUBRIC achieves a +5.5 point gain on ArenaHard over the SFT baseline. Trained only on instruction-following data, it further transfers to three held-out benchmarks spanning legal, moral, and narrative reasoning (+6.3 points on average), with improvements concentrated in reasoning-related dimensions. These results provide evidence that co-designing queries and rubrics can make rubric-based RL a practical complement to RLVR beyond strictly verifiable tasks.

---


### 306. [Video-Mirai: Autoregressive Video Diffusion Models Need Foresight](https://arxiv.org/abs/2606.03971)

**<font color=#1a73e8>作者：</font>** Yonghao Yu, Lang Huang, Runyi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Causal video generators must predict from the past, but they need not learn only from it. In streaming autoregressive video diffusion, each emitted segment becomes a commitment that future segments must preserve. Standard training, however, only asks each causal state to explain the present. This creates what we call a representation-level planning gap: states that fit the current segment may discard identity, layout, and motion information needed for a consistent future. We introduce Video-Mirai, a training-only method that closes this gap without changing causal inference: the generator rolls out causally, a frozen foresight encoder reads the completed rollout non-causally, and a lightweight predictor distills the resulting stopped-gradient targets into causal states. Future frames supervise representations, never generator inputs. At inference, the encoder and predictor are discarded, leaving the original architecture, per-step FLOPs, and KV-cache behavior unchanged. Video-Mirai improves a strong Causal-Forcing baseline on 5-second VBench from 83.8 to 84.6 in terms of Total Score. On 30-second rollouts beyond the training horizon, subject consistency improves from 84.9 to 88.5 and background consistency from 90.2 to 91.9. Ablations identify future-conditioned targets as the key ingredient, and probes show that future frames become more decodable from current features. Causality should constrain inference, not representation supervision. Our study highlights that visual autoregressive models need foresight. Project page: this https URL.

---


### 307. [AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation](https://arxiv.org/abs/2606.03972)

**<font color=#1a73e8>作者：</font>** Haobo Li, Yanhong Zeng, Yunhong Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present AAD-1, an Asymmetric Adversarial Distillation framework for One-step autoregressive image-to-video generation. State-of-the-art methods adopt adversarial distillation but suffer from motion collapse and training instability, resulting in static videos. AAD-1 addresses these challenges through two key designs in architecture and training strategy. Our key architectural insight is to break the symmetry between generator and discriminator. While the generator remains causal to preserve autoregressive sampling capability, the discriminator attends bidirectionally over the full spatiotemporal context and produces a single holistic realism score for the entire video sequence. This asymmetric design enables the discriminator to effectively detect global temporal failures and long-range drift that cause motion collapse in autoregressive generation. To stabilize training, we introduce a phased strategy that first uses distribution matching to bootstrap a stable one-step generator, providing a warm-up phase that brings the student distribution closer to the teacher before adversarial distillation begins. Extensive experiments on VBench demonstrate that AAD-1 achieves state-of-the-art performance in one-step autoregressive video generation.

---


### 308. [Formalizing the Binding Problem](https://arxiv.org/abs/2606.03976)

**<font color=#1a73e8>作者：</font>** Lianghuan Huang, Yihao Li, Saeed Salehi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representations of the world, arguably, contain information about features (e.g. something is blue, something is a circle) but also information about which features are part of the same object (e.g. the circle is blue), which we call binding information. Any system with the ability to understand scenes with multiple objects must be able to solve the binding problem: it needs to know which features belong together. However, despite work showing that Vision Transformers (ViTs) know which patches belong together, it is not known whether current deep learning models learn to exhibit binding information, i.e., for features. We may believe that there is not much binding information, after all misattributing features to wrong objects is a common failure of ViT-based architectures, especially in scenes with objects sharing features. Here we formalize the binding problem with an information-theoretic approach, and introduce a probing method to measure binding information in model representations. We perform experiments on ViTs, measuring binding from different components of the architecture, such as the image summary token [CLS] or the spatial tokens. We use datasets with different binding challenges, such as feature sharing, occlusion, and natural features, while comparing the performance of several pre-trained ViTs. Overall, our research demonstrates binding as a key ingredient to strong visual recognition and reasoning.

---


### 309. [PixVOD: Pixel-Distributed Direct Visual Odometry and Depth Estimation](https://arxiv.org/abs/2606.03989)

**<font color=#1a73e8>作者：</font>** Shinjeong Kim, Ignacio Alzugaray, Callum Rhodes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images composed of 2D pixel arrays are the standard input to computer vision algorithms, yet many underlying computations can be distributed across pixels. Transmitting raw, redundant, and noisy pixel data off the sensor remains inefficient, motivating a shift toward focal-plane sensor-processors that perform a significant part of the computation directly within each pixel. We envision pixels synthesizing higher-level signals locally, reducing downstream load, and providing richer inputs for higher-level vision tasks.
We propose a fully parallelizable form of visual odometry and depth estimation across pixels, where sensor-processors exchange information through Gaussian Belief Propagation (GBP) to achieve consensus about camera motion and infer depth from per-pixel photometric observations and a surface normal prior. To maintain geometric stability during optimization, we introduce a keyframe-like anchoring mechanism that regulates the effective baseline between frames, enabling consistent motion and depth updates. Our method is evaluated on realistic datasets, demonstrating the feasibility of GBP-based pixel-level distributed odometry and depth estimation with keyframe anchoring on-sensor. Project Page: this https URL

---


### 310. [Neuron Populations Exhibit Divergent Selectivity with Scale](https://arxiv.org/abs/2606.03990)

**<font color=#1a73e8>作者：</font>** Amil Dravid, Yasaman Bahri, Alexei A. Efros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether neuron populations within neural networks evolve predictably with scale, extending scaling laws beyond macroscopic observables such as loss. To probe this question, we study Rosetta Neurons, a previously characterized class of neurons whose activation patterns are similar across independently trained models (Dravid et al., 2023). In separate analyses of language models up to 30B parameters and vision models up to 5B parameters, we observe that the population of Rosetta Neurons follows a sublinear power law in model size, growing in absolute number but occupying a shrinking fraction of the total neuron count. We further observe a Neuron Polarization Effect: Rosetta Neurons become more selective and increasingly monosemantic with scale, separating from a growing non-Rosetta population that remains less selective. An analytical model balancing feature utility against limited neuron capacity explains the sublinear power-law scaling and this polarization effect. Finally, we find that Rosetta Neurons become more domain-specialized with scale and illustrate their selectivity through a targeted data-filtering case study for continued pretraining. Our results point to a scaling law for interpretable, shared neuron-level structure, linking model size to systematic changes in neuron universality, selectivity, and specialization.

---


### 311. [Exploring Easy Boosts for Lidar Semantic Scene Completion](https://arxiv.org/abs/2606.03992)

**<font color=#1a73e8>作者：</font>** Tetiana Martyniuk, Jonathan Seele, Alexandre Boulch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper investigates "free lunch" strategies to boost the performance of lidar semantic scene completion (SSC) without requiring complex architectural redesigns. We first demonstrate that endowing input point clouds with semantic pseudo-labels from off-the-shelf segmentors significantly improves the performance of existing architectures. By evaluating these models against an oracle, we establish that high-quality semantic priors are a primary driver of mIoU gains. Furthermore, we equip the input lidar scan with visibility information that distinguishes between empty and unknown spaces, which provides a secondary performance boost across the tested architectures. Using these simple enhancements, we observe that older models remain competitive with state-of-the-art systems, and can even outperform them. Our code is available at this https URL.

---


### 312. [SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image](https://arxiv.org/abs/2606.03994)

**<font color=#1a73e8>作者：</font>** Inhee Lee, Sangwon Baik, Sungjoo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing interactive, simulation-ready 3D scenes from a single image is a critical bottleneck for robotic manipulation. While recent single-image lifters recover plausible per-object shapes, composing them yields scenes that collapse under physical simulation due to interpenetrating, hovering, or sinking objects. Existing physics-aware methods address this strictly as a post-hoc layout correction, leaving the underlying geometric errors unresolved. To address this, we introduce SimuScene, a compositional 3D reconstruction pipeline that puts physics in the loop of shape and layout estimation. Rather than using physics merely for layout cleanup, we utilize the physics engine as a diagnostic measurement tool during the generative process itself. By diagnostically simulating reconstructed objects under gravity, we convert penetration and support failures into quantitative correction signals that drive gravity-axis stretching and amodal shape resampling. This physics-informed feedback loop mitigates accumulated reconstruction errors and produces a stable, simulation-ready compositional 3D scene. Extensive experiments demonstrate state-of-the-art performance on physical stability and geometric alignment benchmarks. We further highlight SimuScene's utility by deploying reconstructed environments in humanoid control and robot-arm manipulation tasks.

---


> [!TIP]
> 当前位于：**301-312**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-312**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
