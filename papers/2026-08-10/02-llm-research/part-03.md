# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **117** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-117**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-117**

---

### 101. [Geo-Spatial Concept Probing of Large Language Models: Abstraction, Compositionality, and Grounding](https://arxiv.org/abs/2608.07353)

**<font color=#1a73e8>作者：</font>** Karim Radouane, Jose G Moreno, Lynda Tamine  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding concepts is fundamental to generalization. Despite their impressive performance on a wide range of tasks, Large Language Models (LLMs) still struggle with genuine concept understanding. Prior work has evaluated conceptual understanding in LLMs using natural-language benchmarks or narrowly scoped synthetic tasks, but these settings often conflate multiple skills or lack precise control over the underlying concepts and their properties. To support controlled probing of concepts in LLMs, we design tests on their core properties: abstraction, compositionality, and groundness. We set up a concept-centric benchmark, targeting spatial concepts such as direction, distance, topology, and their compositions, and use question answering tasks serving as a proxy. We conduct extensive experiments across multiple LLM architectures and training regimes to analyze how model scale and design impact conceptual understanding. The results reveal clear limitations in current LLMs and provide insights into the factors shaping their ability to acquire and compose structured concepts. Our findings shed light on how concept-based LLMs can be redesigned for improved information access and knowledge management. The code will be available at this https URL.

---


### 102. [People Are Not Just Their Countries. Disentangling Social Determinants of LLM Value Alignment Across Europe](https://arxiv.org/abs/2608.07367)

**<font color=#1a73e8>作者：</font>** Maria-Louisa Wightman, Guillaume Bied, Tijl De Bie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly used as a primary source of information and advice, understanding their alignment to humans in terms of values becomes a pressing concern. A growing literature has leveraged large scale surveys to investigate to what extent LLMs' and humans' stated values and opinions align. With limited exceptions, studied populations have been defined country borders or cultural bounds. Yet, this focus neglects the role that socio-demographic divides may play for value alignment disparities.
Relying on the European Social Survey, we address this knowledge gap by considering value alignment displayed with respect to 10 prominent commercial LLMs in terms of 15 socio-demographic variables as well as country of residence. Our analyses reveal that LLMs are indeed unequally aligned to the values of different socio-demographic groups, notably those defined by education, income, occupation and religion. When examining alignment at the individual level, a respondent's country, taken as a stand-alone variable, explains a substantial amount of variation that is on par with the full set of considered socio-demographics. Further disentangling the respective role of country-level and socio-demographic factors, we find they are complementary in explaining value alignment patterns, with their relative weights varying across the subset of questions considered.

---


### 103. [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.07371)

**<font color=#1a73e8>作者：</font>** Haoyu Zheng, Yun Zhu, Qing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent agentic reinforcement learning methods use hindsight to complement sparse outcome rewards. However, a completed rollout can yield many such signals, leaving their appropriate allocation across turns unclear. We introduce TRIAL, a trajectory-relative hindsight distillation framework with a unified turn-aligned scoring protocol. For each decision turn, TRIAL extracts an outcome view of that decision's realized consequence and evaluates the same response under ordinary and hindsight-conditioned contexts. The signed log-probability gap determines the direction and local strength of token-level supervision, while turn-level magnitudes are normalized jointly over the realized trajectory. The resulting allocation multipliers have an eligible-token-weighted mean of one, redistributing dense supervision across turns while fixing its average multiplier. Experiments on WebShop and ALFWorld with different backbones show that TRIAL outperforms GRPO across all eight combinations of backbone, environment, and evaluation metric, while achieving the best or tied-best performance among six methods on six of them. On WebShop with Qwen3-1.7B, TRIAL improves the success rate from 56.4% to 75.2% and the task score from 78.7% to 85.7%. Controlled ablations further show that trajectory-relative turn allocation provides substantial gains beyond those of dense hindsight distillation alone.

---


### 104. [Addressable Memory for Video World Models](https://arxiv.org/abs/2608.07408)

**<font color=#1a73e8>作者：</font>** Xindi Wu, Sven Elflein, James Lucas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study visual persistence in interactive video world models. These models rely on a Key-Value (KV) cache as a growing visual memory to carry forward previously generated frames. However, we find that models can no longer reliably address stored content once rollouts extend beyond the training horizon, because temporal Rotary Positional Embeddings (RoPE) offsets then fall outside the range seen during training and the model struggles to retrieve the relevant visual information through attention. Moreover, naively compressing the cache in the RoPE-rotated space corrupts memory by averaging together incompatible positional phases. To address this, we propose WorldTrace, a training-free memory framework for long-horizon visual persistence. WorldTrace keeps compressed memory addressable by assigning each summary slot a distinct, in-distribution virtual position. Within this addressable cache, we study two memory compression approaches: WorldTrace-Field compresses history for temporal coherence, while WorldTrace-Landmark stores verbatim scene traces at detected transitions for episodic recall. We further introduce LoopBench, a benchmark evaluating whether a compressed cache can reconstruct a previously visited scene after a long detour. WorldTrace-Field improves temporal consistency by +15.5%, and WorldTrace-Landmark improves episodic recall by +19.5% on LoopBench, extending visually persistent generation without retraining.

---


### 105. [UniJEPA: A Unified Joint-Embedding Predictive Architecture for Task-Agnostic Visual World Modeling](https://arxiv.org/abs/2608.07409)

**<font color=#1a73e8>作者：</font>** An Lanji, Dawei Liu, Jin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) have emerged as a principled framework for self-supervised learning of world models in compact latent spaces, yet existing methods are fragmented: some predict masked parts of a single image in latent space (I-JEPA), others learn to predict global photometric transformations (Image World Models), while video-scale JEPAs predict future temporal states and are post-trained for action-conditioned planning (V-JEPA~2, DINO-World, DINO-WM). These objectives are treated as distinct recipes with separate encoders, predictors, and anti-collapse regularizers, hindering a single model from unifying image-level and video-level world modeling. We present UniJEPA, a unified JEPA that jointly learns photometric prediction (image-level transformations) and temporal prediction (video-level next-state dynamics) in one shared latent space. A single end-to-end objective, composed of a next-embedding prediction loss and a Gaussian regularizer, yields a provably anti-collapse encoder-predictor pair trainable from raw pixels without EMA, stop-gradient, or pre-trained encoders. We show that the same latent space supports controllable abstraction: photometric prediction learns invariant structure while temporal prediction learns equivariant dynamics. After action-conditioned post-training on offline trajectories, UniJEPA enables zero-shot planning by treating goal features as prediction targets. On image, video, and control benchmarks, UniJEPA matches or surpasses task-specific JEPAs while requiring a single loss hyperparameter, and plans up to tens of times faster than generative world models at comparable accuracy.

---


### 106. [GeoBenchLLM: A Comprehensive Benchmark for Evaluating LLMs on Geo-Related Tasks](https://arxiv.org/abs/2608.07411)

**<font color=#1a73e8>作者：</font>** Rodrigo Ferreira Rodrigues, Karim Radouane, Jose G Moreno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the context of geodata, existing Large Language Models have often been studied in a homogeneous setting, which has considerably limited insights into their generalization capabilities. In this paper, we present \benchName, a comprehensive benchmark for probing LLMs on geo-related tasks. We leverage a careful selection of twelve publicly available datasets from diverse geo-related tasks and domains, and evaluate a set of LLMs on geo-spatial and temporal understanding using our benchmark. Our results show that reasoning and size have a strong impact on overall performance. GeoBenchLLM is publicly available at this https URL.

---


### 107. [I Seek You in Videos: Identity-Conditioned Queries for Person-Centric Video Reasoning](https://arxiv.org/abs/2608.07417)

**<font color=#1a73e8>作者：</font>** Shibo Gao, Chongxiao Wang, Chenglong Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world video reasoning often involves multimodal, multi-source inputs, whereas existing video reasoning tasks typically assume a simplified video-text setting, limiting identity matching and person-centric reasoning. To bridge this gap, we introduce the Identity-conditioned Queries (ICQ) task, in which models are required to jointly associate and interpret an input video and a reference image of a person, and leverage this conditioning to address identity grounding, behavior understanding, and temporal reasoning, among other challenges. Building on ICQ, we present ISYV (I Seek You in Videos), a systematic solution comprising three components: (1) ISYV-Bench, a challenging evaluation benchmark with 1,377 real-world complex videos and 1,377 question-answer pairs, organized into six difficulty levels spanning capabilities from identity recognition to causal reasoning; (2) ISYV-75K, a large-scale training set of 75K high-quality samples constructed via automated annotation, multi-stage verification, and manual review; and (3) ISYV-Framework, containing an ICQ-oriented model and training strategy for learning to exploit informative video shots without additional shot-level annotations. Extensive experiments show that both mainstream closed-source and open-source MLLMs struggle on ISYV-Bench, especially in cross-domain identity matching and long-horizon tracking. ISYV-Model outperforms strong baselines and in some aspects approaches closed-source performance. Overall, ISYV provides a unified task definition, scalable datasets/benchmarks, and modeling insights for person-centric video reasoning.

---


### 108. [Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration](https://arxiv.org/abs/2608.07419)

**<font color=#1a73e8>作者：</font>** Ruochen Jin, Zhanliang Wang, Zongyu Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference alignment often makes large language models (LLMs) overconfident and poorly calibrated. Traditional post-hoc temperature scaling is inherently domain-dependent: a temperature fitted on one domain does not generalize across domains. This motivates us to modify model parameters during training to improve calibration. We propose maximizing the entropy of predictive distributions as the calibration objective, which directly targets overconfidence by discouraging overly concentrated predictions. Inspired by temperature scaling, we realize this through a bilevel optimization formulation, where the lower level trains the model under a parametric loss and the upper level selects loss hyperparameters to maximize entropy. To make the framework practical at LLM scale, we adopt an efficient first-order approximation that avoids explicit second-order computation. Across both multiple-choice and open-ended generative question answering, experiments demonstrate that our method yields well-calibrated LLMs with particular advantages in out-of-domain generalization.

---


### 109. [Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future Prediction](https://arxiv.org/abs/2608.07420)

**<font color=#1a73e8>作者：</font>** Xinyi Li, Zaishuo Xia, Chenjie Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are expected to support imagination over extended temporal horizons, yet most are still trained through local few-step prediction objectives and deployed by recursively rolling out their own predictions. This creates a fundamental mismatch: few-step losses optimize local transition fidelity, while long-horizon prediction depends on how errors and gradients propagate through the entire trajectory. As a result, transitions with different downstream influence on the endpoint are treated uniformly during training, and small local errors are amplified through recursive inference. We argue that long-horizon accuracy is better achieved by optimizing directly, through an end-to-end endpoint prediction objective. To instantiate this paradigm, we introduce the Direct Prediction World Model (DPWM), a non-recursive architecture that compresses an action sequence of arbitrary length into a single embedding and predicts the endpoint observation in a single forward pass. This design avoids recurrent rollout in both prediction and gradient propagation, making long-horizon end-to-end training practical at horizons where unrolled autoregressive training becomes unstable. Empirically, DPWM substantially improves long-horizon endpoint prediction over recursive world-model baselines on continuous-control and pixel-based benchmarks, with larger gains as the prediction horizon increases. We further show that recurrent baselines benefit similarly when retrained with the same long-horizon endpoint objective, supporting our central claim that the training objective, rather than the particular backbone choice, is the main driver of long-horizon prediction accuracy. Our results suggest that world models can benefit from being trained and evaluated at the temporal scales where they are ultimately used, shifting the focus from local transition modeling toward long-horizon predictive accuracy.

---


### 110. [A Picture is Worth a Thousand Tokens: How Vision Language Models Cut AI Energy Costs While Improving Accuracy](https://arxiv.org/abs/2608.07427)

**<font color=#1a73e8>作者：</font>** Bhavika Jalli, Nikhil Korati Prasanna, Jayanta Choudhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM inference accounts for over 90% of AI operational energy, scaling directly with input token count---a critical inefficiency for telecom network analytics and numerical time-series data analysis (NTSDA), where raw multivariate KPI windows from 4G/5G cell sites expand into thousands of floating-point tokens. Vision-Language Models (VLMs) eliminate this mismatch by encoding time-series as 2D plots, achieving 3.6-10.4x input token reduction across Llama-3.2-90B, Qwen2.5-VL-72B, and Pixtral-12B architectures. This translates to 1.8-2.5x measured inference energy reduction, saving approximately 7.2 MJ/day at telecom edge deployments and CloudRAN that monitor 200 cells per 15-minute interval. Critically, efficiency gains do not sacrifice accuracy: a fine-tuned Llama-3.2-90B-Vision VLM achieves 220.7% higher precision than its text-only counterpart and outperforms LSTM and ARIMA baselines by over 144% on telecom anomaly detection. On public benchmarks, Pixtral-12B achieves a 20.6x improvement in J/F1 score at mean F1 = 0.82. At 24 KPIs, text representations exceed the 128K context window of most production LLMs, rendering text-only processing infeasible without truncation, while visual representations remain within standard limits. These results establish VLMs as an energy-efficient and accuracy-superior modality for numerical time-series workloads, providing empirical grounding for AI inference systems that treat energy consumption as a first-class engineering constraint.

---


### 111. [Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits](https://arxiv.org/abs/2608.07430)

**<font color=#1a73e8>作者：</font>** Elena Dumitrescu, Gert Lek, Lydia Y. Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (DLLMs) replace autoregressive next-token prediction with iterative parallel denoising, yet their internal safety mechanisms remain poorly understood. In this work, we investigate DLLMs both as targets and as adversaries, exposing mechanistic vulnerabilities in diffusion-based alignment.
We first show that safety alignment in DLLMs remains sparse and transferable across architectures. DLLMs initialized from autoregressive predecessors inherit the same mechanistic safety footprint as their source models, enabling transfer attacks via direct safety neuron mapping and pruning. Self-pruning increases attack success rates (ASR) from 2.6% to 73.8% on LLaDA and from 1.9% to 86.6% on Dream, while transfer pruning from Qwen2.5 increases ASR from 1.9% to 73.2% on Dream and from 7.0% to 86.3% on Fast-dLLM.
Building on these findings, we introduce SN-Guided Diffusion, a fully offline black-box jailbreak framework that steers the diffusion process away from safety-triggering regions using a weighted safety neuron loss, which achieves near-perfect prompt separability (AUROC = 1.0 for benign-vs-jailbreak discrimination). Across multiple open and proprietary targets, our method achieves a transfer ASR of up to 77.1% on Llama-3-8B-Instruct, 86.9% on Qwen2.5-7B-Instruct, and 74.3% against Gemini-2.5-Flash-Lite, while requiring only 20 generation episodes per prompt. Compared to prior jailbreaking frameworks, our method achieves competitive transferability with orders-of-magnitude lower generation cost.
Our codebase is available at this https URL.

---


### 112. [Conformal Coverage Guarantees for Any Video Temporal Grounder](https://arxiv.org/abs/2608.07434)

**<font color=#1a73e8>作者：</font>** Aseel Mohamed, Rasul Khanbayov, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event boundaries in continuous video are ambiguous: re-annotate the same query-video pair and independent annotators mark moments that overlap by less than half on a large fraction of samples. The ground truth for video temporal grounding is therefore a distribution over intervals, yet every grounder returns a single interval with no statement of reliability, so at deployment a wrong interval is indistinguishable from a right one. COVER changes the output object: a post-hoc, model-agnostic wrapper that turns any grounder, a trained localizer or a black-box video--language model, into one that emits a temporal region containing the true moment with probability at least $1-\alpha$, by calibrating the quantile of a temporal nonconformity score on held-out labels and widening the base prediction by that amount. The guarantee is finite-sample and distribution-free under exchangeability, and requires neither retraining nor white-box access. We give two score families, a two-sided boundary-widening score for grounders that emit an interval and a super-level-set score for grounders that emit a relevance signal, and develop theory specific to grounding that bounds how large the certified region becomes, when coverage survives conditioning on event length, and how it degrades when moments from one video break exchangeability. Across three benchmarks and five grounders, realized coverage tracks the target, and calibration exposes what point metrics hide.

---


### 113. [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](https://arxiv.org/abs/2608.07437)

**<font color=#1a73e8>作者：</font>** Jiacheng Miao, Jin Mu, Guanhua Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable hypothesis testing is the foundation of many empirical scientific claims. Large language model (LLM) agents are increasingly used to automate this process, as they can inspect datasets, generate code, and produce analyses end-to-end. However, we show that they frequently make subtle inferential errors that lead to incorrect conclusions despite correctly executed analyses. Existing benchmarks fail to capture this failure mode, as they rarely assess whether a reported p-value is statistically valid given the assumptions underlying the data. We address this gap by building P-Bench, a benchmark comprising 425 open-ended, realistic hypothesis-testing tasks spanning economics, biology, and medicine. Each task requires an agent to select a statistical method, compute a p-value, and draw a conclusion given only a scientific hypothesis and a dataset. We further introduce Fisher-R1, an open-weight LLM agent trained for rigorous hypothesis testing using synthetic tasks and reinforcement learning. On P-Bench, Fisher-R1-14B substantially improves over its backbone and outperforms strong proprietary and open-source baselines, including GPT-5.4 and DeepSeekV4-Pro, achieving a 21% average relative improvement in single-trial success over DeepSeek-V4-Pro, with gains up to 26% on the most challenging tasks. Our results demonstrate that current LLM agents lack reliable statistical reasoning for hypothesis testing and that reinforcement learning on tasks with verified statistical reward substantially improves reliability.

---


### 114. [PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents](https://arxiv.org/abs/2608.07438)

**<font color=#1a73e8>作者：</font>** Mohammad Amanlou, Parham Abed Azad, Farbod Davoodi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-like cognition does not select past experience by topical similarity alone: affective significance and unresolved conflict also shape what becomes accessible. We present PsychoAgent, a cognitive architecture for LLM agents that separates factual and affective memory and integrates both through a conflict-aware executive controller. Affective memories are first filtered by semantic relevance and then re-ranked by salience, preserving topical fit while allowing emotionally important traces to enter the prompt. Across three controlled conflict scenarios, the full architecture retrieved more conflict-critical memories than semantic-affective and single-memory RAG baselines (0.933 vs. 0.500 and 0.667), with a small semantic-similarity cost. Five blinded raters evaluated 27 outputs. After within-rater standardization, the full architecture had the highest overall mean (+0.22 SD), but corrected pairwise differences were not significant. A three-day illustrative trace further shows persistent affect, offline memory recombination, and selective memory reweighting. The findings support affect-sensitive retrieval as an inspectable mechanism for modeling human-like conflict effects in LLM agents.

---


### 115. [An Exploratory Evaluation of LLM-Assisted Rewriting of Moderate-Complexity Financial Sentences for DisCoCat-Based Sentiment Analysis](https://arxiv.org/abs/2608.07439)

**<font color=#1a73e8>作者：</font>** Brian Llinas, Nikos Chrisochoides  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantum natural language processing (QNLP) provides a grammar-aware framework for text modeling, and Distributional Compositional Categorical (DisCoCat) is one of its theoretically grounded formulations. Prior work on financial sentiment analysis has identified practical limitations of DisCoCat, including parser sensitivity, high simulation cost, and difficulty handling longer sentences. We study an LLM-assisted preprocessing workflow that uses controlled rewriting to compress, simplify, or decompose moderate-complexity financial sentiment sentences into parser-compatible, circuit-efficient variants while preserving sentiment-bearing meaning. We compare prompting strategies, language models, and filtering configurations with the low-complexity-only DisCoCat baseline of Stein et al. At the circuit level, the strongest compression variants reduce average qubit and gate counts by more than 70 percent relative to the raw moderate-complexity subset. Across repeated training runs, GPT-4.1-mini with Prompt B achieves the highest observed mean accuracy, $0.550 \pm 0.035$, compared with $0.521 \pm 0.050$ for the baseline. Larger training splits do not necessarily improve downstream performance; across evaluated configurations, training-split size has a moderately negative association with accuracy (Pearson $r=-0.446$). These results provide exploratory evidence that LLM-assisted rewriting can make some moderate-complexity inputs usable within the evaluated DisCoCat configuration, while highlighting prompt design, filtering, and circuit-aware preprocessing as considerations for more scalable QNLP-based financial sentiment analysis.

---


### 116. [CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG](https://arxiv.org/abs/2608.07458)

**<font color=#1a73e8>作者：</font>** Gyuwan Kim, Cheoneum Park, Tao Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent optimization studies on Retrieval-Augmented Generation (RAG) have exploited chunk-level KV cache reuse to avoid processing long retrieved contexts for higher efficiency, while significant information redundancy and noise still remain in the coarse-grained chunks. This paper optimizes the Pareto frontier under low prefill latency constraints while maximizing accuracy by proposing CoinRAG (Contextualized Information Nugget KV Cache Reuse for Long-Context RAG). The name metaphorically reflects our core mechanism: much like assembling small tokens (or "coins") to accumulate a larger value, CoinRAG compositionally reuses offline-computed, fine-grained nugget caches to form a learned contextual representation efficiently in a more semantically relevant but compact manner. Specifically, instead of full-chunk encoding, CoinRAG identifies query-relevant semantic units within retrieved chunks through two-stage retrieval and seamlessly assembles their sliced KV representations with a chunk-level context. Extensive evaluations on LongBench multi-hop question answering tasks demonstrate that CoinRAG significantly reduces operational costs and outperforms the other baselines with a new Pareto frontier and an average 5.3% relative improvement in answer quality (F1) under a standard fast prefill latency budget.

---


### 117. [CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity](https://arxiv.org/abs/2608.07460)

**<font color=#1a73e8>作者：</font>** Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While post-training improves the capabilities of large language models (LLMs), it generally lowers their output diversity and creativity, negatively impacting tasks that explicitly require creativity (e.g., story generation) as well as those that require it implicitly, e.g., reinforcement learning (RL). We instead propose CreativeInstruct, a scalable instruction-tuning method that teaches LLMs to balance creative, base-model-like generations with the quality of post-trained models, by learning to inject special [StartCreativity] spans that bias generation toward creativity. Furthermore, we introduce a structural diversity metric based on graph edit distance, which captures narrative level variation missed by purely lexical and semantic metrics. On narrative generation, CreativeInstruct matches or exceeds the diversity of both multi-model baselines and distilled variants of their outputs, without sacrificing quality or requiring multiple models at inference time. These results are mirrored in our human evaluation, where we find that annotators rate CreativeInstruct generations as more creative than the post-trained LLMs' generations in 70.3% of cases. We also show the benefits of creative models as a substrate for RL: GRPO applied to a CreativeInstruct checkpoint improves by ~4% on AMC and ~5% points on MATH over the same training applied to the post-trained checkpoint.

---


> [!TIP]
> 当前位于：**101-117**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-117**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
