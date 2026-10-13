# 🧠 大模型相关研究 | 2026年10月14日

> 本类共 **230** 篇论文：已确认 **202** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-230**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-230**

---

### 201. [Hide and Seek: HIDE Concepts to SEEK explanations for black box models](https://arxiv.org/abs/2610.13935)

**<font color=#1a73e8>作者：</font>** Bhanu Tokas, Rahul Nair, Rockwell Jackson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that does not require access to model weights or labeled concept datasets. HnS can interpret a wide range of vision models. Given a concept and image set, HnS retrieves concept-aligned images using a vision-language model, localizes the concept within each image, masks the localized region, and measures attribution from the change in the black-box model's output between the original and masked images. This enables faithful attribution by directly measuring the model's behavior and supporting local attributions. We validated HnS on CelebA and COCO-Stuff. Compared to existing methods, HnS showed better agreement with ground-truth attributions. We demonstrated the applicability of HnS on diverse tasks, including image captioning and satellite image segmentation, where no existing concept attribution method can be used. We provided our anonymous code in the supplementary material.

---


### 202. [Can Language Models Play the Wikipedia Game?](https://arxiv.org/abs/2610.13948)

**<font color=#1a73e8>作者：</font>** Alexander Hickey, Joanna Knight, James Bishop  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models increasingly support or automate information retrieval from document collections too large to index. This task is difficult when it requires specialist linguistic or scientific knowledge. We used the Wikipedia Game to test language models on an analogous information retrieval task. In the game, players must reach a target article using only article links. We compared sentence embedding models and LLMs across five Wikipedia languages and five academic-literature datasets. We construct very large local graphs of Wikipedia pages and of paper citations using OpenAlex and provide code to build and navigate them. This allows the study of language models' navigation capabilities without relying on third-party APIs. We compared the models with human and TF-IDF benchmarks. The Wikipedia Game format enables robust comparisons across techniques, languages, and domains. No model significantly outperformed humans, although the best models (GPT-o3 mini, GPT-4o, QwQ:32B, and DeepSeek-R1:70B) achieved comparable success. Performance and rankings varied across languages and topics, with implications for practitioners utilising these techniques.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 203. [An Exploration of Attacks on AI Agent Systems](https://arxiv.org/abs/2610.12524)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Cathleen Qiao, Layah Vigneaud, Chloe Brandon 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As autonomous AI agents become more integrated into sensitive domains, it is crucial that single and multi-agent AI systems are secured. This paper investigates how prompt injection attacks can exploit both direct user inputs and inter?agent communication to leak sensitive information and trigger cross-agent infections. While our tests mostly highlight key vulnerabilities in single-agent systems, we also extend these attacks to multi-agent frameworks, investigating how weaknesses can propagate across agents. Our findings emphasize the need for more robust defenses as AI agents become more commonly embedded in real-world workflows.

---


### 204. [Market Impact Estimation via Causal Foundation Models](https://arxiv.org/abs/2610.12537)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dennis Thumm, Ying Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a trader executes a large order, the relevant question is not \emph{what will the price be?} but \emph{what would the price have been had I not traded?} Market impact is thus a causal quantity, yet classical models (Almgren--Chriss, propagators) regress price on flow, which is biased whenever informed flow moves prices through information as well as trading. We present a proof-of-concept \emph{Causal Market Simulator}: a continuous-time causal prior-data fitted network (PFN) trained on a synthetic market prior in which a hidden informational flow confounds the flow--price relation by construction, with confounding strength an exact per-episode knob. On this prior, the naive estimator's bias follows a closed form we confirm empirically (up to 68\% overestimation), while the PFN tracks the unbiased true-parameter oracle at high confounding. Its \emph{do-ablated twin}, the same model with the intervention inputs removed, collapses onto the pre-window mean. Zero-shot, the model responds at the ground-truth scale to metaorders in an ABIDES limit-order book ($+0.38$ pre-onset standard deviations against seed-replay counterfactuals), and its intervention response replicates on about 2,300 detected flow bursts in BTC/ETH/SOL perpetuals and 3,800 on Nasdaq equities, evidence consistent with, though not proof of, causal transfer. Off-prior the response degrades gracefully, and split-conformal recalibration repairs interval calibration. Transfer hinges on encoding the metaorder as added flow rather than a clamped price level, not on more training. A recurrent state-space variant closes the remaining shape gap: its impact accrues over execution duration where the transformer's stays flat, raising the correlation with measured metaorder impact from $+0.68$ to between $+0.92$ and $+0.96$, at the cost of weaker on-prior deconfounding that traces to the training recipe rather than to recurrence.

---


### 205. [DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models](https://arxiv.org/abs/2610.12572)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhenglin Wan, Jiayu Chen, Zhengfeiyang Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assignment, while forward-process methods such as DiffusionNFT are efficient yet unstable without carefully tuned exponential-moving-average (EMA) off-policy training. We show that NFT-style objectives contain a hidden forward--reverse consistency force that joint positive--negative training cancels only partially, and that EMA stabilizes training through restoration rather than off-policy rollouts. We introduce DiffusionART (Diffusion Reinforcement with Aggregation-First Reward Tilting), which aggregates each prompt's rewards into a shared reward-improving direction for reverse-process states, removing the consistency force by construction, and adds a trust-region-masked second update for drift-adaptive restoration without EMA tuning. It requires no differentiable reward model, remains effective with fewer samples per prompt, and supports pairwise reward models (DiffusionART-Pairwise). Across image and video generation, DiffusionART trains efficiently and stably without per-task tuning. In particular, on HunyuanVideo-13B with equally weighted visual and motion quality rewards, DiffusionART reaches the late-stage mean reward levels of DiffusionNFT and Flow-GRPO-Fast with 12.02 and 11.72 times fewer GPU hours, respectively, while achieving 28.8% and 53.0% higher mean training rewards.

---


### 206. [Scaling Multi-Teacher Distillation for Digital Pathology](https://arxiv.org/abs/2610.12574)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sofiène Boutaj, Pierre Marza, Varun Belagali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-teacher distillation allows transferring knowledge from multiple "teacher" networks to a single "student" network. This method is promising in fields such as digital pathology, where many powerful foundation models were proposed recently. However, as we show in this paper, the standard multi-teacher distillation approach reacts poorly to an increase in the number of teachers used to train a student encoder. We demonstrate that learning teacher-specific representations is a key to scaling in MTD. Importantly, different design choices, such as learnable teacher tokens, a tailored attention scheme, additional mixture-of-experts layers and a contrastive loss, are proposed to better learn such teacher-specific representations. We show that our method better scales with respect to the number of considered teachers, allowing us to train compact student encoders, up to 10x more efficient than larger teacher foundation models, while matching their performance and even outperforming them on a large set of tile-level and slide-level tasks. We conduct a thorough empirical validation, evaluating more than 10 foundation models on 39 tasks spanning tile and slide levels. As a result, we release a new collection of strong and efficient foundation models, named OMNI, trained from the knowledge of 10 state-of-the-art foundation models. We finally conduct an analysis of the learned teacher-specific representations, highlighting their complementarity and explaining why they can be easily aggregated at downstream time.

---


### 207. [Machine Learning and Time-Series Foundation Models for Day-Ahead Electricity Forecasting in a University Building](https://arxiv.org/abs/2610.12638)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Amey Vasulkar, Samuel Kernan Freire, Arie-Willem de Leeuw 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Day-ahead electricity forecasts can help building operators schedule heating, ventilation, and other services around anticipated demand. Choosing a forecasting model also requires balancing accuracy with its forecast-time inputs, local training, and computational requirements.
We benchmark statistical, machine-learning, recurrent neural-network, and pretrained TimesFM models for a university building. We use chronological validation and evaluate all configurations on the same 57 test days, comparing accuracy across workdays, weekends, and holidays alongside local fitting and forecasting time. Weather covariates use retrospective observations.
TimesFM 3.0 with covariates achieves the lowest overall errors, reducing mean absolute error by approximately 43\% relative to weekly seasonal-naive forecasting. XGBoost remains competitive, although paired daily comparisons do not establish a clear mean-absolute-error advantage for TimesFM. TimesFM also performs strongly using only past electricity consumption. Adding covariates improves its holiday forecasts but slightly worsens workday and weekend forecasts, leaving overall mean absolute error almost unchanged. TimesFM requires no building-specific weight training, while XGBoost offers rapid local fitting and inference. The evaluated LSTM takes longer to fit without outperforming either approach.
An exploratory historical evaluation reveals seasonal variation, while a separate weather-source comparison produces only small changes in the selected TimesFM configuration's accuracy. These results support pretrained TimesFM as a strong initial forecasting baseline for this building, with XGBoost as a competitive locally fitted alternative. Covariates are particularly useful when improved holiday forecasts justify the additional input preparation.

---


### 208. [Cancerous Backdoor Attack: Gradual Activation via Invisible Tokens and A Stage Controller](https://arxiv.org/abs/2610.12644)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tahmid Imtiaz Imu, Emama Nahid, Prodipta Sen Amartya 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor Attacks on Large Language Models (LLMs) typically follow a trigger-response pattern, where satisfying a trigger condition activates a single terminal behavior. However, this single-point backdoor activation does not explore attacks in which malicious behavior develops gradually through multiple intermediate stages before reaching the terminal activation stage. We present Cancerous Backdoor Attack, that gradually corrupts an LLM's reasoning over a sequence of interactions by leveraging invisible tokens and a stage controller. Specifically, invisible tokens provide hidden stages to the model without appearing in the user's visible request and the stage controller tracks the attack's progression during inference to realize gradual activation. We evaluate Cancerous Backdoor Attack across several reasoning datasets. The attack consistently produces gradual reasoning corruption across models and tasks. We compare Cancerous Backdoor Attack with prior backdoor attack baselines to demonstrate our proposed attack outperforms the baselines. Our results indicate that reasoning corruption can develop gradually before it becomes visible, making answer accuracy alone insufficient for detecting backdoor attacks.

---


### 209. [Kronecker Product Attention: Memory-Efficient KV Compression via Structured Factorization](https://arxiv.org/abs/2610.12657)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bahareh Nikpour, Hossein Rajabzadeh, Maryam Dialameh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient autoregressive generation is increasingly limited by the memory footprint of the key-value (KV) cache, which grows linearly with sequence length, batch size, and model depth. Existing approaches such as Multi-Query Attention (MQA), Grouped-Query Attention (GQA), Multi-Head Latent Attention (MLA), and Tensor Product Attention (TPA) reduce this cost through different trade-offs, but often sacrifice expressivity, require additional positional-encoding machinery, or impose restrictive low-rank structure. We propose Kronecker Product Attention (KPA), which represents key and value activations as sums of Kronecker products of compact, token-dependent matrix factors. KPA strictly generalizes TPA: rank-one vector-outer-product factorization arises as a degenerate Kronecker split, while non-degenerate matrix factors can represent richer block-structured patterns. We further show that a structured rotary embedding operator matched to the Kronecker representation preserves the relative-position property of RoPE while rotating only the compact factors, removing the need for a decoupled RoPE branch as in MLA. Empirically, KPA matches or exceeds TPA, MHA, MQA, GQA, and MLA across four model scales and nine downstream benchmarks under identical training conditions, while achieving up to 10x KV cache compression. The Kronecker head split is a tuneable hyperparameter that allows practitioners to navigate the compression-accuracy trade-off at design time without architectural changes.

---


### 210. [Zebra3D: Efficient Hybrid Foundation Models For Scalable 3D Reconstruction](https://arxiv.org/abs/2610.12727)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Utkarsh Saxena, Ruijing Yang, Mehdi Rezagholizadeh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D foundation models reconstruct scenes from unposed images, but the quadratic cost of global attention limits their scalability to large view sets. We present Zebra3D, a layerwise sparse-linear hybrid attention framework that improves the efficiency of pretrained 3D foundation models without training from scratch. Across VGGT, HunyuanWorld-Mirror, and $\pi^3$, we observe a broadly consistent depth-wise pattern: early stages are relatively tolerant to linear replacement, while sensitive middle-to-late stages tend to exhibit more concentrated attention. Zebra3D exploits this structure by assigning linear-centered attention to tolerant stages and tile-sparse attention to sensitive stages, using landmark summaries to preserve unselected context. Closed-form affine fitting enables training-free conversion, while optional post-conversion training combines task supervision with output and relational feature distillation. Across all three backbones, Zebra3D achieves strong reconstruction and camera-pose accuracy at high attention sparsity, with training-free variants remaining close to their dense counterparts. End-to-end speedups increase with input view count, reaching up to $7.1\times$ at 1,024 views. After post-conversion training, Zebra3D-VGGT reaches 80.5\% RealEstate10K AUC@30 at 94\% mean attention sparsity, within 1.1 percentage points of dense VGGT fine-tuned on the same data and schedule.

---


### 211. [Neural expectation-maximization and meta-models](https://arxiv.org/abs/2610.12741)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhuolin Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We interpret Transformer networks as learned approximations to a hybrid probabilistic-inference procedure that combines max-product Loopy Belief Propagation (LBP) with Expectation--Maximization (EM). In this view, a Transformer performs inference in partially observed Markov Random Fields (MRFs) whose structure and parameters are not given a priori but are inferred from data. We show that self-attention implements a differentiable approximation to max-product LBP on an input-conditioned, dynamically structured MRF, with attention weights encoding learned structural affinities. We further establish an EM correspondence at the level of depth: each layer updates latent representations in an E-step-like forward pass, while the transition $\theta^{(l)} \to \theta^{(l+1)}$ across layers acts as an implicit M-step. Building on this interpretation, we introduce \emph{meta-models}, a design paradigm in which inputs generate instance-specific parameters, unifying mechanisms such as self-attention, mixture-of-experts, and gated units within a single framework. Empirical results support the proposed perspective.

---


### 212. [HART: Hybrid Attention-RWKV Time series Foundation Model](https://arxiv.org/abs/2610.12883)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qingwen Lin, Boyan Xu, Shifeng Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-autoregressive multi-step forecasting (NAF) enables time series foundation models to predict an entire future horizon in a single forward pass. Despite its strong sequence modeling capabilities, RWKV-7 exhibits long-horizon degradation in our NAF experiments. In this setup, future patches are represented as missing inputs, requiring the recurrent state to evolve across the prediction horizon without new observations. Our analysis of RWKV-7's generalized delta rule suggests a mechanism we term Placeholder Idling Decay (PID): repeated state transitions can attenuate historical information when placeholder-driven writes provide insufficient compensation. Layer-wise analysis reveals reduced state-injection norms in most layers, while transition-matrix norms remain similar between historical and prediction regions, consistent with PID. Motivated by this analysis, we propose HART, a Hybrid Attention-RWKV Time-series Foundation Model that alternates attention and RWKV blocks, combining direct access to historical tokens with recurrent temporal modeling. Controlled experiments on GIFT-Eval and TIME-Benchmark show that HART improves over pure RWKV at medium and long horizons while maintaining comparable short-horizon performance, and achieves better aggregate performance than a comparably sized pure Transformer. With 36M parameters, HART achieves long-horizon MASE comparable to Toto-2.0-1B on GIFT-Eval (0.752 vs. 0.754), using approximately 1/28 of its parameters.

---


### 213. [GIST: Generator-state-Informed Supervision for Tabular Foundation Models](https://arxiv.org/abs/2610.12904)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhangyang Peng, Jingze Shi, Tongyi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) based on prior-data fitted networks typically use sampled hard query labels, leaving avoidable sampling variability in pretraining. A key observation is that intermediate generator states can reveal label uncertainty beyond a sampled outcome. We propose Generator-state-Informed Supervision for TFMs (GIST), which uses these states to average query losses over conditional label distributions. GIST jointly designs task generation and query supervision, using entropy-calibrated encodings to obtain tractable, input-consistent targets on supported label-dependent branches. We show that this averaging preserves the population objective and yields no larger gradient covariance at fixed parameters within each generating distribution. Under matched pretraining schedules, GIST improves mean rank across three architectures on both TabArena and TALENT without changing architecture or inference. Across these benchmarks and architectures, GIST wins 62.1% of paired dataset-level comparisons against the corresponding hard-label controls.

---


### 214. [SEEDS: Preview-Guided Evidence Admission for Search Agents](https://arxiv.org/abs/2610.12932)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiajin Liu, Chenxi Xu, Dongzhe Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search agents extend large reasoning models with multi-round access to external knowledge, yet most existing systems largely conflate retrieving evidence with consuming it. Retrieved documents are commonly incorporated according to fixed or rank-based policies, despite the fact that evidence utility is conditioned on the agent's current reasoning state. Consequently, a lower-ranked candidate may be critical for the current step, while a higher-ranked candidate may provide redundant, irrelevant, or misleading information. We formulate this overlooked problem as evidence admission, which asks, at each search step, which retrieved candidates should be allowed to enter the agent's evolving reasoning context. To enable such selective control, we introduce SEEDS (Selective Evidence Entry During Search), a preview-guided evidence admission framework for search agents. SEEDS first exposes lightweight previews of retrieved candidates and then lets the agent jointly determine which candidates and how many should be fully inspected, conditioned on its current reasoning state. Unlike fixed or adaptive prefix policies, SEEDS can select arbitrary subsets with flexible cardinality, and it can be instantiated directly with an existing reasoning agent or further optimized through learning. Across nine knowledge-intensive QA benchmarks under both local corpus and live web search, SEEDS consistently improves search effectiveness while substantially reducing full-evidence consumption. Experimental analyses show that SEEDS more effectively selects useful candidates beyond the corresponding retrieval prefix. These results establish evidence admission as a complementary dimension of agentic search, separating what information is retrieved from what information is ultimately allowed to shape reasoning.

---


### 215. [MotionCoach: Constructing Multimodal Guidance for Video Professional Motion Editing](https://arxiv.org/abs/2610.12963)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Siyi Qian, Hanqing Yang, Weihuang Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video editing models achieve strong performance in modifying appearance, backgrounds, styles, and motions, empowered by large-scale training data. Beyond general scenarios, professional motions are significant in performance, sports, and martial arts. This paper focuses on professional motion editing, which involves fine-grained motion technique and temporal structure. Given professional motion names but lacking detailed descriptions, existing models often fail to generate professional motions, such as incorrectly lifting the front wheel under a Stoppie instruction. To address this challenge, we introduce MotionCoach, a trained multimodal agent that uses multi-turn tools and performs self-verification, producing a grounded prompt and a reference clip as reliable and sufficient multimodal guidance to inject external professional motion knowledge into video editing models. To supply training data, we build a data pipeline to construct trajectories. We cold-start the agent on MotionCoach-SFT-10k and apply Group Relative Policy Optimization (GRPO) on MotionCoach-RL-2k with rewards on the motion guidance prompt, the motion outcome video, and the format. For evaluation, we introduce VPMEBench, comprising 314 professional motion editing tasks with fine-grained references and annotations. Extensive experiments show that MotionCoach improves the overall score from 55.1 to 65.6 on Seedance 2.0 and from 51.2 to 64.5 on MiniMax-H3. Learning to construct multimodal guidance enables precise professional motion editing without retraining video editing models.

---


### 216. [Dataset-Specific Encoding of Image Content Underlies Cross-Dataset Failure in Brain MRI Foundation Models](https://arxiv.org/abs/2610.13027)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Minh Sao Khue Luu, Bair N. Tuchinov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen features of brain MRI foundation models lose accuracy on new datasets, a failure usually blamed on the features encoding where each scan came from. We show that the failure lies elsewhere. Across 17 public datasets and eight frozen representations, every representation recognizes the MRI sequence within each dataset, yet most fail on an unseen one. The cause is neither dataset encoding nor a shift of each dataset: the content itself is encoded along different directions in each dataset. This explains which datasets fail, for the sequence and for sex, and why removing the dataset signal with INLP, LEACE, CORAL or adversarial training never improves sequence transfer. Only the broadly pretrained 3DINO and SAM-Med3D encode the sequence consistently enough to transfer; the brain-specific BrainIAC and BrainFM do no better than an untrained network. Code is available at this https URL.

---


### 217. [Scaling RNA Foundation Models through Iterative Refinement](https://arxiv.org/abs/2610.13106)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Pengan Chen, Liang Hong, Xinyuan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological function in RNA is encoded across scales, from local sequence motifs to long-range structural dependencies. Conventional RNA foundation models couple parameter capacity and inference depth within a fixed architecture, prescribing a fixed computation graph for each inference. Here we present Eco-RNA, an 80M-parameter RNA foundation model that makes inference depth adjustable through learned iterative refinement. Its shared, input-conditioned Transformer core refines sequence representations through repeated application. The iteration count is selected after training and controls effective depth at fixed model parameters. We train across recurrent depths with masked reconstruction, state regularization, and a one-sided loss that anchors deeper reconstruction to a shallow reference. On the 70-assay RNAGym fitness benchmark, increasing refinement from one to four iterations raises aggregate absolute Spearman correlation from 0.242 to 0.286, with the gain retained through eight iterations. At four iterations, Eco-RNA surpasses the current SOTA Evo 2 40B on all three aggregate fitness metrics despite 500x fewer parameters. Its iteration configurations advance the compute-performance Pareto frontier among the evaluated models. It also outperforms the evaluated baselines in non-coding RNA family classification, RNA secondary-structure prediction, and chemical probing profile prediction. These results establish internal inference computation as an effective scaling dimension for RNA foundation models.

---


### 218. [Continually Post-training Small Models via Synthetic Self-distillation](https://arxiv.org/abs/2610.13113)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Woosung Koh, Hyunsoo Lee, Kyungjae Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual post-training faces a dual challenge of acquisition and retention: models must learn new capabilities while preserving prior knowledge. While Self-Distillation Fine-Tuning (SDFT) mitigates this using self-supervision with in-context demonstrations, it relies on strong in-context learning and instruction-following abilities. Consequently, SDFT fails on smaller models critical for low-latency, on-device use. To enable continual learning at smaller scales, we first identify the root cause of failure. We show that poor acquisition and forgetting correlate linearly with the post-trained model's distribution shift, revealing the necessity of in-distribution learning. We thus introduce Synthetic Self-Distillation (SynthSelf), imitating SDFT's in-distribution rewrite by outsourcing the task to a minimally larger, same-family aligner. Coupled with off-policy supervision and rejection sampling, this provides the high-quality supervision small models require without breaking their original distribution. Evaluations spanning 4 acquisition datasets (including a mixture) and 14 retention benchmarks show SynthSelf consistently outperforms 6 methods (including off- and on-policy distillation) across 3 small model scales. Extensive further analyses confirm SynthSelf paves the way toward effective small-model continual learning.

---


### 219. [How Much Computation Does Every Forecast Need? Structured Block Skipping in Two Time-Series Foundation Models](https://arxiv.org/abs/2610.13208)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Max Bourgeat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models use the same network depth for every input, although forecasting windows differ in structure and difficulty. We test whether whole Transformer blocks can be removed at inference time in two pretrained models: Chronos-Bolt and TimesFM 2.5. Our bypasses avoid the original block computation and preserve the dense model exactly when all blocks are enabled. Masks are selected only on calibration windows and evaluated on 1,088 held-out windows from ETTh1, Traffic, Weather, and Exchange. At moderate sparsity, Chronos-Bolt with 7/11 candidate blocks and TimesFM with 16/20 blocks show little change in mean relative forecasting quality across datasets while reducing median A100 batch-1 latency by 11.2% and 13.4%. More aggressive TimesFM skipping accelerates inference further but substantially harms Traffic and Weather. Across both models, different equal-budget masks win on different windows, and a retrospective oracle significantly improves over the best static mask on every dataset. However, dataset-specific masks transfer inconsistently, and Chronos representations do not support reliable unseen-domain routing. These results establish cross-architecture structured redundancy and input-dependent opportunity, but not a deployable dynamic inference method.

---


### 220. [Tabular Foundation Models Are Effectively Shallow](https://arxiv.org/abs/2610.13253)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Irene Cannistraci, Julia E. Vogt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context-learning Tabular Foundation Models (TFMs) are uniquely suited to scenarios with limited resources or privacy constraints, as they solve new tasks without additional training. However, their architecture consists of multiple transformer blocks, resulting in high computational and memory footprints. Meanwhile, traditional alternatives like Gradient-Boosted Decision Trees (GBDTs) remain highly competitive and run efficiently on CPUs, suggesting that tabular tasks may not inherently require deep architectures. This contrast raises a fundamental question: can TFMs be simplified by removing architectural redundancies without sacrificing performance? To answer this, we introduce a closed-form, label-free affine translator that replaces a contiguous window of up to 96% of the blocks, leaving the rest unchanged. Evaluating eight frontier TFMs on 171 classification datasets, we reveal that tabular transformers are vastly overparameterized: replacing half of a model's blocks costs at most $0.002$ median AUROC across all architectures, with the half-depth TabFM still outperforming every other full-depth TFMs and tuned GBDTs. Furthermore, different model families are overparameterized in different ways: TabPFN-3 relies on its encoders, maintaining performance regardless of which single block is retained. Other single-axis models spread computation thinly, needing only their first block, while dual-axis models concentrate it in one critical block. Ultimately, removing depth saves up to 1.5B parameters, speeds up GPU inference by up to $6\times$ at a median cost of $0.03$ AUROC, while a single-block TabPFN-3 serves cached queries $2.4\times$ faster using $6\times$ less memory at negligible cost.

---


### 221. [PPG-Bench: A Unified Benchmark for PPG Foundation Models](https://arxiv.org/abs/2610.13435)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Arvasu Kulkarni, Mahir Jain, Aditya Ray Mishra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG) is increasingly recorded by wearable and clinical devices at enormous scale, and a growing number of PPG foundation models (FMs) have been developed to compute reusable representations for various downstream tasks. These models are difficult to compare: different evaluations use different datasets, task definitions, preprocessing, downstream heads, hyperparameter tuning, and baselines. We present PPG-Bench, a unifying open-source benchmark evaluating five public PPG FMs across nine open-access datasets and 26 tasks spanning cardiovascular state estimation, activity, sleep, screening, and identification. We evaluate models under four downstream regimes of increasing adaptability (linear probing, random forests, frozen MLP probes, and end-to-end finetuning), with model-specific hyperparameter optimization and subject-disjoint cross-validation. We also evaluate against three controls: random/constant baseline, a deterministic pulse-rate-variability (PRV) feature set, and a generic time-series FM (MOMENT). Across all 68 task-regime combinations, 35.3% show no meaningful FM advantage over the random/constant baseline, and in 83.8% no PPG-specific FM outperforms both PRV and MOMENT. We also find that added downstream head capacity generally improves performance, but can cause significant degradation if the model is performing at chance/constant level. Current PPG FMs therefore cannot yet claim to provide generalised and transferrable representations of PPG signals, and future evaluation in this field should include checks against simple, non-learned controls. Code for the benchmark and instructions to evaluate more models can be found here - this https URL.

---


### 222. [Multi-Stream Attention Residuals](https://arxiv.org/abs/2610.13630)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaohan Qin, Xiangdong Zhang, Tuo Dai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attention Residuals (AttnRes) enables content-dependent retrieval over network depth, which can be viewed as single-stream softmax attention along the depth axis. Inspired by the success of multi-head attention along the sequence axis, we introduce Multi-Stream Attention Residuals (MSAR), an extension of AttnRes that generalizes this mechanism to multi-head depth attention, yielding substantial performance gains with minimal additional overhead. MSAR draws stream diversity from sequence context through multi-scale causal convolutions, allowing different heads to retrieve historical representations through distinct contextual views while preserving the integrity of the hidden representation. The retrieved streams are combined through lightweight adaptive mixing to generate the single-stream layer input. By retaining single-stream sources and expanding them on demand, MSAR supports multi-stream computation without requiring persistent multi-stream storage or communication. Across all 12 downstream benchmarks at the 18B and 28B MoE scales, MSAR consistently outperforms prior residual variants, including standard residual connections, manifold-constrained Hyper-Connections (mHC), and AttnRes. Scaling-law experiments yield an iso-loss compute speedup of $1.58\times$ over the standard residual baseline, compared with $1.35\times$ for AttnRes and $1.30\times$ for mHC. These results make MSAR a promising residual architecture for large-scale pre-training.

---


### 223. [TabReliBench: Evaluating Tabular Foundation Models Beyond Predictive Accuracy](https://arxiv.org/abs/2610.13654)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianqi Zhao, Jia Guo, Yan Shuo Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) are increasingly popular for their strong predictive performance. Many also provide posterior predictive distributions (PPDs), whose reliability remains less studied. We assess reliability through point prediction, distributional quality, marginal and subgroup calibration, and interval efficiency. We then introduce TabReliBench, a large classification and regression benchmark for these comparisons and dataset-level analyses. We find that TFMs' rankings change between TabArena and our benchmark and across reliability metrics. Regression TFMs usually achieve near-nominal marginal coverage and retain narrow intervals, but this favorable marginal behavior does not imply valid conditional coverage. Dataset-level analyses show that classification difficulty often accompanies poor calibration, whereas regression predictive performance is not a reliable indicator of calibration. Ensembling improves predictive performance but does not consistently improve calibration of PPDs; TFMs also benefit little from conformal post-processing, which does not reliably resolve subgroup gaps. Reliable TFM selection therefore requires multidimensional evaluation beyond aggregate rankings. Code is available at this https URL.

---


### 224. [On the Encoding of Calendar Features in Covariate-Informed Time Series Foundation Models](https://arxiv.org/abs/2610.13676)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alexander Kreusel, Maximilian Beichter, Alexandra Nikoltchovska 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) increasingly offer covariate support, with calendar information being the most common type of categorical covariate in practice, as it is available for every point in time. However, how these features are encoded is largely treated as an implementation detail rather than as an object of study, despite encoding being one of the few design choices left for pretrained models at inference time. With the present study, we demonstrate that the way information is propagated into the model substantially affects forecast accuracy of TSFMs. Therefore, we systematically compare seven calendar encodings, including three conventional target-agnostic representations (ordinal, one-hot, and cyclic) and four target encodings, across four state-of-the-art TSFMs on nine datasets from multiple domains in a zero-shot rolling evaluation. The nine datasets are influenced by social activities, such as weekends and holidays, making calendar information particularly relevant for forecasting. We find that encoding choice affects forecast accuracy across all models, with MASE differences of up to 9.9 % on non-holidays and 83 % on holidays within a single model. Effectiveness and utilization vary substantially across models. Improvements are concentrated around holidays, where calendar information provides signals unavailable from target history, while some model encoding combinations also improve non-holiday forecasts. A SHAP-based attribution analysis locates the contribution of the covariates relative to the autoregressive component and explains why some model-encoding combinations degrade performance. Our findings suggest that current benchmarks for covariate-informed TSFMs can distort model comparisons by imposing fixed encoding strategies.

---


### 225. [Transformer-based In-Context Score Operator Learning for Diffusion Models](https://arxiv.org/abs/2610.13690)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wuzhe Xu, Zhaiming Shen, Yulong Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models typically learn the generative dynamics of a single target distribution or a family of distributions indexed by conditioning variables fixed during training. This limits their ability to adapt to a previously unseen distribution from only a small set of examples. We introduce an in-context solution operator learning framework for diffusion models, in which each target distribution is treated as a task drawn from a meta-distribution and is specified at inference time by an empirical context set. Our method learns an in-context score operator that maps the context samples, a noisy query point, and the diffusion time to the task-dependent score, enabling reverse-diffusion sampling on unseen tasks without retraining or parameter updates. A key observation is that the task-dependent score admits a Gaussian-kernel conditional-mean representation. Its empirical Nadaraya--Watson approximation can be represented exactly by a model in our constructed transformer class, providing a principled foundation for the proposed query-dependent attention architecture. The operator is trained through amortized denoising score matching across task distributions. We establish generalization-error bounds that quantify the effects of the context size, the numbers of training tasks and within-task samples, model complexity, and intrinsic and ambient dimensions. Numerically, we evaluate the method on a range of scientific and visual datasets, including Navier-Stokes, ERA5 climate data, QuickDraw sketches, and Food-101. The results show that the proposed method performs well on relatively simple task families, while its performance degrades as task complexity increases, thereby illustrating both the promise and the limitations of in-context learning for diffusion models.

---


### 226. [A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning](https://arxiv.org/abs/2610.13744)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mayug Maniparambil, Ayush Rai, Ekansh Verma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation promises to replace the sparse outcome signal of verifiable-reward RL with dense token-level credit: a teacher conditioned on the reference solution scores the student's own rollout, and the resulting distributional shift is distilled back into the policy. We investigate whether this scoring signal actually contains corrective credit. Using gold error spans in student rollouts, we test the two signals consumed by self-distillation objectives, the full-distribution KL and the token log-ratio, for two properties: whether they localize errors and whether they push probability away from erroneous student tokens. They exhibit neither of these properties nor can they reliably distinguish correct from incorrect rollouts within the same problem. We argue that this failure is structural: locating an error in a reasoning trace is itself a search problem, while a scoring teacher is never explicitly asked to perform that search. The same model, with the same privileged information, localizes errors substantially better when allowed to generate a critique. This forms the motivation for \emph{critique-conditioned self-distillation}: first generate a critique of the current rollout, then condition the scoring teacher on that critique. The resulting signal localizes errors, is corrective within error spans, and shifts probability toward tokens that initiate backtracking such as ``Wait'', ``But'', and ``Actually''. We further show that the critique is useful both at test time, where resuming a wrong rollout with the critique in context converts math problems the model cannot solve by sampling, and in cold-start GRPO, where it provides an advantage signal on prompts for which verifiable rewards alone provide none.

---


### 227. [Shortcut Learning in Geospatial Foundation Model Embeddings for Cross-Disaster Damage Assessment](https://arxiv.org/abs/2610.13766)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ali Shibli, Andrea Nascetti, Yifang Ban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models can support disaster damage assessment, but high accuracy on familiar disasters may hide shortcut learning: prediction from event or scene characteristics rather than evidence that transfers to a new disaster. We study embeddings from TerraMind, Prithvi-EO-2.0, DOFA, and DINOv3 on the multi-disaster datasets xView2 and BRIGHT. Holding out an entire disaster, instead of randomly splitting image tiles, reduces mean balanced accuracy from 0.807 to 0.638 on xView2 and from 0.818 to 0.568 on BRIGHT. Four sets of tests examine what information supports prediction: event and acquisition context, before/after image inputs, building count, and correct image pairing. Pre-event images remain predictive, and a classifier given only the annotated number of buildings reaches balanced accuracy of 0.629 and 0.653. Combining before/after features performs best on average on xView2, but does not improve over pre-only features on BRIGHT. Shuffling image pairs within the same disaster and damage class causes modest losses. Motivated by these findings, we test whether feature transformations learned only from training disasters improve generalization to unseen disasters. These transformations improve performance, with supervised contrastive learning performing best on xView2 and PCA on BRIGHT. Our results highlight the importance of evaluation on unseen domains for assessing model robustness and show that simple feature-level transformations can improve generalization. Code and experiments can be found at this https URL.

---


### 228. [SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models](https://arxiv.org/abs/2610.13781)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Changhui Jing, Haochen Tian, Hongchen Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving world action models (WAMs) learn from paired trajectories and future observations. Post-training with reinforcement learning allows the policy to explore alternative trajectories and improve planning using driving rewards. However, driving logs contain future videos only for the recorded trajectories, leaving these alternatives without corresponding visual supervision. Thus, we introduce SimVTA, a simulation-grounded post-training framework that combines trajectory optimization with video supervision. First, we sample candidate trajectories for each observation and use a real-world simulator (e.g., World Engine) to render future videos for high-reward candidates in real-world scenes reconstructed with 3D Gaussian Splatting (3DGS). This provides trajectory-matched supervision independent of the model's own predictions. Under a limited rendering budget, we prioritize video supervision for higher-error futures among these rendered candidates. Finally, we optimize trajectory planning with Group Relative Policy Optimization (GRPO) and use a flow-matching loss on the matched videos to update shared representations. At inference time, the model predicts trajectories directly, without simulator calls. On NAVSIM v1, applying SimVTA to a WAM initialization improves PDMS from 86.2 to 91.3 (+5.1). It achieves 88.2 EPDMS on NAVSIM v2 and an average HD-Score of 38.8 in closed-loop evaluation on HUGSIM. Ablations show that updating shared representations with video supervision improves planning, while prioritizing higher-error futures among high-reward trajectories further improves performance.

---


### 229. [TabMF: Learning Dataset Representations with Tabular Foundation Models](https://arxiv.org/abs/2610.13818)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rafiq Kamel, Nicolas Atienza, Aziz Fouché 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representations of supervised datasets support higher-level machine-learning tasks such as dataset retrieval and distribution-shift monitoring. However, existing approaches typically rely either on hand-crafted meta-features or on dataset encoders trained specifically for representation learning. We introduce TabMF, a framework that repurposes pretrained tabular foundation models (TFMs) as encoders of supervised datasets. TabMF equips a predictive TFM with an architecture-aware dataset-level readout and adapts the model end-to-end using contrastive post-training on stochastic views of synthetic supervised datasets. We instantiate TabMF on TabICLv2 and TabPFN-2.5 and evaluate the resulting representations across six tasks on unseen real datasets. Simple frozen TFM readouts yield competitive representations, indicating that predictive pretraining already induces substantial dataset-level structure. The two TabMF encoders obtain the strongest aggregate performance among the evaluated learned and classical dataset representations, with particularly strong results in dataset retrieval, compact benchmark construction, and distribution-shift severity assessment.

---


### 230. [InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators](https://arxiv.org/abs/2610.13944)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuanlang Dai, Jiazi Bu, Yujie Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion/flow models have emerged as the de facto paradigms for image generation, giving rise to a diverse family of modern generators with increasingly heterogeneous architectures and representations. Despite their remarkable generation capabilities, the cross-model alignment of latent representations and the consistency of their underlying denoising dynamics remain underexplored. In this work, we uncover an intriguing cross-model compatibility: independently trained generators exhibit similar latent spatial organization, while directly handing off intermediate states between unaligned models can still preserve coarse visual content. Motivated by these observations, we propose InstantFusion, a lightweight shared latent interface that connects the denoising trajectories of heterogeneous image generators. Specifically, to enable flexible cross-model state translation, model-specific Latent AutoEncoders (LAEs) are introduced to project intermediate states from different generators into a shared latent space and decode them into the latent space of a target generator. This shared space is constrained by two complementary objectives: aligning intermediate states derived from the same image at matched noise levels and synchronizing their corresponding local denoising velocities. Once trained, InstantFusion allows denoising to seamlessly transition across frozen generators without requiring a dedicated mapping for every model pair. The versatility of InstantFusion is demonstrated across acceleration, multi-preference composition, cross-architecture on-policy distillation, and cross-model composition, achieving competitive performance across these diverse settings.

---


> [!TIP]
> 当前位于：**201-230**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-230**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
