# 🧠 大模型相关研究 | 2026年06月03日

> 本类共 **376** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-376](./part-08.md)

---

### 251. [DOT-MoE: Differentiable Optimal Transport for MoEfication](https://arxiv.org/abs/2606.01666)

**<font color=#1a73e8>作者：</font>** Udbhav Bamba, Arnav Chavan, Aryamaan Thakur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The scaling of Large Language Models (LLMs) has driven significant performance gains but created substantial challenges in inference efficiency. While Mixture of Experts (MoEs) architectures address this by decoupling model size from inference cost, training MoEs from scratch is often unstable and compute intensive. Conversion of pre-trained dense models into sparse MoEs has emerged as an alternative solution; however, existing methods typically rely on heuristic neuron clustering or random splitting to partition the Feed-Forward Network (FFN) into experts. In this work, we propose DOT-MoE, a novel framework that formulates the decomposition of dense layers as a Differentiable Optimal Transport (DOT) problem. Instead of static heuristics, we model neuron assignment as a balanced transport problem, utilizing differentiable Sinkhorn-Knopp iterations to enforce strict expert capacity constraints. Furthermore, we utilize Straight-Through Estimators (STE) to jointly learn the discrete neuron-to-expert assignment and the token-to-expert routing policy end-to-end. Extensive experiments across multiple architectures and benchmarks demonstrate that DOT-MoE significantly outperforms structured pruning, heuristic clustering, and random-split baselines, retaining 90% of the original dense model's performance while reducing active parameters by 50%.

---


### 252. [ATLAS: Agentic Test-time Learning-to-Allocate Scaling](https://arxiv.org/abs/2606.01667)

**<font color=#1a73e8>作者：</font>** Peijia Qin, Qi Cao, Pengtao Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling has become a major way to improve large language model reasoning, but its orchestration has remained designer-engineered: a fixed sample budget, a fixed refinement loop, a fixed scoring rule, or a fixed search policy decides how compute is spent, leaving the model in charge of solving but not of orchestration. We introduce ATLAS, an agentic test-time scaling framework in which an LLM orchestrator owns the control loop end-to-end. Through a single action, explore, which dispatches a fresh independent solver on the original problem, the orchestrator decides whether to gather more evidence, when to stop, and how to synthesize the final answer; the action space is extensible, with each explore call optionally specifying solver, reasoning effort, or prompting strategy. We evaluate ATLAS on four benchmarks covering scientific question answering, code generation, and multimodal reasoning under a Claude Sonnet 4.6 backbone, where it reaches 56.00% on HLE-Verified, 82.29% on LiveCodeBench, 85.75% on GPQA-Diamond, and 23.71% on BabyVision while using far fewer API calls than fixed-workflow baselines. A multi-model extension, ATLAS-MM, that exposes solver choice as an additional action dimension further improves HLE-Verified to 60.00% and LiveCodeBench to 85.63%, with consistent gains on GPQA-Diamond and BabyVision. Ablations replacing the orchestrator's direct synthesis with a separate integrator degrade or fail to improve accuracy on three of four benchmarks, consistent with the role of stateful evidence management in producing the gains.

---


### 253. [When Meaning Travels: A Granular Lens on Hybrid-MoE's Role in Idiomatic Understanding for Language Models](https://arxiv.org/abs/2606.01671)

**<font color=#1a73e8>作者：</font>** Sarmistha Das, Vaibhav Vishal, Shreyas Guha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the contemporary epoch of multilingual education, learning idioms provides a fascinating gateway towards creativity, cultural values, historical context, and diverse perspectives inherent to various linguistic traditions. This paper showcases the navigation of retaining figurative and cultural semantics in low-resource Southeast Asian languages such as Hindi, Bengali, and Thai, where culturally rich idioms pose significant obstacles for computational modeling and cross-linguistic transfer due to their deep metaphorical complexity. To tackle such complexity, we present Varnika, a reconstructed multimodal idiom corpus comprising 3,533 multilingual idioms, enriched with seven idiomatic tones aligned with both textual and visual representations. Additionally, to infer informative idiomatic understanding, we introduce a Hybrid Mixture-of-Experts (HybridMoE) framework that embeds multiple idiomatic expert opinions while mitigating expert sparsity by integrating outputs from both selected and unselected experts through controlled hybridization, further augmented with Idiomatic Property Signals via masked multimodal embeddings. To analyze the performance across multiple dimensions, we propose the IDIO-TONE and Idiomatic Validation Score, a three-stage evaluation pipeline measuring (i) literal translation fidelity, (ii) visual-semantic alignment, and (iii) idiomatic meaning retention. Empirical evaluations highlight that HybridMoE achieves 5--6\% performance gains across advanced vision language models, demonstrating improved representation of figurative language and culturally embedded meaning in multilingual multimodal settings

---


### 254. [Off-the-Shelf LLMs as Process Scorers: Training-Free Alternative to PRMs for Mathematical Reasoning](https://arxiv.org/abs/2606.01682)

**<font color=#1a73e8>作者：</font>** Atoosa Chegini, Soheil Feizi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Selecting the best response from multiple small-model samples using a stronger scorer is a simple inference-time strategy, but fails when the small model has already committed to incorrect reasoning paths. PRM guided search avoids this by scoring candidate continuations during generation, but requires a reward model trained with step-level labels.
We propose Chunk-Level Guided Generation, a training-free alternative that uses an off-the-shelf large language model as a process scorer. At each step, a small model samples k fixed-length candidate chunks, while the larger model scores the candidates using likelihoods without generating any text. The selected chunk is committed before the next step, steering generation before errors can propagate.
We instantiate this framework with two selection rules: Likelihood-Guided Selection (LGS), which selects the chunk with the highest length-normalized large-model log-probability, and Contrastive-Guided Selection (CGS), which subtracts the small model's log-probability to favor chunks where the large model's preference diverges from the small model's. We show that scoring variable-length reasoning steps with large-model likelihoods is unreliable due to a systematic length bias that persists even after length normalization, and that fixed-length chunks avoid this confound.
On GSM8K, MATH, Minerva Math, AMC23, and AIME24 with Qwen2.5-1.5B guided by Qwen2.5-32B and Llama-3.2-1B guided by Llama-3.1-70B, CGS outperforms majority voting by up to 28 pp and, under matched guidance budgets, matches or outperforms Qwen2.5-Math-PRM-72B guided search on most benchmarks without reward-model training. With Qwen2.5-7B guided by Qwen2.5-72B, CGS reaches 81.8% on MATH and 63.6% on Minerva Math at k=16, surpassing majority voting by 4--6 pp. Finally, Chunk-Level Guided Generation produces substantially shorter reasoning traces than PRM guided search.

---


### 255. [CANARY: Zero-Label Detection of Fine-Tuning Contamination in Language Models](https://arxiv.org/abs/2606.01695)

**<font color=#1a73e8>作者：</font>** Swapnil Parekh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversaries can implant latent harmful behavior by poisoning as few as 1% of fine-tuning examples. The contamination is invisible to every output-level defense: harmful behavior lies dormant in the model's hidden-state geometry and does not appear in generated text until contamination exceeds 7.5%. We introduce CANARY (Contamination Auditor via Neural Activation Representation Yield), a zero-label checkpoint auditor that detects this hidden shift directly from two forward passes over an unlabeled prompt set. CANARY projects the hidden-state difference through a Sparse Autoencoder, filtering style noise to isolate meaningful semantic drift. It achieves AUROC = 1.000 at 1% contamination (95% CI = [0.997, 1.000]; Cohen's d = 3.28) across four model architectures and two training paradigms, 7.5x below where any output-level method fires, with zero false positives on benign fine-tuning and full robustness to style-matching and gradient-noise adaptive attacks. The same SAE feature basis drives a complete governance pipeline: SAE-filtered amplification surfaces latent harm at a 5x higher rate than standard generation; score-ranked prompts yield 4.2x red-teaming lift; and suppressing a handful of contamination-specific features at inference time reduces harm from 70% to 10% with no perplexity penalty. CANARY is the first zero-label framework to detect, verify, prioritize, and remediate supply-chain contamination from hidden states alone.

---


### 256. [Density-Aware Translation of Spurious Correlations in Zero-Shot VLMs](https://arxiv.org/abs/2606.01710)

**<font color=#1a73e8>作者：</font>** Afsaneh Hasanebrahimi, Hanxun Huang, Christopher Leckie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language models (VLMs), such as CLIP, achieve powerful zero-shot classification. However, their predictions remain sensitive to spurious correlations, where contextual cues dominate over semantic content. Earlier solutions typically rely on fine-tuning or prompt engineering, which either undermine the advantages of pre-trained models or are prone to hallucination. In this work, we propose Density-Aware Translation (DAT) that refines image-text similarity scores using a local geometric density term derived from group reference sets. Our approach is motivated by the phenomenon that CLIP embeddings exhibit a modality gap and lie on an anisotropic shell in the feature space: common patterns cluster near the mean, while rare patterns are pushed outward. This geometry creates uneven alignment, where spurious correlations are amplified while semantically meaningful but rare cues are marginalised. To address this, we employ a relative measure to rescale similarities based on embedding density, suppressing overconfident scores in diffuse regions while preserving dense, semantically consistent matches. Experimental results on benchmark datasets demonstrate consistent improvements in worst-group and average accuracy, highlighting density-aware translation as a simple and effective calibration mechanism for reliable zero-shot classification using multimodal models.

---


### 257. [Improving Visual Token Reduction via Rectifying Distortions for Efficient Multimodal LLM Inference](https://arxiv.org/abs/2606.01711)

**<font color=#1a73e8>作者：</font>** Hyeonwoo Cho, DongHyeon Baek, Yewon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Multimodal Large Language Models (MLLMs) have achieved remarkable success in vision-language tasks, yet the quadratic computational complexity arising from the vast number of visual tokens incurs significant memory and latency bottlenecks. While visual token reduction (VTR) strategies have been explored to mitigate this burden, existing methods overlook the positional and attentional consistency between the full and reduced sequences, resulting in a distorted representation. To this end, we propose RESTORE, a novel VTR framework that rectifies the positional and attentional distortions while maintaining efficiency. Specifically, we present a simple yet effective calibration method that restores lost visual attention by augmenting attention weights based on relative distances. We also introduce a distinctive anchor selection for token merging to mitigate information loss during feature averaging. Experimental results on multiple benchmarks demonstrate that our method consistently improves the accuracy of various reduction methods, achieving state-of-the-art performance while maintaining computational efficiency.

---


### 258. [Decentralized Instruction Tuning: Conflict-Aware Splitting and Weight Merging](https://arxiv.org/abs/2606.01717)

**<font color=#1a73e8>作者：</font>** Minsik Choi, Geewook Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instruction tuning aligns large language models, including multimodal ones, with diverse user intents, but scaling to heterogeneous mixtures is hindered by gradient interference and bandwidth-heavy synchronization. We ask whether these two bottlenecks can be addressed jointly by training parts of the mixture independently and reconciling them once in parameter space. We develop a local quadratic theory inside a shared flat basin that yields three results: weight merging produces a curvature-weighted variance reduction; PCA-aligned conflict splitting maximizes this gain along high-curvature directions; and merging additionally acts as spectral filtering with implicit norm regularization. These results directly motivate MERIT, a decentralized merge-ready instruction-tuning pipeline that estimates dataset-level gradient conflicts, partitions the mixture along the top PCA conflict axes, fine-tunes each partition independently with no inter-partition communication, and merges once via token-weighted averaging. On Qwen2.5-VL-3B with 136 Vision-FLAN tasks, MERIT improves the 8-benchmark average from 54.3 (joint training) to 57.0. The same recipe scales to a 7B model on a 1.6M-example, 176-source mixture -- matching or exceeding centralized joint training with minimal cost overhead -- and transfers to text-only FLAN. Our code is available at this https URL.

---


### 259. [Characterization of Multi-Model Agentic AI Systems on General Tasks via Trace-Driven Simulation](https://arxiv.org/abs/2606.01725)

**<font color=#1a73e8>作者：</font>** Donghwan Kim, Prakhar Singh, Younghoon Min 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI completes tasks through iterative planning, tool use, and reasoning based on observed outcomes. Despite its popularity, its system-level behavior remains poorly understood, particularly for complex datasets and agent architectures-owing to highly non-deterministic execution, prohibitive evaluation costs, and limited visibility into proprietary models. This paper presents GAIATrace, the first token-level trace dataset of two state-of-the-art agentic systems (MiroThinker and OWL) running GAIA, a benchmark composed of a heterogeneous mix of general-purpose tasks. Unlike prior trace datasets, GAIATrace captures full reasoning tokens, task-level structures, and activities of every major participating LLMs, enabling in-depth systems research. Complementing the dataset, we present Vidur-Agent, a trace-driven simulator that can replay GAIATrace to perform reproducible, low-cost system evaluation across diverse simulated environments. Using both artifacts, we characterize how modern agentic systems handle general tasks and how various system design choices shape their behavior, yielding several unique findings.

---


### 260. [Evidence-Gated LLM Priors for Multi-Objective Bayesian Optimization](https://arxiv.org/abs/2606.01730)

**<font color=#1a73e8>作者：</font>** Jiangyu Chen, Banyi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as heuristic advisors for black-box optimization, yet their suggestions and self-reported confidence are not necessarily calibrated to downstream objective values. This issue becomes more pronounced in multi-objective Bayesian optimization, where different objectives may require different expert knowledge and where an LLM expert can be useful for one objective but misleading for another.
We study how to use LLM-generated expert priors in discrete multi-objective Bayesian optimization without blindly trusting them. We propose an objective-wise reputation-market mechanism that treats each expert-objective pair as a falsifiable prior source. Expert weights are updated online from observed objective feedback, discounted over time, and gated by market-level trust. We then introduce a decoupled counterfactual gate that can use the LLM prior without confidence, use it with confidence, or abstain from the LLM prior entirely.
Across controlled synthetic stress tests and three molecule optimization benchmarks with \qwenflash{}-generated expert priors, we find that dynamic objective-wise calibration improves robustness over fixed LLM priors. However, raw LLM confidence is not reliably beneficial: on ESOL, confidence is positively correlated with prediction error; on FreeSolv, confidence can help; and on Lipophilicity, ignoring confidence remains strongest. Our fixed three-arm counterfactual gate improves over the first counterfactual variant on ESOL and FreeSolv, while an attempted margin portfolio exposes a useful negative result: margin selection should be acquisition-aware rather than based only on one-step prior error.

---


### 261. [FlatVPR: Plug-and-play Geo-linear Residual Adapter for Geometric Rectification of Foundation Model Feature Manifolds](https://arxiv.org/abs/2606.01734)

**<font color=#1a73e8>作者：</font>** Rai Hisada, Kanji Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes ``FlatVPR,'' a novel geometric rectification paradigm that effectively bridges the trade-off between map lightweightness and localization accuracy in visual place recognition (VPR) by enforcing a feature manifold structure where any descriptor between two adjacent anchors $\mathbf{z}_A$ and $\mathbf{z}_B$ can be accurately reconstructed via linear interpolation $\hat{\mathbf{z}}_{pseudo} = (1-t)\mathbf{z}_A + t\mathbf{z}_B$, where $t \in [0,1]$ denotes the relative position. While state-of-the-art foundation models such as DINOv2-ViT-S/14 provide robust semantic features, their latent manifolds exhibit prominent curvature, projecting uniform linear motion in physical space onto highly non-linear trajectories in the feature space, which hinders reliable reconstruction under sparse anchor conditions. To enable the aforementioned interpolation-based reconstruction, we introduce a residual transformation $\hat{\mathbf{z}} = \mathbf{z} + \text{Res}(\mathbf{z})$ to the raw foundation features $\mathbf{z}$, where $\text{Res}(\cdot)$ represents a learnable adapter. Our method explicitly suppresses manifold curvature using a mathematically grounded Pullback Flatness Loss that minimizes the deviation of intermediate features from the linear segment connecting adjacent anchors, thereby minimizing the intrinsic curvature of the manifold. Through this spatial flattening, map construction is formulated within an Expectation-Maximization (EM) framework, decoupled into a continuous M-step for manifold adaptation and a conceptual E-step for optimal anchor selection guidelines. Experiments on the NCLT dataset demonstrate that the application of our adapter leads to significant performance improvements even under extremely sparse anchor conditions with 100m intervals and extreme seasonal changes.

---


### 262. [Argument Collapse: LLMs Flatten Long-Form Public Debate](https://arxiv.org/abs/2606.01736)

**<font color=#1a73e8>作者：</font>** Yekyung Kim, Yapei Chang, Chau Minh Pham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs are increasingly used to draft public-facing arguments, they may flatten public debate by repeatedly introducing the same polished, plausible arguments. We study argument collapse, the tendency of essays generated by different LLMs to converge to a smaller set of main arguments, sub-arguments, and paragraph-level structures. We compare 1,039 human responses from 195 New York Times (NYT) debates, 448 human responses from 61 longer-form Boston Review (BR) forums, and 23,384 LLM-generated essays. In the NYT corpus, 65.3% of human main arguments are unique within a debate, compared to 3.4% of LLM main arguments. Asking LLMs to generate diverse answers adds variation, but a typical model recovers only about half of the distinct human main arguments, with much of the added variation falling outside the observed human argument space. Collapse also appears in sub-arguments, where among essays with the same main argument, 41.0% of human sub-arguments are unique versus 9.1% from LLM responses. Qualitatively, LLMs often reuse generalized and hedged sub-arguments, while humans prefer more concrete and topic-specific ones. Structure-wise, LLM-generated essays tend to follow a more fixed arc, often opening with a direct claim and moving quickly toward proposals. The same patterns hold in longer BR essays, suggesting that argument collapse extends beyond short-form responses.

---


### 263. [TrafficRAG: A Multimodal RAG Framework for Traffic Accident Liability Determination](https://arxiv.org/abs/2606.01737)

**<font color=#1a73e8>作者：</font>** Xu Li, Zedong Fu, Xinyi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traffic accident liability analysis is a critical yet challenging task in intelligent transportation and legal assistance. Existing methods often suffer from low efficiency, subjective judgment, and inconsistent analysis results. Meanwhile, large language models are constrained by noisy video inputs and insufficient legal domain knowledge. To address these issues, this work presents TrafficRAG, a multimodal retrieval-augmented framework for automated traffic accident analysis and report generation. Specifically, the proposed framework first adopts a vision-language model to produce structured textual descriptions of accident scenarios, which serve as accurate retrieval queries. Based on these textual queries, a hybrid retrieval strategy integrating BM25 sparse retrieval and dense embedding retrieval is employed to fetch relevant traffic regulations and similar historical cases. Finally, the large language model incorporates retrieved legal knowledge and multimodal accident evidence for comprehensive reasoning, and generates standardized, legally grounded liability analysis reports. Extensive experiments show that TrafficRAG consistently outperforms baseline methods, achieving 77.32% Legal Norm Adaptation Accuracy, 81.71% Factual Faithfulness, and a Liability Ratio MAE of 5.48%. The results validate that integrating multimodal factual evidence with legal clauses via retrieval augmentation can effectively improve the reliability and accuracy of traffic accident liability determination.

---


### 264. [THRD: A Training-Free Multi-Turn Defense Framework for Jailbreak Attacks on Large Language Models](https://arxiv.org/abs/2606.01738)

**<font color=#1a73e8>作者：</font>** Zhiqing Ma, Zhonghao Xu, Dong Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreak attacks pose a growing threat to LLMs by exploiting conversational dynamics such as gradual escalation and cross-turn coordination. Existing defenses either rely on costly retraining -- often degrading model utility -- or apply single-turn analysis independently at each turn, failing to capture how risk accumulates along interaction trajectories. We observe that safety behavior in multi-turn interaction is trajectory-dependent: dialogue history continuously reshapes the model's conditioning context, making it insufficient to evaluate each turn in isolation. Motivated by this insight, we present THRD, the first training-free framework that explicitly models temporal risk accumulation for multi-turn jailbreak defense. THRD integrates four modules: a Turn-level Risk Assessor (TRA) for instantaneous risk estimation, a Historical Context Analyzer (HCA) for cross-turn intent escalation detection, a Response Evaluator (RE) for identifying facilitative outputs, and a Decision Module that combines these signals through a time-evolving scoring mechanism with attenuation-based modulation and trend-aware adjustment. Experiments against state-of-the-art multi-turn attacks -- including tree-search-based and multi-agent collaborative methods -- across two target models show that THRD reduces ASR to 0.2--4.0% while preserving model utility within 1.5% degradation on MMLU and GSM8K. Ablation studies confirm non-redundant module contributions and stable cross-architecture generalization. Analysis of first rejection triggers reveals that over 70% of multi-turn attacks require Turn~2 or later to detect, validating the necessity of explicit temporal aggregation.

---


### 265. [TriAlign: Towards Universal Truth Consistency in Personalized LLM Alignment](https://arxiv.org/abs/2606.01755)

**<font color=#1a73e8>作者：</font>** Thi-Nhung Nguyen, Linhao Luo, Rollin Omari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized large language models adapt responses to users' preferences and social attributes, but can introduce substantial universal truth inconsistencies across social groups, where some groups systematically receive less accurate responses on objective tasks. Existing alignment methods either ignore personalization or mainly focus on subjective preference alignment, largely overlooking fairness and consistency in universal truths. To address this gap, we study Truth-Invariant Alignment (TIA), an alignment problem for personalized LLMs that aims to ensure universal truths remain consistent across social groups while preserving personalization. We propose TriAlign, the first offline multi-agent reinforcement learning (MARL) framework for TIA, where each social group is modeled as an agent interacting. TriAlign jointly optimizes universal truth accuracy, cross-group truth consistency, and personalization through a fairness-aware objective and an explicit inconsistency penalty. Experiments across diverse benchmarks demonstrate that TriAlign achieves a stronger balance among these three objectives than strong baselines, reducing universal truth disparities across social groups while improving both objective task performance and personalization quality.

---


### 266. [EvoCut: Multi-Layer Evolution-Aware Visual Token Compression for Efficient Large Vision-Language Models](https://arxiv.org/abs/2606.01756)

**<font color=#1a73e8>作者：</font>** Hongyu Lu, Feng Zhang, Wenwei Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) achieve strong performance on image and video understanding tasks, but their inference efficiency is constrained by the large number of visual tokens produced by vision encoders. Most existing visual token compression methods estimate token importance from attention scores or representation properties at specific layers, overlooking how visual tokens evolve across the vision encoder. Such layer-specific criteria may provide incomplete importance estimates and limit performance preservation after compression. To address this issue, we analyze layer-wise visual token evolution directions and observe that tokens form multiple group evolution directions across vision-encoder layers. Our analysis further shows that informative tokens tend to exhibit persistent deviations from common group evolution directions. Based on this observation, we propose EvoCut, a training-free and attention-free visual token compression method that estimates token importance from multi-layer evolution deviation. Experimental results show that EvoCut can retain only 11.1\% of the visual tokens on LLaVA-1.5-7B while preserving 94.4\% of the average performance, demonstrating its effectiveness in balancing efficiency and accuracy.

---


### 267. [EvoBrain: Continual Learning of EEG Foundation Models Across Heterogeneous BCI Tasks](https://arxiv.org/abs/2606.01767)

**<font color=#1a73e8>作者：</font>** Yangxuan Zhou, Sha Zhao, Jiquan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is the cornerstone of non-invasive brain-computer interfaces (BCIs), yet conventional decoding relies on fragmented, task-specific architectures that severely limit cross-task scalability. While EEG foundation models pre-trained on massive corpora promise universal brain decoding, current post-training depends on task-isolated fine-tuning. This static paradigm restricts knowledge transfer across heterogeneous tasks, hinders model scalability, and incurs computational and storage overheads that scale linearly with task count. To overcome these bottlenecks, we formulate downstream adaptation as a cross-task continual learning problem and propose EvoBrain, a dynamic, task-aware continual learning framework for unified EEG decoding. EvoBrain addresses the plasticity-stability trade-off via two complementary components: (1) Neuro-Spectral Task Normalization (NSN) aligns incoming tasks with historical statistics while recalibrating spectral responses to handle distributional and neuro-spectral shifts; and (2) Response-Affinity Distillation (RAD), combined with time-dependent replay, preserves old-task response geometry and promotes selective knowledge transfer between spectrally compatible tasks, effectively mitigating forgetting. Extensive evaluations across six distinct BCI tasks demonstrate that EvoBrain consistently surpasses state-of-the-art methods across diverse foundation backbones, optimally balancing plasticity and stability. To our knowledge, this work pioneers cross-task continual learning in the EEG domain, advancing the realization of a unified, one-for-all brain decoding system.

---


### 268. [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams](https://arxiv.org/abs/2606.01770)

**<font color=#1a73e8>作者：</font>** Zewen Liu, Zhan Shi, Yisi Sang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-harness systems such as A-Evolve, GEPA, and Meta-Harness improve LLM agents by optimizing prompts, skills, tools, memories, and supporting infrastructure from execution feedback, but they are typically evaluated on fixed offline benchmarks. Real deployments instead present open-ended task streams: histories grow without a fixed endpoint, heterogeneous tasks require different harnesses, and problem distributions shift over time. These challenges make a single repeatedly and densely updated harness brittle, causing performance degradation as accuracy peaks early and then declines. This motivates sustained harness construction with task-wise adaptation. We introduce Adaptive Auto-Harness, a framework and system for such streams. The framework decomposes the gap to an oracle harness into evolution loss and adaptation loss. The system addresses these losses with a stateful multi-agent evolver, a harness tree with solve-time routing, and human-steering hooks for cases where history lacks the needed signal. Across prediction-market, security-competition, and event-forecasting streams, Adaptive Auto-Harness outperforms five existing auto-harness baselines and ablations attribute gains to better construction, routing, or targeted human steering. Code is available in this https URL .

---


### 269. [FLARE: Diffusion for Hybrid Language Model](https://arxiv.org/abs/2606.01774)

**<font color=#1a73e8>作者：</font>** Yuchen Zhu, Jing Shi, Chongjian Ge 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) large language models (LLMs) have achieved broad practical success, but sequential decoding remains a key bottleneck for low-latency deployment. Recent efficient-inference work has progressed along two axes: reducing the cost of each model invocation through efficient architectures, and reducing serial decoding steps through parallel generation. Hybrid attention backbones address the former, while diffusion language models (dLLMs) pursue the latter via iterative parallel denoising. Combining these advantages remains challenging: AR-to-dLLM conversion often fails to preserve seed-checkpoint capability, and hybrid-attention recurrent states and masking constraints make diffusion training and serving nontrivial. We present FLARE, a systematic conversion framework for hybrid-attention LLMs. Our analysis identifies transfer data quality as the primary determinant of capability preservation, outweighing loss formulation and attention-mask design. The resulting framework combines a token-equal AR-and-diffusion objective, hardware-aware kernels, and unified inference, enabling one checkpoint to support both AR-style verified decoding and diffusion-style parallel denoising. Starting from strong AR checkpoints with limited post-training data, FLARE is competitive with leading open-source dLLMs across model scales and delivers consistent throughput gains over open-source dLLM baselines in single-GPU concurrent serving. Our results further suggest that practical dLLMs are limited not only by decoding algorithms, but also by transfer data quality and the training inefficiency of current block-diffusion objectives, motivating joint design of data, objectives, architectures, and inference systems.

---


### 270. [HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems](https://arxiv.org/abs/2606.01779)

**<font color=#1a73e8>作者：</font>** Mingju Chen, Can Lv, Guibin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly expected to operate across heterogeneous task regimes that require distinct execution paradigms. This challenges fixed agent systems and motivates system-level meta-adaptation beyond isolated component updates. While existing works have adapted external harness or trained underlying reasoning policies, full-system adaptation remains insufficiently characterized. The adaptation space between structure and execution is rarely made explicit, and the compatibility between the external harness and the internal reasoner is not optimized jointly. We propose HarnessForge, a meta-adaptive framework for evolving LLM agent systems. HarnessForge formulates an agent system as a harness--policy pair, defining a stable adaptation space that separates harness-level execution structure from policy-level reasoning behavior. It then performs harness--policy co-evolution through fault-guided harness tailoring and harness-conditioned policy alignment. Experiments across five benchmarks from diverse domains show that HarnessForge consistently improves both Qwen3-4B and Qwen3-8B backbones, outperforming harness-only and policy-only baselines with gains of up to 12.0\% over the strongest baseline and achieving favorable rollout-efficiency tradeoffs, demonstrating that harness--policy co-evolution is effective, and that executable compatibility between the harness and reasoning policy is essential for agent-system adaptation. The code is available at this https URL.

---


### 271. [STaR-KV: Spatio-Temporal Adaptive Re-weighting for KV Cache Compression in GUI Vision-Language Models](https://arxiv.org/abs/2606.01790)

**<font color=#1a73e8>作者：</font>** Yuhang Han, Wenzheng Yang, Yujie Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-model-based graphical user interface (GUI) agents have shown broad automation capabilities, yet deployment is bottlenecked by a key-value (KV) cache that grows linearly with interaction steps. For instance, UI-TARS-1.5-7B consumes 76 GB of GPU memory on merely five screenshots, approaching the capacity of mainstream 80 GB accelerators. Existing KV compression methods share two structural assumptions: aggregating visual-token importance into a single shared saliency map, and applying a fixed top-B cutoff to the fused score distribution. Pilot measurements refute both: spatial specialization lives at the attention-subspace level and migrates across layers, while the score distribution drifts in shape along a trajectory. We propose STaR-KV (Spatio-Temporal Adaptive Re-weighting), a training-free KV cache compression framework that calibrates token importance along three axes: (i) subspace-aware scoring driven by online spatial mutual information; (ii) a temporal stability discount that suppresses redundant cache entries from persistently attended subspaces; and (iii) an entropy-derived temperature that adaptively reshapes the score distribution. Across four GUI benchmarks, STaR-KV achieves the strongest average accuracy among state-of-the-art KV compression methods (e.g., GUIKV, SnapKV) at matched budgets, with no compression-stage FLOPs overhead (-0.07%) and cutting peak GPU memory by nearly 40% at a 20% KV-cache budget. Code is available at this https URL.

---


### 272. [Multilinguality of Large Language Models From a Structural Perspective](https://arxiv.org/abs/2606.01800)

**<font color=#1a73e8>作者：</font>** Haruki Sakajo, Yusuke Sakai, Hidetaka Kamigaito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have excelled in processing multiple languages through pre- and post-training on multilingual data, even though English dominates the training data. Prior work focusing on token representations has revealed how those LLMs process non-English text. Although these analyses have provided insightful findings, they fail to capture a structural view, which is an inherent property of language. In this study, we explore the multilinguality of LLMs through representational structural analysis. Our findings reveal that low-resource languages are structurally more different from English than high- and mid-resource languages, and that language-specific post-training alters their structures while preserving inter-language relationships.

---


### 273. [MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand](https://arxiv.org/abs/2606.01801)

**<font color=#1a73e8>作者：</font>** Shouang Wei, Houcheng Min, Xinpeng Dong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multimodal agents have achieved notable progress on complex reasoning tasks through tool use, yet remain limited by two issues: statically predefined tool inventories fail to generalize to unseen scenarios, and indiscriminate tool invocation incurs redundant cost and noise-induced errors. We propose MetaForge, a multimodal agent framework that learns when to invoke tools and how to evolve its toolset on demand. MetaForge factorizes agentic behavior into four coupled stages: Decide (judging whether tool use is warranted), Retrieve (selecting suitable tools), Adapt (grounding tool parameters in task context), and Forge (synthesizing new skills online and recycling them into the tool library for reuse), forming a closed judge-retrieve-adapt-forge-recycle loop. A unified orchestration policy enables the agent to choose among answering directly, reusing existing tools, or forging new ones. We jointly optimize invocation necessity, retrieval accuracy, execution effectiveness, and forged-skill reusability via reinforcement learning, with an explicit invocation-cost penalty discouraging redundant calls. Across 12 benchmarks, MetaForge consistently surpasses 16 baselines in accuracy, efficiency, and generalization, validating a paradigm shift from static tool inventories to on-demand self-evolution.

---


### 274. [OctoT2I: A Self-Evolving Agentic Text-to-Image Router](https://arxiv.org/abs/2606.01803)

**<font color=#1a73e8>作者：</font>** Xu Jiang, Bin Chen, Gehui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The explosive growth of Text-to-Image (T2I) models, from large-scale versions to lightweight, real-time ones, now faces diminishing marginal returns from single-model scaling. Agentic T2I methods emerged to alleviate this bottleneck by using multiple models. However, existing agentic T2I methods suffer from three key challenges: reliance on expensive handcrafted priors or human annotations, rigid single-path decision mechanisms, and a neglect of inference efficiency. To address these challenges, we introduce OctoT2I, a novel agentic framework that reformulates the T2I task as a joint optimization of generation quality and inference efficiency. OctoT2I implements a stateful, multi-round routing strategy that adaptively selects the most suitable tool based on its knowledge and memory. This strategy is enabled by a knowledge base built from scratch by our novel Self-Evolving Mechanism. This mechanism, which requires no human supervision, first autonomously defines foundational Conceptual Dimensions (eg, style, color, count) and then intelligently explores their combinations via an iterative" Propose--Solve--Evaluate--Learn"(PSEL) loop. The PSEL loop efficiently discovers each tool's capability frontier, driving continuous improvement without external guidance. Extensive experiments demonstrate that OctoT2I achieves competitive performance (0.96) on GenEval while delivering a 90.3% inference speedup and a 56.6% energy-efficiency gain over the leading baseline (Flow-GRPO), striking an exceptional balance between performance and efficiency. Code and models will be made available.

---


### 275. [ProbeScale: Probing Analysis to Optimize Neural Scaling Laws for Efficient Small Language Model Inference](https://arxiv.org/abs/2606.01806)

**<font color=#1a73e8>作者：</font>** Sourav Das  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small Language Models (SLMs) offer a balance between capability and computational feasibility. Neural scaling laws inform their optimal training, suggesting that they possess rich internal representations that scale with their size. However, deploying even these SLMs can be challenging under strict resource constraints. Language model probing provides methods for analyzing the linguistic knowledge encoded in a model's internals. We propose ProbScale, a framework that unifies insights from scaling laws and probing to identify parameter-efficient subnetworks within pre-trained SLMs. ProbScale utilizes the high-quality representations of well-scaled SLMs and uses task-specific probes to mathematically quantify the relevance of each layer for target downstream capabilities. This allows selecting subnetworks that optimally trade off performance against parameter size. We formulate the subnetwork selection as finding a layer subset maximizing aggregated, task-weighted probe performance under a parameter budget. Experiments on representative SLMs such as RoBERTa-Large and T5-Base demonstrate that ProbScale identifies subnetworks achieving significant parameter reduction, from 5 to 10 times, while maintaining high performance (95% to 98% of the original SLMs) on targeted tasks, outperforming heuristic baselines.

---


### 276. ["I've Seen How This Goes": Characterizing Diversity via Progressive Conditional Surprise](https://arxiv.org/abs/2606.01811)

**<font color=#1a73e8>作者：</font>** Matthew Khoriaty, David Williams-King, Shi Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Measuring the diversity of creative outputs is central to evaluating post-training mode collapse, comparing decoding strategies, and quantifying creative behavior in both AI and human writing. We propose a new approach to measuring diversity using in-context learning, of which the ``Decan'' metric, $D_{Ca_n} = C \times a_n$, is the working instance we evaluate: a per-byte score read off the per-token log-probabilities of a base model $\theta$ in a \emph{single forward pass} per permutation, with no embedding model, no reference corpus, and no human labels. This approach is grounded in information theory, makes use of language model in-context learning to detect a wide range of similarities between any number of inputs, and obviates the need to train a special-purpose model. The same pipeline scores AI samples and human-written response sets, with diversity treated as a property of (responses, prompt, scoring model). On Tevet and Berant's human-grounded McDiv benchmark, $D_{Ca_n}$ reaches OCA 0.846 on the McDiv prompt\_gen set where it performs best, behind the strongest neural baseline reported in Tevet and Berant (SentBERT, 0.897). On the OLMo-2-7B post-training pipeline, $D_{Ca_n}$ drops monotonically across the base $\to$ SFT $\to$ DPO $\to$ RLVR stages, detecting the type of diversity loss that creative-writing applications care about.

---


### 277. [CRAB-Bench: Evaluating LLM Agents under Complex Task Dependencies and Human-aligned User Simulation](https://arxiv.org/abs/2606.01815)

**<font color=#1a73e8>作者：</font>** Danqing Wang, Akshay Sivaraman, Lei Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM agents in realistic service scenarios requires complex task dependencies, imperfect user behavior, and an evaluation that accommodates multiple valid solutions. We introduce CRAB-Bench (Constraint-based Realistic Agent Benchmark) and RUSE (Realistic User Simulation Engine) to address this gap. CRAB-Bench generates tasks via a constraint graph over multiple interdependent entities with structured distractors, requiring agents to reason carefully over thousands of misleading candidates where only a tiny fraction of solutions are valid. RUSE replaces cooperative, template-like simulators with realistic users grounded in human behavioral studies, instantiated across diverse personas and four behavioral dimensions. Experiments on four frontier LLM agents show that the best model achieves only 61% pass@1 on CRAB-Bench, and switching to RUSE causes further drops of up to 57%, concentrated in task-solving ability rather than conversational quality. Information Disclosure is the most damaging behavioral dimension, and agents interacting with RUSE are less likely to admit mistakes, instead masking errors through implicit corrections.

---


### 278. [ROGLE: Robust Global-Local Alignment with Automated Region Supervision for Text-Based Person Search](https://arxiv.org/abs/2606.01825)

**<font color=#1a73e8>作者：</font>** Zequn Xie, Xibei Jia, Sihang Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-Based Person Search (TBPS) aims to retrieve pedestrian images using natural language queries. However, existing TBPS models, especially those based on CLIP, struggle with fine-grained understanding due to global representational bias and semantic sparsity inherited from training on short captions. This results in weak fine-grained alignment, exacerbated by the scarcity of region-level annotations. To address this, we propose ROGLE (Robust Global-Local Embedding), a unified framework that overcomes reliance on costly manual annotations through an automated Region-to-Sentence Matching (RSM) strategy. RSM automatically mines pseudo region-sentence pairs for scalable fine-grained supervision. Furthermore, ROGLE employs a multi-granular learning strategy that fuses global contrastive learning with region-level local alignment. We also introduce the P-VLG Benchmark, a large-scale dataset constructed by curating and enriching images from established public benchmarks. It features over 100,000 annotated regions and rich long-form captions, making it the first TBPS benchmark to support both global and local assessment protocols. Extensive experiments show that ROGLE significantly outperforms existing approaches, particularly on challenging long-form queries. Code and the P-VLG benchmark will be made publicly available.

---


### 279. [Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus](https://arxiv.org/abs/2606.01828)

**<font color=#1a73e8>作者：</font>** Wanshuang Gou, Zihan Liu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model-driven multi-agent systems enhance the reliability of complex reasoning tasks through multi-round deliberation, role specialization, and cross-validation. However, existing multi-agent debate and collaboration frameworks typically adopt fully connected communication, causing the number of messages, token costs, and end-to-end latency to grow approximately quadratically with the number of agents; although fixed sparse topologies reduce overhead, they cannot adapt communication relationships to different task instances or intermediate reasoning states, making them prone either to preserving low-value interactions or to losing critical error-correction information. To address this problem, this paper proposes DySCo (Dynamic Sparse Consensus), a dynamic trust-aware sparse consensus mechanism. In each round of reasoning, DySCo estimates the value of communication edges based on agent reliability, answer divergence, and task relevance, and selects a small number of high-value edges for message exchange under budget constraints; it then aggregates the answers of different agents through dynamic trust weights and terminates the discussion early once consensus stabilizes. This mechanism replaces universal broadcasting with on-demand communication, thereby reducing communication overhead while preserving essential cross-validation information. We further present analyses of communication complexity and consensus stability, and evaluate the performance of DySCo on mathematical reasoning, logical reasoning, and factual question-answering tasks.

---


### 280. [LayerRoute: Input-Conditioned Adaptive Layer Skipping via LoRA Fine-Tuning for Agentic Language Models](https://arxiv.org/abs/2606.01838)

**<font color=#1a73e8>作者：</font>** Prateek Kumar Sikdar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic language model systems alternate between two structurally distinct step types: structured tool calls (short, deterministic, low perplexity) and open-ended planning/reasoning steps (long, complex, high perplexity). Despite this heterogeneity, current inference systems apply identical compute to every step. We introduce LayerRoute, a lightweight adapter that learns to selectively skip transformer blocks on a per-input basis. LayerRoute augments each of the 24 transformer blocks in Qwen2.5-0.5B-Instruct with: (1) a per-layer router (~897 parameters, Linear(896,1)) that outputs a hard binary gate via the straight-through estimator, and (2) LoRA adapters (rank 8, ~1.08M parameters) on the Q/K/V/O attention projections. The backbone weights remain frozen. A single end-to-end training pass on agentic data (Hermes, Glaive, GSM8K, Turing) with a gate regularisation term forces the system to discover which blocks are skippable per input type. After 3,000 steps (6.4 minutes on an A100 40GB), LayerRoute achieves a 12.91% skip differential: tool calls skip 15.25% of FLOPs while planning steps skip only 2.34%, using only 1.10M trainable parameters (0.22% of the 494M backbone). Quality improves over the base model due to LoRA adaptation, with perplexity delta of -1.29 on tool calls and -1.30 on planning.

---


### 281. [Unveiling the Limits of Large Language Models in Inferring Pragmatic Meaning from Non-Verbal Responses](https://arxiv.org/abs/2606.01845)

**<font color=#1a73e8>作者：</font>** Sugyeong Eo, Heuiseok Lim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) have shown considerable progress in pragmatic language understanding, prior research has focused mainly on their comprehension of verbal behavior. Nonetheless, non-verbal behavior remains a fundamental component of human communication, especially when deliberately utilized in isolation to convey indirect meanings. In this work, we present the first systematic evaluation of LLMs' ability to infer pragmatic meaning in dialogue consisting solely of non-verbal responses. We explore three research questions: (1) Can LLMs recognize indirect intent conveyed through non-verbal responses? (2) When and how do LLMs fail to capture non-verbal intent? (3) How can we improve LLMs' ability to interpret non-verbal intent?. Through the evaluation, we observe that LLMs struggle to infer underlying meaning from non-verbal responses, with accuracy dropping by up to 60% points compared to verbal ones. Further extensive analysis reveals a behavioral pattern in LLMs' interpretations of non-verbal behavior and demonstrates that in-context learning facilitates pragmatic inference.

---


### 282. [Does Compression Preserve Uncertainty? A Unified Benchmark for Quantized and Sparse LLMs via Conformal Prediction](https://arxiv.org/abs/2606.01850)

**<font color=#1a73e8>作者：</font>** Yujia Tong, Yuxi Wang, Yunyang Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model compression techniques such as quantization and pruning are widely used to reduce the deployment cost of large language models (LLMs), with existing evaluations focusing almost exclusively on accuracy preservation. However, in safety-critical applications, a model's ability to reliably quantify its own uncertainty is equally important. We ask: does compression preserve this ability? To answer this question, we benchmark 12 LLMs under various compression configurations across five NLP tasks, using conformal prediction to provide a rigorous, distribution-free measure of uncertainty. Our experiments reveal that: (I) compression frequently decouples accuracy from uncertainty; (II) larger models absorb compression-induced uncertainty far more effectively than smaller ones; and (III) uncertainty inflation is often threshold-like rather than gradual. These results suggest that accuracy-only evaluation is insufficient for assessing the deployment readiness of compressed LLMs, and that uncertainty-aware benchmarking should be a standard component of model compression pipelines.

---


### 283. [WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis](https://arxiv.org/abs/2606.01869)

**<font color=#1a73e8>作者：</font>** Shuo Lu, Yinuo Xu, Kecheng Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly asked not only to write static interfaces, but to construct executable interactive worlds from natural language. Browser-native 3D, commonly built with this http URL, is a natural next frontier: generated programs must integrate assets, obey spatial and physical constraints, and keep user-facing controls synchronized with hidden runtime state. Existing web-generation benchmarks and evaluators, however, largely observe only pixels or DOM nodes, while the mechanics of a this http URL world unfold inside an opaque <canvas>. We introduce WorldCoder-Bench, a benchmark for autonomous, physically grounded 3D world synthesis. WorldCoder-Bench contains 2,026 expert-curated tasks across Simulation, Rendering, and Application scenarios, with optional .glb assets and hidden behavioral contracts. We further propose StateProbe, an execution-based protocol that probes generated programs in a sandboxed browser and verifies hidden, mutation-hardened contracts over runtime states and transitions. Beyond verification coverage, we report Return on Automation and Time Efficiency Multiplier to measure correctness-adjusted cost and time savings. Across nine frontier models, the best system reaches only 27.8% verification coverage on WorldCoder-Core and 19.9% on WorldCoder-Robust, with failures dominated by state-schema drift and broken interaction chains rather than missing scene elements. Utility metrics further show that cheap or fast models can still provide substantial value on easier domains. WorldCoder-Bench is available at this https URL.

---


### 284. [G2LoRA: Gradient Orthogonal Low-Rank Adaptation Framework for Graph Continual Learning on Text-Attributed Graphs](https://arxiv.org/abs/2606.01873)

**<font color=#1a73e8>作者：</font>** Yuhan Wang, Yibo Ding, Yutong Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-Aligner has emerged as a prevalent pre-training paradigm for Text-Attributed Graphs(TAGS), aligning graph and text modalities into a shared embedding space via CLIP-style contrastive learning. While effective on individual downstream tasks, we observe severe catastrophic forgetting when such models are sequentially fine-tuned on streaming tasks. Although parameter-efficient fine-tuning alleviates forgetting to some extent, it remains insufficient to resolve task interference and ineffective knowledge transfer. In this work, we study graph continual learning for LLM-as-Aligner models on TAGs, with the goal of mitigating interference while promoting positive transfer across tasks. This setting introduces two fundamental challenges: (1) heterogeneous downstream tasks induce shifting optimization objectives, hindering unified fine-tuning; and (2) graph and text encoders exhibit different sensitivities to adaptation, making uncoordinated updates prone to misalignment. To address these challenges, we propose G2LoRA, a continual learning framework for TAGs. G2LoRA unifies node-, link-, and graph-level tasks under a single graph--text alignment objective, and enables consistent optimization across domain/class/task incremental modes. To reduce task interference while encouraging positive transfer, G2LoRA performs category-aware gradient projection in structured subspaces, resolving conflicting updates and enabling conditional backward transfer to balance forward and backward knowledge flow. To further prevent cross-modal drift, G2LoRA introduces gradient magnitude modulation to coordinate update rates between graph and text encoders. Extensive experiments on benchmark datasets demonstrate that G2LoRA consistently outperforms strong baselines across different backbone architectures, achieving superior continual performance and transferability.

---


### 285. [CultureForest: Understanding and Evaluating Cultural Norm Grounded Reasoning in LLMs](https://arxiv.org/abs/2606.01879)

**<font color=#1a73e8>作者：</font>** Yangfan Ye, Xiaocheng Feng, Jialong Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing research largely reduces cultural intelligence in LLMs to a knowledge-level problem, overlooking whether models can effectively utilize their acquired knowledge in realistic scenarios. To bridge this gap, we introduce CultureForest, a benchmark for \textit{Cultural Norm Grounded Reasoning}. Each question is grounded in a small set of atomic norms, enabling verifiable and attributable evaluation. CultureForest comprises 5,378 examples across 8 domains and 53 countries/regions, and supports a progressive evaluation from multiple-choice to open-ended generation. Extensive experiments reveal that even top-tier models degrade substantially in open-ended settings, accompanied by pronounced cross-region disparities. Through targeted analysis, we uncover several consistent patterns: (1) test-time reasoning yields limited gains and may exacerbate inequity; (2) models exhibit highly shared regional preference structures; (3) model responses are markedly conservative, especially under stricter cultural constraints; and (4) by disentangling cultural knowledge acquisition from cultural reasoning, we show that while LLMs possess substantial cultural knowledge, their performance is further bottlenecked by its effective use. These findings point to a necessary shift from knowledge-centric evaluation toward measuring knowledge-grounded reasoning.

---


### 286. [Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents](https://arxiv.org/abs/2606.01886)

**<font color=#1a73e8>作者：</font>** Ailiya Borjigin, Igor Stadnyk, Ben Bilski 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial AI agents often fail for a simple reason: they make users carry the complexity. A user must repeatedly restate goals, risk preferences, portfolio context, past judgments, and shifting market assumptions, while the agent answers, retrieves, acts, and forgets. In finance, this is not just inconvenient. In tasks such as market analysis, copy-trading review, and trade preparation, forgotten context and stale memory can create latency, repeated errors, weak auditability, and unsafe decisions.
We propose the interaction-native knowledge harness (InKH), an architecture for financial LLM agents that absorbs complexity into the system. InKH converts user, market, portfolio, and tool events into structured operational knowledge. It uses passive knowledge injection to assemble a bounded working context buffer before the main model step, temporal graph memory for low-latency retrieval, a wiki audit surface for human-readable governance, and background extraction with maturity, decay, and write-time invalidation.
We evaluate InKH on a reproducible controlled synthetic benchmark with 24 random seeds, 4 rounds, 80 episodes per round, and 6 baselines, producing 46,080 baseline-conditioned evaluations. InKH achieves mean task quality of 0.815 at 900 ms latency. Compared with agent-driven wiki-walk memory, it reduces latency by 82.95 percent, token cost by 82.29 percent, and stale-knowledge usage by 96.58 percent, while improving quality by 0.108 and traceability by 0.461. Compared with a temporal-graph system without invalidation, it improves quality by 0.050 and reduces stale-memory usage by 96.58 percent with comparable serving cost.
The results support a design thesis for financial AI: adoption happens when complexity is absorbed by the system rather than transferred to the user. The benchmark validates architecture-level behavior, not live trading performance.

---


### 287. [Segment-driven Structural Induction and Semantic Alignment for Heterogeneous Tabular Representation](https://arxiv.org/abs/2606.01890)

**<font color=#1a73e8>作者：</font>** Woojun Jung, Susik Yoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world domains often contain heterogeneous tables whose headers vary while their underlying attribute semantics are shared, making it difficult to induce domain-specialized semantics from table-local evidence alone. Existing encoders model parts of this problem, but often underuse column-level value distributions and apply uniform objectives across attributes with different semantic roles. We propose NAVI, a segment-centric pretraining framework that treats each header-value pair as the unit for aggregating schema-level structural evidence and column-level distributional evidence. We realize this design through Masked Segment Modeling and Entropy-driven Segment Alignment, which jointly enforce structured header-value coupling and semantic alignment across stable and instance-specific attributes. Experiments on heterogeneous in-domain tables show improved reconstruction, semantic consistency, and downstream utility across evaluation settings overall.

---


### 288. [Auteur: Language-Driven Cinematographic Framing for Human-Centric Video Generation](https://arxiv.org/abs/2606.01900)

**<font color=#1a73e8>作者：</font>** Muhammed Burak Kizil, Enes Sanli, Niloy J. Mitra 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video models have achieved remarkable visual fidelity and temporal coherence, yet intentional camera control remains elusive. Existing frameworks treat camera motion as a byproduct of pixel synthesis, producing trajectories that are stochastic, spatially inconsistent, and indifferent to the human subject driving the scene. In this work, we present Auteur, a method for language-driven, human-centric camera framing in generative video. Our core insight is that professional filmmakers conceive shots not as world-space trajectories but as framings defined relative to the actor, encoding shot size, angle, and composition as functions of human pose and motion. We formalize this intuition as a human-centric camera parameterization and introduce a Domain-Specific Language (DSL) that is convertible to standard 6-DoF camera parameters. A fine-tuned multimodal large language model then acts as a virtual director, mapping natural language descriptions and coarse human motion to sparse DSL keyframes that are deterministically interpolated into continuous camera trajectories, which are then provided as input to video generators. We train and evaluate Auteur on a new dataset of 34K aligned text, human motion, and DSL-annotated camera trajectories drawn from procedural synthesis and real-world movie footage from the CondensedMovies dataset. Auteur enables cinematographic framing of human-centered scenes, a capability largely absent in prior generative models. To assess this behavior, we propose new framing-focused metrics, and our experiments show that Auteur consistently outperforms existing methods

---


### 289. [The Image Reconstruction Game: Drawing Common Ground Through Iterative Multimodal Dialogue](https://arxiv.org/abs/2606.01901)

**<font color=#1a73e8>作者：</font>** Sherzod Hakimov, Mattia D'Agostini, Ivan Samodelkin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce the Image Reconstruction Game, a fully automated benchmark in which a vision-language model issues corrective instructions to an image generator across multiple turns, making accumulated common ground directly observable as a rendered image. Benchmarking two Describer models crossed with two Generator models across seven image categories, we find that the describer is the dominant factor in reconstruction quality, while the generator determines whether iterative refinement helps or hurts. Mathematical and geometric images pose the greatest challenge. The describer's token budget strongly affects convergence: shorter budgets yield sparser first renderings with more room for visible improvement, while longer budgets raise absolute quality but leave less to fix. Stronger describers use a richer correction vocabulary spanning spatial, numeric, and structural categories, while weaker describers concentrate on surface properties and tend to stop after a few turns. Human validation shows that the best automated judge reaches only slight-to-fair agreement with human preferences, and automated scores require human recalibration to be used reliably.

---


### 290. [SMH-Bench: Benchmarking LLM Agents for Environment-Grounded Reasoning and Action in Smart Homes](https://arxiv.org/abs/2606.01912)

**<font color=#1a73e8>作者：</font>** Kuan Li, Shuo Zhang, Huacan Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Smart homes are evolving toward complex state-dependent living environments, requiring Large Language Models (LLMs) to reason over user intent, preferences, and multi-device interactions. However, existing smart-home benchmarks often focus on static instruction-to-API mapping or limited simulations, failing to evaluate whether LLMs can reason, interact, and act reliably in realistic household scenarios. To address these limitations, we introduce SMH-Bench, a comprehensive benchmark for evaluating LLMs in smart-home environments. Built upon HomeEnv, an executable and verifiable smart-home simulator, SMH-Bench contains 1,100 high-quality tasks spanning 7 categories and 22 fine-grained subcategories. It further stratifies tasks across simple, medium and complex homes, ranging from small apartments to dense multi-room environments with 135 devices. Experiments show that although frontier LLMs achieve strong performance on explicit control and query tasks, they still exhibit significant weaknesses in automation task scheduling, ambiguity handling and personalized reasoning, especially as home complexity increases. We hope SMH-Bench will facilitate the development of more reliable, context-aware, and practically deployable smart-home agents.

---


### 291. [Mechanistic Diagnostics of Spatial Lexical Bias in Multimodal Large Language Model Spatial Reasoning](https://arxiv.org/abs/2606.01914)

**<font color=#1a73e8>作者：</font>** Chuang Ma, Qianying Liu, Tomoyuki Obuchi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) remain unreliable on spatial multiple-choice questions, and their failures are often attributed to poorly attended visual information. In this work, we identify a complementary failure mode, spatial lexical bias: adding a spatial relation word to the answer options can attract the model's decision and make the newly added option likely to be selected. Using nine open-weight MLLMs, we show that this phenomenon is widely observed. In particular, models can answer a binary spatial question correctly, yet consistently select an incorrect third spatial option once it is added to the answer set. We isolate such binary-stable but ternary-fragile cases as diagnostic examples and leverage mechanistic interpretability tools, revealing that a substantial part of the failure instead originates on the language side rather than the visual side: visual attention analyses and residual-stream probes show the correct spatial relation remains internally available on these failures, while irrelevant-option controls, activation patching, and sparse component interventions trace the bias to specific LLM-side channels and neurons. Based on this finding, we show that a lightweight LLM-only DPO update on tiny single-object-pair synthetic data mitigates the bias, lifting four-way robust accuracy by up to 100 points on synthetic data, and by 68.0, 32.6, and 20.1 points on broader evaluation datasets WhatsUp, SpatialMQA-Direct, and VSR.

---


### 292. [Resonant Context Anchoring: Decoupling Attention Routing and Signal Gain at Inference Time](https://arxiv.org/abs/2606.01923)

**<font color=#1a73e8>作者：</font>** Mingkuan Zhao, Yide Gao, Wentao Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) frequently exhibit "contextual disregard" when faced with input evidence that conflicts with their internal parametric memory, leading to persistent factual hallucinations. Existing mitigation strategies primarily rely on suppressing specific neuron activations or employing computationally expensive contrastive decoding mechanisms, which often result in increased perplexity or significantly elevated inference latency. To address these limitations, we propose Resonant Context Anchoring (RCA), a lightweight inference-time intervention method grounded in the perspective of residual stream signal dynamics. RCA aims to resolve the signal attenuation of external evidence during its propagation through deep networks. The core mechanism involves the orthogonal decoupling of routing logic and information magnitude within the self-attention module. By utilizing raw pre-softmax attention scores as an instantaneous metric of semantic alignment, we construct a dynamic gain field via non-linear rectification to selectively amplify the norms of value vectors corresponding to context tokens, without altering the attention probability distribution. This mechanism effectively elevates the signal-to-noise ratio (SNR) of input evidence within the residual stream mixture, thereby robustly anchoring the generation trajectory to the truthful context during inference. Extensive experiments on the Llama-3 model series demonstrate that RCA significantly improves contextual faithfulness across multiple factual consistency and strong knowledge-conflict tasks, effectively suppressing parametric hallucinations. Furthermore, results confirm that as a training-free and computationally negligible plug-and-play module, RCA achieves a Pareto improvement in faithfulness and fluency while maintaining the model's general language understanding capabilities.

---


### 293. [QoEReasoner: An Agentic Reasoning Framework for Automated and Explainable QoE Diagnosis in RANs](https://arxiv.org/abs/2606.01925)

**<font color=#1a73e8>作者：</font>** Qizhe Li, Haolong Chen, Shan Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Diagnosing Quality-of-Experience (QoE) degradations in operational Radio Access Networks (RANs) is a critical but notoriously complex task, traditionally requiring labor-intensive expert analysis over high-dimensional, cross-layer telemetry. While Large Language Models (LLMs) offer unprecedented reasoning capabilities, they are fundamentally unsuited for raw RANs troubleshooting: they fail at numeric time-series analysis, hallucinate protocol-violating causal links, and lack the stateful rigor required for multi-step fault localization. To bridge this gap, we present QoEReasoner, an end-to-end, LLM-driven agentic system designed for automated and explainable QoE diagnosis. QoEReasoner tames the inherent unpredictability of LLMs by grounding their reasoning in the physical realities of the network. It employs deterministic tools to reliably translate raw numeric KPIs into structured evidence, enforces protocol-consistent fault propagation through a domain-specific Knowledge Base, and leverages a Historical Bank of expert-validated cases to guide hypothesis generation. A stateful central planner orchestrates this closed-loop process across anomaly detection, causal tracing, and root-cause localization. Evaluations on real-world operational RANs datasets demonstrate that QoEReasoner outperforms strong baselines by 18\%-40\% in accuracy across multiple diagnostic tasks. Furthermore, it reduces diagnostic time from approximately 30 minutes of manual expert analysis to just 3 minutes per session, delivering highly interpretable, expert-grade reports while remaining robust across diverse LLM backbones.

---


### 294. [Mitigating Bias in Locally Constrained Decoding via Tractable Proposals](https://arxiv.org/abs/2606.01926)

**<font color=#1a73e8>作者：</font>** Meihua Dang, Linxin Song, Honghua Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generations from large language models often fail to conform to desired constraints such as JSON schema. Existing locally constrained decoding (LCD) approaches enforce constraints by myopically masking out next tokens, resulting in biased sampling and degradation in performance. Recent work uses sequential Monte Carlo (SMC) methods to mitigate such biases, but designing effective proposal distributions or potential functions remains a key challenge. In this work, we propose a generic approach to construct proposals and potentials for SMC sampling from $p_{\mathrm{lm}}( \cdot \mid \mathrm{constraint})$. First, we show that constraints specified as finite automata can be tensorized for efficient execution on GPUs, which we use to construct globally constrained decoding (GCD) proposals. In addition, leveraging the fact that tensorized finite automata share the same circuit structure as hidden Markov models, we circuit-multiply them to obtain the probabilistic GCD (P-GCD) proposals encoding both logical and probabilistic information about the target distributions. We evaluate (P-)GCD on the tasks of function calling, keyword-based generation, and SQL generation. Experiments show that under the same SMC sampling setup, compared to LCD proposals, (P-)GCD converges faster to the target distribution with significantly fewer particles.

---


### 295. [3rd Place at CVPR 2026 CASTLE Challenge: Agentic Multi-View Long-Context Video Understanding via Hierarchical Knowledge Graph Retrieval](https://arxiv.org/abs/2606.01933)

**<font color=#1a73e8>作者：</font>** Raghad Albusayes, Munirah Alyahya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents our winning methodology for the CASTLE 2026 Challenge at the CVPR 2026 EgoVis Workshop, where our team secured third place globally. The challenge tasks participants with answering highly complex visual, spatiotemporal, and verbal questions, including visual counting, action localization, multi-view tracking and speaker temporal reasoning, within massive, multimodal video streams. The underlying dataset consists of over 600 hours synchronized footage captured by 15 ego and exo camera sources. To tackle the extreme scale and long-context demands of this environment, we introduce a training-free agentic framework optimized for long-form video understanding. Our framework introduces two core architectural components: i) a Video Knowledge Graph that maps static and dynamic entities, their temporal relationships, and intersecting events to enable multi-hop relational reasoning, and ii) an adaptive agentic workflow that resolves complex queries through a hierarchical retrieval and indexing. Empirical results demonstrate that our framework achieves high zero-shot reasoning accuracy on long-context multi-view streams. Our code will be released at this https URL.

---


### 296. [HMPO: Hybrid Median-length Policy Optimization for Chain-of-Thought Compression](https://arxiv.org/abs/2606.01934)

**<font color=#1a73e8>作者：</font>** Minghui Zheng, Hongxu Chen, Huimin Ren 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models achieve remarkable performance via extended chain-of-thought (CoT) reasoning, yet this lengthy process incurs substantial inference overhead. Existing CoT compression methods struggle with inflexible manual length budgets, computationally expensive multi-stage training pipelines, and fragile scalability restricted to small models. We propose HMPO (Hybrid Median-length Policy Optimization), a cost-effective, single-stage reinforcement learning framework. HMPO efficiently compresses CoT via three synergistic components: an adaptive median-based budget derived from successful rollouts to eliminate manual tuning, a cosine-decay token reward for smooth length penalization, and a multiplicative reward formulation that substantially mitigates trivial reward hacking by strictly prioritizing answer correctness. Trained exclusively on mathematical data, HMPO generalizes seamlessly across math, code, science, and instruction-following tasks. Extensive experiments scaling from 9B to 122B parameters across dense and Mixture-of-Experts (MoE) architectures demonstrate that HMPO achieves 19%--46% token compression with negligible accuracy degradation, all while drastically reducing training costs compared to existing multi-stage baselines.

---


### 297. [Unified Driving Tokens: Representation- and Geometry-Guided Discrete Tokenizer for Driving World Models and Planning](https://arxiv.org/abs/2606.01935)

**<font color=#1a73e8>作者：</font>** Ziyang Yao, Zeyu Zhu, YunCheng Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete visual tokens should provide a compact representation for both token-based world modeling and planning in autonomous driving. However, most tokenizers are inherited from image generation and are optimized mainly for pixel reconstruction, which may leave a gap between what is easy to generate and what is useful to decode for driving decisions. We present a representation-guided and geometry-enhanced tokenizer that learns discrete tokens under joint supervision. The tokenizer aligns its discrete bottleneck with a frozen DINO feature space through feature decoding, while preserving appearance via RGB reconstruction with perceptual and adversarial losses. To inject geometric state-related cues, we add adjacent-frame depth and relative-pose supervision during training and stabilize joint objectives with multi-codebook quantization. We evaluate the same learned tokens with a lightweight planning readout and a GPT-style next-token world model. Experiments on NAVSIM show improved reconstruction fidelity and representation consistency, competitive planning performance under a fixed decoder, and better generative quality under matched settings.

---


### 298. [What to Format and How: A Benchmark and Workflow Approach for Document Formatting](https://arxiv.org/abs/2606.01936)

**<font color=#1a73e8>作者：</font>** Shihao Rao, Liang Li, Jiapeng Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have opened up new possibilities for automated document formatting. However, real-world formatting often requires identifying targets based on document content. This content-aware setting remains challenging and underexplored, primarily due to the lack of dedicated evaluation this http URL enable evaluation in realistic content-aware scenarios, we introduce DocFormBench, a benchmark that extends Text-to-Format evaluation to diverse formatting requirements, along with metrics for both accuracy and this http URL mitigate redundant document reading in existing methods during formatting, we propose DocFormFlow, a workflow formatting method that decouples target localization from modification execution into what to format and how. Extensive experiments across multiple LLMs and multimodal models show that DocFormFlow consistently improves formatting accuracy while reducing token consumption compared to representative baselines. Further analysis reveals that precise target localization is the primary factor influencing formatting performance. We hope DocFormBench and DocFormFlow will facilitate future research toward more intelligent and reliable document formatting.

---


### 299. [Parameter-Efficient Fine-Tuning of Large Pretrained Models for Instance Segmentation Tasks](https://arxiv.org/abs/2606.01947)

**<font color=#1a73e8>作者：</font>** Nermeen Abou Baker, David Rohrschneider, Uwe Handmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Research and applications in artificial intelligence have recently shifted with the rise of large pretrained models, which deliver state-of-the-art results across numerous tasks. However, the substantial increase in parameters introduces a need for parameter-efficient training strategies. Despite significant advancements, limited research has explored parameter-efficient fine-tuning (PEFT) methods in the context of transformer-based models for instance segmentation. Addressing this gap, this study investigates the effectiveness of PEFT methods, specifically adapters and Low-Rank Adaptation (LoRA), applied to two models across four benchmark datasets. Integrating sequentially arranged adapter modules and applying LoRA to deformable attention--explored here for the first time--achieves competitive performance while fine-tuning only about 1-6% of model parameters, a marked improvement over the 40-55% required in traditional fine-tuning. Key findings indicate that using 2-3 adapters per transformer block offers an optimal balance of performance and efficiency. Furthermore, LoRA, exhibits strong parameter efficiency when applied to deformable attention, and in certain cases surpasses adapter configurations. These results show that the impact of PEFT techniques varies based on dataset complexity and model architecture, underscoring the importance of context-specific tuning. Overall, this work demonstrates the potential of PEFT to enable scalable, customizable, and computationally efficient transfer learning for instance segmentation tasks.

---


### 300. [AutoMedBench: Towards Medical AutoResearch with Agentic AI Models](https://arxiv.org/abs/2606.01961)

**<font color=#1a73e8>作者：</font>** Junqi Liu, Salena Song, Yuhan Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents are increasingly expected to support end-to-end medical-AI research workflows, moving beyond isolated prediction tasks or short-form clinical question answering. However, existing medical agent benchmarks primarily evaluate final outputs, providing limited visibility into agent behavior within the research process. To address this gap, we present AutoMedBench, a workflow-aware benchmark for autonomous medical-AI research across diverse medical imaging and multimodal inference tasks, organizing agent execution into a unified five-stage workflow (S1-S5): Plan, Setup, Validate, Inference, and Submit. It comprises long-horizon tasks with each run averaging 33 agent turns, spanning five research tracks: segmentation, image enhancement, visual question answering (VQA), report generation, and lesion detection. Each task is evaluated under two difficulty tiers, Lite and Standard, which use the same data and metrics but differ in the amount of task-brief scaffolding, and each run is scored using both final task performance and S1-S5 stage scores, enabling stage-level analysis from the initial task brief to the final submitted artifact. Across thousands of recorded runs, stage-level scoring reveals that Validate is the weakest workflow stage on average, whereas Setup is the strongest, suggesting that current agents are better at making pipelines executable than at verifying their reliability. Post-run error analysis further shows that verification and submission failures dominate tagged errors, accounting for 37.7% and 38.1% of fired codes respectively, whereas task-understanding errors are rare at 0.9%, and runs with one fired error code have a 48% lower overall score than runs with no error code on average.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-376](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
