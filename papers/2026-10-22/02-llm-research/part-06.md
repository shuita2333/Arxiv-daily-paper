# 🧠 大模型相关研究 | 2026年10月22日

> 本类共 **299** 篇论文：已确认 **275** 篇，待复核 **24** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-299**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-299**

---

### 251. [Asymmetric Looped Transformers: Fixed Global Representations for an Iterative Decoder](https://arxiv.org/abs/2610.28489)

**<font color=#1a73e8>作者：</font>** Cheng Liang, Tengfei Zhang, Wenjie DU 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped Transformers increase effective depth by repeatedly applying shared layers, offering a way to scale computation without increasing parameter count. However, full-stack looping places context construction and iterative state refinement within the same recurrent computation, without explicitly distinguishing their roles. We introduce the Asymmetric Looped Transformer (AsymLoop), which separates single-pass context encoding from recurrent state refinement. A single-pass causal encoder produces layer-specific Global key-value (KV) caches that remain fixed across iterations, while a weight-tied recurrent decoder generates Local KV from its evolving state. Joint attention over both sources under a single softmax allows each update to integrate persistent contextual information with the current intermediate state. For training, we apply a heavy-tail-guided layerwise learning-rate method to the encoder and decoder. Experiments on FineWeb-Edu across four model scales, from 60M to 1B, show consistently lower validation perplexity and higher average downstream accuracy than Full Loop under matched effective depth and training token budgets. At 1B, AsymLoop improves average zero-shot accuracy across seven commonsense reasoning benchmarks from 49.58% to 50.85%. Further experiments extend these benefits to longer training budgets, an OLMo-style backbone, and sparse mixture-of-experts models. These results support asymmetric context encoding and state refinement as an effective design for recurrent language models.

---


### 252. [OptionWorld: A Benchmark for Diagnosing Failures of LLMs as Long-Term Personal Assistants](https://arxiv.org/abs/2610.28491)

**<font color=#1a73e8>作者：</font>** Ruoyu Zhang, Zhaocen Liu, Weiyi Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term assistants must follow unfinished tasks across days as information and circumstances change. Finding information or starting an action, however, does not ensure that the task gets completed. We introduce OptionWorld, a benchmark that traces information acquisition, judgments, actions, and outcomes in simulated daily-life tasks to identify where current LLMs fall short as long-term personal assistants. In runs with archived decision inputs, the key facts remain in the model's last input before the deadline in 35.5% of failed instances. Failure analysis identifies the three most frequent problems: needed information is not obtained or combined, available opportunities to act go unused, and agents impose restrictions that the task does not require. Three follow-up experiments show that supplying missing facts restores task success in some cases; action reminders can restart work while subsequent steps still miss the deadline; and correcting a supplied note that wrongly forbids contact restores permitted inquiry. These findings locate shortcomings in maintaining task state: connecting facts to unfinished work, following through before deadlines, and separating actual restrictions from the agent's assumptions.

---


### 253. [Present but Hard to Read: Probing Latent Reasoning with Minimal Pairs](https://arxiv.org/abs/2610.28498)

**<font color=#1a73e8>作者：</font>** Aur Shalev Merin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probing studies of latent reasoning often read a model's state where the answer begins and take a failed probe as evidence that a value is absent. We test this with a digit copied from the question, in the looped model Ouro-1.4B and the standard transformer Qwen2.5-1.5B. Comparing prompts that differ only in that digit shows it is present at the last prompt token, in a code shared across questions (readout about 0.9). A probe that sees one prompt at a time, the usual setting, barely reads it: 0.36 in Ouro and 0.19 in Qwen even after 5,249 training questions. The digit's change is small rather than crowded: random noise lands on equally busy directions, while a random word in its place moves the state far more and is readable. Since every varied token leaves a trace, a successful probe is ambiguous too. We give a protocol, including a synthetic null for generic mixing, for testing computed values against copies and mixtures of the inputs. In pre-registered studies of two-step problems it finds a small signal for the unwritten intermediate a+b just before Ouro writes the answer's last digit, and its sign follows the operation, though mixing alone produces much of that sign-following part. Holding that value at another problem's from the first loop on does not move the written digit toward the other problem's, while the same patch of the answer does: the value is readable but not used.

---


### 254. [BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models](https://arxiv.org/abs/2610.28500)

**<font color=#1a73e8>作者：</font>** Ning Zhang, Shihao Wang, Jinrui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For efficient deployment of large language models (LLMs), methods of ultra-low-bit backbones reduce weight storage, memory traffic, and linear-layer execution cost, while multi-token prediction (MTP) methods reduce sequential decoding steps by predicting multiple future tokens in parallel. Although complementary, the direct combination of these methods cannot accelerate decoding at comparable quality: masked drafting lacks intermediate token input supplied in next-token training, while wider computation and causal key-value (KV) updates can offset the savings from fewer steps. To address these challenges, we propose BitMTP, an algorithm-system co-design framework for efficient MTP on ultra-low-bit LLM backbones. A joint next-token prediction and MTP objective equips a single model with both autoregressive (AR) generation and block-causal drafting. Confidence-only decoding, speculative-only decoding, and hybrid decoding provide different quality-throughput operating points without using separate draft and verifier models. Accepted-prefix alignment keeps the committed prefix, materialized causal KV boundary, and CUDA Graph replay state consistent for continued generation. BitMTP uses this contract to select width-specialized low-bit execution and reuse captured graphs over shared KV storage. On NVIDIA H20, BitMTP with hybrid decoding achieves five-task mean speedups of 2.2x on BitNet b1.58-2B and 2.1-2.4x on 1.7B-4B Bonsai models at comparable task quality. On RTX 3090 and Jetson Orin, it further achieves up to 2.0x in five-task mean throughput and 3.3x on MBPP+, respectively. These results demonstrate that BitMTP accelerates ultra-low-bit LLM generation across backbones, model sizes, and GPU types. The source code is released at this https URL

---


### 255. [GazeLens for Efficient Egocentric Video Question Answering with Simple Gaze-Driven Adaptive Token Reduction](https://arxiv.org/abs/2610.28502)

**<font color=#1a73e8>作者：</font>** Trong-Thang Pham, Anh Nguyen, Hien Van Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Smart glasses can help users understand their activities and surroundings, but small vision-language models must preserve useful evidence within limited computation. This is difficult because redundant frames consume the visual budget, while aggressive spatial compression can discard relevant details. Although gaze identifies the wearer's focus, the question may require evidence from the surrounding scene. To address these constraints, we propose GazeLens, which combines frame selection with gaze- and question-guided token reduction. First, HOG transitions and image sharpness select frames before visual encoding. For each selected frame, Gaussian pooling then forms gaze-focused and complementary summaries. Because their relevance depends on the question, a lightweight gate blends them into a primary token. Together with a global scene token, this retains both focused and contextual summaries within two tokens per frame. On StreamGaze, GazeLens achieves higher macro and micro accuracy than the evaluated full-grid and token-reduction baselines, with lower input-forward FLOPs than the shared-backbone token-reduction baselines.

---


### 256. [SenseAlign: Understanding Vision and Touch through Language at Test Time](https://arxiv.org/abs/2610.28511)

**<font color=#1a73e8>作者：</font>** Chuyang Ye, Qinting Jiang, Jingyan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tactile-visual-language models combine vision and touch through a shared language space to recognize objects and materials. In real-world deployment, changes in lighting, contact quality or sensor hardware can shift visual or tactile inputs and degrade recognition performance. When both modalities contribute to a prediction, an unreliable modality can override correct evidence from the other. Since labeled data are generally unavailable during deployment, test-time adaptation offers a way to recover recognition performance from unlabeled observations. In this setting, we find that comparing accumulated observations with the text embeddings of candidate classes reveals modality reliability differences that confidence can miss. Refining features against competing classes also improves recognition beyond geometric alignment alone. These findings motivate SenseAlign, which uses a common semantic reference for test-time modality weighting and feature correction. Alignment Trust weights each modality according to its support for shared predicted classes. Anchor Realignment uses the same class text embeddings to fit a shared feature correction that separates predicted classes from alternatives. Both modules use the same unlabeled history while keeping all encoders frozen. Extensive experiments across diverse datasets demonstrate strong recognition performance under both natural shifts and controlled corruptions.

---


### 257. [DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems](https://arxiv.org/abs/2610.28522)

**<font color=#1a73e8>作者：</font>** Xialie Zhuang, Mingcong Lei, Zunhai Su 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models support routing, guardrails, and output verification in LLM systems. However, item accuracy alone cannot establish whether models make correct decisions across controlled variations or assign reliable confidence to their predictions. We introduce DecisionPivot, a diagnostic benchmark comprising 48 tasks and 40,033 items across seven decision roles. Its core track contains 7,800 items from 13 generated task families, organized into contrast groups with computed answers verified by independently implemented solvers. The complementary reference track contains 32,233 items from 35 public test sets, preserving their original evaluation metrics. We evaluate 40 decision models and 14 general models using documented, model-specific protocols, assessing item and contrast-group accuracy, probability ordering, calibration, and empirical selective coverage. Our results reveal substantial differences obscured by aggregate scores: two 27B models separated by only 2.6 points on the reference track achieve contrast-group accuracies of 70.1% and 44.2%. Across 2,400 binary contrast pairs, Perplexity Decider correctly ranks the positive member above the negative member in 92.3% of pairs but answers both members correctly in only 74.1%, exposing a gap between probability ordering and decision correctness. Models with similar item accuracy also differ in the reliability of their high-confidence predictions. On a separate 1,296-item subset, GLM-5.3 achieves 93.5\% contrast-group accuracy at a higher reasoning setting, compared with 81.5% at its lowest effort. By linking errors to pivotal details and difficulty levels, DecisionPivot provides fine-grained diagnostics of decision failures that aggregate evaluation alone cannot reveal.

---


### 258. [Humans Correct Their Judgments Through Debate, but Weaker AI Models Do Not](https://arxiv.org/abs/2610.28539)

**<font color=#1a73e8>作者：</font>** Maria Victoria Carro, Denise Alejandra Mester, Facundo Nieto 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How can we effectively oversee AI systems that surpass human intelligence? AI Safety via Debate proposes that two AI systems argue opposing positions and a judge, either a human or a weaker model, decides which is correct. By facilitating supervisors in providing high-quality training signals, debate aims to encourage truthful and safe behavior from AI systems whose capabilities exceed our own. However, human judgment is not neutral: people often rely on biases which advanced AI systems may learn to exploit. Drawing on insights from collective intelligence and social cognition, this paper investigates whether debate can guide human and LLM supervisors toward the truth despite their prior beliefs. We evaluate several protocol configurations. We also explore setups inspired by the wisdom of the crowd such as the number and diversity of judges, as well as interaction mechanisms including deliberation and voting. Overall, we find that debate increases accuracy relative to prior beliefs for human judges, whereas the consultancy baseline, in which a single expert argues for one answer, does not. For weaker language models, however, the results are mixed: debate provides no comparable gains in most settings and can even reduce accuracy. Among multi-judge protocols, weighted voting produces the highest accuracy for human supervisors, whereas for LLMs none of them significantly improves group accuracy, even as the number of judges increases. Notably, the behavior of minority judges in non-diverse deliberation protocols suggests that, under symmetric settings, incorrect positions could be more persuasive than correct ones. These findings support debate as a viable path toward scalable human oversight, but cast doubt on its benefits for weaker AI supervisors, raising concerns about fully automated training and control pipelines in high-stakes settings.

---


### 259. [Predictive Latents for Autoregressive Language Models: Possibility, Gauge, and Obstruction](https://arxiv.org/abs/2610.28540)

**<font color=#1a73e8>作者：</font>** Yuzhou Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models are trained by next-token cross-entropy, yet several recent systems also iterate a hidden state without emitting a token: continuous thoughts, pause steps, and recurrent depth. This note separates three risks on one latent process. The token risk $R_{\mathrm{tok}}$ scores a readout. The teacher-forced latent risk $R_1$ scores a one-step map that sees the true hidden state. The open-loop risk $R_H$ scores the same map after it has been iterated on its own outputs. If the Bayes next-token posterior is a function of a $k$-dimensional statistic with full-rank covariance, a width-$k$ latent, a linear least-squares transition, and a refit unembedding match the Bayes token predictor. The statistic is identified only up to an invertible gauge: whitening the residual stream does not change the token law once the unembedding is refit. The matching obstructions are sharp. A constant latent drives $R_1$ to zero while token cross-entropy falls back to the marginal entropy. A perfect token predictor can still hide a null-space walk whose open-loop error grows linearly in the horizon. A small next-latent loss does not certificate next-token prediction, and a small next-token loss does not certificate free latent rollout, unless a rank or injectivity condition is stated with the number.

---


### 260. [When Do LLMs Help with Feature Selection? A Systematic Empirical Study](https://arxiv.org/abs/2610.28556)

**<font color=#1a73e8>作者：</font>** Fateme Memar, Dongjie Wang, Arvin Agah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can leverage semantic feature names alongside summary statistics for tabular feature selection, yet it remains unclear when such information improves subset selection relative to established statistical methods. We investigate this question within an 18-dataset framework comprising 10 datasets for Group Relative Policy Optimization (GRPO) training, 2 for checkpoint validation, and 6 held-out evaluation datasets. We compare five classical baselines, frozen Qwen2.5-7B and Llama-3.3-70B selectors, and two GRPO-adapted Qwen2.5-7B models, reporting classification ROC-AUC and regression R^2 separately and using dataset-wise ranks for cross-task comparison. Across five seeded evaluation partitions, classical selectors generally achieve higher predictive performance than the tested 7B LLM/RL selectors, including under a pre-specified ~33% feature budget with strict train-only classical fitting, while the 7B selectors retain compact subsets. A cardinality-matched semantic sensitivity experiment shows that, for Zero-shot Qwen-7B, informative feature names improve regression performance over anonymized and shuffled alternatives (+0.1964 and +0.1606 mean R^2), whereas aggregate classification differences are smaller (+0.0159 and +0.0084 ROC-AUC) and dataset-dependent. These results characterize when semantic information benefits LLM-based feature selection and show that classical selectors remain strong baselines for predictive tabular feature selection.

---


### 261. [Large Flow Language Models](https://arxiv.org/abs/2610.28559)

**<font color=#1a73e8>作者：</font>** Arnav Chavan, Chanhyuk Lee, Udbhav Bamba 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion-parameter scale remain less established. We present Lafa (Large flow language model), a fast, high-performing flow language model scaled to 8B parameters in a data-efficient manner. Lafa is a blockwise flow model with causal attention on the prefix and bidirectional, asynchronous flow within each block. This design enables efficient training by adapting pretrained autoregressive (AR) models and fast inference via prefix caching and blockwise parallel decoding. We train Lafa at 0.5B, 7B, and 8B scales with fewer than 30B tokens, more efficient than previous diffusion models, and evaluate it on instruction following, reasoning, and coding, where the learned flow matches or surpasses the quality of AR and can be distilled into flow maps for one- and few-step generation. Notably, flow training preserves or even improves pretrained AR capabilities via a multi-token prediction effect, which we leverage in a self-speculative decoding scheme that verifies flow-based drafts autoregressively within a single model. This yields 2.54x the throughput of an AR model at comparable quality, outperforming multi-token prediction and discrete diffusion methods. Our findings show that continuous flows can serve as a scalable foundation for language modeling.

---


### 262. [Agentic Ensemble with Vision-Language Models for Visual Anomaly Detection](https://arxiv.org/abs/2610.28560)

**<font color=#1a73e8>作者：</font>** Shangquan Sun, Wenjun Luo, Xu He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual anomaly detection aims to detect abnormal objects, while anomaly samples are often scarce during model training. Assembling multiple pretrained detectors can help by leveraging their transferable image scores and anomaly maps. However, most existing ensemble methods apply fixed fusion rules over saved predictions which struggle when pretrained detectors clearly disagree due to different training objectives, priors, and visual representations. To this end, we design AnomalyAgent, a post-training fusion framework for accurate visual anomaly detection. AnomalyAgent aligns heterogeneous scores and maps, summarizes score- and region-level disagreement, and treats fusion as a finite action-selection problem. It implements two types of actions: 1) score actions that determine how to fuse image-level detector confidence via consensus, robust aggregation, detector weighting, or score-map consistency; 2) map actions that fuse dense anomaly responses via consensus, detector weighting, geometric aggregation, or disagreement correction. A constrained vision-language model (VLM) is introduced to inspect high-conflict samples and select valid score action and map action to produce the final prediction. We evaluate AnomalyAgent on MVTec AD and VisA as primary benchmarks, together with seven additional public anomaly benchmarks and Real-IAD for large-scale score-level evaluation. Across these benchmarks, AnomalyAgent consistently improves over equal-weight fusion and achieves the best mean image AUROC and pixel AP among the compared fusion methods on MVTec AD and VisA, while demonstrating robust transfer across additional anomaly domains.

---


### 263. [OptScientist: Automated Discovery of Optimization Laws](https://arxiv.org/abs/2610.28562)

**<font color=#1a73e8>作者：</font>** Ma ZhenYao, Yue Liang, Jian-Qiao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many scientific phenomena are best understood as outcomes of underlying optimization problems, yet automated scientific discovery has largely focused on recovering equations that describe observed input-output patterns. We introduce OptScientist, a novel automated framework for discovering compact symbolic optimization laws directly from data. OptScientist comprises (i) a model that infers symbolic optimization problems by first learning to represent data as an optimization problem and then extracting its symbolic form, and (ii) an LLM agentic system embedding the model in a discovery process that integrates theoretical priors from scientific literature, discovers candidate laws, abstracts their underlying mechanisms, and suggests new data to collect. We first evaluate OptScientist on OptFeynman, a novel benchmark of 99 physics-derived optimization problems, where OptScientist recovers ground-truth laws for over 80% of the problems and remains robust to noisy contextual information, while substantially outperforming machine-learning, symbolic, and LLM-based model-discovery baselines. On human risky choice and central-bank monetary policy, OptScientist discovers compact symbolic optimization laws that achieve held-out predictive performance competitive with leading baselines, while using few parameters and substantially fewer tokens than LLM baselines. Overall, OptScientist extends automated scientific discovery to uncovering optimization laws that generate observed phenomena, enabling automated theory building across the physical, biological, behavioral, and social sciences.

---


### 264. [Evolving Semantic Indexes for Generative Retrieval](https://arxiv.org/abs/2610.28568)

**<font color=#1a73e8>作者：</font>** Jinming Nian, Jyun-Yu Jiang, Henry Tsai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative retrieval (GR) casts search and recommendation as autoregressive generation of discrete semantic identifiers (SIDs). SID design largely determines GR quality, but its discrete, interdependent components (SID construction, collision handling, decoding, and training) cannot be optimized end-to-end with gradients and remain largely hand-designed. We introduce a framework that improves these components through LLM-driven evolutionary program search, to our knowledge the first application of this approach to GR. A locally served, open-weight 31B model mutates executable GR components, so no proprietary LLM API is used, and a 1M-parameter proxy decoder provides fast feedback in place of repeatedly training the 1B target generator. Across 21 SID programs on NQ320K, proxy and target Recall@100 show strong rank correlation (Spearman $\rho = 0.90$). Guided by this proxy, evolution improves the seed GR on NQ320K, MSMARCO300K, and a multilingual e-commerce dataset under a fixed training recipe. On NQ320K, jointly evolving SID construction and collision handling improves Recall@1 from 55.8% to 59.3% and Recall@100 from 85.8% to 90.6%. A component study shows that proxy reliability depends on what is evolved: improvements transfer reliably for the semantic index but not for the generator's training objective or the full pipeline. LLM-driven evolutionary search is thus a practical tool for GR design, provided proxy reliability is established for the chosen search space.

---


### 265. [The Token-Energy Law of LLM Decode: Active Bytes and Realized Time Account for Joules per Token](https://arxiv.org/abs/2610.28576)

**<font color=#1a73e8>作者：</font>** Chenxu Niu, Batuhan Sencer, Wei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy-efficient deployment of large language models requires understanding how model architecture, hardware, and serving settings shape energy per generated token. We introduce the Token-Energy Law, a compact, interpretable model of GPU-board energy per output token for dense, full-history decoding. It relates token energy to two core dimensions: active bytes and realized decode time. Active bytes describe logical byte demand per output, separating dense weights shared within a decode iteration from private key--value (KV) histories read and updated for each request. Realized decode time is the elapsed decode duration divided by the number of output tokens produced. We combine the two byte coordinates and time in a common affine form, with coefficients calibrated for each model and hardware/runtime configuration. This formulation explains how batching amortizes shared-weight work, longer attended histories increase private KV demand, and throughput determines the time-associated cost per output. Our experiments cover three models under BF16 decoding on NVIDIA Hopper and Blackwell GPUs, including two-GPU tensor parallelism on Hopper. Using fixed coefficients and observed decode time, held-out condition-mean energy estimates differ from measurements by at most 3.73%.

---


### 266. [Cache Engineering for Agents](https://arxiv.org/abs/2610.28577)

**<font color=#1a73e8>作者：</font>** Tianyu Fu, Ruoxi Wang, Zihan Min 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache I/O and storage become the dominant cost. Trajectories can also exceed the LLM's maximum context length, requiring control over active cache growth. Prior work uses context engineering to reduce cache size by trimming or summarizing history. However, modifying the trajectory prefix invalidates subsequent cached states and triggers costly re-prefilling of retained context. Task accuracy can also suffer when too little context is retained to limit re-prefill costs. We propose cache engineering as a new scheme. It allows agents to directly control their active KV cache without modifying the trajectory or re-prefilling retained context. Specifically, agents can proactively use drop to exclude selected cache from future attention and repos to adjust retained keys' position encodings. We formalize these cache operations and identify history dependence as a serving challenge: identical token sequences can yield different cache states under different cache operation sequences, making prefix matching insufficient for correct cache reuse. Thus, we co-design the AKV serving engine. It provides a stateless interface compatible with existing serving APIs, while internally managing stateful cache reuse, eviction, and restoration. Experiments show that a tool-response rolling-drop cache policy improves average benchmark scores by 1.7 points and reduces average cost by 27.7%, compared with conventional threshold-triggered summarization. With AKV, it achieves up to 1.2x the output throughput and a 1.5x speedup in P95 request latency. Recursive self-improvement of cache policies further reduces cost by 7.1% over expert design. Our code is at this https URL.

---


### 267. [Beyond the Sequentiality Bottleneck: A Hybrid Diffusion-Autoregressive Framework for Efficient Multimodal Reasoning](https://arxiv.org/abs/2610.28584)

**<font color=#1a73e8>作者：</font>** Wei Cai, Jian Zhao, Yuchen Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive models (ARMs) face a "Sequentiality Bottleneck" in reasoning, while diffusion language models (DLMs) offer parallelism but lack semantic coherence. To addresses both limitations, we propose Collaborative Reasoning Asymmetric Learning (CoRAL), a hybrid framework via an Asymmetric Planner-Executor (APE) architecture: a DLM Planner generates K diverse reasoning trajectories in parallel, while a large ARM Executor selects the optimal plan and synthesizes the final answer. To train the Planner effectively, we introduce Reward-Guided Denoising for CoT (RDC), which integrates outcome-based rewards into the diffusion process to steer it toward goal-directed reasoning. Experiments on vision-language benchmarks show that CoRAL significantly outperforms prior diffusion-based methods and achieves competitive performance against strong ARMs, achieving both superior efficiency and quality.

---


### 268. [Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation](https://arxiv.org/abs/2610.28586)

**<font color=#1a73e8>作者：</font>** Shu Zhao, Tan Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher intervention where the two disagree. We show this explanation is incomplete. From the states where the student departs most from the teacher, the teacher's own takeovers still finish the task, yet the student trained on its token scores keeps running out of turns. We attribute this to the myopia of next-token scoring. The teacher rates each token without seeing where the episode ends, so its scores let through the safe, delaying moves that outcome-based RL would punish with zero reward, a penalty agentic OPD lacks. We call this difference between what the teacher does and what it scores the rollout-scorer gap. We propose Rollout-to-Scorer Distillation (R2S), which repairs the scorer before distillation by mining high-disagreement states from the untrained student, running teacher takeovers from them, keeping the states where enough takeovers pass a reward-free check such as consensus or an LLM judge, and fine-tuning the teacher to give its takeover-informed scores on every assistant token from the divergence turn onward, without the takeover in context. The repaired teacher is frozen as the sole scorer for standard OPD, requiring no task reward during repair or training. Across three environments, two teachers and four students, R2S outperforms three state-of-the-art agentic-OPD methods in all twelve teacher-student-environment cells, by 12.8 success points on average over the best of them in each cell. Project page: this https URL.

---


### 269. [Evolving Agent Interfaces](https://arxiv.org/abs/2610.28601)

**<font color=#1a73e8>作者：</font>** Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function. Both the interfaces and the knowledge of when to use each are built by hand, which cannot keep pace with new applications, workflows, and models. We argue that interface design should itself be an agent capability. We introduce Agent S4, an autonomous computer-use scientist that builds Evolving Agent Interfaces from task experience. A meta-agent examines task agents' trajectories on synthetic training tasks, without success labels, and constructs and revises interfaces and usage knowledge in a repository. Population-based evolution then selects which repositories to develop further by their performance on validation tasks the meta-agent never sees, favoring changes that generalize beyond the seen tasks. On OSWorld V2, Agent S4, with Qwen3.8-27B and the evolved repository of interfaces, sets a new state of the art in open-source computer-use agents, reaching 21.3% binary score, 3.8 times the same model with fixed interfaces. This is above both GPT-5.5 (13.0%) and Claude Opus 4.8 (20.6%), at about 4.3% and 1.5% of their respective costs. On ScienceBoard, the evolved interfaces improve the success rate from 41.4% to 58.6% with the same model. These results suggest that useful interfaces can be evolved from experience, making autonomous interface design a source of improvement complementary to advances in models and harnesses. We open-source our code at this https URL.

---


### 270. [Value-Rich, Differently Organized: Measuring Value Expression and Organization in AI-Generated Debates](https://arxiv.org/abs/2610.28604)

**<font color=#1a73e8>作者：</font>** Maoyuan Li, Haoyuan Li, Zhongsheng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current evaluation of LLM-generated debate largely focuses on argumentative quality, leaving the value structure of generated arguments underexamined. We introduce a diagnostic metric framework for comparing how values are expressed and organized in human-reference and AI-generated debates. The framework separates value expression, the range of recognizable values a debate invokes, from value organization, how those values are distributed and sustained across turns. Grounded in Schwartz's Basic-10 value theory, it represents debates as multi-level value distributions over argumentative units, utterances, stances, and full debates, enabling metrics for value coverage, alignment, diffusion, and cross-turn dynamics. Across multiple generation systems, AI-generated debates are broadly value-expressive, often activating as many or more value dimensions than matched human references, but they organize these values differently. Their utterances are more locally value-diffuse, and source-blind judges distinguish value clarity from value focus. These findings show that debate evaluation should consider not only value presence, but also value organization. Code and supplementary materials are available at this https URL.

---


### 271. [Benchmarking Arabic Dialects for Math Problems](https://arxiv.org/abs/2610.28607)

**<font color=#1a73e8>作者：</font>** Noor Abo Mokh, Teresa Lynn, Nizar Habash 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning remains underexplored for low-resource languages, including Dialectal Arabic. To bridge this gap, we introduce the DAR-MGSM (Dialectal Arabic Multilingual Grade School Math) Benchmark, the first manually curated benchmark for evaluating mathematical reasoning in Dialectal Arabic. DAR-MGSM consists of math word problems (MWPs) requiring multi-step reasoning and covers five major Arabic dialects alongside Modern Standard Arabic (MSA). The benchmark comprises two parallel versions: translated-only and translated & culturally localized. The latter version adapts entities and references to regional varieties. We evaluate eleven Arabic-centric and multilingual large language models on DAR-MGSM. The results show that the performance generally declines on the localized version, highlighting the challenges introduced by culturally grounded adaptations. However, the magnitude of this effect varies across models, with Arabic-centric models exhibiting different levels of sensitivity to localization. A mechanistic interpretability analysis shows that translated and localized variants of the same MWPs often induce distinct internal reasoning trajectories, even when aggregate accuracy remains similar. Overall, our results show that mathematical reasoning performance depends on both linguistic variety and cultural context.

---


### 272. [Semantic Observability for Autonomous Systems Diagnostics](https://arxiv.org/abs/2610.28611)

**<font color=#1a73e8>作者：</font>** Jitendra Solanki, Anand Todkar, Ziran Min  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern distributed microservice deployments generate massive volumes of heterogeneous, multi-format observability logs across physically and logically partitioned infrastructure. Isolating root causes during cascading failures remains an arduous task for Site Reliability Engineers (SREs), bottlenecked by manual keyword filtering and disjointed temporal correlation across monitoring dashboards. We introduce Semantic Observability, an autonomous multi-agent framework that unifies disparate log streams into a dynamic, queryable Property Graph Database. By modeling physical infrastructure topologies, logical software dependencies, and chronological event sequences as attributed nodes and directed relations, it bridges the semantic gap inherent in flat, unstructured log repositories. Building on this unified substrate, we deploy a stateful multi-agent system orchestrated through Directed Cyclic Graphs (DCGs). The system autonomously navigates the topology, applying causal graph algorithms and temporal back-traversal to isolate the precise blast radius of anomalies. The pruned subgraph is then interpreted by a Large Language Model (LLM) reasoning engine to generate contextualized, code-level Root Cause Analyses (RCA) and actionable remediations. This paper establishes the foundational system architecture, formal relational ontology, and multi-agent control loops of Semantic Observability. We show conceptually how the framework eliminates ambient telemetry noise, reduces Mean Time to Resolution (MTTR), compresses LLM token consumption, and prevents structural hallucinations. We also specify an open-source validation framework on standard benchmarks (LogHub and Train-Ticket), laying the groundwork for a forthcoming companion paper on exhaustive quantitative evaluation and production benchmarking.

---


### 273. [NarraSpace: Multimodal Scene-Grounded Evidence for Picture-Description Dementia Classification](https://arxiv.org/abs/2610.28616)

**<font color=#1a73e8>作者：</font>** Qingming Li, Ruiyan Sun, Satoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Picture-description dementia classification uses a shared visual scene, but a transcript-level prediction alone does not identify the scene evidence underlying its inputs. NarraSpace links words and speech times to named picture elements and retrieves utterances for predefined scene events. Narrative-spatial descriptors summarize coverage and temporal organization. A frozen language model contrasts each event's text under examples from Alzheimer's disease and healthy-control training participants, alongside transcript surprisal and coverage measurements. Retained source records link event scores to their source utterances, speech intervals, and lexical matches. On the official 48-participant test set of the Alzheimer's Dementia Recognition through Spontaneous Speech benchmark, a fixed support vector classifier achieves $80.88\%\pm2.56\%$ mean accuracy over fifty seeds; averaged probabilities yield $81.25\%$ accuracy and $91.32\%$ area under the receiver operating characteristic curve. NarraSpace makes the construction of scene-linked classification inputs explicit and inspectable by connecting event-indexed language-model measurements to their source utterances, speech timing, and extraction records. Such source-linked measurements could support clinician review of picture descriptions by presenting quantitative summaries alongside the original speech evidence.

---


### 274. [Adaptive Multi-Token Prediction: How far should we go?](https://arxiv.org/abs/2610.28619)

**<font color=#1a73e8>作者：</font>** Emile Anand, Mohammed Rehan Parwani, Xinyuan Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-token prediction (MTP) can accelerate language-model decoding by drafting several tokens and verifying them in a single target-model pass. However, the best speculation horizon changes with context: longer drafts offer greater amortization when reliable, but can waste compute on suffixes discarded after a rejection. Unlike autoregressive drafting, where a stopping rule can decide token by token, MTP must fix the horizon before drafting, as all heads fire in the same forward pass. We therefore formulate horizon selection as an online control problem, using verification feedback to learn how far the draft can be trusted in each context, and introduce Adaptive Multi-Token Prediction (AMTP): a lightweight controller that requires no retraining and leaves the exact verifier unchanged. To guide horizon selection, we characterize the expected number of tokens committed at each horizon via acceptance survival, the probability that a draft prefix is fully accepted. Before each round, AMTP predicts how far the draft is likely to survive and picks the horizon with the highest expected tokens per second, learning freely from every verification pass. Theoretically, we show that any online learner's prediction error translates into throughput regret against the best horizon for each context, and in turn into a bound on wall-clock completion time. With online gradient descent, this regret is sublinear. Across five draft-target pairings built on Llama-3.1-8B-Instruct with Medusa heads, Meta's MTP models, and Qwen3-4B-Inst-2507-MTP, evaluated on AIME 2025 and GSM8K, AMTP decodes up to 4.1x faster than standard decoding and matches or outperforms the fixed window in 8 of 10 settings, with throughput gains of up to 10%.

---


### 275. [SolarRenderer: Few-Step Generative Reference Rendering](https://arxiv.org/abs/2610.28630)

**<font color=#1a73e8>作者：</font>** Guian Fang, Shengju Qian, Dongyue Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, need tens of denoising steps or a costly distillation of their own, and learn from conditions that are not aligned with their target videos. We present SolarRenderer, a structure-conditioned video renderer that adapts a frozen MiniMax-H3 33B backbone with two lightweight LoRAs. Structural videos enter the native reference pathway of the backbone at the positions of the frames they describe, without a type identifier and described only in plain text, so that a single control LoRA follows arbitrary structural representations. Starting from a pretrained four-step LoRA, structure-guided distribution matching renders in four steps, 12.3 times faster than 50-step sampling, while preserving the learned control. A block-causal variant extends the same design to streaming and renders 768p video in real time. To train the model, we build a frame-aligned corpus of 136K clips from game engines, simulators, and YouTube videos. Experiments on an in-distribution test set and a generalization benchmark of 16 structural representations show that SolarRenderer achieves state-of-the-art results across both, and generalizes to 11 unseen representations, including pose skeletons, drawings, and point clouds.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 276. [Mixture of Phonetic Experts Based Low-Rank Adaptation of Conformer Models for Accented English Speech Recognition](https://arxiv.org/abs/2610.26888)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Santosh Dahal, Anmol Guragain, Tianchi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Mixture of Phonetic Experts based Low-Rank Adaptation (MoPE-LoRA), a parameter-efficient adaptation framework for accented English speech recognition. Recent mixture-of-experts approaches typically allocate experts per accent, implicitly treating accent identity as the primary axis of variation. In contrast, we organize adaptation along phonetic categories, motivated by the observation that accent differences are often expressed as systematic distortions of phoneme realization. MoPE-LoRA introduces a fixed set of six low-rank experts aligned with manner-of-articulation classes and performs frame-level routing through a hybrid mechanism that combines phoneme supervision with learned acoustic gating. Because the expert set is shared across accents, the model does not require accent-specific modules and naturally extends to previously unseen accents. Experiments on L2-ARCTIC show that MoPE-LoRA consistently improves over single LoRA and full fine-tuning. In zero-shot evaluation where one accent is held out during training, the proposed method yields a 12.3% relative improvement over single LoRA. These results indicate that phonetic-category-based decomposition offers a scalable and transferable alternative to accent-level adaptation.

---


### 277. [Understanding the Benefits of Scaffolds through Computational Separations](https://arxiv.org/abs/2610.27157)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jingchu Gai, Adam Block, Andrej Risteski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time harnesses, i.e., external procedures that call a model many times and keep state across calls, can substantially improve model capabilities. In this paper, we investigate the benefits of using such harnesses and the extent to which these benefits can be internalized through training. More precisely, we conceptualize a harness $\mathcal{A}$ as an arbitrary wrapper around a base model $M$ and attempt to distill a student model from the harness's traces. Empirically we find that, even with simple scaffolds and small models, the inference-time harness significantly outperforms a distilled student. We then prove that such a gap is due to a fundamental representational limitation: inference-time harnesses can compute a closure of their per-call primitive that is $\NL$-complete even when the primitive is a trivial $\AC^0$ lookup, and that no fixed-depth forward pass can represent under the widely believed conjecture that $\NL\not\subseteq\TC^0$. Our theory suggests that expanding the representational capacity of the student relative to the task at hand, e.g., by enlarging the model, making the task easier, or lengthening its chain-of-thought, is necessary to close the gap, which we verify empirically. Finally, we scale to an agentic harness on competition math, where the same gap reappears. Overall, our results show that a harness confers on the base model a profound gain in representational power, one that training a same-class student on its traces cannot transfer back into the weights.

---


### 278. [You Are the Trigger: Speaker-Activated Backdoors](https://arxiv.org/abs/2610.27210)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nataša Krčo, Euodia Dodd, Peter Romov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speech models are increasingly used as an interface to AI systems, from transcription tools to voice agents. Existing audio backdoors require an attacker to introduce triggers at inference time. We study a different threat model in which the attacker compromises the model during fine-tuning but has no access to the victim's inference-time inputs. We introduce the Speaker-Activated Backdoor (SAB) setting, in which a target speaker's natural voice serves as the trigger. We develop a two-phase fine-tuning method that first makes speaker identity more accessible and then binds the target speaker to an attacker-chosen payload. Compared with a one-phase baseline with the same training budget, the two-phase method substantially improves selectivity and clean performance, and is especially important for content-dependent attacks. SAB achieves 90.2% and 97.0% backdoor success on Whisper-medium and Parakeet, with false-positive rates of 1.7% and 0%, respectively using as little as two minutes of real audio from the target speaker. We further demonstrate content-dependent semantic rewriting and downstream tool-use attacks, where malicious instructions are inserted into 96.9% of target-speaker transcripts. When these transcripts are passed to frontier LLM agents, GPT-4o and Claude (Opus, Sonnet, and Haiku), the injected instruction drives the agent to carry out the harmful action in up to 87.5% of cases. The attack generalizes to held-out recordings, multiple target speakers, and common acoustic degradations. These results establish speaker identity as a practical backdoor trigger that requires no inference-time attacker access and is invisible at the transcript layer.

---


### 279. [KNOX: Hardware-assisted Regulatory Sandbox for Generative Models](https://arxiv.org/abs/2610.27543)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Vasisht Duddu, Adam Caulfield, Xi He  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Regulations require companies to run AI models in a regulatory sandbox, an isolated environment that enables monitoring model behavior by regulators, prior to deployment. But, they do not spell out the technical mechanisms to design such a sandbox. Ideally, a regulatory sandbox should show (i) compliance (checks against regulations, and deviations from intended behavior, i.e., unauthorized tool and system calls); (ii) confidentiality (protects model weights from regulators); (iii) attestability (produces tamper-resistant evidence of model behavior for monitoring); and (iv) scalability (evidence is verifiable by multiple regulators). Several prior works (information-flow control, prompt-injection defenses, control-flow integrity, and traditional sandboxing) address specific compliance aspects but lack confidentiality, attestability, and scalability. TEEs meet some of these requirements, but simply running models inside a TEE is insufficient as we need compliance mechanisms.
We present KNOX, the first regulatory sandbox, built by running AI workloads inside TEEs. We demonstrate KNOX using agentic workloads. For compliance, we derive an attested policy manifest (with the applicable regulations, the expected tool calls, and the permitted system calls) for a given user prompt. Before an executor performs an action, an attested reference monitor compares it against the attested policy manifest and allows it only if it matches. Every action and verdict is recorded in an attested execution graph, enabling regulators to verify the model's execution and its compliance. We show that KNOX meets all requirements, and can check for compliance with regulations and deviations from intended behavior (e.g., due to prompt injection); and incurs low overhead (<1%).

---


### 280. [Foundations of the Scaling Law](https://arxiv.org/abs/2610.27789)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianyu Zhao, Zhixiang Ren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Empirical scaling laws relate validation loss to model size, training exposure and compute, providing a quantitative basis for allocating resources. This technical note explains these relationships through three linked analyses. Geometric approximation connects spatial resolution, intrinsic dimension and smoothness to function error; the loss function determines how that error transfers to task risk. Spectral analysis combines feature visibility, covariance eigenvalues and target alignment to describe how additional data reduce unresolved predictive mass. Constrained optimization then gives the parameter-data balance and the training-inference trade-off. We also examine emergence and grokking, separating scoring thresholds from learning dynamics, and test-time scaling, separating candidate coverage from selected-answer accuracy. Applications to vision and molecular prediction show how domain-specific coordinates change the resource comparison. An $\mathrm{SE}(3)$ case study quantifies the dimension dependence of quotient-space approximation gains and compares optimized compute frontiers, alongside separate analyses of conformational coverage and correlated-sample precision.

---


### 281. [Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization](https://arxiv.org/abs/2610.27889)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Younghyun Kim, Wooseok Seo, Minseo Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies in harness optimization have shown substantial performance gains in language model agents without updating model weights. A well-designed harness more effectively leverages the underlying model's capabilities by shaping context, tool use, and execution workflows. However, naïve success rates alone do not fully characterize whether optimized harness yields more reliable success on tasks already within reach (elicitation) or a broader range of solvable tasks (expansion). This distinction is crucial for recursive self-improvement and evolutionary search, as expansion may provide a broader range of successful experiences to push the capability boundaries. Despite the growing significance, this distinction remains underexplored in harness optimization. We conduct a systematic analysis to study the effect of gains from harness optimization. Building on pass@k analyses in the reinforcement learning (RL) literature that compare models before and after RL training, we compare optimized harnesses with their pre-optimization counterparts. Specifically, we assess changes in reachable task coverage, compare harness optimization with model scaling and increased inference-time compute, and examine how gains vary with task difficulty. Across static prediction and dynamic tasks, we find that pass@1 advantages of harness over stronger interventions can reverse at larger attempt budgets and aggregate gains conceal shortfalls on hard tasks, underscoring the need for a fine-grained diagnosis.

---


### 282. [Staged Continual Adaptation of Multimodal Foundation Models for Japanese Financial Documents](https://arxiv.org/abs/2610.27904)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Genshin Kakimoto, Atsushi Yanagisawa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Staged post-training of multimodal foundation models chains vision-language alignment, reasoning distillation, and domain tuning, yet how each phase trades capabilities against the others remains under-characterised. Tracking an 8.4B-parameter model from an un-fine-tuned baseline through three training phases on Japanese financial documents (evaluated on five text-input benchmarks), we find the phases interact non-additively: math-only distillation overwrites the financial knowledge acquired earlier even as procedural math skill survives, and the domain phase repairs more than it installs. A skip-phase ablation is best for domain knowledge but forfeits numerical-reasoning gains, so per-phase contributions are not decomposable and the best checkpoint is task-dependent, with implications for checkpoint retention and scheduling rather than added stages.

---


### 283. [On-Policy Transition Distillation](https://arxiv.org/abs/2610.28048)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Runyang You, Yongqi Li, Tiezheng Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) consolidates expert capabilities into a single student by matching teacher and student final-layer distributions on student-generated rollouts. We investigate whether depthwise prediction transitions, the changes in predictions between layers, can provide additional task-relevant supervision. Our diagnostic study finds that stronger teacher--student agreement in intermediate transitions is associated with higher answer correctness within questions, with correct responses exhibiting lower mean transition KL across all measured intermediate layer pairs. These observations motivate On-Policy Transition Distillation (OPTD), which augments final-layer distribution matching by aligning teacher and student layer-to-layer log-probability increments on student-generated rollouts. Evaluations across three backbones and eight benchmarks spanning mathematics, coding, and instruction following show that OPTD achieves the best or tied-best overall performance in both dual- and three-domain distillation. In the three-domain setting, OPTD recovers $\approx 90\%$ of the overall teacher--student capability gap, compared with $\approx 75\%$ for OPD.

---


### 284. [IECG: Weakly-Supervised Interpretability-Enhancing Foundation Model for Electrocardiogram](https://arxiv.org/abs/2610.28083)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Huynh Dang Nguyen, Trong-Thang Pham, Anh-Thuan Do 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electrocardiography (ECG) is a cornerstone of cardiac diagnosis, yet most machine learning methods for ECG analysis lack interpretability, limiting their clinical adoption. We present IECG, a weakly-supervised ECG foundation model that jointly performs diagnostic classification and abnormality localization without requiring manual abnormal region annotations, overcoming a long-standing bottleneck in interpretable ECG learning. Central to IECG is a weakly-supervised attention strategy that explicitly incorporates clinical priors by deriving abnormality heatmap pseudo-labels from established ECG clinical knowledge. These pseudo-labels guide the model's CLS-token attention through a KL-divergence loss, encouraging it to focus on diagnostically relevant waveform regions. During pretraining, IECG is jointly optimized with clinically guided attention supervision, ECG-text contrastive alignment, and report captioning objectives, enabling it to learn rich multimodal representations while producing localized waveform evidence. By explicitly aggregating features from clinically guided attention regions, IECG grounds its diagnostic predictions in interpretable waveform evidence without sacrificing classification performance. Extensive experiments demonstrate that IECG achieves state-of-the-art abnormal region localization while maintaining strong classification performance, advancing trustworthy foundation models for ECG analysis.

---


### 285. [Offline Makes Online Better: Calibrated Cache Compression for Video Generation](https://arxiv.org/abs/2610.28192)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhen Wang, Ning Lai, Qingtao Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Token merging is an effective approach to reducing KV-cache memory consumption in autoregressive video generation by clustering temporally redundant tokens and retaining only a small set of representatives. Existing methods, however, typically apply a uniform merging ratio across all attention layers and heads. We observe that different layers and heads exhibit substantially different yet jointly correlated sensitivities to token merging, and that these sensitivity patterns remain consistent across prompts. Based on this observation, we introduce CALM, a Calibrated Allocation for Layer-Head Merging that uses offline calibration to improve online cache compression. Exhaustively evaluating all possible layer-head allocations is prohibitively expensive. To enable efficient calibration, we show that attention-output error strongly correlates with end-to-end video quality and can therefore serve as a lightweight proxy for allocation risk assessment. We evaluate different allocation strategies using this proxy and construct a fixed layer-head risk map offline. Given a cache budget at inference time, CALM uses dynamic programming to determine the best allocation of merging ratios. Experiments across three different autoregressive video models demonstrate that CALM consistently outperforms uniform token merging under the same memory budget, by reducing the LPIPS to original videos by around 21% with higher video-quality scores.

---


### 286. [Parameter-Efficient Adaptation of Time Series Foundation Models for Electrical Load Forecasting](https://arxiv.org/abs/2610.28200)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aliullah, Julian Oelhaf, Edouard Fouché 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate electrical load forecasting supports power-system operation across countries, regions, cities, and buildings, but repeated development of target-specific models is costly. Time series foundation models (TSFMs) provide reusable pretrained backbones, although multi-domain pretraining may not fully capture load-specific characteristics. This paper compares pretrained inference, full fine-tuning, and low-rank adaptation (LoRA) in terms of forecasting accuracy and adaptation efficiency across four electrical load aggregation levels. MOIRAI 1.0 Large serves as the primary backbone, while Chronos-2 assesses whether the findings transfer across model families. The evaluation covers both in-distribution (ID) and out-of-distribution (OOD) settings and examines whether compact adaptation provides consistent gains over strong pretrained checkpoints. Pretrained foundation models outperform the implemented seasonal naive and XGBoost baselines across the evaluated aggregation levels. On MOIRAI Large, rank-16 LoRA reduces normalized mean absolute error (NMAE) by 7.5% on average while updating 3.146 million parameters, about 1% of the model, and retains most of the improvement from full fine-tuning. Chronos-2 achieves lower pretrained NMAE than MOIRAI but benefits less from adaptation. OOD results show that adaptation benefits vary by target, with the clearest gains for the local-area series and several buildings. Overall, LoRA provides a favorable accuracy-efficiency trade-off when adaptation yields a meaningful gain over a strong pretrained checkpoint.

---


### 287. [MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2610.28201)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu Cui, Hong He, Ruiqing Yue 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) of agent harnesses has emerged as an effective approach to enhancing the capabilities of large language model (LLM) agents. By searching the harness space for a specific LLM on a given dataset, RSI can discover a harness tailored to the capabilities and behavioral characteristics of that model. However, such optimization often creates a strong coupling between the learned harness and its target LLM, limiting generalization across models and requiring substantial computational resources to adapt to new LLMs. Moreover, existing RSI methods typically optimize a harness using feedback from a single model and evaluate its generalization to other models only after training. This paradigm treats model differences primarily as a criterion for evaluating generalization rather than as valuable evidence for optimization. In this paper, we introduce a new perspective that treats models as data and places the harness at the center of optimization. Building on this perspective, we propose \textsc{MaD-RSI}, a framework that directly optimizes a shared harness across multiple heterogeneous LLMs by incorporating their diverse failure trajectories into the training process. Rather than assessing model differences only after optimization, \textsc{MaD-RSI} leverages these differences as training evidence to guide the self-improvement of a shared harness. Furthermore, we introduce a new evaluation framework with two complementary metrics designed to assess the effectiveness of harness optimization across models. Experiments across multiple datasets and LLMs demonstrate that \textsc{MaD-RSI} improves generalization over existing approaches while reducing training costs.

---


### 288. [Convergent Performance, Divergent Mechanisms in LoRA-Adapted Vision Foundation Models for Brain MRI](https://arxiv.org/abs/2610.28255)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Cecilia Diana-Albelda, Fiona Kekwick, Raghav Mehta 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting Vision Foundation Models (VFMs) to medical imaging via LoRA has become standard practice, yet model selection is guided almost entirely by downstream task metrics, treating backbones with similar performance as interchangeable. We investigate whether equal performance implies equal internal representational shift. We analyse four ViT-B/16 backbones, DINOv3, SigLIP2, MerMED-FM, and BiomedCLIP, pre-trained with different objectives (self-distillation vs. contrastive vision-language) and on different data domains (natural vs. medical images). We adapt each to brain tumour segmentation and evaluate on six datasets covering both segmentation and Alzheimer's disease classification. Using attention divergence, weight-change analysis, and activation patching, we find that the four models converge to similar segmentation performance (mean Dice 78-81%) through markedly different internal dynamics, yet diverge in cross-task transfer: segmentation adaptation improves Alzheimer's disease classification for DINOv3 but degrades it for the other three backbones. We reveal a dissociation between modification magnitude and causal importance: the most heavily modified layers are not the causally relevant ones, with early-to-mid layers identified as sufficient for segmentation recovery. Restricting LoRA to these layers matches or approaches full-layer segmentation while reducing classification degradation in the three affected backbones, providing a mechanistically grounded strategy that is more parameter-efficient and more robust than standard full-layer adaptation.

---


### 289. [ChartEvo: Self-Evolving Agent Harnesses for Long-Tail Chart Reasoning](https://arxiv.org/abs/2610.28282)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qi Wang, Peijie Wang, Jun Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have substantially advanced chart understanding and reasoning, yet their performance remains highly uneven across chart types. While modern MLLMs perform well on common charts, their accuracy drops sharply on long-tail charts with diverse visual structures and reasoning requirements. Tool-augmented agents can improve complex chart reasoning by introducing specialized visual capabilities, but manually engineering strategies and tools for the heterogeneous and evolving long tail is difficult to scale. We introduce \textbf{ChartEvo}, a recursive self-improvement framework that enables chart agents to adapt to underperforming chart types through experience-driven harness-level self-improvement. ChartEvo jointly evolves reusable chart-specific Skills and executable Tools, while learning reusable local tool-call chains to compose evolved capabilities and control the inference overhead of tool-augmented reasoning. On long-tail charts from ChartBench and ChartX, ChartEvo improves accuracy over its base MLLM, Qwen3.7-Plus, by \textbf{45.6\%} and \textbf{32.5\%}, respectively, demonstrating the effectiveness of recursive self-improvement for long-tail chart adaptation.

---


### 290. [Adaptive Replay Refinement: Allocating Test-Time Compute Between Revision and Resampling](https://arxiv.org/abs/2610.28294)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling allocates additional inference compute to refining existing solutions or generating new ones. This raises a fundamental question: Should I keep improving this solution, or stop working on it and try a completely new solution? Existing methods make this decision using fixed refinement schedules, self-verification judgments, or learned controllers, which can waste compute or rely on signals that may be incorrect or require additional training. We introduce Adaptive Replay Refinement (ARR), a training-free method that detects when a stationary revision reaches a fixed point and reallocates the released compute to a new independent sample; replay decoding treats the current solution as a draft and verifies unchanged tokens in parallel, enabling efficient fixed-point detection. Across seven models from five families and seven benchmarks, ARR matches majority voting on three of five mathematical reasoning benchmarks at equal compute, while reducing critical-path serial passes by up to 2.4 times. On MATH500, ARR achieves 84.6% accuracy with only 41% of the serial passes required by majority voting. These results demonstrate that detecting refinement exhaustion enables adaptive reallocation from revision to independent sampling, improving inference efficiency while highlighting the limits of self-revision. Code is available at this https URL.

---


### 291. [Towards Consistent Geospatial Representations: Aligning One Encoder to Many Foundation Models](https://arxiv.org/abs/2610.28313)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Arthur Ouaknine, David Rolnick  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models (GFMs) differ widely in pretraining objective, modality and resolution, and none leads across benchmarks. We ask whether their representations are complementary, and whether a single encoder can inherit that complementarity. We introduce Pangaea-Latents, an extension of the Pangaea benchmark providing frozen embeddings of $5$ GFMs over its $11$ datasets, along with reproduced baselines, and find GFM embeddings to be neither redundant nor disjoint. We then propose GeoMixture, a preliminary framework to align a ViT to several GFMs per dataset through a multi-representation alignment (mREPA) objective. Our encoder ties the best GFM in average rank across nine Pangaea datasets, trading peak performance for cross-task consistency.

---


### 292. [Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented Design](https://arxiv.org/abs/2610.28380)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Gaotang Li, Bhavana Dalvi Mishra, Yifei Ming 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent harnesses are executable code that specifies the prompts, tools, and control flow around a language model. A single global harness can struggle with heterogeneous tasks that require different execution strategies. In this work, we introduce Object-Oriented Harness (OO-Harness), a harness optimization framework that evolves a hierarchy of executable harness classes using object-oriented design. During training, an evolution agent uses execution records to create a family of specialized harnesses, each implemented as a subclass of the base or an existing specialized harness via inheritance. At test time, a harness router uses routing lessons accumulated during training to select a specific harness for each task. Across three long-horizon benchmarks spanning business workflows, workspace tasks, and tool use, OO-Harness achieves the best performance among the compared methods, with an absolute improvement of up to 15% over the base. Extensive ablation studies examine the contributions of its core components.

---


### 293. [RACE: RoPE-Aligned Attention Compression Based on Query-Key Activation Energies](https://arxiv.org/abs/2610.28385)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Irene Tenison, Abdulrahman Alabdulkareem, Daniel Karl I. Weidele 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Head-dimension compression can reduce the memory required by the key-value (KV) cache, but existing methods often reconstruct full-dimensional representations during inference, adding significant decoding FLOPs overhead. We formalize the design considerations for converting pretrained attention into a natively reduced-dimensional form that reduces both KV-cache storage and attention computation using a calibration set. Specifically, we consider reductions that (1) apply a shared projection to queries and keys so that they remain in a common reduced feature space, (2) derive this projection jointly from query and key activations to better preserve their interaction, and (3) are compatible with the pretrained RoPE transformation. To obtain a reconstruction-free realization of this reduction, we restrict it to coordinate selection and theoretically show that RoPE compatibility then holds if and only if complete rotary pairs are retained. Building on this characterization, we introduce RACE, a post-training method that selects rotary pairs using their joint query-key activation energy. We theoretically show that this criterion minimizes a separable, calibration-dependent upper bound on post-RoPE query-key product approximation error. The resulting reductions are folded into the model weights and require neither runtime reconstruction nor specialized kernels. Across three model families and different compression levels, RACE outperforms structured pruning and remains competitive with reconstruction-based methods on language-modeling, zero-shot, and long-context tasks. At 50% KV-cache retention and 256K context, RACE reduces total inference FLOPs by 47.8%, yielding 1.79x higher throughput, 43.2% lower time-to-first-token (TTFT), and 28.1% lower allocated GPU memory in comparison to an uncompressed model.

---


### 294. [Brain2Vec: A Self-Supervised 3D Foundation Model for Structural Brain MRI](https://arxiv.org/abs/2610.28411)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Spiros Maggioros, Guray Erus, Gareth Harman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models have become essential tools in medical imaging, yet training them end-to-end for diverse tasks remains challenging due to limited labeled data and computational constraints. To address this, we introduce Brain2Vec, a foundation model pre-trained on 74,425 T1-weighted Magnetic Resonance Imaging (MRI) scans pooled from multiple studies. Brain2Vec can serve both as a weight initialization backbone for fine-tuning downstream tasks and as a standalone feature extractor. We evaluated Brain2Vec in three tasks: downstream predictive performance, convergence speed, and embedding quality. Using Brain2Vec's pretrained weights as initialization and fine-tuning on labeled data for a brain age prediction task, results demonstrate improved final accuracy and faster convergence compared to random initialization. Additionally, its frozen embeddings outperform anatomically defined volumetric features on four of five downstream classification tasks and perform competitively with a state-of-the-art foundation model pre-trained on substantially more data. Lastly, we show that Brain2Vec encodes information primarily from a spatially localized and neuroanatomically meaningful set of brain regions, and that manipulating a subset of latent features produces monotonic, region-specific effects on the reconstructed anatomy. Brain2Vec code and trained models are available as an open-source package on this https URL. Users can apply Brain2Vec locally by installing the package, or directly through the NiChart cloud platform this https URL, where Brain2Vec features can be derived without requiring local installation or specialized infrastructure.

---


### 295. [Beyond 4 bits: Data-Centric Post-training Quantization and Recovery](https://arxiv.org/abs/2610.28537)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rhea Sanjay Sukthanker, Riccardo Grazzi, James Hensman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) compresses the weights of a trained model with limited compute and data. Down to 4 bits it is near-lossless, but at 2 bits scalar PTQ configurations fall to chance-level accuracy. We study three choices usually treated as implementation details that matter little at 4 bits but decide 2-bit quality: the quantization representation, the calibration data, and the recovery fine-tuning data, across six dense and mixture-of experts models (ranging from $3.8$ to $32$B parameters). Representation is the largest factor and vector codebooks restore usable models where scalar PTQ pipelines collapse. Most of the remaining loss in accuracy is on \emph{generative} tasks, and the amount of performance drop is model-dependent. Furthermore, at a short recovery budget, calibration and recovery data are coupled. The best recovery data depends on the calibration data, so the two must be chosen jointly. The resulting recipe involves a vector codebook representation, a small task-aligned calibration mixture, and an inexpensive codebook-only recovery stage. Including codebooks, it uses about $2.3$ effective bits per weight and retains $89$ to $97\%$ of full-precision question-answering (QA) accuracy where scalar PTQ is at chance, and, including recovery, uses $1.4$ to $30\times$ less compute than the strongest quantization-aware-training (QAT) baseline.

---


### 296. [Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition](https://arxiv.org/abs/2610.28578)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenjie Lou, Tianshuo Peng, Shiyang Feng 等 99 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach during execution. Sage-A1.5 highlights three improvements: agentic orchestration, verification, and open scientific discovery. First, agentic orchestration extends single-agent execution through task delegation and parallel collaboration among subagents with isolated contexts, enabling complex tasks to be decomposed and addressed concurrently and supporting efficient execution while reducing interference across concurrent subagents. Second, agentic verification strengthens long-horizon reliability through progress checking, evidence validation, and reflective strategy revision, allowing the agent to recognize unproductive search paths and pursue alternative approaches. Third, open scientific discovery extends agentic capabilities beyond answering predefined questions to conducting exploratory research, connecting scientific inquiry with interactive analysis and inspectable research artifacts. We showcase these capabilities through complicated agentic tasks and multidisciplinary scientific applications. Besides, we hope Sage-A1.5 provides the community with an accessible foundation for open scientific discovery, offering a practical path from long-horizon task execution to collaborative, verifiable, and inspectable scientific exploration.

---


### 297. [Turning TS2Vec into a Foundation Model for Time Series Classification](https://arxiv.org/abs/2610.28602)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Vasilii Feofanov, Zhenghan Tai, Andrei Ermakov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TS2Vec is one of the strongest self-supervised methods for time series classification, introduced in 2022. It is designed to be trained anew on every dataset: self-supervised pre-training followed by linear probing. Since then, the field has shifted towards foundation models that reuse one encoder across datasets. Yet TS2Vec offers a compact convolutional architecture that operates directly on temporal samples and accepts variable-length inputs without resampling. We ask whether these properties can be retained when the encoder is pre-trained only once, and show that they can: TS2Vec can essentially be turned into a foundation model. Three changes suffice: pre-train on a synthetic corpus, feed the encoder a raw amplitude view and an instance-normalized shape view of the input through two small stems, and distill one specialist encoder per view into a single encoder. The result, TS2Vec-FM, is a 1.6M-parameter dilated convolutional network that, kept frozen, reaches 83.3% on UCR-128 and 75.3% on UEA-27 under linear probing, within 0.3 pp of MantisV2, the current state of the art, and above TS2Vec trained separately on each target dataset. What we find most interesting is how different TS2Vec-FM is from other foundation models in design: near-parity is reached without attention, without a patch tokenizer, and without intermediate-layer extraction, using an "old-school" convolutional encoder and a two-layer MLP stem.

---


### 298. [Planning under Noise with Neural Operators](https://arxiv.org/abs/2610.28623)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Michael Chen, Hong Chul Nam, Xi Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planning under uncertain control execution noise requires reliable feedback policies across diverse environments. We introduce Planning Under Noise (PUN), a neural operator that learns noise-aware value fields for planning in unseen geometries. Building on an established screened-Poisson formulation of stochastic optimal control, we address two challenges: specifying boundary conditions that support navigation across varying geometries and efficiently computing fields with reliable gradients. Zero-Dirichlet obstacle boundaries terminate sampled paths at walls, weakening the goal signal along long routes and making it harder to estimate reliably. We instead impose reflecting Neumann conditions on obstacles and a Dirichlet condition at the goal, allowing sampled paths to continue exploring free space until they reach the target. To solve the resulting PDE without a configuration-space mesh, we extend a Monte Carlo (MC) solver, Walk on Stars (WoSt), to higher dimensions. However, local MC fluctuations can reverse estimated gradient directions and cause planning failures, making direct planning require costly sampling. PUN amortizes this computation by learning geometry-to-field mappings from noisy, partially converged Monte Carlo labels, avoiding expensive convergence for every training example. At inference, test-time scaling uses bounded local search guided by the predicted global field. We evaluate PUN on planning tasks across dimensions. Across four noise levels, PUN matches or outperforms all compared planners, achieving 95-100% success on the 4D replanning benchmark while maintaining the lowest runtime. At the highest tested noise level in 4D, PUN achieves 10.7-60.6% relative gains in success rate over other methods while running 3.29-32.15 times faster.

---


### 299. [PsycheMME: A Psychology-Informed Benchmark for Social Understanding and Interaction in Videos](https://arxiv.org/abs/2610.28625)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Heran Hu, Yuhang Dong, Zhucun Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human needs and selecting responses require distinct judgments that aggregate accuracy can obscure. We introduce PsycheMME, a video benchmark informed by psychology, with eight capabilities spanning grounding, states, needs, interaction decisions, memory, and risk. Drawing on Social Information Processing and the Perception-Action Cycle, this organization separates human understanding from response selection. We construct 1,000 questions from 630 episodes through independent answering with proposed references withheld and expert review. Our Reasoning-Verified protocol weights answer credit by the support and logical consistency of explicit rationales against annotated cues. Across 17 models, Timing has the lowest Verified scores and credit retention, with weaker support judgments for correct Timing answers. Models with similar Need scores still differ in answer completeness on open questions. Input controls and SFT/GRPO examine context dependence and adaptation. Evaluating answers alongside rationales locates where models fail across understanding, response selection, and justification.

---


> [!TIP]
> 当前位于：**251-299**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-299**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
