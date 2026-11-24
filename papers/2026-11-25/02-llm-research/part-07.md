# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

---

### 301. [ESGPT: A Data-Centric ESG Language Model with Unified Instruction and Benchmark Resources](https://arxiv.org/abs/2611.30052)

**<font color=#1a73e8>作者：</font>** Jaeyoung Lee, Misuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ESG analysis requires complex language understanding across diverse sources, including corporate reports, news, and disclosures, for tasks such as ESG relevance detection, action interpretation, impact analysis, and question answering. However, existing ESG datasets are fragmented by task and source, with heterogeneous formats and annotation schemes, limiting their use for training general-purpose ESG LLMs and unified evaluation. In this work, we construct ESG-Instruct, a 30,000-instance ESG instruction dataset built from public ESG resources, and ESGU-Bench, an ESG understanding benchmark covering six representative ESG tasks. Based on these resources, we further develop ESGPT, an 8B ESG-specialized LLM, and evaluate it against diverse open-source and API-based LLMs. Experimental results show that general-purpose LLMs exhibit substantial performance variation across ESG tasks, while ESGPT, despite its relatively small scale, achieves the best performance on multiple ESG tasks. This work provides unified data and benchmark resources for training and evaluating ESG-specialized LLMs.

---


### 302. [Beyond Binary Correctness: A Surrogate for Confidence Learning in Large Language and Vision-Language Models](https://arxiv.org/abs/2611.30059)

**<font color=#1a73e8>作者：</font>** Chen Li, Xiaoling Hu, Chao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Confidence estimation for large language models (LLMs) and vision-language models (VLMs) aims to assess how likely a particular generated response is to be correct. We investigate how learning this assessment can benefit from the model's predictive reliability on the underlying query. Binary correctness supervision, however, assigns identical labels to occasional errors and frequent failures, as well as isolated successes and consistent success. These outcomes can arise from substantially different predictive behavior under stochastic decoding. We propose a confidence-learning framework that supplements realized response correctness with query-level predictive reliability. We estimate reliability through repeated generations under a fixed model and decoding configuration, then combine the empirical success rate with individual correctness to construct a graded confidence surrogate. The surrogate differentiates responses sharing the same correctness label while preserving the average predictive reliability of the sampled response pool. To learn this target, we condition an independent confidence estimator on the query and its full generated response, and optimize backbone LoRA adapters together with a projection and scalar confidence head using mean squared error. Repeated sampling is required only for supervision construction; inference scores an individual response without additional generations. We establish ordering and mean preservation properties of the surrogate and derive a selective-risk bound connecting population surrogate prediction error to the error rate among accepted responses. We evaluate the framework across language and vision-language models, examining confidence calibration and selective prediction.

---


### 303. [Pixel as the Common Language: Unified Multimodal Embedding via Visual Rendering](https://arxiv.org/abs/2611.30069)

**<font color=#1a73e8>作者：</font>** Xu Yuan, Pangjing Wu, Wenqi Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal embedding models map heterogeneous inputs into a shared representation space, yet text-only, image-only, and composed inputs are still presented in distinct formats and follow different routes through the model. This fragmentation prevents heterogeneous tasks from jointly optimizing the same end-to-end encoding process, limiting supervision transfer across input configurations. To address this issue, we propose unification before encoding and instantiate this paradigm in RenderEmbed. The framework uses Visual Substrate Rendering to convert heterogeneous inputs into a common visual substrate for encoding with a VLM. From the resulting visual tokens, Progressive Hierarchical Anchor Encoding produces compact retrieval representations by interleaving learnable anchors and fusing their states across layers, retaining broad context and fine-grained cues. Interventional Rendering Learning trains these representations to remain sensitive to content changes and stable across rendering variations through complementary semantic and rendering interventions. Extensive experiments on MMEB and ViDoRe v2, spanning diverse retrieval tasks, show that RenderEmbed outperforms prior state-of-the-art models at the same scale and exhibits strong out-of-domain generalization. Compared with MetaEmbed, RenderEmbed improves MMEB Overall Precision@1 by 1.7 points, with a larger 2.1-point gain on out-of-domain tasks. Transfer and scaling analyses further show that a shared visual pathway enables more effective learning from heterogeneous supervision.

---


### 304. [Context-Grounded Skill Internalization for Vision-Language Agents](https://arxiv.org/abs/2611.30075)

**<font color=#1a73e8>作者：</font>** Jinlin Liu, Yumeng He, Qihan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill internalization offers a way for agents to learn useful behaviors from skills and use them without explicit guidance in context at inference time. A common approach is to generate demonstration trajectories with the skill in context and then fine-tune the same model on its own trajectories with the skill removed. However, this leads to the problem that the model may learn to reference the removed skill, which we named as context misalignment (CoMi). In this work, we first analyze agent behaviors related to CoMi under this common pipeline. Across ALFWorld, WebShop, and ARC-AGI-1, skill-removed fine-tuning consistently results in CoMi: 12.2-46.0% of test trajectories reference the removed skill. To address this problem, we develop Context-Grounded Skill Internalization (CGSI). CGSI uses a sentence detector to identify unsupported references and then masks or rewrites the selected sentences before fine-tuning. Experimental results demonstrate the effectiveness of CGSI and reveal two key findings. (i) Compared with directly fine-tuning with the skill removed, CGSI reduces CoMi at test time by 72.5-94.6% while preserving task success. (ii) Compared with existing reinforcement learning-based skill-internalization baselines, CGSI achieves comparable performance with substantially less training time. CGSI also significantly reduces processing costs compared with large-scale trajectory auditing and correction.

---


### 305. [Post-Training Agents for Long-Document Reasoning](https://arxiv.org/abs/2611.30090)

**<font color=#1a73e8>作者：</font>** Sushant Mehta, Logan Ritchie, Edwin Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Professional documents are a long-context workload that retrieval-style benchmarks do not capture. In a ten-domain enterprise collection, a task's evidence is spread across a source document of median length 27 pages (mean 48.8, maximum 873); a third of tasks rest mainly on charts, drawings, and maps; and 70.9% require two or more reasoning hops. We post-train Kimi-K2.7, an open-weight foundation model, at its full context window on 1,465 expert-authored tasks with atomic rubrics from that collection, training rank-32 adapters with one round of privileged-context on-policy self-distillation followed by two rounds of rubric-reward reinforcement learning. We render each PDF as text for training and as extracted text plus selected page images at evaluation. The smoothed RL training reward rises from 0.37 in the first tenth of the run to 0.67 in the last. On the 100-task this http URL holdout, served in a 262,144-token window, strict pass (all rubric criteria met) more than doubles after the second round, from 11.0% to 24.5%, with gains across input lengths up to 240K tokens. Mean tokens generated stay flat (9,803 to 9,733), so the gain does not come from longer outputs. GPT-5.6 Sol's leaderboard strict pass is 30.7% at a measured 3,422 tokens. On 220 out-of-domain GDPval tasks, where the model runs as a long-horizon tool-using agent, mean rubric reward rises from 0.571 to 0.746 after the third round and zero-credit tasks fall from 54 to 10, while messages per task fall 18%, from 70.9 to 58.2. In paired trajectories, the third round replaces a context-thrashing retry loop with one up-front check of all sources, and verification extends from checking that files exist to checking what they contain. We argue that long-context evaluation of agents should report accuracy jointly with tokens and turns, and that datasets of long documents should ship text and image renderings alongside each PDF.

---


### 306. [Character Information in Language Models: A Prompt-Independent Word Store and a Late, Question-Driven Signal That Grows With Scale](https://arxiv.org/abs/2611.30094)

**<font color=#1a73e8>作者：</font>** Pratyush Acharya, Nuraj Rimal, Apar Baral 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear probes recover character properties of a word from a language model's hidden states, but a probe at the answer position cannot say whether the property was stored with the word or produced because the prompt asked for it. We separate the two with a word-position baseline: the same held-out-word probe applied to the query word's own tokens in a sentence that asks nothing. Across 16 open-weight models from seven families (0.6B--14B) and eleven character tasks, the word tokens encode \texttt{first\_letter}, \texttt{last\_letter} and \texttt{most\_frequent\_letter} above a word-only nuisance floor in all 16 models, and about 70\% of that signal is already present in the token embedding. Asking the question adds a second signal at the answer position. Its size grows with model scale for all four prompt-sensitive tasks (Holm-corrected permutation $p \leq 0.018$, also within model families), and the growth is confined to the late layers: restricted to the first quarter of the network, the slope is indistinguishable from zero. Small models' answer positions hold less linearly decodable signal than their word-level store; large models' hold more. Four controls bound these claims. Measured against the nuisance floor, the question-free signal that a majority-baseline analysis counts as retained largely disappears (\texttt{last\_letter}: $-0.01$). Count tasks become measurable only after length, repetition and query-letter shortcuts are removed by design. A pre-registered test finds that a question placed before the word does not change the word's own encoding beyond what an arbitrary prefix change does. Representation--readout gaps show no robust scaling once probe saturation is accounted for. Pre-registered criteria, a fixed estimator (held-out layer selection, cold-start folds) and all analysis code accompany the paper.

---


### 307. [Could This BE Any More Wrong? Teaching VLMs to Know What They Don't Know in Document Extraction](https://arxiv.org/abs/2611.30119)

**<font color=#1a73e8>作者：</font>** Varad Srivastava, Victor Casas Hernandez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models can extract structured fields from scanned financial documents, yet they provide no indication of when a field might be wrong. We derive per-field confidence estimates from the token log-probabilities the model already produces, via a token-to-span alignment procedure that maps logprobs onto each extracted value within the structured JSON output. Evaluated on two benchmarks (CORD v2 receipts, Kleister NDA legal contracts) with three VLM families, the minimum token probability per field achieves Area Under the ROC Curve (AUROC) 0.74-0.91 for error detection, far exceeding verbalized confidence (0.53-0.56). The uncertain fields form a natural training curriculum: fine-tuning via Group Relative Policy Optimisation (GRPO) improves accuracy from 78.5% to 87.5% on CORD (67 examples) and from 70.7% to 75.1% on multi-page NDA contracts (259 examples), while substantially improving error detection on Kleister NDA (AUROC 0.70 to 0.85, Area Under the Accuracy-Rejection Curve (AUARC) 0.78 to 0.92). The loop requires no annotation beyond the training-split ground truth, demonstrating that confidence-guided curriculum selection transfers to complex multi-page documents when combined with native multi-image training. A frontier model (Claude Sonnet 4) used as a pseudo-label judge achieves ~92% reward agreement with ground truth on both benchmarks, suggesting this loop can operate without human annotation.

---


### 308. [Parameter-Efficient Vocabulary Expansion via Cross-Lingual Embedding Alignment](https://arxiv.org/abs/2611.30123)

**<font color=#1a73e8>作者：</font>** Andrew Ivan Soegeng, Muhammad Reza Qorib, Weishi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual pretraining with vocabulary expansion is often used to make large language models (LLMs) more effective and efficient at handling new languages. However, when LLMs are extended to many languages simultaneously, the number of model parameters increases significantly. In addition, the newly added tokens do not receive the same number of training steps as the tokens in the original vocabulary, which sometimes causes vocabulary expansion to yield only limited performance improvements. We propose leveraging the semantic equivalence between words in the model's primary language and those in the extended vocabulary to transfer learned representations. In this paper, we introduce MATE, a parameter-efficient vocabulary expansion method that enables effective cross-lingual transfer with 8 times fewer additional parameters per token. MATE reduces the average tokenization compression ratio and delivers improvements on multiple benchmarks.

---


### 309. [When Does Optical Context Compression Pay Off? A Decode-Aware Cost Analysis of Reasoning VLMs](https://arxiv.org/abs/2611.30130)

**<font color=#1a73e8>作者：</font>** Ziqing Ge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rendering long text as images lets a vision-language model (VLM) read a document with fewer input tokens, and evaluations often count mainly these prefill tokens. We show that for reasoning models this accounting is incomplete. Across five models and two long-context benchmarks, reading the rendered document makes the model think longer: decode length grows by 1.5-3.5x on the four general-purpose VLMs tested, and under typical output pricing this decode tax makes image input more expensive than text for two of the five models on QuALITY. Unrecoverable information loss is not sufficient to explain the tax at moderate compression: Qwen's OCR of the same images recovers 98.7% of words, and feeding Kimi-K3 its own transcription as text restores text-mode reasoning length and accuracy. Whether compression pays off reduces to an exchange rate, (1-1/c)/(r-1), that must exceed the workload's price-weighted ratio of output to input tokens; this accounting decomposition shows why Kimi-K3 and DeepSeek-V4.1-Flash can benefit and Qwen and GLM cannot. None of the training-free signals we test predicts the tax before generation. As a practical heuristic, an image-first policy that sends only inputs with a per-input compression ratio of at least 1.6 to images and falls back to text once image-mode reasoning costs as much as the input's prefill saving cuts the bill by 6-14% on Kimi-K3 and DeepSeek-V4.1-Flash at an accuracy cost of 0.3-1.2 points; on QuALITY, asking for a reasoning budget on both paths is a stronger lever.

---


### 310. [WASP: Continual Weight Adaptation for Streaming LLM Personalization](https://arxiv.org/abs/2611.30134)

**<font color=#1a73e8>作者：</font>** Linxi Xie, Chonghua Liao, Mengxuan Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized large language models (LLMs) should continually adapt to users' evolving preferences. Yet extracting preference changes from noisy interaction histories while supporting inexpensive updates remains challenging. We introduce WASP (Weight Adaptation for Streaming Personalization), a recurrent framework that captures fine-grained preferences directly from raw user interactions and generates personalized LoRA adapters without expensive per-user optimization. Specifically, WASP achieves this by training a shared hypernetwork that maintains a compact user representation and outputs adapter weights in a single forward pass. As new interactions arrive, WASP updates this representation without reprocessing full interaction history, enabling continual adaptation with per-update costs independent of history length. Experiments on personalization benchmarks and chronological interaction streams show that WASP sustains high-quality personalization over long horizons under fixed compute and storage budgets. Together, these results support efficient streaming personalization and facilitate privacy-preserving on-device deployment.

---


### 311. [AutoSECO: Automated Skill Evolution for Cross-Problem Combinatorial Optimization with General-Purpose LLM Agents](https://arxiv.org/abs/2611.30139)

**<font color=#1a73e8>作者：</font>** Zirui Zhu, Cong Zhang, Ni Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose large language model (LLM) agents can develop complete solvers for combinatorial optimization problems. Their specialization, however, often relies on workflows engineered for individual problems, limiting the reuse of development expertise. We propose AutoSECO, an automated skill evolution method that learns reusable solver-development guidance from experience. The challenge is that external evaluation measures the completed solver, while the skill guides decisions during development. AutoSECO connects this feedback to guidance deficiencies by tracing performance shortfalls through solver code and recorded development decisions. Revisions are expressed as general instructions and retained only if a fresh solver developed under the revised skill achieves a lower mean evaluation gap. Evolved solely on the traveling salesperson problem (TSP), the skill guides fresh agents in developing solvers for capacitated vehicle routing, job-shop scheduling, and three-dimensional bin packing without further skill evolution. On TSP, the final mean benchmark gap is 0.52\%, compared with 0.98\% for the skill-evolution baseline SkillOpt. Across all four problems, the evolved skill achieves better aggregate results than no skill guidance, the initial skill, and SkillOpt. The same frozen skill also supports solver development under alternative model--harness configurations. These findings suggest that solver-development experience can be retained as reusable expertise for general-purpose LLM agents.

---


### 312. [Reading the Tea Leaves, Again: Can Large Language Models Predict Language Model Training Runs?](https://arxiv.org/abs/2611.30141)

**<font color=#1a73e8>作者：</font>** Xinran Zhao, Xiang Li, Tong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents now propose research ideas and run the experiments that test them, but they train every run to its end, whereas a researcher reads a run's configuration and the beginning of its curve and stops the runs that show no promise. Reading a run this way takes more than describing or implementing a training method: it takes knowing what a design choice does to a run. We build Tea Leaves to measure this knowledge on 682 real training runs across pretraining, fine-tuning, and reinforcement learning (RL): a forecaster sees the first 20% of a run with its configuration, description, and code, and predicts the rest. Across 11 LLMs and a range of forecasting baselines, the strongest LLMs match or exceed the best curve fitter on smooth loss curves (skill 0.66 against 0.62) and lead on noisy RL reward curves (0.43 against 0.13). What bounds every forecaster is what the log carries: on sparsely logged community runs all methods lose most of their skill, and none reliably flags a failing run in advance. Beyond the curve, information helps and effort does not: related runs in the prompt cut the error on loss curves by 39%, and knowledge of training dynamics lets the strongest LLMs order all 36 pairs of runs that differ by a described code change, which the early curves do not separate, whereas tools add little. This knowledge can be learned from logged runs: a small open model trained on public runs matches the best LLM on loss curves. Applied to the progress curves of research agents, the same reading ranks tasks by their remaining headroom, although for a single agent run it does not improve on the last value. We release the benchmark, the trained readers, and their training data to test and train LLMs' understanding of training and to help research agents decide which runs deserve their compute.

---


### 313. [RMR-VLA: Recurrent Memory Reasoning for Vision-Language-Action Models](https://arxiv.org/abs/2611.30145)

**<font color=#1a73e8>作者：</font>** Yiheng Du, Jingqi Tian, Xu Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon, history-dependent robotic manipulation often requires acting on visual cues that have disappeared, such as an object indicated earlier or a target hidden under a moving cup. The key challenge is to maintain what past evidence means for the next action as the scene changes. We introduce Recurrent Memory Reasoning (RMR), an explicit reasoning step that connects memory to action inside a vision-language-action model (VLA), with no external reasoning model. At each update, the VLA first infers an event from visual evidence, then revises the task state and grounds a subgoal in the current scene to guide action generation. Carrying the state and subgoal across updates lets remembered identities and task progress determine the current target, doubling RoboMME success over an otherwise identical model without recurrence. Joint training lets one VLA both reason and act; because its memory decisions are text tokens with exact likelihoods, GRPO refines them from rollout rewards without making action generation stochastic. Among the compared methods, RMR-VLA achieves the best results on RoboMME (66.46% overall, 79.83% on the Reference category) and LIBERO-Mem (90.08%).

---


### 314. [STMemoLLM: A Spatial-Temporal Memory-Augmented LLM for Robust Traffic Forecasting](https://arxiv.org/abs/2611.30148)

**<font color=#1a73e8>作者：</font>** Jian Zhou, Binqing Wu, Zongjiang Shang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting is essential for intelligent transportation systems. However, traditional deep-learning models often rely heavily on high-quality observations. Recent LLM-based approaches incorporate pretrained knowledge to improve forecasting, but they remain sensitive to input perturbations and struggle to preserve long-term patterns. To address this, we propose STMemoLLM, a spatial-temporal memory-augmented LLM for robust traffic forecasting. STMemoLLM introduces memory prototypes to compress inputs into compact summary tokens while extracting reliable dynamics from residual signals, achieving a balance between stability and variability. Specifically, a memory-enhanced tokenizer encodes prototypes and sensor characteristics into attention biases to guide adaptive compression of correlated sensors into semantic summary tokens. A memory-calibrated router further evaluates contextual deviation, compression deficiency, and prototype alignment to identify reliable residual signals, which complement the summaries while suppressing noise. Extensive experiments on eight real-world datasets show that STMemoLLM achieves state-of-the-art performance. Additional experiments examine point masking, additive Gaussian noise, structured missingness, and limited training data, demonstrating strong robustness. Code is available at this https URL.

---


### 315. [Revisiting Continual Learning in Language Models: A Three-Interface Diagnosis of Stability and Plasticity](https://arxiv.org/abs/2611.30151)

**<font color=#1a73e8>作者：</font>** Keuntae Kim, Beomseok Lee, Hyunwoo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning in language models is commonly studied in the incremental learning (IL) setting, where a model learns a sequence of tasks and is evaluated through its final classifier or language-model (LM) head. This interface, however, does not indicate where forgetting occurs: a drop in accuracy may reflect representation degradation in the backbone, readout mismatch in the head, or both. We therefore argue that backward transfer (BWT) and forward transfer (FWT) should be interpreted as interface-dependent quantities rather than as single modellevel properties. We study three evaluation interfaces: the trained head, which is updated sequentially with the backbone; a probe newly trained on frozen backbone features; and a classifier-free backbone diagnostic. They measure deployed performance, recoverability under a new readout, and representation separability, respectively. Across class-incremental experiments with encoder and decoder language backbones, plus task-incremental sanity checks, conclusions about forgetting and plasticity change with the interface: the trained head often indicates severe forgetting, the probe near-complete recoverability, and the backbone diagnostic intermediate representation drift with a consistent negative relation between stability and plasticity. This relation holds for clustering-free diagnostics such as nearest-class-mean accuracy and across five clustering algorithms and three metrics. Finally, Just LM-Head Tuning (JLT), a head-only intervention on a fixed incrementally trained backbone, recovers 96-99% of the gap to joint training for replayand distillation-based methods but only about three quarters for plain sequential fine-tuning, suggesting that many failures attributed to catastrophic forgetting reflect head-backbone mismatch plus partial representation drift. Our results call for reporting where forgetting is measured, not only how much.

---


### 316. [OpenViVE: New Benchmark and Dual-Stream Co-Attention Framework for Vietnamese Visual Entailment](https://arxiv.org/abs/2611.30161)

**<font color=#1a73e8>作者：</font>** Bao Quoc Trinh, Tin Van Huynh, Kiet Van Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Entailment (VE) determines whether a textual hypothesis is entailed, contradicted, or unverifiable from an image. However, existing VE benchmarks are largely English-centric and do not capture Vietnamese-specific linguistic distinctions or culturally grounded visual contexts. To address this gap, we introduce OpenViVE, the first large-scale native Vietnamese VE benchmark, containing 62,268 balanced image-hypothesis pairs from 10,378 culturally grounded images. OpenViVE is constructed using an Artifact-Aware Hybrid LLM-Human Pipeline that combines constrained generation, human validation, and PMI-guided refinement. The pipeline substantially reduces hypothesis-only shortcuts, with Contradiction accuracy dropping from 96% to 66% after artifact refinement. We further evaluate a dual-stream PhoBERT-ConvNeXt framework with bidirectional co-attention to align visual evidence with Vietnamese hypotheses. The framework achieves 84.84% accuracy and 84.90% macro-F1 on the test set, while PhoBERT consistently outperforms multilingual XLM-R variants. These results highlight the importance of language-specific encoding and explicit cross-modal interaction for Vietnamese VE.

---


### 317. [AdaptRouter: Adaptive Routing across Evolving Tasks and Models](https://arxiv.org/abs/2611.30162)

**<font color=#1a73e8>作者：</font>** Jingpu Yang, Fengxian Ji, Tianhao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model routing assigns each query to a suitable foundation model, but tasks and available models keep changing, and existing routers are either untrained for the pool at hand or fit once and forget earlier tasks when updated. We present AdaptRouter, an adaptive router trained by policy learning: a compact multimodal decision model reads each question with cards describing the current experts and learns from native task feedback, without routing labels, to select one frozen expert. Open-weight and API experts share the router, its inputs, and the quality-cost trade-off but use different losses: cheap open-weight experts are explored with RL, whereas paid API experts are queried once and their cached feedback is reused as soft labels. New tasks are learned without replay, new experts enter as cards, and an open-weight quality-first advantage provably keeps cost from overriding quality. Across four task stages, AdaptRouter loses at most 0.4 points on earlier tasks, whereas feedback-trained routers lose up to 7.0, and as its pool grows from three to ten experts, its accuracy rises from 67.2% to 72.1%. On five API models, it exceeds GPT-6.1 Sol and GPT-6 Astra (low) by over 22 points at under a third of their cost.

---


### 318. [Multimodal View Training: Learning More Through Different Modalities](https://arxiv.org/abs/2611.30165)

**<font color=#1a73e8>作者：</font>** Devang Kulshreshtha, Priyanka Kaswan, Minh Pham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a language model learn more from the same information simply by encountering it in different forms? We answer this in the affirmative by introducing Multimodal View Training (MVT), a simple training approach that presents identical information through text, speech, and images, without requiring new facts or supervision. Starting from a text sample, MVT generates corresponding audio and rendered-text image views, and trains a multimodal language model to produce the same target output across all three views. To further bring these benefits to text-only large language models (LLMs), we train lightweight connector modules to pretrained audio and vision encoders, allowing the LLM to learn from multimodal inputs while retaining its text-only architecture at inference. Across question answering, machine unlearning, and knowledge editing, adaptive MVT improves QA recall by +15.2 percentage points, forget quality by +40.7 points, and editing generality by +25.2 points over text-only training. Combining MVT with standard augmentation further improves QA and editing generality. Our theoretical analysis illustrates how training across modalities can shift weight updates toward shared factual content and reduce their reliance on features specific to each view.

---


### 319. [PathStream: Towards Streaming Diagnostic Copilots for Whole-Slide Pathology](https://arxiv.org/abs/2611.30167)

**<font color=#1a73e8>作者：</font>** Dankai Liao, YuFeng Wu, Ziyue Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathologists reach a diagnosis by integrating morphological evidence across regions and magnifications along viewing trajectories. Existing pathology AI rarely reflects this process: models predict from selected image regions, answer questions within fixed visual contexts, or navigate slides autonomously. We formalize pathologist-led streaming diagnosis, in which the pathologist controls navigation while a copilot selectively describes incoming views and synthesizes accumulated evidence into a final diagnosis. We record five pathologists' viewing trajectories on 1,791 TCGA whole-slide images (WSIs) spanning ten organs, with response labels, morphological descriptions, and session-level findings and diagnoses. We construct PathStreamBench to assess response timing, morphological description, and session-level diagnosis, alongside auxiliary video understanding. We introduce PathStream, which jointly learns streaming responses and diagnosis through two-stage training, with a diagnosis-attention loss guiding attention during diagnosis to relevant visual and textual evidence accumulated as the examination unfolds. PathStream outperforms 14 vision-language models and three domain-fine-tuned baselines on the core tasks, achieving a trajectory WSI Relevance score of 77.87, surpassing the strongest domain-fine-tuned baseline's 62.76. Without additional training, its diagnostic capabilities generalize to new educational pathology videos, three external centers, and an unseen organ.

---


### 320. [FiRE: Fine-grained Ranking Evaluation for Machine Translation](https://arxiv.org/abs/2611.30168)

**<font color=#1a73e8>作者：</font>** Wenyang Gao, Yinghao Yang, Xi Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing reliable machine translation (MT) systems hinges on our ability to distinguish superior translations from inferior ones. However, existing evaluation paradigms, whether limited to coarse overall rankings or misaligned with human preferences, fail to deliver interpretable, fine-grained feedback in reference-free settings. We present a Fine-Grained Ranking Evaluation method (FiRE) that leverages off-the-shelf large language models to perform criterion-driven pairwise comparison across three complementary dimensions: faithfulness, fluency, and consistency of style, instead of producing a single holistic judgment. To enable rigorous meta-evaluation of evaluation paradigms in the absence of any suitable testbed, we construct the first human-annotated, reference-free benchmark for fine-grained ranking evaluation, achieving substantial inter-annotator agreement. Through meta-evaluation on this benchmark and existing MQM datasets, FiRE demonstrably outperforms regression-based and error-analysis metrics in aligning with human comparative judgments, while providing more informative insights into translation quality. Finally, our examination of LLM evaluator biases (position and self-enhancement) and their handling of tied cases offers guidance for more nuanced MT evaluation. Code and benchmark resources are available at this https URL.

---


### 321. [Audio-Visual Rearrangement](https://arxiv.org/abs/2611.30171)

**<font color=#1a73e8>作者：</font>** Ruohao Guo, Jiatong Ye, Chenwei Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Audio-Visual Rearrangement (AVR), a novel task in which an agent hears a spoken request, retrieves a suitable object, and delivers it to the requesting user or an instruction-specified destination. AVR requires the agent to understand the spoken request and acoustically localize the speaker for delivery. To support this task, we construct a dataset covering three query types: explicit target specification, speaker-relative spatial references, and implicit user intent, spanning eight subtypes with diverse object selection and delivery requirements. Moreover, we propose a framework that integrates a motion-aware spatial audio module into an audio-visual large language model to encode spatial cues from the spoken request and update them as the agent moves. We further incorporate auxiliary supervision for speech understanding, spatial audio perception, and visual grounding through multitask instruction tuning to improve action prediction. Experiments establish baseline performance in both seen and unseen environments, laying the groundwork for future research on embodied intelligence and human-robot interaction. The code will be publicly available soon.

---


### 322. [OmniSenMo: A Unified Multisensory Language Model for Generalizable Human Motion Estimation, Understanding, and Prediction](https://arxiv.org/abs/2611.30176)

**<font color=#1a73e8>作者：</font>** Cheng Guo, Qiming Cao, Pu Perry Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) estimate, understand, and predict human motion, but mainly from RGB cameras. Depth, LiDAR, mmWave, and WiFi complement RGB under poor lighting, through occlusions, and in privacy-sensitive applications, but existing multisensory models cover only some of these sensing tasks. Covering all of them from any sensor subset is challenging, since the tokens of heterogeneous sensors are semantically inconsistent and spatially misaligned, paired multisensory data are scarce, and the tasks need different temporal granularities. We present OmniSenMo, a multisensory language model that takes the human skeleton as a common reference for all sensors. Its skeleton-grounded motion representation turns each sensor into joint tokens, one per body joint, so that any sensor subset is fused joint by joint and expressed in the motion vocabulary that the language model learned from motion capture and text. We pretrain it on all five sensors generated by our multisensory simulator, and Multi-Granularity Observation gives each task the frames it needs. On a cross-action split of MM-Fi, the same model with all five sensors outperforms the models compared on each task, including LEO-Fuse in pose estimation (84.1 vs. 89.0 mm MPJPE) and HoloLLM in unseen-action recognition (69.2% vs. 42.8%). Even without RGB, it outperforms both methods that use RGB, and in a cross-dataset validation on XRF55, it recognizes unseen actions far better than HoloLLM.

---


### 323. [Retrieval-Augmented Generation in the Agentic Era: Tradition, Present, and Prospect](https://arxiv.org/abs/2611.30181)

**<font color=#1a73e8>作者：</font>** Chenming Tang, Haolin Li, Yiran Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) couples frozen language models with external, updatable knowledge, so that generation is grounded in retrieved evidence rather than in parametric memory alone. This work maps RAG in the agentic era by joining them on a single lifecycle axis, from offline indexing through pre-retrieval, retrieval, post-retrieval, and orchestration over these stages. It treats indexing and orchestration as first-class components and agentic workflows as a paradigm of their own, and it covers the agentic work that has appeared since those reviews. Beyond these components, it covers evaluation, applications, and the questions that remain open for future exploration. From tradition to present and beyond, this work systematically reviews RAG from a perspective of the agentic era.

---


### 324. [PCC: Pivotal Channel Compensation for Layer Pruning of Large Language Models](https://arxiv.org/abs/2611.30183)

**<font color=#1a73e8>作者：</font>** Xiangqian Wang, Yucheng Zhang, Zhaohong Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Treating independent layers as the minimal pruning unit allows layer pruning to efficiently eliminate many redundant parameters and achieve high compression rates. Layer pruning has become a promising and prevalent structured pruning technique for large language models (LLMs). However, multi-layer removal can lead to significant performance degradation for LLMs. Although some works have explored various compensation methods for pruned layers, they are inefficient and costly. Observing that the expression of a large proportion of information is concentrated on a small number of pivotal channels, we propose a novel post-pruning compensation method for layer pruning, called pivotal channel compensation (PCC). PCC can achieve significant performance improvement by compensating for a small number of channels through learnable linear transformations at the pruning interface. Besides, we propose a new evaluation metric, called channel-wise average performance improvement (CAPI), which can measure the efficiency of channel-wise compensation. Our experimental results across various LLMs demonstrate that PCC can achieve significant and consistent improvements and high CAPI on language modeling and zero-shot question answering for the state-of-the-art cross-layer and consecutive-layer pruning methods. Compared with existing compensation methods, PCC can achieve competitive results with fewer additional parameters and less training cost.

---


### 325. [Visual-RFT++: Extending Visual Reinforcement Fine-Tuning to Multimodal Tool Use](https://arxiv.org/abs/2611.30193)

**<font color=#1a73e8>作者：</font>** Ziyu Liu, Zeyi Sun, Xiaoyi Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Fine-Tuning (RFT) has recently become a central paradigm for advancing Large Reasoning Models (LRMs), as demonstrated by systems such as OpenAI's o3 and the R1 series. Despite significant progress in LLMs, how to leverage RFT to unify visual perception, step-by-step reasoning, and agentic tool use into one coherent training paradigm remains an open challenge. In this work, we present Visual Reinforcement Fine-Tuning++ (Visual-RFT++), a unified framework that extends RFT to both visual perception tasks and multimodal agentic workflows, enabling LVLMs to reason with images, act upon images, and evaluate their own outputs using verifiable reward. With Visual-RFT++, open-source LVLMs not only show significant gains on diverse visual perception tasks, but also acquire agentic abilities such as web searching for real-time information and code-based image manipulation (e.g., cropping, rotation, and analysis). Across visual perception tasks, including fine-grained classification, few-shot detection, reasoning grounding, and open-vocabulary detection, Visual-RFT++ delivers strong gains over SFT, including a +24.3 percentage points improvement in one-shot fine-grained classification and +21.0 percentage points on COCO's 4-shot setting and +15.4 percentage points on LVIS with around several hundred samples. To evaluate agentic behaviors, we introduce the Multimodal Agentic Tool Bench (MAT) with MAT-Search and MAT-Coding. Visual-RFT++ surpasses its baseline by +18.6 F1 / +13.0 EM percentage points on MAT-Coding and +10.3 F1 / +8.7 EM percentage points on MAT-Search. It also shows gains of 29.3 F1 and 25.9 EM percentage points on multi-hop QA benchmarks such as 2Wiki and HotpotQA, demonstrating strong cross-modal generalization. Visual-RFT++ introduces a data-efficient and reward-driven framework that strengthens both visual reasoning and agentic adaptability.

---


### 326. [Quantization for Action, Execution for Deployment: Joint Precision and Execution Selection for World Action Models](https://arxiv.org/abs/2611.30195)

**<font color=#1a73e8>作者：</font>** Tianqi Li, Xin He, Xue Geng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models guide robots by predicting the effects of actions or generating commands from observations. A model may compare hundreds of candidate futures before acting, repeatedly reading weights that must fit in device memory. Post-training quantization reduces the number of bits used to store pretrained weights, but a smaller model is not necessarily a deployable one: temporary tensors can exceed graphics processing unit (GPU) memory limits, while even small prediction errors can change the selected action. This creates two coupled challenges: identifying bit assignments that preserve task performance and determining which of them meet real execution constraints, without exhausting costly task trials. We present PTQ4WAM, a framework for choosing layer-wise bit assignments and execution routes under memory, latency and task-evaluation budgets. Calibration measurements guide candidate proposals, optionally with a language model agent. We profile full-model routes on the GPU before spending task trials on feasible assignments. Fusing group rescaling and reading visual history in place can make an otherwise infeasible assignment deployable. Across 15 workloads from four model families, the median task score is 99.2% of the corresponding 32-bit floating-point (FP32) score. On fixed GPU replays, the median speedup over FP32 is 2.36 times and the median reduction in peak allocated memory is 71.5%. The code will be released soon.

---


### 327. [Laya-IsoToken: Day-One Clinical Codebook Switching via Closed-Form Operator Compilation](https://arxiv.org/abs/2611.30196)

**<font color=#1a73e8>作者：</font>** Zeqiang Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Healthcare systems periodically revise diagnostic and procedural classifications (ICD-9 to ICD-10/11), update hospital reimbursement groupers (MS-DRG), and deploy clinical coding across languages. Supervised coding networks bind clinical text encoders to fixed per-code classifier weights, forcing hospitals to re-annotate tens of thousands of records before switching codebooks, whereas standalone large language models incur high latency and hallucinate invalid codes. Here we show that day-one clinical codebook switching becomes feasible without target-labeled notes when local clinical evidence reading is decoupled from a strictly frozen multilingual concept space. Laya-IsoToken trains a clinical span reader once on source records with zero per-code classifier parameters, separating text evidence from historical disease prevalence. Given only public target code descriptions, closed-form matrix compilation aligns distributional shifts, compensates for paraphrased definitions, and deduplicates sibling codes in under three seconds, while a pre-deployment geometric residual routes unfamiliar concepts to offline language model verification. Across 32,804 MIMIC-IV ICD-9 discharges, Laya-IsoToken matches published supervised baselines (62.6% Micro-F1) while reducing active calibration error by 32%. Switched with zero target training notes to 13,783 unseen-patient ICD-10 discharges, MS-DRG groups, and multilingual cohorts, it outperforms biomedical dense retrievers, semantic crosswalks (+5.4 F1 points on ICD-10, paired $d_z = 0.49$, $p < 0.001$), and official US CMS equivalence mappings (+3.5 points, $p < 0.001$) at 9.4 ms per admission. Pairing this reader with an offline 31B verifier across 1,000 full discharge summaries lifts zero-training ICD-10 coding to 40.6% Micro-F1 (57.0% category F1, $d_z = 0.66$, $p < 0.001$) with 0.0% invalid code hallucinations.

---


### 328. [VADE: A Verifiable Agent Data Engine from Professional Sources](https://arxiv.org/abs/2611.30202)

**<font color=#1a73e8>作者：</font>** Xiangchao Chen, Zhiheng Lyu, Kai Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language agents have shown their practical value, particularly in software engineering, where abundant public code and executable tests support training and evaluation at scale. Extending this success to other professional domains, such as law and finance, is not straightforward: many agent tasks involve open-ended analysis, making outcomes hard to verify and, in turn, hard to use as scalable supervision. As a result, high-quality tasks in these domains are still largely expert-authored, making them expensive to scale and limiting their use for training. To address this bottleneck, we introduce VADE, a data engine that automatically constructs verifiable analysis tasks from public sources used in professional practice. VADE exploits a simple asymmetry: professional analyses are difficult to solve because the relevant evidence must first be found and interpreted, but much easier to verify once that evidence is fixed. During task synthesis, the engine constructs a reference analysis from source evidence and asks an independent agent to reproduce its conclusions from the same evidence without seeing it. Only after the analysis is verified is it compiled into an open-ended task with an item-level scoring contract, allowing the same task to support both evaluation and training. We apply VADE across four professional domains; in an independent expert review of 186 finance tasks, 93.5% meet a high bar for source fidelity, answer correctness, and evaluation fairness. In finance, these tasks expose substantial remaining model errors, particularly unsupported facts and inferences, while training on verified solver trajectories improves held-out performance and yields gains that transfer to public finance benchmarks such as Finance Agent Benchmark v2. Together, these results suggest a practical path toward scalable, verifiable supervision for open-ended professional tasks.

---


### 329. [ToWo-VTON: Take-Off Wear-On Virtual Try-On via Topology-aware Decoupling](https://arxiv.org/abs/2611.30203)

**<font color=#1a73e8>作者：</font>** Zhenchen Wan, Tianxi Chen, Runqi Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual Try-On (VTON) aims to synthesize garment transfer without physical trials. Although recent methods perform well on upper-body garments, they still struggle in lower-body and full-body scenarios with complex occlusions and large silhouette changes. To address this limitation, we introduce ToWo (Take-Off Wear-On), a two-stage paradigm that decouples body structure estimation from garment synthesis. Take-Off first generates a tight-fitting body proxy that provides estimated structural guidance, and Wear-On then synthesizes the target garment conditioned on this prior. This decoupling reduces source-garment interference, supporting garment placement under substantial silhouette variations. Built on this paradigm, we propose ToWo-VTON, a unified topology-aware framework with structure-aware supervision. We construct the Body-Fitting DressCode (BFDC) dataset via body-aware diffusion and VLM-based filtering to provide body-proxy supervision across upper-, lower-, and full-body cases. We instantiate ToWo-VTON on both diffusion-based and MLLM-guided backbones. For diffusion-based models, we fine-tune on BFDC using the body proxy as the person input. For the MLLM-guided model, we use native backbone conditioning for the body proxy and target garment, and add Garment Boosting Attention (GBA) to preserve garment details. Experiments on VITON-HD and DressCode demonstrate improvements over the evaluated baselines, with KID reductions of 26.1% and 58.6% for diffusion-based and MLLM-guided implementations, respectively. The combined BFDC-training and Take-Off/Wear-On strategy also produces more coherent limb layouts and garment boundaries across the evaluated garment categories.

---


### 330. [PackLoop: Row-Packed Self-Speculative Decoding for Looped Language Models under Concurrency](https://arxiv.org/abs/2611.30205)

**<font color=#1a73e8>作者：</font>** Runguo Li, Dezhen Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models reuse one block of weights T times per token, trading parameters for test-time depth, but autoregressive decoding then pays T sequential passes per token. Self-speculative decoders recover 2-10x for a single request, yet their gains fade as requests share a GPU, and current practice is to speculate less as load grows. We show that what fails under load is the layout of speculative work, not speculation. In concurrent decoding the unit of cost is the row, one request advancing on one loop, which reads that loop's key-value (KV) cache once; additional positions inside a row are nearly free. Pipelined schedules such as the wavefront place every speculative position on a different loop, hence in a row of its own, so each token is still read T times. We present PackLoop, built on one principle: speculate only inside rows that are read anyway. Deep loops accumulate positions and advance them as a block in one row, context-copy proposals join the row that the first loop already reads, and a closed-form admission rule, the economic order quantity of inventory theory, sets how long to accumulate from a cost model calibrated once per engine. PackLoop is exact: in FP32 its output is token-for-token identical to autoregressive decoding, also under sampling and early exit. Across 164 load points spanning three GPUs, four Ouro models, six benchmarks, and contexts up to 32K tokens, one PackLoop configuration is faster than the best existing schedule, chosen per point, at 161 points (median 1.25x, up to 1.76x) and never significantly slower. Its lead grows with concurrency and context length, the regime in which existing self-speculation gains least.

---


### 331. [What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym](https://arxiv.org/abs/2611.30207)

**<font color=#1a73e8>作者：</font>** Yikai Zhang, Mai Xu, Yunbei Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task collections check these tests only against the reference fix. We ask what makes a task good training data, focusing on the correctness of its reward labels. We audit SWE-Gym with two LLM families, and a suspected error counts only if execution reproduces it. We find that unsolved often means mislabelled: 74% of the tasks that a 9B base model never solves have a test that rejects correct fixes (a false negative), versus 20% of those it sometimes solves. We repair or remove such tasks, and the audited tasks that remain train better policies. At equal size and matched difficulty, models trained on them score 2.4 and 2.7 points higher on held-out tasks from SWE-bench Verified and SWE-bench Pro than models trained on the original tasks, whereas simply dropping the never-solved tasks shows no such gain. We further find that wrong patches that pass (false positives) make up about a quarter of all passing patches, and that new tests that catch a quarter of them do not change held-out scores detectably. A pass rate shows whether a task yields reward, not whether that reward is right, so the reward labels themselves must be checked. To this end, we release SWE-Gym-Verified with its 1,087 audited tasks, every verdict with its executed evidence, our training sets, and the full audit pipeline.

---


### 332. [VeriWorld: A Verifiable Visual SWE-Bench for Spatial Reasoning in 3D Environments](https://arxiv.org/abs/2611.30226)

**<font color=#1a73e8>作者：</font>** Yan Zheng, ShengYun Peng, Xuyao Liang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used for spatial tasks such as navigation and manipulation, where they must infer geometry and object relationships from visual input in order to act correctly. Existing benchmarks usually test perception and reasoning in isolation, making it hard to tell whether failures come from visual understanding, downstream reasoning, or the bridge between them. We introduce VeriWorld, a benchmark for spatial reasoning in interactive 3D environments with executable actions and deterministic verification. For task families where all three channels are well-defined, we evaluate matched visual, structured, and combined input conditions on the same instance, environment, and verifier; families without a clean visual/structured/combined split are reported separately. This design supports controlled comparisons of perception, reasoning, and their interaction. Using this setup, we uncover two diagnostic findings. First, models often perform much better when task-relevant information, such as object identity, current state, or target location, is given explicitly than when it must be read from the rendered scene, revealing a recurring visual-to-structure gap. Second, action-space and harness design can change outcomes even under the same task and information condition, showing that interaction protocol is itself a confounding variable. VeriWorld is open-sourced to support reproducible and fine-grained evaluation of spatial reasoning in VLMs.

---


### 333. [CLIP-FMoE: Scalable CLIP via Fused Mixture-of-Experts with Enforced Specialization](https://arxiv.org/abs/2611.30233)

**<font color=#1a73e8>作者：</font>** Luong Tran, Lan-Cuong Nguyen, Huynh Dang Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have emerged as a promising approach for scaling deep learning models while maintaining computational efficiency. However, existing MoE adaptations for Contrastive Language-Image Pre-training (CLIP) models suffer from significant computational overhead during sequential training and degradation of zero-shot capabilities. To address these limitations, we propose CLIP-FMoE, a novel approach that integrates MoE architecture into CLIP fine-tuning. Our method uses Isolated Constrained Contrastive Learning, a pipeline that trains specialized experts on cluster-based data partitions to accelerate expert specialization. Additionally, we introduce a Fusion Gate mechanism to mitigate catastrophic forgetting of pre-trained knowledge. Extensive experiments across multiple benchmarks demonstrate that our approach achieves consistent improvements on downstream tasks while preserving zero-shot capabilities. Furthermore, our method demonstrates robust performance across varying context lengths, making it particularly suitable for diverse real-world applications.

---


### 334. [TriSegAgent: Context-Efficient 3D Annotation with MLLMs via Tri-Planes](https://arxiv.org/abs/2611.30240)

**<font color=#1a73e8>作者：</font>** Qingqiao Hu, Jialin Li, Meilong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive segmentation models turn a few clicks into a segmentation prediction across domains, so annotators only decide where the prediction still needs correction. Annotation thus becomes a loop of inspecting the prediction and clicking again. Each step of this loop is a visual judgment, which suits general-purpose multimodal large language model (MLLM) agents. In this work, we focus on letting these agents run this loop on 3D volumes. However, the MLLM in such an agent takes only 2D images as input, so the agent must observe the 3D volume in 2D. Since the loop calls the MLLM many times, this observation must be token-compact enough to keep every call cheap, yet informative enough to show error regions in the 3D prediction. We meet both needs with tri-planes, the three orthogonal planes that cross at one point in the volume. We show, both theoretically and empirically, that tri-planes are context-efficient yet keep sufficient detail to show error regions in the 3D prediction. Building on tri-planes, we introduce TriSegAgent, an MLLM agent that refines the 3D prediction iteratively. Within the agent, the MLLM only judges the prediction on tri-planes, while a visual harness turns each judgment into a 3D action in code. To make the loop reliable, the harness places each click at an exact voxel in the volume and checks whether to accept the 3D prediction. To evaluate the agent, we build a diverse benchmark of 690 regions of interest (ROIs) from 35 public medical datasets across three imaging modalities. With frontier MLLMs, TriSegAgent reaches an overall Dice about 10 points above the strongest baseline, and its lead is even larger on targets below 3 cm. With flash-level MLLMs, it outperforms a recent 3D segmentation agent built on a frontier MLLM.

---


### 335. [Attributing Security Outcomes in LLM-Agent Evaluations: The Role of Content-Free State](https://arxiv.org/abs/2611.30259)

**<font color=#1a73e8>作者：</font>** Abdelmonaim Bounite, Zangir Iklassov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security benchmarks for LLM agents record whether each attack succeeded and compare agents, attacks, and defenses by attack success rate (ASR). Such comparisons are valid only if the agent, the attack, and the defense cause each verdict. We show that verdicts also depend on content-free state: details of a run that carry no information about the system under test, such as the Python hash seed, the order of tools or evidence, and the scoring of failed runs. We require that this state influence no verdict (decision noninterference) and treat it as untrusted input, because evaluators and requesters of LLM-based gates can choose it. Our framework, TARE (Testing Attribution of Reported Effects), attributes a reported effect to the agent, attack, or defense only if it exceeds the measured influence of content-free state. On Agent Security Bench (ASB), runs with a fixed hash seed are identical for seven agents from four model families, yet changing the seed changes up to 17% of an agent's verdicts while the ASR moves by at most 5 points. The seed acts through the tool order: sorting the tool list instead of reverse-sorting it raises the ASR by up to 19 points, because ASB's naming convention places attacker tools first. When the same evidence is reordered, six of seven LLM judges change their decision on 17-91% of 98 proposed actions. Across eighteen agent-defense combinations, TARE's worst-case test attributes effects to two of three defenses, one of them in opposite directions on two agents, and a test fixed in advance confirms a 4.8-point decrease from the third; in the attributed decreases, 35-69% of the stopped attacks end without any tool call, which ASB counts as a failed attack. Reproducible verdicts are thus not necessarily attributable, and security evaluations of LLM agents should report the influence of content-free state. We release TARE, the ASB patch, and all verdict tables.

---


### 336. [Evaluating Persona Consistency in LLM User Simulators Without External Reference Annotations](https://arxiv.org/abs/2611.30280)

**<font color=#1a73e8>作者：</font>** Anping Zhang, Yang Tan, Yipeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard evaluations assess LLM-simulated personas against an external ground truth, such as community trait annotations, but that reference is unavailable when the persona is inferred only from a short, task-oriented chat. We ask how persona consistency can be evaluated without such a reference, and propose a self-anchored internal-consistency diagnostic: the persona describes itself once and acts twice. A Likert self-report supplies a soft internal anchor; two behavioral profiles come from constrained scenario choices scored without a judge and from open-ended responses judged by an LLM. Consistency is the correlation between the self-report and each behavioral profile, in a shared six-facet BFI-2 space. The framework compares persona-construction strategies by assessing how consistently their elicited responses reflect their self-reported traits. Across ordinary-user chats (WildChat and LMSYS) and well-documented personas with community annotations (the Personality Database, PDB), profile-enriched representations agree with the anchor more closely than a raw-dialogue baseline. On PDB, this self-anchored ordering reproduces the community-annotation ordering. The pattern is stable across answering and judge models.

---


### 337. [Learning Heterogeneous Reasoning in Large Language Models: From Mode Compatibility to Local Bottlenecks](https://arxiv.org/abs/2611.30281)

**<font color=#1a73e8>作者：</font>** Sunbowen Li, Dandan Song, Shengkun Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training large language models routinely pools reasoning trajectories from diverse teachers or algorithms, yet it remains unclear whether standard supervised fine-tuning (SFT) can learn such heterogeneous strategies without explicit mode conditioning. We study the learnability and local bottlenecks of heterogeneous reasoning through a formal mixture formulation and controlled experiments. We first formalize the representational compatibility of the optimal autoregressive model with latent reasoning mixtures: the target next-token distribution weights modes by their prefix posteriors and concentrates on a single mode once alternative modes assign negligible likelihood to the prefix. In a verifiable symbolic graph-search environment with paired breadth-first and depth-first search trajectories, no consistent disadvantage is observed for unlabeled mixed SFT relative to homogeneous or labeled baselines under matched token budgets while preserving both modes. Scaling across 0.6B--14B models and data budgets largely eliminates global mode confusion, shifting the primary bottleneck to local state-tracking transitions. Because a local mistake affects the final outcome only when subsequent reasoning is sensitive to that step, we find that only a small fraction of local errors are outcome-determining \emph{Critical Reasoning Nodes (CRNs)}, and that single-step repairs at these nodes rescue failing trajectories across symbolic search and natural language benchmarks whenever the model has sufficient downstream competence to complete the remaining derivation. Our environment is open-sourced at this https URL.

---


### 338. [A statistical measure of trust in generative AI](https://arxiv.org/abs/2611.30286)

**<font color=#1a73e8>作者：</font>** Alina Ermilova, Valeria Yakupova, Nikita Sushko 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trustworthiness is a crucial issue for generative AI, as modern models can produce convincing and confident responses even when their outputs are incomplete, unsupported, or wrong. The frequent absence of ground-truth knowledge or labels complicates verification of generative AI outputs. To address this issue, we propose a trustworthiness framework grounded in model-internal confidence calibrated against an external expert reference. We estimate per-token trustworthiness of a student generative model as the statistical typicality of each generated token relative to an expert model's distribution, where the expert is used as a distributional reference rather than as a source of factual verification labels. To this end, we introduce an AI ontology calibrator that leverages the student model's internal latent features and token-level output statistics to compute expert-reference acceptance scores. Combined with traditional token-level confidence, entropy, and perplexity statistics, calibrator scores yield a compact set of $15$ response-level indicators for correctness classification. Evaluated across BF program generation, mathematical problem solving, and medical question answering, combined calibrator and traditional indicators provide complementary reliability signal which could be used to build detectors of untrustworthy outputs and hallucinations. Remarkably, our experiments show that these detectors are transferable across domains, although transferability is not always symmetric.

---


### 339. [MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation](https://arxiv.org/abs/2611.30287)

**<font color=#1a73e8>作者：</font>** Yuxuan Chen, Changwei Lv, Yunfei Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related questions. Existing multimodal memory methods largely focus on storing and retrieving records, with limited mechanisms for learning from completed tasks and consolidating task-specific experience. We therefore propose MMMem, a task-aware multimodal memory framework that extracts and consolidates experience from completed tasks through four complementary strategies. First, source-linked multi-view memory organizes original text, images, and rendered pages alongside generated scene images that combine clues across records for retrieval. Second, source-generated tasks support knowledge alignment at two levels: warm-up consolidates source knowledge into task-relevant experiences in external memory, while self-training adapts the model's parametric knowledge to task demands. Third, the same vision-language model distills completed tasks into experiences that record the task context, conclusion, and support links. Finally, task-aware retrieval recalls source views and relevant experiences for answering and verification, while source-supported reuse guides long-term retention. Across three memory benchmarks and two vision-language readers, MMMem outperforms eight baselines. With Qwen3.5-9B, MMMem achieves relative gains of 36.9%, 17.6%, and 15.2% over the best-performing baselines on LoCoMo, Mem-Gallery, and LooGLE v2, respectively. Ablations show consistent gains from training and memory warm-up, while case studies illustrate how individual components work in practice.

---


### 340. [Uncovering Separable and Composable Skill Mechanisms in Vision-Language Models](https://arxiv.org/abs/2611.30290)

**<font color=#1a73e8>作者：</font>** Miaoyu Li, Boyang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work has sought to localize the internal mechanisms underlying visual reasoning skills in vision-language models. These methods largely overlook separability and composability in both mechanism identification and evaluation. We propose separability and composability as two important desiderata for skill localization. Separability requires identified mechanisms to contribute primarily to their target skills while having limited effects on other skills, enabling precise diagnosis and targeted intervention. Composability requires skill mechanisms to be combinable to support complex tasks, allowing a small set of mechanisms to account for broader capabilities. In this work, we propose a multi-skill interpretability framework DISCO, built around these two properties. For identification, we propose Separable Head Selection, which selects skill-specific attention heads based on their contributions across skills. For evaluation, we are the first to design metrics for measuring separability and composability of identified heads. Extensive experiments on three VLMs and four fundamental visual reasoning skills demonstrate the effectiveness of DISCO. It achieves the highest separability, outperforming the strongest baseline by 24.80, 18.38, and 13.75 points across the three models, respectively, while also achieving the highest composability on all three models.

---


### 341. [PinGround: Pinning Queries to Points for Parallel Grounding in Vision-Language Models](https://arxiv.org/abs/2611.30304)

**<font color=#1a73e8>作者：</font>** Shuxuan Li, Jialiang Kang, Yanghao Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can localize through their text interface, grounding open-vocabulary objects, complex referring expressions, text lines and layout regions with strong semantic understanding. They write the boxes one after another as a single sequence, although the instances of a query, unlike the words of a sentence, form an unordered set with no sequential dependence. The number of decoding steps therefore grows with the number of instances, which makes dense scenes the most expensive. Decoding the instances in parallel avoids this growth, but streams that cannot see each other duplicate some instances and miss others. We propose \method, which writes a single point into each query as a spatial anchor and asks for the matching instance nearest to that point within a local radius, or \none. Given the image, the anchored queries are independent, so they are decoded in parallel as leaves of a prefix tree that shares the image and the query, and the model is trained on the same tree. Coarse-to-fine anchors refine only the regions where instances are found, duplicate suppression keeps one box per instance, and set-level reinforcement learning optimizes the set F1. Only the prompt and the attention mask change, not the architecture. On three different VLMs and 12 benchmarks covering detection, OCR, layout and referring, \method is at most 5.5 F1 below sequential decoding trained on the same data, while its speedup grows with instance density and reaches 21.9$\times$ on dense scenes.

---


### 342. [Accuracy Is Not Evidence: Measuring and Training Evidence Dependence in Video Temporal Grounding](https://arxiv.org/abs/2611.30320)

**<font color=#1a73e8>作者：</font>** Zijie Jin, Shuai Zhao, Haoran Tao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In video temporal grounding, a correct interval can come from finding the event, answering blind or fitting one annotation style, and Recall at IoU scores them alike. We measure evidence dependence, how much the answer rests on the event's frames. Our fixed-answer audit edits either the frames inside the annotated interval or, as a placebo, as many frames elsewhere in the same video, and compares the two drops in the annotated answer's likelihood. Supervised fine-tuning and three public checkpoints trained with IoU-reward reinforcement learning raise the accuracy of Qwen2.5-VL-7B by 9 to 20 points, partly by answering blind and by fitting one annotation. Yet their answers rest on the event no more than the base model's, and the same holds for IoU-reward training on our data at the audit's frame rate. This comparison is a difference of the model's own likelihoods, so we can train on it. A placebo contrast and a bound on the placebo drop rule out learning to react to any edit. With them, evidence dependence rises in all five base models we train, and the weight on clean supervision controls how much. Added to IoU-reward training, the objective raises evidence dependence while keeping the accuracy gain. Masking the event's frames makes the trained models decline or miss the event more often than their base; masking as many other frames does not. The dependence moves to another event when the query names it, and holds on a second dataset and under patch scrambling, an edit never used in training.

---


### 343. [Verifiable On-Policy Distillation](https://arxiv.org/abs/2611.30325)

**<font color=#1a73e8>作者：</font>** Juntong Shi, Stefano Ermon, Jure Leskovec 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a powerful approach for improving language-model reasoning, but its supervision is inherently sparse: a sequence-level verifier reward is propagated only through sampled trajectories and provides no direct signal for alternative actions. On-policy distillation (OPD) offers a complementary form of supervision by providing dense teacher feedback over the full next-token distribution, but this signal is not grounded in verified task outcomes. Simply co-optimizing the two objectives does not couple these signals: verifier feedback remains sparse and does not inform the dense teacher supervision. We introduce Verifiable On-Policy Distillation (VOPD), which transfers sparse verifier feedback into dense, verifier-grounded supervision. Our key observation is that the implicit-reward view of OPD places teacher supervision and verifier feedback in a common reward space while retaining a reward signal available for every next-token action. Under this view, VOPD projects verifier preference onto the teacher's implicit-reward direction and Rao--Blackwellizes the resulting signal over the full vocabulary, propagating verifier-grounded supervision to actions that were never sampled. The resulting objective can also be interpreted as adaptively extrapolating the distillation target according to teacher--verifier agreement. Across two teacher--student configurations and eight mathematical reasoning benchmarks, VOPD consistently improves both final performance and learning efficiency over vanilla OPD and other on-policy distillation baselines. Our code is available at this https URL.

---


### 344. [When Does Reasoning Help Entity Disambiguation? Small LLMs In-Domain and Under Shift](https://arxiv.org/abs/2611.30334)

**<font color=#1a73e8>作者：</font>** Samy Haffoudhi, Fabian M Suchanek, Nils Holzenberger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entity disambiguation (mapping ambiguous mentions in text to entities in a knowledge base) is a foundational step in tasks such as knowledge graph construction, question answering, and information extraction. Recent work has applied LLMs to this problem, achieving stateof-the-art performance. Notably, reasoning LLMs have been shown to perform entity disambiguation in a true zero-shot fashion, generalizing across knowledge bases and domains. However, it is unclear whether this capability survives, or remains competitive, with smaller LLMs, where entity disambiguation has typically relied on reranking rather than reasoning. We ask when reasoning is worth its cost at small scale. We compare pointwise, listwise, and reasoning-based candidate-selection components within a classical coarse-to-fine entity disambiguation pipeline, across the classical, few-shot and true zero-shot settings. The reasoning paradigm is trained with distillation and reinforcement learning recipes. The benefit of reasoning grows with domain shift: negligible in-domain, decisive in the true zero-shot setting. We show that two distinct factors are at work: the reranker's uncertainty over the candidates locates where the paradigms disagree, while shift governs which is right when they do.

---


### 345. [MH-RAG-DIVE: Dynamic and Cost-Efficient Multi-Hop RAG Evaluation via Tree-Cached Dialogue Simulation](https://arxiv.org/abs/2611.30335)

**<font color=#1a73e8>作者：</font>** Lorenz Brehme, Daniel Hillebrand, Thomas Ströhle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quality assessment is essential for determining whether changes to a Retrieval-Augmented Generation system improve or maintain its performance. However, existing evaluation approaches often rely on single-turn or single-hop interactions and therefore do not capture the complexity of multi-hop, multi-turn conversations. We introduce MH-RAG-DIVE, a dynamic interactive user simulation framework designed to evaluate RAG systems in more complex multi-hop and multi-turn settings. The framework extends RAG-DIVE with a Context Discoverer, which identifies documents that can be combined to generate multi-hop questions within an ongoing conversation. To address the high computational cost of dynamic user simulation, we further introduce a Conversation Cacher, which reuses turns from previous evaluation runs while preserving the dynamic nature of the evaluation. We evaluate the framework across six distinct RAG configurations and compare its results with the original RAG-DIVE evaluation and the static, human-created CLAPNQ dataset. Our experiments show consistent performance trends across the evaluation approaches, while the more complex multi-hop and multi-turn setting exposes additional challenges for RAG systems. Furthermore, the Conversation Cacher substantially reduces token consumption, demonstrating its potential to make dynamic evaluation more cost-efficient. Finally, we apply MH-RAG-DIVE to an industrial RAG system with domain-specific data, demonstrating its applicability to real-world evaluation scenarios. Overall, our results show that the proposed approach provides a more complex and cost-efficient framework for evaluating RAG systems. All code and experimental data are publicly available in our GitHub repository (this https URL).

---


### 346. [Learning Teacher Output Preferences from Final Responses for Reasoning Distillation](https://arxiv.org/abs/2611.30338)

**<font color=#1a73e8>作者：</font>** Hongli Shen, Shaopeng Fu, Qinbo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many large language models (LLMs) use chain-of-thought (CoT) to solve complex problems, but hide their CoT traces to prevent reasoning capabilities from being distilled. While recent studies have shown that hidden CoTs can be reconstructed, existing methods typically require training a separate attacker for each target LLM. This paper studies model-agnostic CoT reconstruction, aiming to reconstruct hidden CoT traces from arbitrary target LLMs using only input prompts and visible final responses. We propose Final-Output Preference Learning (FOPL), which trains a single reconstruction model that generalizes to unseen LLMs without target-specific adaptation. To achieve this, the reconstruction model must learn which reasoning patterns match a given final response without knowing the target LLM's identity. We address this using preference optimization, training the reconstruction model to prefer native CoTs over synthetic alternatives for the same question and final response. By learning these preferences from LLMs with accessible CoTs, the reconstruction model learns to distinguish reasoning patterns based on visible responses. Experiments show that reconstructed CoTs capture distinct reasoning patterns across LLM families, including a family unseen during training. Moreover, students trained on reconstructed CoTs match or outperform those trained on native CoTs across several reasoning benchmarks.

---


### 347. [SceneCast: Learning Indoor Scene Synthesis from Curated Synthetic Videos with LLM Reward](https://arxiv.org/abs/2611.30345)

**<font color=#1a73e8>作者：</font>** Ziyang Zong, Canming Xia, Haoran Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D indoor scene synthesis requires generating objects to form a complete and coherent scene. Existing approaches rely heavily on manually annotated datasets, leading to high costs and limited generalization. We present SceneCast, an annotation-free framework that trains on large-scale, unlabeled videos, addressing two key challenges: (1) Videos provide only partial views of a scene, requiring the model to extrapolate unseen 3D regions, which is inherently error-prone; (2) Raw videos available online are uncurated, suffering from uncontrolled conditions and variable data quality. First, we design a Transformer-based model that predicts objects sequentially and is fine-tuned with reinforcement learning (RL), where an LLM acts as a spatial common-sense evaluator. The LLM provides reward signals through chain-of-thought reasoning and code-executable geometric checks to refine object configurations. Second, we introduce \trim, a data curation approach that generates training videos with controllable video generation models. Crucially, it retains only high-quality prefix clips via multi-criteria quality assessment with an entropy-based weighting strategy. Evaluated on curated synthetic video sets, our annotation-free approach outperforms state-of-the-art supervised methods in scene quality.

---


### 348. [Toward a Theoretical Understanding of Transformer Attention: Bayesian Estimation and Predictive Sufficiency](https://arxiv.org/abs/2611.30349)

**<font color=#1a73e8>作者：</font>** Fouad B. Chedid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a theoretical account of Transformer attention by organizing existing probabilistic and information-theoretic results. It identifies the assumptions under which attention computes a posterior mean and the additional conditions required for accurate next-token prediction. Posterior-mean optimality under squared-error loss does not by itself establish predictive sufficiency; even a sufficient representation requires a prediction head that uses its information correctly. An excess-log-loss decomposition makes this distinction precise by separating representation information loss from prediction-head error. The analysis clarifies the conditions required for predictive guarantees. Determining when these conditions hold in trained models, and how architectural or training choices can support them, could guide the development of AI systems that preserve and use predictive information more effectively.

---


### 349. [AutoClip-DPZO: Practical Private Clipping Selection for Differentially Private Zeroth-Order LLM Fine-Tuning](https://arxiv.org/abs/2611.30352)

**<font color=#1a73e8>作者：</font>** Xinghe Chen, Haichao Sha, Zihao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differentially private zeroth-order optimization (DPZO) is a promising approach for privacy-preserving LLM fine-tuning, offering exceptional memory efficiency. However, its utility is highly sensitive to the clipping threshold $C$, a key DP-specific hyperparameter that controls the trade-off between noise injection and clipping bias. Existing DPZO methods typically tune $C$ by repeatedly evaluating candidate values and reporting the best result, which is computationally expensive and incurs additional privacy cost that must be accounted for under DP. Designing a practical DP procedure for selecting $C$ in DPZO is challenging because no fixed choice performs well across settings, straightforward search-based strategies suffer from poor utility and efficiency, and existing clipping-selection methods for DPSGD do not transfer well to DPZO due to its fundamentally different error regime. In this paper, we propose AutoClip-DPZO, a practical DP method that automatically and efficiently selects $C$ for DPZO. Our key idea is to avoid fine-tuning-based search by reducing clipping selection to a private quantile estimation problem, where the target quantile depends only on public privacy and training parameters. To derive this selection rule, we develop a novel characterization of DPZO error as a function of $C$ that captures both noise variance and clipping bias while remaining accurate and easy to optimize. Experiments show that AutoClip-DPZO achieves utility comparable to that obtained with the optimal $C$, while avoiding repeated fine-tuning-based search and incurring negligible additional overhead. Moreover, AutoClip-DPZO does not rely on sensitive hyperparameters.

---


### 350. [PseuDRAGON: Knowledge-Guided Local LLMs for Financial-Data Pseudonymization in Closed Networks](https://arxiv.org/abs/2611.30353)

**<font color=#1a73e8>作者：</font>** Gwangui Hong, Seonho An, Seonkyu Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Staff pseudonymizing financial data in closed networks must interpret abbreviated column names, identify personal information, and choose processing methods. Local language models can assist, but may give different labels for the same input. PseuDRAGON keeps confirmed judgments and corrections outside a fixed model and reuses them through exact-name lookup and learned rules. For expert review, the workflow searches institutional policy, national privacy law, then international sources. Across 92 columns from one institution, rules increase reuse under the same approval checks from 75 to 83 labels without reuse errors when all training judgments are available. With 25% of the training judgments, withholding non-PII rules for unseen names eliminated the extra PII misses in replay at the cost of lower reuse. Revising or withdrawing approvals rebuilds derived rules, and tests on synthetic records verify that selected methods produce the specified outputs. In three paired runs, the history-first baseline cut automated identification time by 83.0% on average versus no reuse.

---


> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
