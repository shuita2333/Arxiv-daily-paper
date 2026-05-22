# 🧠 大模型相关研究 | 2026年05月23日

> 本类共 **162** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-162**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-162**

---

### 151. [Conceptualizing Embeddings: Sparse Disentanglement for Vision-Language Models](https://arxiv.org/abs/2605.22679)

**<font color=#1a73e8>作者：</font>** Piotr Kubaty, Patryk Marszałek, Łukasz Struski 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models learn powerful multimodal embeddings, yet their internal semantics remain opaque. While sparse autoencoders (SAEs) can extract interpretable features, they rely on expanding the representation dimension, which compromises the original geometry and introduces redundancy. We introduce CEDAR (Conceptual Embedding Disentanglement via Adaptive Rotation), a post-hoc method that reveals the compositional structure of pretrained embeddings without increasing dimensionality. By learning an invertible transformation with a top-$k$ sparsity bottleneck, CEDAR concentrates semantic information into axis-aligned disentangled coordinates. In CLIP-like architecture, individual coordinates can be interpreted with textual concepts, while for generative models such as BLIP, they can be decoded into natural language descriptions. Experiments demonstrate that CEDAR achieves a competitive reconstruction-sparsity trade-off while producing explanations that are more interpretable and better aligned with human perception. Our results suggest that the apparent entanglement in vision-language representations can be resolved through a suitable change of basis, eliminating the need for overcomplete expansions.

---


### 152. [ChronoVAE-HOPE: Beyond Attention -- A Next-Generation VAE Foundation Model for Specialized Time Series Classification](https://arxiv.org/abs/2605.22684)

**<font color=#1a73e8>作者：</font>** José Alberto Rodríguez, Luis Balderas, Miguel Lastra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) have become a new component of the state-of-the-art in general time series forecasting. However, adapting them to specialized classification tasks remains constrained by two interconnected challenges: the quadratic cost of standard attention mechanisms and the inability to disentangle the structural components underlying time series variability. This technical report introduces ChronoVAE-HOPE, a next-generation TSFM that reconciles massive generalization with structured latent representation for time series classification. The core of the proposal is a Variational Autoencoder (VAE) framework built upon the HOPE Block, which replaces quadratic attention with a dual-memory system: Titans modules for dynamic short-term retention and a Continuum Memory System (CMS) for the abstraction of long-term historical context. A key architectural novelty is the disentangled latent space, which factorizes representations into independent trend and seasonal components via dedicated encoder heads and separate decoder pathways. ChronoVAE-HOPE undergoes self-supervised pre-training on the Monash archive, combining a Masked Time Series Modeling (MTSM) auxiliary objective with a disentangled VAE reconstruction loss. The pre-trained encoder is subsequently frozen and used to generate fixed-length embeddings for downstream classification on the UCR benchmark datasets. Empirical results demonstrate strong performance across diverse temporal domains, particularly in settings characterized by strict causal structure. ChronoVAE-HOPE establishes a robust and interpretable framework for the adaptation of foundation models to time series classification through structured generative representations.

---


### 153. [AMEL: Accumulated Message Effects on LLM Judgments](https://arxiv.org/abs/2605.22714)

**<font color=#1a73e8>作者：</font>** Sid-ali Temkit  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are routinely used as automated evaluators: to review code, moderate content, or score outputs, often with many items passing through one conversation. We ask whether the polarity of prior conversation history biases subsequent judgments, an effect we call the accumulated message effect on LLM judgments (AMEL). Across 75,898 API calls to 11 models from 4 providers (OpenAI, Anthropic, Google, and four open-source models), we present identical test items in isolation or following histories saturated with predominantly positive or negative evaluations.
Models shift toward the conversation's prevailing polarity (d = -0.17, p < 10^-46). The effect concentrates on items where the model is genuinely uncertain at baseline (d = -0.34 for high-entropy items, vs d = -0.15 when the baseline is deterministic). Bias does not grow with context length: 5 prior turns and 50 produce the same shift (Spearman |r| < 0.01; OLS slope p = 0.80). And there is a negativity asymmetry: paired per item, negative histories induce 1.62x more bias than positive (t = 13.46, p < 10^-39, n = 2,481). Scaling helps but does not solve it (Anthropic: Haiku -0.22 to Opus -0.17; OpenAI: Nano -0.34 to GPT-5.2 -0.17).
Three follow-ups narrow the mechanism. The token probability distribution shifts continuously, not at a threshold. The negativity asymmetry has both token-level and semantic components, though attributing the balance is exploratory at our sample sizes. Position does not matter: five biased turns anywhere in a 50-turn history produce the same shift. The simplest fix for evaluation pipelines is a fresh context per item; when batching is unavoidable, balancing the history helps.

---


### 154. [Reading Task Failure Off the Activations: A Sparse-Feature Audit of GPT-2 Small on Indirect Object Identification](https://arxiv.org/abs/2605.22719)

**<font color=#1a73e8>作者：</font>** Mahdi Nasermoghadasi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We report a small, reproducible audit of which sparse-autoencoder (SAE) features of GPT-2 small fire differently on failed versus successful trials of the Indirect Object Identification (IOI) task. On 300 prompts, GPT-2 small reaches 79.7% accuracy; 146 of the 24,576 features in the layer-8 residual-stream SAE release of Bloom (2024) clear a Holm-corrected significance threshold and 105 reach a large effect size (|Cohen's d| > 0.8). The strongest single correlate of failure -- feature 17,491, d=+2.93, Neuronpedia label 'cryptographic keys' -- is essentially silent except when the prompt's transferred object is 'the keys,' on which GPT-2 small fails 93.3% of the time vs. 7.5% on the other seven objects (Fisher exact p = 8.79 x 10^-33). We put this correlate through three controls that a mechanistic claim should pass. (i) A causal ablation: zeroing feature 17,491 in the residual stream across all token positions of the 45 keys prompts does not restore accuracy (6.7% -> 4.4%); the feature is a correlate, not a sufficient cause at this layer. (ii) A representation baseline: a logistic regression on the raw 768-dimensional residual stream reaches 5-fold ROC AUC = 0.929, matching the top-100 SAE features (0.927); the SAE basis adds interpretability, not predictive power. (iii) A seed-robustness check: across five random seeds the keys-subset failure rate stays in 75.0--93.3% (the behavioural effect is real), but feature 17,491 is the top-|d| feature in only 1 of 5 runs. The methodological contribution is therefore the audit pipeline (cheap, model-agnostic, surfaces named correlates) rather than any single feature found through it. We release the code, the 300-prompt corpus, the 300x24,576 activation matrix, the ablation and baseline scripts, and the figures. The full pipeline runs on a laptop (Apple M3 Max, no discrete GPU).

---


### 155. [Can AI Make Conflicts Worse? An Alignment Failure in LLM Deployment Across Conflict Contexts](https://arxiv.org/abs/2605.22720)

**<font color=#1a73e8>作者：</font>** Andrii Kryshtal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI models are already deployed in societies affected by armed conflict, and journalists, humanitarian workers, governments and ordinary citizens rely on them for information or for their work processes. No established practice exists for checking whether their outputs can make those conflicts worse. We tested nine model configurations from four providers (OpenAI, Anthropic, DeepSeek, xAI) on 90 multi-turn scenarios designed to surface misaligned behaviour in conflict contexts: false equivalence between documented atrocities, denial of genocide, and failure to recognise ethnic slurs, among others. When such outputs feed into journalism, humanitarian reporting, or public debate, they can deepen divisions in fragile societies. Failure rates span 6\% to 47\% between the best and worst performing models, which makes model choice a safety question in its own right and when users pushed for ``balance'' in cases where international courts have already assigned responsibility, five of nine configurations failed 80 to 100 percent of the time. We release the first evaluation framework for this domain and propose adding it to alignment evaluation portfolios.

---


### 156. [Self-Evolving Multi-Agent Systems via Decentralized Memory](https://arxiv.org/abs/2605.22721)

**<font color=#1a73e8>作者：</font>** Guangya Hao, Yunbo Long, Zhuokai Zhao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Self-evolving multi-agent systems (MAS) have emerged as a promising route to LLM agents that continually improve from experience, with persistent memory at their foundation. However, existing designs almost exclusively adopt a centralized repository shared across agents, incurring communication and coordination overhead, raising privacy concerns, and collapsing agent diversity. We propose DecentMem, a decentralized memory framework in which each agent maintains its own dual-pool memory -- an exploitation pool of consolidated past trajectories and an exploration pool of LLM-generated candidates for unseen contexts. The two pools are reweighted online based on stage-wise feedback from an LLM-as-a-judge. Theoretically, we prove that this design guarantees global reachability of the solution space and achieves $O(\log T)$ cumulative regret, matching the stochastic bandit lower bound up to constants. In practice, across three MAS frameworks (AutoGen, DyLAN, AgentNet), three Qwen3 backbones (4B/8B/14B), two Gemma4 backbones (E2B/E4B) and five benchmarks spanning math, code, QA, and embodied tasks, DecentMem improves average accuracy by up to 23.8% over the strongest centralized memory baseline and by up to 52.5% over the no-memory baseline, while reducing token usage by up to 49%.

---


### 157. [Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation](https://arxiv.org/abs/2605.22731)

**<font color=#1a73e8>作者：</font>** Dong Nie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model post-training methods such as supervised fine-tuning (SFT), reinforcement learning (RL), and distillation are often analyzed through their loss functions: maximum likelihood, policy gradients, forward KL, reverse KL, or related objective-level variants. We study a complementary factor: the state distribution on which supervision is applied. For an autoregressive policy, a state is a prompt plus generated prefix. SFT trains on fixed dataset states, while RL and on-policy distillation (OPD) train on states induced by the current learner. We formalize post-training as state-distribution shaping and run a controlled smallscale study using Qwen3-0.6B-Base on GSM8K, with TruthfulQA and MMLU as retention evaluations. Our results show three phenomena. First, a mild SFT run improves GSM8K with little forgetting, while a stress SFT run causes substantial retention loss. Second, OPD from a degraded SFT teacher surpasses that teacher on GSM8K, TruthfulQA, and MMLU, despite using the teacher as its only supervision source. Third, a lightweight on-policy RL run improves GSM8K while preserving retention. These results support a state-centric view of post-training: the source and locality of training states can be as important as the form of the supervision signal.

---


### 158. [Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models](https://arxiv.org/abs/2605.22732)

**<font color=#1a73e8>作者：</font>** Juergen Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate whether acoustic emotion recognition models can serve as proxies for the Pathos dimension in political speech analysis, as operationalised by the TRUST multi-agent large language model (LLM) pipeline. Using a Bundestag plenary speech by Felix Banaszak (51 segments, 245 s) as a case study, we compare three analysis modalities: (1) emotion2vec_plus_large, an acoustic speech emotion recognition (SER) model whose continuous Arousal and Valence values are derived via post-hoc Russell Circumplex projection; (2) Gemini 2.5 Flash, an LLM analysing the full speech audio together with its transcript in an open-ended, context-aware fashion; and (3) TRUST-Pathos scores from a three-advocate LLM supervisor ensemble. Spearman rank correlations reveal that Gemini Valence correlates strongly with TRUST-Pathos (rho = +0.664, p < 0.001), whereas emotion2vec Valence does not (rho = +0.097, p = 0.499). We further demonstrate, via a systematic quality evaluation of the Berlin Database of Emotional Speech (EMO-DB) using Gemini in an open-ended annotation paradigm, that standard SER benchmark corpora suffer from acted speech, cultural bias, and category incompatibility. Our results suggest that LLM-based multimodal analysis captures semantically defined political emotion substantially better than acoustic models alone, while acoustic features remain informative for low-level Arousal estimation. Future work will extend this approach to video-based analysis incorporating facial expression and gaze.

---


### 159. [Towards a General Intelligence and Interface for Wearable Health Data](https://arxiv.org/abs/2605.22759)

**<font color=#1a73e8>作者：</font>** Girish Narayanswamy, Maxwell A. Xu, A. Ali Heydari 等 40 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While ubiquitous wearable sensors capture a wealth of behavioral and physiological information, effectively transforming these signals into personalized health insights is challenging. Specifically, converting low-level sensor data into representations capable of characterizing higher-level states is difficult due to high phenotypic diversity and variation in individual baseline health, physiology, and lifestyle factors. Moreover, collecting wearable data paired with health outcome annotations is laborious and expensive, and retrospective annotation remains practically unfeasible, contributing to a scarcity of data with high-quality labels. To overcome these limitations, we propose a foundation model for wearable health that is pretrained on more than one trillion minutes of unlabeled sensor signals drawn from a large cohort of five million participants. We demonstrate that the joint scaling of model capacity and pretraining data volume leads to systematic improvements in performance, as evaluated on a diverse set of 35 health prediction tasks, spanning cardiovascular, metabolic, sleep, and mental health, as well as lifestyle choices and demographic factors. We find that this population scale representation unlocks label-efficient few-shot learning and generative capabilities for robust daily metric estimation. To further leverage this learned representation, we deploy a classroom of LLM agents to autonomously search the space of downstream predictive heads built on the model embeddings, showing broad performance improvements that increase with LLM model capacity. Finally, we show how integrating these downstream predictors into a Personal Health Agent can support model responses that are more relevant, contextually aware, and safe, and we validate this via 1,860 ratings from a cohort of clinicians.

---


### 160. [Understanding Data Temporality Impact on Large Language Models Pre-training](https://arxiv.org/abs/2605.22769)

**<font color=#1a73e8>作者：</font>** Pilchen Hippolyte, Fabre Romain, Signe Talla Franck 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are typically trained on shuffled corpora, yielding models whose knowledge is frozen at train time and whose temporal grounding remains poorly understood. In this work, we study the impact of pre-training dynamics on the acquisition of time-sensitive factual knowledge, focusing specifically on data ordering. Our main contributions are twofold. First, we introduce a comprehensive benchmark of over 7,000 temporally grounded questions and an evaluation protocol that enables analysis of whether models correctly associate facts with their corresponding time periods. Second, we pretrain 6B-parameter models on temporally ordered Common Crawl snapshots and compare them against standard shuffled pre-training. Our results show that sequentially trained models match shuffled baselines on general language understanding and common knowledge while consistently exhibiting more up-to-date and temporally precise knowledge. Temporally ordered pre-training yields improved factual freshness, while shuffled pre-training peaks on older data, possibly due to increased factual repetition. These findings, along with the release of our code at this https URL , checkpoints, and datasets at this https URL provide a foundation for future research on continual learning for LLMs.

---


### 161. [CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation](https://arxiv.org/abs/2605.22774)

**<font color=#1a73e8>作者：</font>** Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time cognitive load assessment is essential for adaptive human-computer interaction but remains challenging due to limited labeled data and poor cross-subject generalization. Recent ECG foundation models pre-trained on millions of clinical recordings offer rich representations, but cannot be directly applied to wearable devices due to sensor configuration mismatch and task differences. In this paper, we propose CogAdapt, a framework that adapts clinical ECG foundation models to wearable cognitive load assessment. CogAdapt introduces LeadBridge, a learnable adapter that transforms 3-lead wearable signals into anatomically consistent 12-lead representations, and ProFine, a progressive fine-tuning strategy that gradually unfreezes encoder layers while preventing catastrophic forgetting. Evaluations on two public datasets (CLARE and CL-Drive) under leave-one-subject-out cross-validation show that CogAdapt substantially outperforms baselines trained from scratch, achieving macro-F1 scores of 0.626 and 0.768. These results demonstrate the promise of foundation model adaptation for subject-independent cognitive load assessment from wearable sensors.

---


### 162. [Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs](https://arxiv.org/abs/2605.22823)

**<font color=#1a73e8>作者：</font>** Jongseo Lee, Hyuntak Lee, Sunghun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (Video-LLMs) have made rapid progress on temporal video understanding, yet many fail at a basic perceptual primitive: signed image-plane motion direction. On simple videos of a single object moving left, right, up, or down, most Video-LLMs perform near chance, with above-chance cases largely attributable to prediction biases rather than genuine direction understanding. We call this failure directional motion blindness. We localize the failure by tracing motion direction information through the Video-LLM pipeline. Motion direction remains linearly accessible from the vision encoder, projector, and LLM hidden states, but the readout fails to bind this signal to the correct verbal answer option, revealing a direction binding gap. Although synthetic motion direction instruction tuning reduces this gap on the source domain, motion direction concept vector analysis shows that visual complexity weakens the signal magnitude and limits out-of-domain generalization. We introduce MoDirect, a dataset family for motion direction instruction tuning and evaluation, and DeltaDirect, a diagnosis-driven, projector-level objective that predicts normalized 2-D motion vectors from adjacent-frame feature deltas. On MoDirect-SynBench, instruction tuning with DeltaDirect improves motion direction accuracy from 25.9% to 85.4%. On MoDirect-RealBench, DeltaDirect improves real-world motion direction accuracy by 21.9 points over the vanilla baseline without real-world tuning data, while preserving standard video-understanding performance. Code: this https URL

---


> [!TIP]
> 当前位于：**151-162**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-162**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
