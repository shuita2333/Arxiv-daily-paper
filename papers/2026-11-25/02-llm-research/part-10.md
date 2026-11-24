# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-486**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-486**

---

### 451. [WorldLatent: A Unified 4D Latent Space for World Perception and Generation](https://arxiv.org/abs/2611.31209)

**<font color=#1a73e8>作者：</font>** Jingxi Chen, Yujia Chen, Cornelia Fermuller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative Pre-Training (GPT) represents a profound milestone in natural language processing, serving as the foundation for most of today's state-of-the-art large language models. By casting diverse understanding and generation problems into a shared token representation, GPT enables a single architecture and unified optimization loop to master heterogeneous tasks across massive corpora, giving rise to powerful foundation models for natural language. In contrast, 4D spatiotemporal vision lacks a common representational protocol: perception (such as depth and camera estimation) and generation are either handled by separate one-way pipelines or bolted together from unaligned single-modality spaces. In this work, we introduce WorldLatent, a framework that formulates a unified 4D latent space as a common protocol for both world perception and generation. Rather than relying on fragmented, task-specific models or stacked single-modality representations, our framework proposes a multimodal VAE architecture that compresses and fuses complex 4D visual appearance, geometry, and dynamics into a single structured latent representation. Within this formulation, perception and generation operate as complementary denoising processes over the same latent space, enabling one generative model to learn both capabilities simultaneously within a single training loop. Experiments across representative 4D benchmarks verify that our fused latent protocol achieves specialist-level zero-shot 4D perception, coherent 4D generation, and controllable editing from a single model. By demonstrating that diverse 4D tasks can be seamlessly unified under a shared representational protocol, our work provides a scalable foundation for general-purpose 4D spatial intelligence.

---


### 452. [Seeking in Space: Benchmarking Purposeful Active Exploration of Vision-Language Models for Spatial Reasoning](https://arxiv.org/abs/2611.31215)

**<font color=#1a73e8>作者：</font>** Xiwei Liu, Yulong Li, Xuhui Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans explore unfamiliar spaces with purpose, deciding where to look until they have gathered the evidence a spatial question requires. However, can vision-language models (VLMs), which reason increasingly well over curated images and videos, also seek in space when the evidence is not handed to them? We present ActSpace-Bench, a benchmark of 994 questions across 234 exploration episodes in 72 real-scanned indoor scenes, where a model starts from a single view, navigates real captured frames, and must gather evidence before answering. To assess whether such exploration is purposeful, we introduce a controlled evaluation protocol that fixes each model as the reasoner and compares its own exploration against a same-budget random walk and an oracle route, separating evidence seeking from spatial reasoning. Every question is verified to require exploration and answered from 3D annotations, masked-evidence questions test whether models know when to abstain, and over 95% of sampled questions are confirmed correct by human verification. Evaluations of 23 proprietary, open-weight, and spatially specialized VLMs reveal that the strongest models do seek evidence with purpose but lose much of it to limited memory, whereas weaker and specialized models explore no better than a random walk or fail to reason over the evidence they are given, pointing to memory and evidence-grounded reasoning as the next targets for active spatial intelligence.

---


### 453. [Agentic AI for Intent Management and Control in Autonomous Communication Networks](https://arxiv.org/abs/2611.31223)

**<font color=#1a73e8>作者：</font>** Burak Demirel, Yu Wang, Pablo Soldati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI)-driven automation will help future mobile networks translate high-level network intents into concrete network optimization or control actions. However, existing approaches often focus on intent management and orchestration, leaving the adaptation of underlying network optimization and control functions largely unaddressed. This article proposes a triadic agentic AI framework that co-designs intent management and intent fulfillment through three agents: an interpreter, powered by a language model, that translates and refines intents into machine-readable optimization templates; an optimizer that adapts controller policies to intent specifications; and a controller that performs fast decision-making. We discuss the design space of each agent and how the workflow can be embedded across network architectural domains. Finally, we develop a concrete realization combining a language-model interpreter with Bayesian optimization for the optimizer and multi-objective reinforcement learning for the controller, and evaluate it in a radio resource management case study for differentiated connectivity. Results demonstrate how the agentic AI framework can connect high-level intents with runtime network control, showing adaptability of intent specifications and control policies to service requirements and changing network conditions.

---


### 454. [Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ](https://arxiv.org/abs/2611.31228)

**<font color=#1a73e8>作者：</font>** Daniel Theron  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompting language models to verbalize stepwise numerical confidence during generation is an increasingly popular approach for triggering backtracking and error correction in agentic reasoning. This strategy presupposes two capabilities: (1) in-situ monitoring fidelity (does confidence drop when an error occurs?) and (2) downstream steering control (does an uncertainty token causally steer the model to repair its error?). We evaluated four open-weights models (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B, and Phi-4, 14.7B) across 15,200 math benchmark attempts, isolating 2,017 reasoning errors within each model's capability frontier. Applying 27,568 counterfactual continuations across these failure points, we demonstrate a consistent decoupling between monitoring and control.
On monitoring, all four models fail to detect their own errors. Verbalized confidence does not distinguish mistake steps from sound reasoning, yielding near-chance within-position AUROCs between 0.500 and 0.561. Even at a model's first reasoning error, trajectory confidence remains saturated at 95.1% to 99.9%, with noticeable drops ($\ge 10$ points) appearing on fewer than 9% of errors in Llama and under 1.6% in the other three models. In contrast, models respond readily to external uncertainty: injecting a low-confidence tag (10%) at the error step significantly increases downstream correction across all models (+3.7 to +22.5 points over format-matched 95% certainty; all $p \le 0.0022$), reaching up to 38.5% under active rethinking instructions. However, injecting doubt onto already-correct steps causes models to discard valid reasoning, reducing solve rates by up to 22.8 points. Inference-time self-correction is thus bottlenecked by in-situ error detection rather than downstream repair capacity: models readily steer toward recovery when prompted with doubt, yet fail to self-monitor during generation.

---


### 455. [TowerBridge: Bridging the Dual-Encoder Modality Gap via Weight-Space Programming](https://arxiv.org/abs/2611.31233)

**<font color=#1a73e8>作者：</font>** Hani Alomari, Md Atabuzzaman, Chris Thomas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP-style dual encoders map images and text through two separate towers into a shared embedding space, where the two modalities occupy distinct regions separated by a modality gap. Retrieval fails when wrong matches, or hard negatives, outrank the correct one, and the gap is the usual suspect. Yet removing it post hoc degrades retrieval on every CLIP checkpoint we test. We introduce a paired statistic that identifies directions where the two towers agree more on hard negatives than on matched pairs. Mildly attenuating these directions improves retrieval while largely preserving the gap. We arrive at this correction through weight-space programming: guided by the statistic, an LLM agent inspects both towers and writes closed-form weight edits without backpropagation. Free to edit any component, the agent improves COCO test retrieval on all 13 CLIP checkpoints and edits an output projection in 12 of the 13. We distill and refine its recurring correction into TowerBridge, a closed-form recipe motivated by a first-order analysis of the hard-negative margin. Computed in seconds from 25,000 labelled pairs, it requires no model-specific tuning and leaves the architecture and inference cost unchanged. TowerBridge improves COCO test retrieval by 16.8 RSUM and Flickr30k test retrieval by 6.6 on average across all 21 evaluated CLIP checkpoints, including 8 unseen by the agent, while limiting any drop in ImageNet zero-shot accuracy to 0.5 points. It also reduces hubness on all 21 checkpoints and improves retrieval on 4 of 5 dual encoders from other families.

---


### 456. [Let Vision-Language Models Generate Images through Their Representations](https://arxiv.org/abs/2611.31237)

**<font color=#1a73e8>作者：</font>** JB Kim, Byungwoo Jeon, Kyungmin Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent unified multimodal models aim to combine visual understanding and generation within a single model, yet effectively integrating the two capabilities remains challenging. Leveraging pretrained vision-language models offers a way to build on already learned multimodal knowledge, but making this knowledge effectively accessible to visual generation remains nontrivial. We find that a central challenge lies in the heterogeneous visual representations used for understanding and generation. To address this challenge, we introduce Integral, which converts a pretrained vision-language model into a unified multimodal model by constructing a shared visual representation space across the two capabilities. Integral implements this design through two complementary components. Abstraction Fusion constructs shared visual tokens by aggregating hierarchical representations from the frozen vision encoder, while Block-wise MoT introduces a lightweight generative stream that interacts with the vision-language model only at block boundaries. Our approach effectively preserves the pretrained understanding capability while extending it to strong visual generation. Controlled comparisons further demonstrate that sharing visual representations between understanding and generation substantially improves generative learning compared with using a separate visual representation space, despite comparable reconstruction fidelity. These results suggest that representations learned by pretrained vision-language models already provide an effective foundation for visual generation.

---


### 457. [Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory](https://arxiv.org/abs/2611.31239)

**<font color=#1a73e8>作者：</font>** Chen Wang, Jiahui Huang, Riccardo de Lutio 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Exploring a scene from as little as a single photo requires generating a long, camera-controlled walkthrough that extends far beyond what was captured, yet remains consistent upon return. Memory-based video generation methods preserve what they have already seen, but have no anchor beyond it, where the camera drifts from its path and a text prompt can name objects but not place them. Layout-conditioned methods provide such an anchor and precise control over what appears where, but rely on layouts that are typically authored by hand. Both limitations arise because, beyond what was captured, nothing anchors the video model unless a human authors one. To overcome both, we propose Lyris, a long video generation framework that never leaves the video model without an anchor: a persistent point-cloud memory where the scene has been observed or generated, and a 3D layout that a vision-language model authors where it has not. Our key insight is that the interface between the two models can be surprisingly coarse. A layout of one labeled 3D box per object is simple enough for a vision-language model to author (and for a user to edit), yet expressive enough for a video model to follow once rendered along the camera path. We demonstrate walkthroughs of over three minutes and 50 meters from a single photo, passing through doorways into rooms it never shows. When evaluated on minute-long round trips across four datasets, Lyris outperforms state-of-the-art methods by a wide margin, reducing camera error by 3.8x and improving consistency upon return by 22% on average.

---


### 458. [Pruning Autonomous Driving VLAs: What to Preserve for Reasoning and Action](https://arxiv.org/abs/2611.31240)

**<font color=#1a73e8>作者：</font>** Seongchan Kim, Soowon Son, Sangoh Kim 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning vision-language-action (VLA) models for autonomous driving use chain-of-thought (CoT) reasoning to guide action generation, but incur substantial memory and computational costs. We study structured pruning for these models, focusing on preserving both scene understanding and trajectory prediction. Our analysis of Taylor importance in Alpamayo-1.5-10B shows that reasoning and trajectory objectives assign different importance to the same vision-language model (VLM) structures. In the action expert, MLP channels exhibit more stable importance rankings across denoising steps than query heads, and a small fraction of channels accounts for most of the measured importance. Based on these findings, we propose MoOP, which combines importance ranks from both objectives for VLM pruning and aggregates stepwise importance to select a fixed subset of expert MLP channels. At 24.0% total parameter reduction, VLM-only pruning with MoOP performs comparably to or slightly better than the strongest baselines in driving, while retaining 94.0% of the dense model's LingoQA score, far above all other methods. At a higher reduction of 30.0%, MoOP degrades much less than every other method, as it is the only one whose reasoning does not collapse. Removing 93.75% of expert MLP channels increases total parameter reduction to 39.4%, with nearly unchanged open-loop errors relative to VLM-only pruning and competitive closed-loop performance. The resulting model achieves a 1.37x end-to-end inference speedup and 36.6% lower peak memory than the dense model, without post-pruning fine-tuning.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 459. [SnakeTranslate: Weakly Supervised Policy Learning from Offline Parallel Text for Simultaneous Translation](https://arxiv.org/abs/2611.28055)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu Pu, Zhiyun Fan, Baiji Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adaptive simultaneous translation requires reliable prefix translation and timely READ/WRITE decisions, but ordinary parallel corpora provide no action annotations. We present SnakeTranslate, which adapts loss-derived alignment to sampled causal histories for jointly learning both capabilities. The framework supports supervised fine-tuning (SFT) on parallel text and on-policy distillation (OPD) with reverse Kullback--Leibler (KL) divergence on student-generated translations. At inference, source and target tokens form one append-only interleaved history, enabling incremental decoding with cache reuse. On FLEURS, NTREX128, and WMT24++, our 4B model improves quality--latency trade-offs over streaming policies applied to the same offline-tuned backbone, with further gains from OPD. It also compares favorably with larger translation models at low and moderate latency, while higher-latency quality gaps remain on WMT24++.

---


### 460. [Benchmarking Foundation Models for Bone Scaffold Pore Detection: A Comparative Analysis of Few-Shot Performance](https://arxiv.org/abs/2611.28113)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tri Tin Vo, Vu Thien An Ngo, Nhi Kieu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating the mechanical properties of bone scaffolds conventionally requires destructive testing or costly Finite Element Analysis, while deep learning alternatives are constrained by the scarcity of labeled biomaterial imaging data. This study introduces the first expert-annotated, pixel-dense dataset of biopolymer bone-scaffold SEM images, spanning five magnification series, and uses it to benchmark two state-of-the-art pre-trained foundation models under a 12-shot fine-tuning regime. SAM3, an instance segmenter, and YOLOv26, a bounding-box detector, feed the predicted pore geometry to regression heads that estimate Young's modulus and compressive yield strength. Our central finding is that both models fail by pore density rather than magnification: YOLOv26's predicted pore counts saturate and porosity estimation collapses on the most crowded frames, whereas SAM3 over-fragments sparse pore fields and merges adjacent pores in dense ones, producing eight catastrophic failures against three for YOLOv26. Averaged across the 44-image evaluation set, YOLOv26 achieves lower porosity error (19.9% vs. 23.1% MAE), higher precision, and a higher F1 score, whereas SAM3 offers pixel-level instance segmentation that YOLOv26's bounding boxes cannot reproduce. We conclude that model selection should be driven by pore density rather than SEM magnification alone.

---


### 461. [HandXFM: Semantic-Structural Distillation for Hand Radiograph Foundation Models](https://arxiv.org/abs/2611.28283)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxi Long, Ganlin Feng, Lianghong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand radiographs support diverse clinical tasks, including skeletal maturity assessment, rheumatoid arthritis scoring, abnormality screening, and anatomical localization, yet existing models are typically trained separately for each task and dataset. We present HandXFM, a domain-specific foundation model that leverages cross-modality knowledge for comprehensive hand X-ray understanding. HandXFM distills semantic priors from BiomedCLIP and structural cues from a chest X-ray Vision Transformer (ViT) through a unified alignment framework, integrating complementary medical knowledge in an interpretable way. After pretraining, HandXFM can be adapted to a range of musculoskeletal tasks, including bone age estimation, SvH score prediction, abnormality detection, joint localization, bone segmentation, and visual question answering. It consistently outperforms task-specific and single-expert baselines, achieving up to 0.11 improvement in Pearson correlation coefficient (PCC) for bone age prediction and a 12\% accuracy gain in abnormality classification. Moreover, HandXFM generalizes to unseen datasets and yields cross-attention maps linking clinical terms to anatomical regions. These results demonstrate that multi-expert distillation effectively unifies semantic and structural supervision within a single pretrained model, establishing HandXFM as an interpretable and generalizable foundation model for hand radiograph analysis.

---


### 462. [Targeted In-Context Poisoning of Tabular Foundation Models: An Empirical Study](https://arxiv.org/abs/2611.28396)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Adem Alparslan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) predict the label of a query row conditioned on a context of labelled rows, without training on them. Drawn from operational data, the context becomes an attack surface. We study targeted in-context poisoning in its simplest form: an attacker with write access to the context's source places exact copies of a target row there with the wrong label. On 30 OpenML datasets for binary classification, one such poison row flips on average 53% (TabICL) and 65% (TabPFN) of the predictions correct without attack, and three poison rows flip almost all. The same copy with the true label flips almost none, and performance on the remaining rows hardly changes. Predictions flip by two routes: in TabICL, the target row's embedding rotates towards the mean of the wrong class; in TabPFN, the poison row pulls genuine rows of the wrong class along. The TFMs thus infer soundly, but from forged evidence. Predictions of trained models flip as well: almost always for a random forest, for CatBoost as often as for the TFMs, hardly for a logistic regression. New with TFMs is not the kind of vulnerability but the timing: the data take effect at the moment of prediction, not through training, and a poison row in a live context can be deleted afterwards. Three established requirements must therefore cover the context: access control for its source, traceability per prediction, which can also deter, and validation at prediction time. A detection mechanism shows how such validation can work.

---


### 463. [Plan Big, Paint Small: Semantic-Aware Computation Allocation for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2611.28402)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yixuan Luo, Yanjing Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion streams a video chunk by chunk, but large AR models are too slow for real-time use. We ask where in an AR rollout a large model is actually needed. Pairing Krea-Realtime-14B with Self-Forcing-1.3B, which share their latent space and denoising schedule, we find that the order of the two models matters: when the 14B model generates only the first chunk and the 1.3B model continues, the rollout keeps 95\% of the 14B model's semantic advantage, whereas the reverse allocation keeps 16\% at about ten times the cost. The large model decides what the video shows; the small model only has to carry it forward. We turn this into BigSmall, a training-free planner--renderer sampler. The 14B model plans the opening chunk and sketches the chunks in which content changes, which preserves motion, and the 1.3B model renders the rest; a faster variant, BigSmall, plans only the opening chunk. A cross-model KV cache that is approximate, windowed and lazy lets the planner leave and re-enter the rollout at low cost. On VBench, BigSmall is $3.02\times$ faster than the 14B model at an unchanged semantic score and motion, and $1.55\times$ faster than SDVG, which lets the small model draft first; BigSmall reaches $3.77\times$ at the same semantic score, trading away 10\% of the motion. On minute-long videos (LoCoT2V-Bench), where the 14B model degrades when it reads its own long history, BigSmall is $3.14\times$ faster than the 14B model and scores higher ($+1.78$).`

---


### 464. [MedCoast: Semantic Abstraction of Reasoning Trajectories for Test-Time Biomedical Question Answering](https://arxiv.org/abs/2611.28586)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yishan Zhong, Jieru Li, Xuanzhe Ding 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical question answering often requires multi-step reasoning under limited inference budgets. While test-time search methods such as Tree-of-Thought can improve reasoning performance, directly searching over free-form language is computationally expensive and highly redundant, as many reasoning trajectories contain semantically equivalent intermediate steps expressed in different surface forms. We introduce MedCoast, an offline-to-online reasoning framework that converts sampled chain-of-thought trajectories into a compact space for structured process supervision. Offline, we recursively cluster semantically similar reasoning steps under shared prefixes to construct an abstract reasoning tree that captures recurring clinical reasoning patterns. We then derive node-level supervision from progress toward correct solutions, and train a lightweight process reward model (PRM) to evaluate partial reasoning states. At inference time, the learned critic guides test-time exploration by prioritizing promising reasoning prefixes. Across seven biomedical QA benchmarks, MedCoast often improves over self-consistency under fixed inference budgets, with gains of up to 15 points. Despite using a reward model more than 50 times smaller, MedCoast achieves performance comparable to state-of-the-art reward models in several settings, highlighting its potential for resource-constrained biomedical reasoning.

---


### 465. [Distilling Visual Agents from Limited Interaction Experience](https://arxiv.org/abs/2611.28618)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Siyu Zhou, Jing Jiang, Chengqi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How much interaction experience is needed to distill a capable visual agent? We study learning from few tasks and recorded interaction histories. Our framework selects representative trajectories using skill-context coverage and ordered visual-decision similarity. On-policy distillation (OPD) learns through fresh interaction on selected tasks or fresh student responses at fixed histories. Across Navigation, Sokoban, and spatial mapping, even one online training task supports transfer to other tasks. Four fixed trajectories raise a 4B student's success from 49.17% to 82.08% on standard Navigation and from 60.16% to 85.55% on Sokoban, recovering over 90% of the measured gap to a 27B teacher on these panels. On an independent Navigation panel, replay improves success from 45.83% to 76.67%, retaining 91.36% of the same-task online gain without new interaction during optimization. Training repetitions, matched supervised fine-tuning (SFT), and a 9B extension further support the value of compact experience.

---


### 466. [PhyMind: Physics-Informed Masked Autoencoding for EEG Foundation Models](https://arxiv.org/abs/2611.28856)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** A Adith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models are pre-trained almost exclusively with masked reconstruction through a free-form decoder, sometimes with hand-crafted spectral targets added, as in MANAS-2. We study what happens when that decoder is replaced by a generative forward model of EEG. PhyMind keeps a standard masked transformer encoder, but its decoder must explain the masked signal through 68 cortical regions, each driven by damped stochastic oscillators and an aperiodic Ornstein-Uhlenbeck process, projected to the recording's own montage by a fixed boundary-element lead field evaluated per derivation. Training combines masked reconstruction with a Whittle spectral likelihood, an oscillator-dynamics residual, a minimum-norm source prior and a penalised neural residual. In a controlled comparison (same encoder, data, steps and seed), the physics decoder produces encoder tokens whose spectral content is far more linearly decodable than with a masked-autoencoder decoder or with the MANAS-2 objective: mean R^2 on a token-level spectral probe with amplitude-normalised targets is 0.67/0.77/0.77 on three datasets, against 0.24/0.50/0.50 (MAE) and 0.48/0.67/0.66 (MANAS-2 objective), approaching the released 92.8M-parameter MANAS-2 (0.71/0.81/0.80). Downstream gains in the controlled setting are small (four-task mean balanced accuracy 56.6 vs. 53.8 for MAE frozen, 63.8 vs. 62.7 fine-tuned). Region-level features from the physics decoder raise frozen four-class motor-imagery accuracy by 7-14 points, so a 7.2M-parameter model pre-trained on 3k hours of open EEG is comparable to the released MANAS-2 with frozen features (63.0 vs. 61.6). After full fine-tuning, MANAS-2 remains better (66.8 vs. 65.4 for our best model). The inferred sources do not reproduce the lateralisation that a classical inverse solution finds in motor imagery, so we do not claim anatomical interpretability. Code and weights are released.

---


### 467. [When Wrong Answers Remain Unsettled: Failure Dynamics in Recurrent Reasoners](https://arxiv.org/abs/2611.28971)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiucheng Zang, Congkai Peng, Yankai Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a recurrent reasoner returns a wrong answer, is its computation finished or merely stopped? We test this on a trained Hierarchical Reasoning Model (HRM; 27M parameters, Sudoku-Extreme) by running the recurrence for one more inference budget and comparing with an unperturbed control. Solved answers persist (0.95 of 512 endpoints). Wrong answers mostly do not: 0.42 of near-miss answers (n=170) and 0.18 of all 512 wrong endpoints keep their answer. Perturbations from 0.05x to 20x the terminal-update scale barely change these rates, so the measurement reflects continued recurrence, not noise sensitivity. The solved-above-wrong ordering also holds in five further settings (a second seed, TRM, Maze, GRAM-guided TRM, N-Queens), but a fixed 1/2 persistence threshold does not, and neither do HRM's endpoint-spectrum and fast-versus-slow predictability patterns, which are not universal diagnostics. Perturb-and-reselect (known from prior work) is consistent with this: frozen noise gains 4.8 accuracy points (197 gained, 2 lost), but compute-matched extended depth gains 5.6 and Sudoku symmetry augmentation 34.6, so noise is not the best use of the budget. Conclusions are limited to finite horizons and one primary HRM checkpoint; they do not exclude asymptotic attractors.

---


### 468. [THETA: Heat Diffusion as a Structural Prior for Cross-Domain Transfer in Graph Foundation Models](https://arxiv.org/abs/2611.29210)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haonan Liu, Shuo Wang, Zhao Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph foundation models (GFMs) aim to learn transferable representations across domains with heterogeneous node attributes and graph structures. However, relations inferred from node attributes can rely on domain-specific feature semantics, limiting their transferability to unseen graphs, particularly in low-label regimes. We propose THETA (Topology-aware HEat-based TrAnsfer), a graph foundation model that leverages Heat Kernel Signatures (HKS) as a topology-based structural prior for cross-domain transfer. By characterizing nodes' heat-return behavior across diffusion scales, HKS provides a common structural descriptor across graphs without requiring aligned attribute semantics, complementing feature-based relations with information about local and multiscale connectivity. THETA incorporates this prior into both pre-training and few-shot adaptation. During pre-training, it combines HKS with node attributes to construct refined graph views and trains a shared encoder via contrastive learning. During adaptation, it uses HKS to guide edge-weight adjustment and prototype refinement while keeping the encoder frozen and retaining the contribution of labeled support nodes. Through HKS, THETA uses structural information from heat diffusion to guide both representation learning and few-shot adaptation with unlabeled target-domain data. Extensive experiments across diverse graph domains demonstrate that THETA consistently outperforms existing baselines on downstream tasks, highlighting the value of heat diffusion as a structural prior for transferable graph representations.

---


### 469. [SleepXA: Composing Pretrained Neural and Cardiac Foundation Models for Sleep Representation Learning](https://arxiv.org/abs/2611.29364)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaoyu Chen, Xiao Gu, Chao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physiological signals recorded during sleep provide synchronized views of neural, cardiac, respiratory, and other bodily systems, while preserving modality-specific information. Existing EEG and ECG foundation models already capture rich but distinct physiological structure, motivating an alternative to training a multimodal sleep model from scratch: composing existing pretrained models. We introduce SleepXA, a framework that uses synchronized polysomnography (PSG) to compose independently pretrained neural and cardiac foundation models. SleepXA combines pretrained EEG and ECG encoders with lightweight encoders for additional PSG modalities, and learns shared and modality-specific representations through sleep-guided alignment. We pretrain SleepXA on 9,230 overnight PSG recordings from three large cohorts and evaluate it on 27 downstream tasks spanning sleep representation, clinical and disease prediction, and daytime physiological transfer. SleepXA ranks among the top two methods on 22 of 27 tasks. Controlled experiments further show consistent benefits across sensor configurations and EEG-ECG backbone choices, while pretrained initialization outperforms architecture-matched training from scratch and SleepXA surpasses alternative multimodal composition strategies. These results suggest that synchronized multimodal physiology can serve as a natural interface for composing existing physiological foundation models, yielding reusable representations that extend beyond sleep to clinical and daytime physiological settings.

---


### 470. [Attacking Tabular Foundation Models: An Experimental Taxonomy of Context Poisoning and Test-Time Evasion](https://arxiv.org/abs/2611.29627)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ramak Nassiri, Sujan Kumar Reddy Challa, Feroz Ahmed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models condition predictions on labeled examples supplied at inference time, creating an attack surface that differs from conventional model training. We study four manipulation families (label flipping, backdoor context poisoning, clean-label context selection, and test-time evasion) and organize them by attack stage, label consistency, and distributional realism. TabPFN-2.5, TabICL, and XGBoost are evaluated on CIC-IDS2017 and N-BaIoT using a common preprocessing and evaluation pipeline. Backdoor context poisoning provides strong targeted control over the in-context models with little change in clean accuracy, whereas selecting real, correctly labeled boundary-crowding rows causes no systematic accuracy degradation up to a 20% bias fraction. A simplified surrogate-transfer constrained PGD attack inspired by, but not equivalent to, CAPGD also produces test-time evasion, outperforming equal-budget random noise in most settings. The comparison shows that attack effectiveness depends strongly on both where manipulation occurs and how much freedom the attacker has to alter the data.

---


### 471. [Reducing Authorship Attribution Risk in Student Texts Through Style-Conditioned Rewriting](https://arxiv.org/abs/2611.29642)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Li Siyan, Zhen Xu, Jiayi Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building NLP applications for education is constrained by data scarcity due to student privacy concerns and data regulations. To address this, we propose a style-aware approach to rewriting student forum posts that retains analytical value while reducing identifiability. Our method isolates content, structure, and style as separate conditioning channels and aggregates over student-disjoint exemplar partitions within style clusters, extending Differentially Private In-context Learning (DP-ICL) with cluster-restricted retrieval. Across three educational NLP datasets, our approach achieves high style fidelity, preserves downstream task performance, and reduces authorship attribution risk relative to the original student-written texts, including against a dedicated authorship-attribution model.

---


### 472. [Relativising Integrity and Robustness: Prompt Injection and Partitioned Enclaves](https://arxiv.org/abs/2611.29802)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Brijesh Dongol  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Relative security (RS) judges a system against a reference system, but has only been applied to confidentiality. We introduce relative integrity (RI), which states that every behaviour a system exhibits under an attacker's influence must be one the reference can exhibit for the same trusted inputs. RS and RI each choose their own reference runs, so together they accept attacks whose leak and effects the reference reproduces only in different runs. We therefore develop a further property, relative robustness (RR), which asks the same runs to reproduce both and is strictly stronger than RS and RI together.
We give proof methods for RI and RR and a disproof method for RI, and apply them in two domains: (1) LLM agents under prompt injection, where the reference runs the same plan with a model that never obeys untrusted content, and (2) C programs partitioned across an SGX or TrustZone enclave boundary, where the reference keeps every function inside. We evaluate the properties on models of five published attacks, a support desk, an OP-TEE HOTP token and common agent defences. Two cases pass RS and RI but fail RR: an injection that makes the support desk's model accept any customer, as one input did in the Tensor Trust game, and the simulation step of the attack on Secret Network, in which an SGX enclave reveals a transfer's outcome without committing it. Our work is fully mechanised in Isabelle/HOL, with the enclave programs verified in C using AutoCorres2.

---


### 473. [CARE-3D: Reinforcement Learning for Evidence Grounded Agentic Reasoning in Situated 3D Scenes](https://arxiv.org/abs/2611.29969)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaoqian Hu, Ruihong Qiu, Yanran Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Situated 3D reasoning requires embodied agents to interpret objects, scene geometry, and viewpoint dependent spatial relations. Existing methods learn grounded interactions from supervised traces, but largely imitate prescribed evidence acquisition patterns rather than optimizing the support that the returned evidence provides for the correct answer. Moreover, outcome rewards provide limited credit for intermediate tool choices and may leave infrequent tools underexplored. An effective agent should instead adaptively decide what to ground, which tool to invoke, and how to assess the utility of returned evidence. To this end, this paper presents CARE-3D, a reinforcement post-training framework for adaptive grounded reasoning. Supervised fine-tuning (SFT) on grounding instructions first establishes valid interactions, after which Group Relative Policy Optimization (GRPO) optimizes the agent while keeping the 3D grounding module frozen. CARE-3D combines Counterfactual Attribution of Returned Evidence for evidence sensitive credit assignment, and Group Coverage Sampling to preserve tool coverage. Experiments on MSQA and Beacon3D show consistent gains over SFT and GRPO using only answer and format rewards, especially in spatial reasoning and grounding answer coherence. Our code is available at \href{this https URL}{CARE-3D}.

---


### 474. [Aligning Judge Models to Be Logically Consistent Multi-Rule Interpreters](https://arxiv.org/abs/2611.29975)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Michel Liao, Nimra Nadeem, Luxi He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Technical governance of AI models will soon require them to reason over and follow thousands of rules from different jurisdictions. However, as we show in this work, presenting an entire ruleset to a judge model---rather than asking it to judge one rule at a time---changes the way the model interprets the requirements, making it reach conclusions that conflict with its rule-by-rule judgments. We call this challenge multi-rule inconsistency and find that models are more lenient when judging rules embedded within the full ruleset than when judging rules separately. For example, we find that when a safety-critical rule prohibiting a model from pursuing objectives other than those it was given appears in a larger ruleset, all tested judge models are less likely to deem it violated. We examine several methods for reducing inconsistency, including prompting, consistency training using GRPO, and iterative rule refinement. As in human statutory interpretation, surrounding rules shape how a rule is interpreted. Unlike the legal setting, however, these interactions are currently happening implicitly inside the judge model's reasoning. We argue that multi-rule interactions must be measured and handled explicitly by ruleset designers to prevent undetected shifts in interpretation from causing downstream alignment failures.

---


### 475. [Benchmarking Geospatial Foundation Models under Calibrated Label Errors](https://arxiv.org/abs/2611.30215)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mollah Md Saif, Showrin Rahman, Anindya Majumder 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth-observation labels from maps, older products or hurried annotation arrive misaligned, coarse, loosely outlined or incomplete. Geospatial foundation models (GFMs) are nevertheless benchmarked with labels taken as correct. A practitioner therefore cannot tell which encoder to choose when the labels are imperfect. We present a benchmark protocol for fine-tuning under such labels. Four spatially structured error types are calibrated to equal label mIoU and applied identically to every model and seed. Every contrast is paired and read against an equivalence margin of $\pm 3$ points and a minimum detectable effect. We apply it to nine encoders, six decoder heads and ten datasets. In an exploratory reading at a matched learning rate the satellite-pretrained and web-pretrained DINOv3 encoders are equivalent within the margin on 8 of 9 datasets. Multispectral GFMs and an ImageNet ResNet-50 are equivalent within the margin on about half of them. Labels with random offsets cost the least at equal label quality. Under other decoder heads the verdicts mostly hold on FLAIR-2 and are decoder dependent on HLS Burn Scars. On four of five real label pairs the real label costs more than its matched simulated type. No choice of pretraining data makes an encoder consistently more robust, so the encoder is better chosen by its accuracy under imperfect labels.

---


### 476. [HEART: Hierarchical Expert Adaptive Refinement Transformer for ECG Representation Learning](https://arxiv.org/abs/2611.30298)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junho Song, Jong-Hwan Jang, Joon-Myoung Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning robust representations from electrocardiograms (ECGs) is challenging because repeated cardiac cycles coexist with subtle and sparse diagnostic cues in local morphology and rhythm-level context. Existing ECG foundation models commonly rely on Transformerbased patch encoders with uniformly shared dense refinement pathways, limiting adaptive processing across heterogeneous ECG tokens. We propose HEART (Hierarchical Expert Adaptive Refinement Transformer), an ECG foundation model that introduces stage-specific conditional expert refinement during self-supervised pre-training. HEART places a local-level MoE over patch-level representations before temporal contextualization and a global-level MoE over context-integrated token representations after self-attention. Token-level Top-1 routing allows different patches or contextual tokens within the same ECG to follow different expert pathways. On public ECG benchmarks, HEART achieves strong performance under both linear probing and fine-tuning, with particularly large frozen-encoder gains on PTB-XL Form and Rhythm (+6.76 AUROC points each over the strongest protocol-reproduced baseline). Routing analyses provide qualitative evidence of complementary local and global expert specialization. We release our code and pretrained models at this https URL.

---


### 477. [Video Generalized Category Discovery](https://arxiv.org/abs/2611.30316)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bardia Safaei, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) aims to categorize unlabeled data from both known and unknown classes using labeled data from only the known classes. While recent GCD methods have shown promise on static images, their performance degrades in videos due to temporal dynamics, larger intra-class variation, and the lack of temporal consistency in existing approaches. We introduce VideoGCD, a framework tailored for video action recognition under the GCD setting. Our method integrates (i) a partitioned Mixture-of-Experts module that encourages specialization for known and novel categories, (ii) a novel-class balancing loss to reduce bias toward known classes, and (iii) a temporal optimal transport loss that promotes consistent routing across frames. Experiments on three video benchmarks demonstrate that VideoGCD significantly improves performance over existing GCD methods, particularly on novel categories. Our findings highlight the importance of combining temporal modeling and expert specialization for video GCD.

---


### 478. [Time Series Foundation Models on the Edge](https://arxiv.org/abs/2611.30404)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Marco Pichler, Patrick Podest, Günter Klambauer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) forecast zero-shot with accuracy exceeding that of task-specific models, and the smaller ones fit on edge devices. Operational deployments must refresh their forecast as new observations arrive, and privacy and latency requirements often force this refresh onto resource-constrained edge devices. To serve as a forecasting system there, a TSFM must refresh quickly, keep latency and peak memory bounded as the stream grows, and retain its accuracy as the observed history accumulates. Refreshing incrementally without altering the forecast requires temporal causality: non-causal models recompute at every update, causal attention admits a KV cache that grows linearly, and causal recurrent models update a fixed-size state in constant time and memory. We make these states persist across refreshes for every causal architecture and verify equivalence to full recomputation. We evaluate nine TSFM configurations on univariate forecasting against all three requirements, measuring accuracy as a function of context length, single-refresh latency, and latency and memory on streams of up to one million time steps on a server-grade GPU and three edge devices. No model gains on average accuracy beyond its trained context and most lose it well before the full history is reached, while KV caches leave latency and memory growing linearly with the retained history. TiRex-2 is the only one of the nine configurations meeting all three requirements: it refreshes in 14 ms on the GPU and 120 ms on a Raspberry Pi 5, keeps latency, energy and peak memory constant over a million steps, and retains its accuracy on the untruncated history.

---


### 479. [Foundation Model and Radiomics Distance Scores for Post-Hoc Segmentation Failure Detection](https://arxiv.org/abs/2611.30582)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Simon Johannes Joham, Gianluca Guglielmo, Mateusz Kozinski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation models can fail silently when clinical data differs from training data. Deployed models rarely ship with quality control, and are often black boxes. Prior methods that work in this post-hoc failure detection setting still need a separate regression or segmentation model, registration, or access to model internals. We instead propose two failure scores based on the Mahalanobis distance to a labeled reference set. The first uses radiomic shape features of the predicted mask. The second uses frozen foundation model (FM) features, made mask-aware by overlaying the mask on the image, encoding it with a frozen DINOv3, and pooling patch features with more weight on the mask region. We test on multi-site prostate and hippocampus MRI under imaging-protocol and population shift. Ranking cases by predicted failure risk within each site, both scores are competitive with the registration-based (Atlas-RCA) and ensemble-based (pairwise Dice) baselines, without registration that can fail silently or access to individual predictions. Our results show that pooling all test cases into one ranking, as prior work does, rewards ordering sites by difficulty, so a detector can rank sites well, miss failures within them, and still look strong. Within-site evaluation measures true per-case failure. The two evaluation schemes reward different behavior, so we recommend reporting both. The code is available at this https URL.

---


### 480. [Skill-Composer: Requirement-Driven Skill Selection from Multiple Marketplaces](https://arxiv.org/abs/2611.30715)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zicheng Chen, Jia Li, Xiaohong Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills have become the primary vehicle through which agents reuse specialized capabilities, yet public skill marketplaces provide skills with individual items: a query, whether matched through keyword or embedding similarity, returns a list of single skills ordered by relevance or by popularity. Such an interface cannot answer the question a developer actually faces: which set of skills should be installed to cover a task's complete requirement? The highest-ranked skills are often functionally redundant, while capabilities that are genuinely required remain uncovered. In this paper, we argue that skill acquisition should be reframed from ranking to set selection. We propose Skill-Composer, an agent-native framework that selects a non-redundant skill bundle for the user requirement, which aims to cover all available required capabilities and report any gaps. Specifically, it clarifies user requirements into atomic requirement points, retrieves and merges candidate skills across fragmented marketplaces, decomposes each candidate's capabilities, and progressively discards overlapping ones, so that each retained skill provides different capabilities. This moves the decision of which skills to acquire from the developer to the agent itself. We position this reframing and sketch its workflow.

---


### 481. [AnchorCredit: Output-Anchored Credit Assignment for Structured Generation with Multiple Verifiable Rewards](https://arxiv.org/abs/2611.30881)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Gen Li, Pengyang Xie, Xiao Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Reinforcement Learning with Verifiable Rewards (RLVR), Group Relative Policy Optimization (GRPO) and related methods typically compute group-relative advantages from response rewards and broadcast the same advantage to every generated token in a response to guide policy updates. However, we identify a systematic problem of cross-component credit misassignment in tasks with multiple verifiable results, such as joint multi-attribute prediction: low rewards for some components can penalize a well-performing component and its associated reasoning. To address this problem, we propose AnchorCredit. The method uses the policy model's attention from output anchors to preceding reasoning sentences to estimate sentence-component associations and assign component-specific advantages to the relevant reasoning, without additional relevance annotations or a separate relevance discriminator. To support the study of credit assignment with multiple verifiable rewards, we construct ProductAttr, a benchmark of 7,200 real product image-text samples. Experiments show that AnchorCredit outperforms existing baselines on this benchmark. Experiments on the public Nutrition5k dataset further support the method's effectiveness in this setting.

---


### 482. [RoFE: Rotated Frozen Embeddings for Low-Data Multimodal Tabular Learning](https://arxiv.org/abs/2611.31049)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yihao Qiao, Jiajian Ma, Wushuang Rui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal tabular learning combines tabular data with images and text, often in settings where labeled data are scarce. Tabular foundation models such as prior-data fitted networks (PFNs) offer a promising solution via in-context learning without task-specific training. However, modern image and text encoders produce embeddings with hundreds or thousands of dimensions, far exceeding the number of features encountered during PFN pretraining. Existing approaches bridge this gap using principal component analysis (PCA) to compress frozen embeddings. Surprisingly, we find that this PCA interface can underperform simple linear classifiers when labeled examples are scarce, even though PFNs are designed for small datasets. We identify the underlying failure mechanism: the PFN's per-column standardization removes the variances of the PCA scores. When the PCA keeps every direction of the labeled examples, the examples collapse into a regular simplex in which all pairwise distances are equal. To address this problem, we propose Rotated Frozen Embeddings (RoFE), a training-free method that rotates PCA scores before PFN inference. We theoretically show that rotation makes the column variances nearly equal, so that standardization approximately preserves the embedding geometry. Across image and text classification tasks, encoders, and tabular foundation models, RoFE improves low-data performance over the PCA interface and outperforms baselines that require task-specific training. The improvements also extend to regression.

---


### 483. [Attention Latent Feedback](https://arxiv.org/abs/2611.31154)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuyuan Xiong, Siyu Chen, Mengzhao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> During autoregressive decoding, the deeper representations of the previous token have already been computed, yet shallow layers at the current token cannot read them directly because standard self-attention connects positions only at the same depth. We introduce Attention Latent Feedback (ALF), an architecture that allows every sublayer to attend to the outputs of the deeper layers at the previous position. Training unrolls this cross-position recurrence into two parallel passes, whereas decoding remains single-pass using cached previous-token states. Across mixture-of-experts models with up to 4.0B parameters, ALF lowers held-out loss by 0.022-0.024 nats over the standard residual with about 1.1% decoding FLOP overhead, and consistently outperforms prior final-state feedback across all three scales on both standard and attention residual backbones. On MoE-1.6B, ALF matches a $1.38\times$ larger baseline token budget, and on MoE-4.0B it lifts average accuracy across seventeen downstream benchmarks from 45.1% to 47.0%. Analysis further reveals that intermediate and nearby deeper layers drive most of this benefit, allowing a fixed nearest-window variant to retain 89%-94% of the gain at linear read cost while learned attention widens its margin with scale.

---


### 484. [When Does Overriding the Majority Vote Help?](https://arxiv.org/abs/2611.31165)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Terry Ma, Aidan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When should additional reasoning or verification replace a majority-vote answer? We call such a replacement an override. We examine two obstacles: the availability of correct alternatives and the reliability of methods that produce or select them. We compare additional reasoning, executed programs, and cross-model reasoning on 150 competition-mathematics questions with three open reasoning models. Starting from a majority vote over 16 responses, we measure how often overrides occur and how many errors they correct or introduce across agreement thresholds. When the vote is incorrect, the correct answer is often absent from the original responses. Additional same-model reasoning rarely overrides, while executed programs correct more errors than they introduce at every evaluated threshold. Cross-model overrides improve some weaker baselines but do not establish an advantage over the more accurate model alone, even with only eight standalone responses. Stricter agreement reduces how often overrides occur but does not consistently increase the fraction that correct errors. At the strictest thresholds, overrides occur on few distinct questions, limiting conclusions about their reliability.

---


### 485. [EEG Decoding in Context: A Framework for Tuning-Free EEG Foundation Models](https://arxiv.org/abs/2611.31171)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hao-Run Cai, Si-Yang Liu, Han-Jia Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) decoding is a central route toward brain-computer interfaces for communication, rehabilitation, cognitive assessment, and neurological monitoring. Recent EEG foundation models have substantially advanced reusable signal representations, but their downstream use still typically requires a task-specific decoder, gradient-based adaptation, and validation-driven model selection. We investigate a complementary foundation-model paradigm based on in-context learning: labeled EEG recordings define the decoding task as context, and new recordings are predicted without updating model parameters. We first pair raw EEG features with a pretrained general-purpose in-context predictor. This direct formulation provides a promising starting point, but its performance remains limited and unstable and does not generalize reliably across EEG paradigms. We find that suitable context construction can address these limitations by improving the effective signal-to-noise ratio and exposing temporal and spatial structure. Building on this insight, we introduce a general framework that combines EEG-specific context construction with a frozen in-context predictor and a metric-based context adaptation mechanism, which matches each downstream task to an appropriate context representation without relying on validation data. Across ten datasets spanning seven EEG decoding paradigms, our method achieves the highest mean BAcc among eleven specialized and fine-tuned EEG baselines, without task-specific parameter updates or validation-based model selection. This framework provides a practical path toward tuning-free EEG foundation models in which adaptation is expressed through context rather than parameter updates.

---


### 486. [On-Policy Codec Distillation for Efficient All-in-One Video Generation](https://arxiv.org/abs/2611.31184)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern visual generative models operate on tokens, and every visual asset they receive, whether an identity, a scribble, a depth map, or a motion video, is tokenized and appended to the input token sequence. Consequently, conditioning quickly dominates the computation cost. Yet most of these tokens carry redundant spatiotemporal information. Our key insight is that identifying what is genuinely new is exactly the problem that classical video codecs have long solved. Thus, we first introduce a codec-based token pruning method that discards redundant tokens. Then, we propose an on-policy self-distillation (OPSD) strategy to train a DiT adapter capable of learning the codec pruning pattern well without quality degradation. Together, they form On-Policy Codec Distillation (CodecOPSD). We scale CodecOPSD to 16 condition modalities on our own video diffusion model, where it prunes 66% of the condition tokens on average with almost no quality drop. Therefore, denoising becomes 2x faster, and the cache memory shrinks by up to 73% in KV cache mode. CodecOPSD also extends to other state-of-the-art pretrained image and video generative models, where its benefit grows further with more conditions, longer frames, and higher resolution.

---


> [!TIP]
> 当前位于：**451-486**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-486**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
