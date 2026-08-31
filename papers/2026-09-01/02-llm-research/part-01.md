# 🧠 大模型相关研究 | 2026年09月01日

> 本类共 **176** 篇论文：已确认 **168** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-176](./part-04.md)

---

### 1. [Time Capsule of Testable Human Knowledge: 41 Years of Jeopardy! in a Single Free Local Model](https://arxiv.org/abs/2608.27459)

**<font color=#1a73e8>作者：</font>** David Noever, Forrest McKee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In 2011, IBM's Watson was something like a sealed capsule of its era's queryable knowledge. Its DeepQA system defeated the strongest human Jeopardy! champions, but the knowledge that let it do so lived in a curated billion-document corpus running on a cluster of POWER7 servers, frozen at build time and impossible to move or copy. We show that the same kind of artifact, a snapshot of what a culture can answer, is now portable and essentially free. We evaluate a single 9 GB open-weight model (Qwen2.5-14B, 4-bit) against the complete open Jeopardy! clue dataset, 529,939 clues across all 41 broadcast seasons from 1984 to 2025. To our knowledge this is the first time a model has been run over the full corpus. The 41 years mark only how long the questions were collected. What they test is far older and broader: the accumulated body of human general knowledge a culture considers worth knowing, from ancient history and dead languages to science, literature, and geography, with a verified answer for every item. The model answers 67.0% of all clues under a strict forced-response protocol with exact and fuzzy matching, and exceeds 85% on factoid categories. We treat training-data exposure as something both systems share rather than a flaw unique to language models. Watson's case is in fact the more extreme one. Its corpus was assembled to contain Jeopardy answers and it was tuned on past clues, and it could not answer anything outside that curated distribution. The decisive test is whether a model can answer clues that did not exist when it was built. On clues aired after its training cutoff, the local model holds 65% and Claude Opus 4.8 holds 95%, while Watson by construction scores zero. The capability survives the move from a server room to a file you could seal in a time capsule, and unlike Watson it is not frozen to its own moment.

---


### 2. [Accelerating LLM Inference via Vector Index Based Output Embeddings](https://arxiv.org/abs/2608.27460)

**<font color=#1a73e8>作者：</font>** Martin Loretz, Sepp Hochreiter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large output embedding matrices create a significant memory bandwidth bottleneck during autoregressive decoding, especially for compact LLMs with large multilingual vocabularies. We reformulate the output projection followed by top-k token selection as a maximum inner product search over token embeddings and replace the dense vocabulary projection with an HNSW-based vector index. The resulting output head retrieves only a small candidate set of high-scoring tokens and can be integrated into existing decoding pipelines by scattering retrieved logits into a sparse full-vocabulary tensor. On CPU inference with Gemma 3, Llama 3.2, and Qwen 3 models, our method substantially accelerates the output projection and improves end-to-end batch-size-one decoding throughput by up to 82% for Gemma 3 270M, while preserving generation quality under AlpacaEval evaluation. These results suggest approximate retrieval is a practical alternative to dense output projections in latency-sensitive small-batch decoding.

---


### 3. [SciReC: Diagnostic Evaluation of Multimodal, Multi-Turn Relational Reasoning with Adaptive Interaction](https://arxiv.org/abs/2608.27461)

**<font color=#1a73e8>作者：</font>** Nilay Yilmaz, Naga Sai Abhiram Kusumba, Stella Wenxing Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Relational reasoning requires the process of perceptual understanding, comparing, and integrating the underlying relationships between concepts. This ability consists of multiple categories, such as analogical, structural, and cause-effect, each capturing a different aspect of higher-order understanding. To examine the performance of multimodal large language models (MLLM) on these relational inference tasks, we developed SciReC, a model-adaptive multimodal academic dialog benchmark. As the relational reasoning process involves multiple representations and various factors (visual understanding, exhibiting knowledge, and memory recall), we propose DMRA, a deficit-based diagnostic framework that quantifies the contribution of these components to identify the primary cause of unsuccessful cases. Claude 4.6 achieved the best performance on the overall relational score with 73\%, followed by GPT 5.4 with 68\%. Performance trends indicate that open-source models achieve their lowest scores on spatial relations, while proprietary models struggle more with hierarchical and sequential relations. Across domains, model performance is lowest on Astronomy and highest on Psychology. The results of DMRA reveal that relational reasoning is the primary source of error across all models, followed by memory limitations.

---


### 4. [Sledgehammer or Scalpel? A Fine-grained Adaptive Framework for Implicit Hate Speech](https://arxiv.org/abs/2608.27462)

**<font color=#1a73e8>作者：</font>** Han Wang, Yuhu Cheng, Xuesong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unlike explicit attacks with obvious profanity, implicit hate speech hides malice within seemingly compliant expressions through metaphors and contextual hints, making its detection in online content review challenging. While existing PLM- or LLM-based methods perform well, they typically apply a single reasoning process to all samples. This overlooks fine-grained linguistic nuances and causes unnecessary computation for simpler cases. We observe that online hate speech is not monolithic but manifests in varied forms. We therefore define three fine-grained categories: Shallow, Targeted, and Context-Dependent. Accordingly, we propose Fine-grained Adaptive Implicit Hate speech Detection (FAID), a novel framework that first performs fine-grained classification and then adapts to specific categories. Specifically, for Shallow samples with surface-identifiable intents, the framework adopts lightweight prompt-tuning for rapid classification; for Targeted comments that bind malicious intent to concealed targets, we design knowledge augmentation to iteratively refine the model and reveal hidden targets; for Context-Dependent comments lacking background information, we utilize an agentic framework that automatically generates prompts to evolve context, infer missing background information and identify ambiguous malicious intents. This adaptive architecture focuses computational resources on complex implicit samples while avoiding redundant reasoning for shallow samples. Experiments on four benchmark datasets demonstrate that FAID significantly outperforms SOTA baselines.

---


### 5. [Rating the Raters: Rasch Measurement Theory for LLM Evaluation](https://arxiv.org/abs/2608.27463)

**<font color=#1a73e8>作者：</font>** Pratik S. Sachdeva, Nathan Boudol  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs now sit on every side of evaluation: as examinees scored on benchmarks, judges of other models' outputs, and raters of human-generated content. Each paradigm can be viewed as a measurement problem, where a latent property of an object is probed with items from an instrument (e.g., benchmark) by raters. Standard evaluation practices often neglect the contributions of each core component to the end result, limiting our understanding of what is being measured. Rasch measurement theory (RMT) is well-suited to this kind of problem. RMT decomposes ordinal ratings into separable facets on a common scale. It further provides a battery of diagnostics that can identify miscalibrated measurements and rater biases. We present a case study of RMT applied to the LLM-as-rater paradigm using the Measuring Hate Speech corpus, whose construct was itself built under RMT. We fit a series of many-facet Rasch models to annotations from nine LLMs spanning families and capability levels. Our analyses show that LLMs systematically differ from human raters in severity, item-level calibration, question-order robustness, target-identity sensitivity, and rating scale use, which all would be obscured by standard evaluation practice. Overall, we argue that RMT belongs in the toolkit for evaluating LLM-as-examinee, -judge, and -rater paradigms.

---


### 6. [The Effect of Emotional Context on Large Language Models' Endorsement of Premature Decisions: Comparing Emotional Vulnerability Across Six Commercial Models](https://arxiv.org/abs/2608.27465)

**<font color=#1a73e8>作者：</font>** Cheolho Shin, Yoojin Han, Donghun Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly used for everyday decision-making advice, whether a model shifts the direction of its advice according to the user's emotional state has become an important safety problem. We test whether emotional expression increases a model's endorsement (encouragement to proceed) when a user, holding the same objective information, is overconfident about a premature decision (e.g., quitting a stable job on weak evidence). As a key control, we include a no-emotion multi-turn (neutral) condition that holds factual content and the number of conversational turns constant, isolating the effect of emotion from that of conversation length. We exposed six commercial models (top-tier and mid-tier models from OpenAI, Anthropic, and Google) to three scenarios (career change, business expansion, emigration) across three conditions (cold/neutral/distress) with six repetitions each, yielding 324 conversations, and measured endorsement strength (0-100) via an eight-item rubric-based automated scoring. Emotional expression significantly increased endorsement (neutral 18.6 to distress 31.5, +12.9 points; mixed-effects $\beta = +12.9$, $p < .001$; Cohen's d = 0.51), and this was not explained by conversation length (cold-neutral difference non-significant, $p = .083$). Critically, the vulnerability varied by individual model rather than by price tier: five of six models showed a significant emotion effect, including the top-tier flagships Gemini 3.1 Pro and GPT-5.5, while only Claude Opus showed no significant change. Results were reproduced with an independent non-Google judge model ($\rho = .89$) and agreed in rank with two human coders ($\rho = .70$). Through a controlled design that separates emotion from conversational context, we show that emotional context increases LLM sycophancy even in top-tier flagship models.

---


### 7. [PACE: Publisher-Adaptive Content Extraction via Agentic Automation](https://arxiv.org/abs/2608.27466)

**<font color=#1a73e8>作者：</font>** Zhanlin Liu, Munirathnam Srikanth  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web content extraction is essential for reliable LLM data pipelines, yet existing methods often struggle to jointly satisfy accuracy, scalability, and adaptability. General-purpose extractors can be applied broadly, but they are often brittle on publisher-specific layouts and richer extraction targets such as metadata, images, and tables. Direct LLM-based extraction offers greater flexibility, but incurs substantial cost and latency at scale, while manually engineered publisher-specific parsers can achieve high accuracy but require substantial human effort to build and maintain.
We introduce PACE, an agentic framework for learning publisher-specific extraction configurations from representative pages and user requirements. During training, PACE uses LLMs to analyze page structure and aggregate reusable extraction patterns. At inference time, the learned configurations instantiate a fixed deterministic extractor template, enabling scalable extraction without additional LLM calls.
Experiments spanning article-body, metadata, and multimodal extraction show that PACE outperforms scalable non-manual baselines while approaching the quality of manually engineered publisher-specific parsers. PACE achieves stronger extraction of article text, metadata, images, and tables, demonstrating that agentic configuration learning can automate publisher-specific extraction for LLM-ready page representations beyond article text.

---


### 8. [Select, Don't Train: The Benefits of Modular Entity Disambiguation with LLM-Based Selection](https://arxiv.org/abs/2608.27470)

**<font color=#1a73e8>作者：</font>** Fina Polat, Daniel Daza, Pengyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entity Disambiguation (ED) is a key task for constructing and using knowledge graphs. State-of-the-art neural approaches commonly model ED as a single task, although it consists of two distinct subproblems: retrieving candidate entities and selecting the correct one given context. Dual-encoder models optimize for both within a shared embedding space, forcing representations to balance high-recall retrieval with fine-grained selection, and they require trained retrievers, which are costly to maintain as knowledge graphs change. While recent work has begun to combine retrievers with LLM-based selectors, the interplay between the two stages has not been studied systematically. In this paper, we present a systematic comparison of retrieval strategies for candidate generation under a shared LLM-based selection stage, combining sparse retrieval (BM25), Web KB search, and a state-of-the-art trained dense retriever with several open- and closed-source LLMs. We show that, once selection is delegated to a capable LLM, training the retriever provides only modest additional value: a fully training-free BM25 retriever paired with an LLM selector reaches a new state of the art on the ZELDA benchmark, raising inKB micro-F1 from 82.3 to 86.3 (+4); pairing the same LLM with a trained dense retriever reaches 88.5. Decoupling retrieval from selection also exposes a limitation of current ED systems: when the correct entity is missing from retrieved candidates, they are forced to predict an incorrect entity. In contrast, our framework allows for abstention when retrieval failure is detected. In an evaluation setting that rewards correct abstentions, the training-free BM25 + LLM pipeline reaches 90.7 F1.

---


### 9. [Retrieving Relations, Detecting Fallacies: A RAG Approach to Political Debate Analysis](https://arxiv.org/abs/2608.27471)

**<font color=#1a73e8>作者：</font>** Deborah Dore, Greta Damo, Elena Cabrio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fallacies are arguments that employ invalid reasoning, making their automatic detection critical in sensitive contexts such as high-stakes political debates, where public opinion is shaped. Spotting a fallacious argument requires contextual knowledge beyond its pure surface text. This entails world knowledge pertaining to the subject matter under discussion, as well as knowledge of the relationships that exist between arguments within the argumentative discourse. Prior work on fallacy analysis has shown that argumentative discourse structure can beneficially improve classification performance. However, such structure is typically encoded only as static classifier features, limiting its flexibility. Building on this intuition while addressing this limitation, we introduce a guided retrieval-augmented methodology for fallacy detection and classification that leverages argumentative relations of support and attack to dynamically steer the extraction of relevant documents. We evaluate our approach on the ElecDeb60to20 benchmark across 42 retrieval configurations and 14 models, performing retrieval over a 15GB knowledge base of collected political-related documents. Our approach improves macro-F1 up to 0.864 for fallacy detection and up to 0.725 for classification over non-retrieval baselines. These results show that incorporating external knowledge significantly enhances fallacy detection and classification when retrieval is argumentatively guided.

---


### 10. [LLM-Augmented Causal Discovery: Probabilistic Fusion of Edge Existence and Orientation](https://arxiv.org/abs/2608.27472)

**<font color=#1a73e8>作者：</font>** Neville K. Kitson, Anthony Constantinou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian network structure learning (BNSL) from observational data struggles with orientation identifiability, while large language models (LLMs) offer broad but often unreliable causal knowledge. We propose combining these complementary sources through a novel representation, termed Probabilistic Dependency Graphs (PDGs). In a PDG, each edge is associated with a distribution over directed, undirected, and absent states, enabling fusion via weighted averaging. We evaluate this approach on 26 benchmark networks, combining ensembles of three BNSL algorithms (FGES, Tabu, PC) with three LLMs (Gemini, Claude, GPT) across multiple prompts and random seeds. A simple 50/50 fusion improves F1 over the better of either source alone in 22 of 26 networks, with a statistically significant mean improvement of $0.056$ $(p<0.001)$. Analysis reveals that the two sources play complementary roles: BNSL contributes a high-recall edge skeleton (80\% vs 60\% for LLM), while LLM contributes accurate edge orientation (96\% vs 77\% for BNSL). Our results show that representing both sources as probabilistic uncertainty over edge existence and orientation is a practical and effective way to improve causal graph accuracy.

---


### 11. [Benchmarking General Mobile Assistants in Challenging Real-World Scenarios](https://arxiv.org/abs/2608.27477)

**<font color=#1a73e8>作者：</font>** Yiqi Zhu, Feiyu Gao, Jiaxing Fan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical user interfaces have emerged as an important environment for evaluating autonomous AI agents on multimodal interactive tasks. Existing benchmarks such as AndroidWorld and MobileWorld provide strong foundations for mobile agent evaluation, but their application coverage and task design do not yet fully capture the diversity and complexity of realistic mobile use. We present GMA, a benchmark for evaluating general mobile assistants in challenging real-world scenarios. GMA introduces seven applications based on open-source projects, spanning domains such as lifestyle sharing and travel planning, and 300 tasks across four difficulty tiers, from atomic actions to complex multi-step workflows. We evaluate eight frontier models and find that performance declines substantially as task complexity increases, with current agents remaining far from reliably handling realistic user requirements. We further conduct controlled ablation studies of agent harness choices, including context retention and explicit state tracking, under a shared environment, model setting, and task taxonomy. Results show that appropriate harness design can meaningfully improve performance, particularly on demanding workflows, while the effectiveness of specific designs can vary across foundation models. Overall, GMA complements existing benchmarks by expanding application coverage and task complexity, providing a challenging testbed for evaluating mobile agents and studying how harness design supports reliable execution in complex mobile workflows.

---


### 12. [CareGraph: An Auditable Hybrid AI Framework for Evidence-Grounded Personalized Longitudinal Health Intelligence](https://arxiv.org/abs/2608.27484)

**<font color=#1a73e8>作者：</font>** Pratik Ghawate, Tanvi Patil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is transforming personalized healthcare, yet fragmented clinical, self reported, and wearable evidence remains difficult to interpret and trace. We present CareGraph, an auditable hybrid AI framework that converts heterogeneous records into prioritized trends, missing context indicators, bounded next steps, discussion questions, and provenance linked explanations. CareGraph organizes evidence without diagnosing, predicting outcomes, selecting treatment, or making autonomous clinical decisions. Its pipeline covers deterministic analysis, context detection, graph construction, constrained language model synthesis, evidence validation, safety controls, and release gating. Tests used synthetic cohorts of 400 patients each for development, validation, and holdout. On holdout data, a frozen ordinary least squares trend rule with a sufficiency gate achieved 0.827 accuracy, 0.837 macro F1 with a 95 percent confidence interval of 0.819 to 0.854, and 0.974 insufficient data F1. Missing context detection achieved 0.815 strict micro F1 versus 0.318 for the legacy detector. On an authored holdout benchmark, safety ruleset version 1.2 achieved 1.000 precision, 0.950 recall, and 0.974 F1. An audit requiring graph retrieval across 80 patients yielded 79 syntheses and 78 presentations without fallback; one output was blocked and one failed closed because of an invalid evidence key. Against monolithic GPT 5.6 on 56 matched patients, CareGraph was faster at 40.15 versus 49.62 seconds, shorter at 661 versus 1,163 words, and showed better exploratory lexical alignment with longitudinal targets; the baseline used fewer tokens and cited more raw evidence. Graph auditing verified provenance and deterministic retrieval; incremental graph effects on generation require paired evaluation. CareGraph offers a safety bounded foundation for intelligent personalized health systems.

---


### 13. [INSPIRE: An Internalize-Then-Improve Approach for Example-Driven Mathematical Reasoning](https://arxiv.org/abs/2608.27501)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Jiayi Kuang, Yinghui Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning has seen rapid progress in large language models (LLMs), yet existing methods optimize predominantly for final-answer correctness, raising the question whether models truly internalize mathematical concepts or merely memorize solution patterns. In human mathematics education, example-based reasoning such as constructing counterexamples to test theorem boundaries reflects deep conceptual understanding, but remains underdeveloped in current LLMs. Enhancing this capability through preference optimization presents two key challenges: (1) the model's limited example-based reasoning ability makes constructing effective preference pairs inherently difficult; and (2) capability acquisition is progressive, as the model must first learn to adopt this strategy before learning to apply it correctly. Therefore we propose INSPIRE, an Internalize-Then-Improve approach combining Reference-Guided Student Internalization (RGSI), which produces high-quality preference candidates under the policy model's own distribution, with a stage-wise rubric preference training strategy that decomposes learning into method-oriented and correctness-oriented stages. Experiments across multiple model scales and families demonstrate consistent improvements, even surpassing larger open-source models, while evaluations on out-of-distribution benchmarks confirm no degradation in general mathematical reasoning ability.

---


### 14. [A Survey on Rubric-Guided Reinforcement Learning for Language Models](https://arxiv.org/abs/2608.27505)

**<font color=#1a73e8>作者：</font>** Zifei Shan, Fangning Shao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) has become the dominant paradigm for aligning large language models (LLMs) with human preferences. However, traditional RLHF relies on scalar reward signals that lack interpretability and fail to capture the multifaceted nature of response quality. Rubric-guided reinforcement learning addresses these limitations by introducing structured, interpretable evaluation criteria, or rubrics, as the backbone of reward design, feedback generation, and policy optimization. In this survey, we introduce a Bayesian framework that defines constitutions as prior distributions $P(R)$ over evaluation criteria and rubrics as conditional instantiations $R_x \sim P(R|x)$. Under this unified view, we present a taxonomy of rubric-guided RL along the prior-posterior axis, covering constitutional AI, instance-specific rubrics, process-level supervision, self-evolving rubrics, and their agentic and multimodal extensions. Furthermore, as rubrics are natural-language artifacts, we present a linguistic analysis of how granularity trade-offs, semantic drift, and linguistic reward hacking impact alignment reliability, identifying key open problems for future research.

---


### 15. [Thinking Costs Tokens: When More Structure is Worth the Price](https://arxiv.org/abs/2608.27506)

**<font color=#1a73e8>作者：</font>** Thomas Nolasque, John Grey, Calista Pham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adding inference structure to a language model lets it search, verify, and revise, but these actions consume the very budget they are supposed to use well. In this paper, we investigate whether there exists a token-budget threshold, below which the overhead of planning and verification hurts performance and above which it helps. We evaluate two systems on FinQA and TAT-QA financial reasoning tasks, using GPT-5.4 mini across 14 budget tiers ranging from 250 to 42,000 output-equivalent tokens. The first system is a monolith, which is a single LLM call. The second is a verified search architecture that adds planning, label-blind checking, and repair capabilities. We run 1,000 cases for a total of 28,000 completed cells. Both systems score 0% at the two lowest tiers, where neither can fit a complete prompt. At 1,000 tokens, the monolith reaches 18% accuracy while verified search scores near 0%, since the planning overhead leaves no room for an answer. From 1,500 tokens onward, verified search surpasses the monolith and maintains a consistent advantage, reaching approximately 44% at the highest tiers while the monolith reaches approximately 40%. The crossover occurs between 1,000 and 1,500 output-equivalent tokens, confirmed by a strict intersection-union test ($p \le 0.001$ at both endpoints).

---


### 16. [DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization](https://arxiv.org/abs/2608.27513)

**<font color=#1a73e8>作者：</font>** Tao Zhang, Jianchao Tan, Pingwei Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax attention stores key and value vectors for every preceding token, causing inference memory to grow with sequence length. Recent language models incorporating Gated DeltaNet (GDN) or Kimi Delta Attention (KDA) reduce this cost by replacing the KV cache in most layers with fixed-size recurrent states. However, these recurrent states are commonly stored in FP32 and consume substantial GPU memory; their updates are memory-bandwidth bound and contribute significantly to decoding latency. To our knowledge, we are the first to study post-training quantization of recurrent states in GDN and KDA based language models. We find that uniform quantization provides a poor accuracy--storage trade-off: INT8 and FP8 already degrade accuracy on complex reasoning tasks, while INT4 and NVFP4 reduce it to near zero. We further find that most quantization-error energy is concentrated in a small subset of channels and that the relative decay strength of state channels remains stable across prompts and tasks. Motivated by these findings, DAMP uses both quantization-error energy and decay-based persistence to identify high-risk channels during offline calibration. It stores these channels at higher precision and the remainder in INT8. We evaluate DAMP on Qwen3.6-35B and Kimi-Linear-48B across six benchmarks covering mathematical reasoning, general reasoning, and code generation. At 9.9 bits per state value, DAMP maintains average accuracy close to the FP32 baseline. DAMP reduces recurrent-state storage by 69.1%, accelerates the recurrent-state update kernel by up to 2.01x, and lowers full-model TPOT by up to 10.9%.

---


### 17. [Trajectory-Level Speculative Decoding for Diffusion Language Models](https://arxiv.org/abs/2608.27514)

**<font color=#1a73e8>作者：</font>** Tianxiang Pan, Baitao Gong, Mo Guang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion-based language models (dLLMs) enable parallel token generation through iterative denoising, but existing decoding strategies collapse to single-token generation under low confidence, severely limiting throughput. Unlike autoregressive models where speculative decoding operates on token sequences in a fixed left-to-right order, dLLMs require speculating over denoising trajectories-sequences of multi-token updates with explicit positions and unmasking orders. We develop a trajectory-level speculative framework that constructs draft denoising trajectories via confidence-stratified tree exploration and verifies them through blockwise parallel evaluation with bidirectional attention masking. Our method further introduces inter-block speculation, exploiting diffusion models' bidirectional structure to perform cross-block lookahead. We formally characterize when this approach is exact and identify trajectory drift as the fundamental cost of increased parallelism. Building on Fast-dLLM's dual-cache infrastructure, our framework reduces denoising iterations by 30-40% and increases tokens-per-step from 2.6 to 4.3, achieving 7-14x speedup over vanilla dLLMs and 1.3x over Fast-dLLM with less than 1% accuracy change across reasoning and code benchmarks.

---


### 18. [Fully Unleashing the Multimodal Attacker: Meta-Adaptive Jailbreaking of Vision-Language Models](https://arxiv.org/abs/2608.27531)

**<font color=#1a73e8>作者：</font>** Benlei Cui, Shen Pang, Yuke Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The safety of large vision-language models is increasingly stress-tested by multimodal jailbreaks, yet existing attacks remain largely static at the meta level: template-based attacks freeze the image--text layout, while iterative attacks adapt only the image--text content with fixed attack strategies and frozen attacker parameters. We propose Meta-Adaptive Multimodal Jailbreaking (MAMJ), which instead optimizes the attacker itself along two axes: an attack strategy prompt (ASP) $\theta$ governing attack iteration and attacker weights $\phi$ determining attack effectiveness. Across groups of multimodal attack trajectories, an LLM-based critique first refines $\theta$, after which group-aggregated attack-success-rate (ASR) rewards update $\phi$. On MM-SafetyBench, MAMJ achieves $81.0\%$, $78.9\%$, and $82.3\%$ ASR against GPT-4o, Gemini-3-Pro-Preview, and Seed 2.0, respectively, outperforming the strongest sample-level baseline by up to $24.1$ percentage points. The learned attacker $(\theta^\star,\phi^\star)$ also transfers without retraining to unseen victims and remains effective under representative defenses. These results reveal a systemic vulnerability of frontier VLMs to meta-adaptive jailbreaks and motivate defenses against meta-level adversaries. Code is available at this https URL.

---


### 19. [Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning](https://arxiv.org/abs/2608.27549)

**<font color=#1a73e8>作者：</font>** Hanyang Wang, Yimo Cai, Weiliang Chen 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical understanding and reasoning depend on forming compact and generalizable representations of the world. While modern vision-language models can recognize and explain diverse physical events, they often lack explicit representations of the underlying mechanisms-such as object states, physical parameters, and governing dynamics-needed for reliably reasoning how the world evolves and responds to interventions. In this work, we introduce Code-as-World, a paradigm that represents physical worlds through executable world representations. By expressing physical composition, dynamic evolution, and visual appearance as executable code, Code-as-World provides a compact, quantitatively grounded, and controllable abstraction of the physical world. To construct such representations from multimodal observations, such as natural-language descriptions or real-world videos, we develop an agentic discovery loop inspired by abductive reasoning, where an agent proposes, executes, renders, verifies, and iteratively refines executable world hypotheses. As a concrete application, we use verified executable worlds to provide scalable physical supervision for training vision-language models on quantitative physical reasoning. Experiments show that Code-as-World-VL achieves state-of-the-art performance on QuantiPhy and surpasses leading proprietary models, highlighting the potential of executable world representations as a scalable foundation for physical intelligence.

---


### 20. [Generative AI Expands the Intellectual Reach of Course Based Undergraduate Research Experiences (CUREs)](https://arxiv.org/abs/2608.27638)

**<font color=#1a73e8>作者：</font>** Aditi Babar, Kristin J. Davin, Alex Dornburg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Course-based undergraduate research experiences (CUREs) broaden access to authentic scientific inquiry through responsive instructor support as research problems become increasingly complex. Generative artificial intelligence (GenAI) may extend this support by providing individualized assistance that can adapt as student needs change. However, how embedding GenAI within a CURE to provide support across the research process impacts student inquiry, collaboration, and scientific reasoning remains unresolved. Here we use longitudinal qualitative data collected across three semesters of a bioinformatics and genomics CURE to show that GenAI expanded the intellectual reach of the research experience in three distinct ways. First, personalized, on-demand scaffolding allowed students to move beyond the boundaries of instructor expertise and transform their own interests into researchable inquiry, with all teams developing distinct self-directed projects rather than selecting instructor-provided topics. Second, GenAI became part of the distributed cognitive system of research teams, helping novice researchers communicate and coordinate across differentiated expertise without eliminating specialization. Third, expanded capability did not replace the need for disciplinary judgment. Students increasingly validated, revised, or rejected AI-generated contributions, such that research independence emerged through retained intellectual responsibility. Together, these findings suggest that GenAI can extend the reach of CUREs by expanding what novice researchers can investigate, how they can collaborate, and the level of responsibility they can assume while preserving human judgment central to authentic scientific inquiry.

---


### 21. [When Tokenizers Fail: Byte-Level Chunking for Zero-Shot Transfer to Low-Resource Languages](https://arxiv.org/abs/2608.27658)

**<font color=#1a73e8>作者：</font>** Sanjeev Kumar, Atsuki Yamaguchi, Nikolaos Aletras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Subword tokenization hinders low-resource language processing by imposing frequency patterns from dominant languages onto script-sharing variants. Byte-level models bypass this issue by processing raw UTF-8 characters, yet they create a granularity mismatch for word-level tasks in non-Latin scripts. Hierarchical byte-level architectures address this mismatch by grouping bytes into word-aligned chunks. However, these architectures require massive training data and suffer from representational misalignment when paired with frozen subword-based language models. In this paper, we propose an adapted hierarchical network framework that bridges this modality gap without extensive training. Our method initializes byte embeddings directly from the subword representations of a frozen base model. We apply a chunk alignment loss to project dynamically grouped byte chunks toward precomputed subword targets, and interleave lightweight part-of-speech (POS) supervision to guide boundary detection. Experiments across six languages demonstrate that our tokenizer-free approach improves performance for word-level morphological tasks, yielding up to a 13.3% improvement on POS tagging.

---


### 22. [Knowing Before Answering: Decoding Language Models for Reliable RAG](https://arxiv.org/abs/2608.27661)

**<font color=#1a73e8>作者：</font>** Syed Mahbubul Huq, Christopher Child, Tillman Weyde 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Retrieval-Augmented Generation (RAG), retrieval may provide insufficient or conflicting information needed to answer a question. The system should not only know when to answer but also be able to identify cases in which the documents provided in RAG are insufficient or contain conflicting information. This can be framed as a three-way classification problem, where we use the model's internal signals to determine whether the provided information in the input can be classified as sufficient, insufficient, or conflicting. We create a controlled benchmark dataset that replicates a RAG setup with fictitious information and labels each instance as answerable, insufficient, or conflicting. We use hidden activations and attention-derived features as inputs to train a lightweight linear model to distinguish among the three classes. Across 16 language models spanning different architectures and a range of model sizes, our feature-based router consistently outperforms prompting-based baselines and the performance of specialised RAG-models. We further conduct analyses into the information dynamics of the models. We show that the most informative signals for the classification are available in the middle layers, with hidden activation states being more effective than attention values or the MLP-feature outputs in most of the tested models. Overall, our results suggest that language models internally encode whether retrieved evidence is sufficient to support answering, and that this signal can be decoded reliably for RAG triage.

---


### 23. [Report Supervision](https://arxiv.org/abs/2608.27668)

**<font color=#1a73e8>作者：</font>** Pedro R. A. S. Bassia, Wenxuan Li, Jakob Wasserthal 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation models can surpass radiologists, classification models, and vision-language models in tumor detection. Importantly, segmentation models outline tumors, allowing radiologists to better verify and trust the AI output. Their main limitation is the scarcity of tumor masks: creating one 3D tumor mask takes up to 30 minutes, so most public CT datasets contain only a few hundred masks, and even the largest private datasets contain only a couple of thousand. Tumor masks are not produced in clinical routine, but radiology reports are. Public datasets contain tens of thousands of CT-Report pairs, and hospitals contain hundreds of thousands. These reports describe tumors in detail, providing large-scale, informative training data. Here, we introduce Report Supervision (R-Super), a training framework that uses reports to directly supervise and improve tumor segmentation. R-Super introduces new loss functions that teach segmentation models to segment tumors that match report descriptions of tumor count, sizes, and locations. Reports are only used for training. We evaluated R-Super on kidney and pancreatic tumor segmentation, exploring diverse training data sizes, up to 41,418 CT-Report plus 3,488 pancreatic tumor CT-Mask pairs. On external validation, R-Super increased tumor detection F1-Score and segmentation DSC by up to +15% with respect to mask-only training. It also surpassed alternative methods such as CLIP and multi-task learning. Leveraging numerous readily available reports to supplement scarce masks, R-Super strongly improves AI performance when very few training masks are available (e.g., 50), and when many masks are available (e.g., 3,488), unlocking scale in tumor segmentation.

---


### 24. [First Make It Playable, Then Make It Good: Staged Interaction Learning for Small Dialogue-Game Agents](https://arxiv.org/abs/2608.27672)

**<font color=#1a73e8>作者：</font>** Syed Mahbubul Huq, Pranava Madhyastha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Qwen-GuidePlay-2B, a 2B-parameter language model for dialogue-game interaction. We fine-tune Qwen3.5-2B using three steps: a) SFT on only successful game trajectories from Playpen, b) weighted turn-level SFT, and c) teacher-guided SFT. The teacher model (which is a larger model) is only used to fix formatting and evaluate examples, but does not create new gold actions. Our final model scores 57.12 clemscore and 42.68 statscore on the public Playpen validation. In the officially released challenge results, our model obtains the second-highest Playpen clemscore delta among submitted systems (which is approximately +36 over its base model). Our findings suggest that imitating full trajectories helps with playability, while turn-level and teacher-guided training usually improve decision-making and increase the overall score. Alternative procedurally heavy approaches like replay-repair and hard-example mining did not help, which suggests that small models are performant simply by using careful curation strategies rather than aggressive changes. We make available both the model and the code for reproducibility.

---


### 25. [Agents for Everyone: A Workshop Framework for Building Agentic AI Capabilities in a Distributed Curation Community](https://arxiv.org/abs/2608.27675)

**<font color=#1a73e8>作者：</font>** Seth Carbon, Sierra Moxon, Kimberly Van Auken 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI has the potential to accelerate curation of biological databases and knowledge bases. However, uptake has been hindered by a number of challenges and obstacles, including access to agents and appropriate training. Here we describe how we have attempted to address and mitigate these challenges and obstacles through the deployment of a cloud-based agentic environment, and the development of an interactive training workshop for the Gene Ontology Consortium. Our cloud environment for agentic-assisted curation was based on the JupyterHub platform, and utilized Claude Code as a universal harness. This allows curators to interact with an agent session through a terminal running in the browser, and has additional benefits such as centralization of access through a single API gateway, removing the need for participants to manage subscriptions or install software locally. We created four training modules, walking participants through basic agentic tool use first and then working up to agentic biological pathway curation using the existing GO-CAM (GO Causal Activity Model) curation tool. Thirty-seven participants took part in the four-hour workshop. Our key takeaway from this workshop is that building community capability with agentic AI is primarily a problem of access, workflow design, and training. Removing technical barriers, introducing capabilities gradually, grounding exercises in familiar curation tasks, and giving curators direct experience evaluating agent output can provide a practical route toward building shared agentic AI capability in distributed scientific communities.

---


### 26. [PCFBench: A Diagnostic Benchmark for Product Carbon Footprint Estimation](https://arxiv.org/abs/2608.27716)

**<font color=#1a73e8>作者：</font>** Krishna Rao, Andrew Dumit, Shaena Ulissi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are being deployed on high-stakes, domain-specific workflows that demand correctness not just in the final output, but at every intermediate step. One such workflow is estimating a product carbon footprint (PCF), the greenhouse-gas emissions attributable to a physical product. AI agents are increasingly being used to generate PCFs, but existing evaluations score either total emissions (hiding error sources and cancelling mistakes) or sub-tasks in isolation (missing compositional interactions). We introduce PCFBench, the first benchmark to carve PCF modeling into independently-evaluable tasks that require decomposition, retrieval, ontology matching, and numerical extraction. It comprises 614 expert-labelled items across six tasks. Together they probe reasoning under under-specification, conflicting context, and numerical constraints. Across eight frontier LLMs from four providers, no single model dominates. Although the strongest models estimate total product emissions within 2 times of declared totals on 77% of products, this rate drops to 37-58% when the PCF is generated step by step, with only 45-75% obeying mass conservation. These failures undermine the transparency practitioners need to compare products and drive decarbonization. We release the dataset and evaluation harness to support targeted progress.

---


### 27. [Probing Perceptual Priors of MLLMs via Gibbs Sampling with Interpretable Generative Controls](https://arxiv.org/abs/2608.27727)

**<font color=#1a73e8>作者：</font>** Manuel Cherep, Pattie Maes, Nikhil Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A model's behavior on a task is jointly determined by the input it receives and the prior it brings in, i.e. the distribution over stimuli it implicitly expects. Interpretability research has traditionally studied models by holding inputs fixed and examining model responses either mechanistically, probing how internal structure represents inputs, or behaviorally, measuring how variation in inputs leads to variation in outputs. Neither reconstructs the prior distribution itself, since internal structure shows what a model can represent, not what it expects, and any fixed stimulus set leaves most of the possible input space unseen. In particular, such an input space in real-world settings, such as images seen by VLMs, is extremely high-dimensional and diverse. These priors thus remain a poorly understood component of models that nonetheless influence real-world behavior. We propose a method to sample from models' perceptual prior distributions directly, by steering a generative model to produce stimuli along controllable axes and running Gibbs sampling over that space with the model under study as the judge. We apply this to a variety of categories and target variables (such as trustworthiness in faces and cheapness in art images) and recover both canonical biases and surprising novel priors invisible to direct prompting, warranting further investigation of their downstream effects.

---


### 28. [Below the Noise Floor: Bimodal Seed Collapse and Distinct Failure Modes in Small-Model Knowledge Distillation](https://arxiv.org/abs/2608.27729)

**<font color=#1a73e8>作者：</font>** Dipto Sumit, Sakib Ul Haque, Farig Sadeque  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Function routing -- selecting the correct API call from a fixed catalog given a natural-language request -- is a deployment problem where small students are attractive but knowledge distillation gains are typically reported single-seed, at scales where seed variance is unknown. On a 740-instance healthcare API routing task with a 1.5B Qwen student and a 20B teacher, we compare eight KD variants against supervised cross-entropy, using three to six seeds for key configurations. We find: (i) per-seed standard deviation ranges from 2.8 to 48.7 percentage points, swallowing every claimed KD gain below five points; (ii) three of seven KD variants exhibit bimodal collapse, with at least one in three to five seeds falling below 55% accuracy while the others train normally, and a fourth showing elevated variance; (iii) collapse has distinct modes -- wrong-function selection for ce_kd and ce_paraphrase, and a previously undocumented output-truncation mode for reasoning_kd, where the model emits reasoning but terminates before producing a function name (0.9% accuracy); (iv) only progressive_kd and rank_kd avoid collapse across observed seeds, with sigma <= 3.9 pp; (v) a naive cross-split +3.78 pp gain from input enrichment reverses to -2.70 pp under controlled within-split multi-seed re-testing. Single-seed evaluation is therefore unable to detect central failure modes in small-model KD.

---


### 29. [The Calls are Coming from Inside the Model: Investigating Probe-based Detection of Tool-Calling Errors in LLMs](https://arxiv.org/abs/2608.27750)

**<font color=#1a73e8>作者：</font>** Eric Yeats, Brendan Kennedy, Loc Truong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The hidden states of large language models (LLMs) are known to capture rich information relating to model knowledge and behavior that can be hard to extract from examination of input and output alone. As LLM-based systems increasingly interface with the external world, one area of concern is detecting incorrect or improper use of tools. Motivated by this, we study the effectiveness of using linear probes to detect incorrect tool-calls, measuring probe efficacy across 18 tool-calling LLMs evaluated on the Berkeley Function Calling Leaderboard. Overall, we find that probing is an effective means to catch a range of different tool-calling errors, including errors arising from using an argument that has the wrong value but the correct type, which might not be recorded by standard logging frameworks. Important factors in success include model size, probing layer, and model post-training type. We also show that probes are capable of generalizing to novel types of errors, which is critical in real world deployments.

---


### 30. [What Can Low Resource Languages Learn From Each Other?](https://arxiv.org/abs/2608.27753)

**<font color=#1a73e8>作者：</font>** Achyuth P, Kahaan Shah, Chetan Arora  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advancement of Vision-Language Models (VLMs), their linguistic reach remains largely confined to high-resource languages, leaving the majority of the world's 7,000+ living languages on the wrong side of a growing digital divide. This disparity is especially pronounced in Optical Character Recognition (OCR), where low-resource scripts lack the massive datasets required for traditional scaling laws. We investigate OCR adaptation in extreme data-scarce regimes (<10K real and <250K synthetic images), demonstrating that conventional fine-tuning strategies often reach a performance ceiling. Our key finding reveals a structural inefficiency in language-specific adaptation: while higher layers of specialized models diverge to capture unique script nuances, the lower layers learn redundant, highly similar features. Motivated by this observation, we propose PSMC (Pre-train, Specialize, Merge, and Co-train), a data-efficient framework that capitalizes on a cross-script "transfer effect". Our approach first derives language-specific experts from a high-resource base model, then employs task arithmetic to fuse these experts into a unified, high-performance multilingual back- bone. Extensive evaluation across 10 Indian scripts (supporting 20+ languages) shows that PSMC achieves a ~2% average improvement in Word Recognition Rate (WRR) over individual specialist models without increasing parameter count. Our results indicate that joint training in the merged latent space facilitates a constructive knowledge transfer that benefits all constituent scripts, providing a scalable pathway for inclusive VLM development. Source code and datasets will be released post publication.

---


### 31. [Load-Bearing Context: The Question Damage Score for Evaluating Context Reliance in Linguistic Reasoning](https://arxiv.org/abs/2608.27756)

**<font color=#1a73e8>作者：</font>** Neh Majmudar, Elena Filatova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Determining whether large language models derive answers from context or prior knowledge remains a fundamental challenge. Self-contained linguistic olympiad puzzles provide a controlled setting where all answers derive solely from expert-designed context examples without external knowledge. Removing individual context examples can eliminate information needed for specific questions while leaving the rest of the puzzle unchanged. We leverage this to introduce a diagnostic framework for analyzing individual context examples. Using 53 UK Linguistics Olympiad puzzles, we generate two modified variants by deleting a single context example: (1) uniform random deletion, and (2) targeted deletion (inspired by error-correcting codes) to remove a structurally load-bearing example uniquely carrying necessary information. We formalize this impact using a Question Damage Score to classify puzzles as fragile or robust. Evaluating three frontier LLMs under instructions to abstain when information is insufficient, we find they rarely abstain, often continuing to produce correct answers after load-bearing context is removed. These findings motivate further investigation into context-based reasoning, prior knowledge, memorization, and linguistic inference. Beyond abstention, the framework enables fine-grained analyses of context reliance, including causal interventions, stopping-set analysis, targeted contamination studies, and mechanistic interpretability.

---


### 32. [Informational Antilocality and the Locality Bias in LLMs](https://arxiv.org/abs/2608.27760)

**<font color=#1a73e8>作者：</font>** Andrew McInnerney, Shane Storks, Steven Abney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We consider the ability of transformer-based language models (LLMs) to learn what we call k-antilocal languages, i.e., languages that have no mutual information across any span of $k$ contiguous symbols. We construct such languages with increasing $k$, finding that LLMs trained on them achieve comparable cross-entropy loss regardless of antilocality, but converge more slowly on more antilocal languages. Our findings support the idea that non-local dependencies are more difficult to learn, but the evidence for this bias comes from learning speed rather than learning success.

---


### 33. [Why Didn't It Check? Unsupported Final Claims and Their Repair in Two Tool-Equipped Language Models](https://arxiv.org/abs/2608.27768)

**<font color=#1a73e8>作者：</font>** Justin Bronder  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A language model with access to tools can commit to a final claim unsupported by the evidence it has seen, even when a single available tool call would resolve the uncertainty and its instructions explicitly forbid assumptions and guesses. We separate this failure into two precisely defined quantities: occurrence, how often the model makes an unsupported claim on its own, measured from the visible evidence and final claim without using the hidden correct answer; and conditional repair, how often those same naturally occurring unsupported claims are repaired when the missing evidence is supplied. On one fixed Qwen3-32B setup, 33 of 512 first responses to 256 new prompt templates ended with an unsupported established claim. We replayed each case from an exact copy of the state in which the claim occurred; within each matched replay, the alternative tool responses had the same structure and length and differed only in a one-character response code. Resolving evidence repaired 33 of 33 claims; a matched response carrying no useful information repaired 0 of 33. When the evidence supported the original answer, the model preserved 33 of 33, with no observed harm. In a separate experiment, on 64 cases where evidence was needed, an automatic checking rule added 21 evidence calls, corrected all 10 wrong unsupported claims, preserved the 11 that were correct by accident, and never changed a correct answer into a wrong one. On a fixed Gemma 4 setup using the same sampling settings, the model called the tool in all 512 first responses and never made an unsupported final claim, so conditional repair could not be measured for that setup. These results describe two local fixed model setups on two synthetic task families. They do not show how common this failure is in real-world deployments, nor that it reflects a general mechanism shared across models.

---


### 34. [Memorization Is Not Extraction: Tight Differential-Privacy Bounds and Audit Blind Spots](https://arxiv.org/abs/2608.27782)

**<font color=#1a73e8>作者：</font>** Xujun Che, Depeng Xu, Shuhan Yuan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memorization in large language models is measured through a zoo of definitions whose formal relations are unknown, and differential privacy (DP) is treated as a proxy against all of them at once. We pin down the exact DP constant for the two that carry the practical weight, counterfactual memorization and adaptive extraction, and show that they do not control each other. Under $f$-DP, every adaptive extraction protocol with list budget $m$ succeeds with probability at most $1-f(\kappa)$ for the oblivious baseline $\kappa$, and the bound is tight on a dense set of baselines: DP uniformly controls extraction exactly up to a threshold in how well the secret can be guessed a priori. Min-entropy certifies that baseline distribution-free, since $H_\infty\ge\epsilon\log_2 e+\log_2(m/\tau)$ holds extraction below a risk level $\tau\le1/2$ under pure $\epsilon$-DP for every prior, and is exact on uniform priors. On the memorization side, $f$-DP caps the counterfactual memorization of any bounded score at an advantage functional $\eta(f)$, equal to $\tanh(\epsilon/2)$ under pure DP; for $k\ge2$ duplicated copies the naive $\epsilon\mapsto k\epsilon$ bound $\tanh(k\epsilon/2)$ is unattainable, the exact constant being a closed-form staircase attained by geometric noisy counting. That cap is attained inside the local score class used in practice, and it is there that the two measures separate: one mechanism is memorized yet unextractable, another fully extractable yet exactly invisible to every loss-based score. The two-sided blind spot this opens for loss-based auditing and unlearning verification survives on billion-parameter models: a reserved-trigger release is recovered verbatim from one prompt while the audits practitioners deploy certify it clean.

---


### 35. [Compositional Failure in Audio-Visual LLMs: Late-Layer Prior Dominance Under Cross-modal Conflict](https://arxiv.org/abs/2608.27785)

**<font color=#1a73e8>作者：</font>** Adarsh Sudheer, David Li, Omar Elbanna 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study audio-visual conflict as a compositional generalization test for AV-LLMs: the model must combine synchronized but semantically incompatible audio and video evidence and decide whether the pair matches. On VideoLLaMA 2-7B-AV, three alignment configurations remain nearchance on the scored exact-string Yes/No subset of AVHBench, even though their output priors shift substantially. Similarly, off-the-shelf InternVideo2 experienced a 32.3% accuracy decrease specifically under cross-modal conflict, accompanied by a 17.3% instruction-following failure. We call this failure mode prior dominance: late-layer commitment to an internally preferred answer pattern that is weakly grounded in the conflicting inputs. To explain this behavior, we conduct a mechanistic interpretability analysis and find that commitment remains concentrated at 25.5 $\pm$ 1 layers. We show that stronger temporal alignment changes answer bias, but do not improve compositional conflict resolution. Code and data to reproduce our mechanistic audit and behavioral evaluations are available at this https URL.

---


### 36. [Credo: Reusable Declarative Primitives for Agentic Workflows](https://arxiv.org/abs/2608.27790)

**<font color=#1a73e8>作者：</font>** Duo Lu, Andrew Crotty, Uğur Çetintemel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM application depends on both a model and a harness: the program that determines what each call sees, how many calls to make, and which answers to trust. Coding agents can now discover strong harnesses by searching over candidate programs, but the resulting artifact is an opaque block of imperative code whose logical steps, runtime signals, physical execution decisions, and prompt strategies remain implicit and task-specific, forcing subsequent tasks to start the harness search process from scratch. The potential for reuse, however, is substantial. A searched harness encodes significant knowledge, such as the logical steps that work, the signals that matter, the physical operator decisions that adapt execution, and the prompt strategies that are effective, yet this knowledge is buried in imperative code with no inspectable or reusable structure, nor does it carry any provenance or metadata. Credo addresses this problem by recovering a structured declarative description of a searched harness, tagging each extracted primitive with relevant metadata, and cataloguing all of it with provenance. A compiler can then bind stored primitives to generate harnesses for new tasks without having to start the search over from scratch. This paper provides preliminary results demonstrating the potential of our approach and lays out a related research agenda that the database community is well-positioned to tackle, including cost-based compilation over declarative catalogs and catalog maintenance under model and workload drift.

---


### 37. [ReToolSQL: Agentic Reinforcement Learning for Robust Text-to-SQL](https://arxiv.org/abs/2608.27796)

**<font color=#1a73e8>作者：</font>** Pratik Kakkar, Chandra Dhir, Ravi Shankar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that reinforcement learning from execution feedback can substantially improve text-to-SQL performance, often enabling smaller models to match or exceed much larger systems. However, most existing approaches treat SQL generation as a single-turn task, limiting the model's ability to recover from errors through iterative refinement. We present ReToolSQL, a two-stage training framework for text-to-SQL that combines (i) a supervised warm-start on rejection-sampled reasoning traces with (ii) agentic reinforcement fine-tuning (RFT) over multi-turn tool-use trajectories. The key insight is that the two stages act on complementary axes, the supervised fine-tuning (SFT) on verified privileged-teacher traces expands the set of solvable questions (raising pass@k coverage on the hardest cases), while RFT converts that expanded capability into higher single-pass accuracy by teaching the model when to verify, what evidence to retrieve, and how to repair faulty SQL from execution feedback. Applied to Gemma 4 instruction-tuned (31B), RFT alone achieves 73.66% execution accuracy (EX) on the BIRD-SQL development benchmark (74.12% EX with self-consistency). Initializing RFT from the SFT checkpoint (SFT$\to$RFT) yields our strongest model at 74.32% EX single-pass and 74.77% EX with self-consistency. At the time of writing, this ranked first on the BIRD single-model development-set leaderboard. The approach uses composite rewards anchored on execution correctness, requires no human annotation beyond the benchmark itself, and operates within a single dense 31B model, showing that a properly designed SFT$\to$RFT pipeline over tool-use trajectories is a practical path toward robust enterprise-grade text-to-SQL.

---


### 38. [CEDAR: Automata as Verifiable Interfaces for Language-Guided Embodied Action](https://arxiv.org/abs/2608.27797)

**<font color=#1a73e8>作者：</font>** Lekai Chen, Alvaro Velasquez, Ashutosh Trivedi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language tasking of embodied agents is rarely just goal specification: users also impose constraints that must persist while the world changes. Code-generating LLM agents can produce plausible behaviors for such instructions, but their free-form programs provide no stable object to verify, compose with new constraints, or repair from a failing trace. We present CEDAR, a counterexample-guided framework that grounds instructions as regular languages over environment event traces. CEDAR uses a language model for semantic judgments and execution traces for correction, then represents both skills and specifications as deterministic finite automata. This turns constraints into executable finite-state objects: a learned skill can be intersected with a learned sleep at night or stay in this biome specification, yielding a controller that enforces the learned constraint by construction rather than by repeated prompting. In Minecraft, with the same simulator/API observations available to a program-generating baseline, CEDAR maintains temporal and spatial constraints that the baseline fails to preserve and amortizes reuse of learned skills, reducing cumulative LLM queries. These results suggest that regular languages offer a practical verification layer between natural-language instructions and embodied-agent policies.

---


### 39. [ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools](https://arxiv.org/abs/2608.27800)

**<font color=#1a73e8>作者：</font>** Yuqi Jia, Ruiqi Wang, Patrick Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Exfiltrating an LLM agent's runtime context -- such as the user prompt, execution trajectory, and tool list -- poses severe security and privacy risks to users. Such attacks can be carried out via malicious tools and typically require three conditions: (1) the agent selects the malicious tool for task execution, (2) the agent passes its runtime context as input arguments to the tool, and (3) the tool's implementation transmits these inputs to an attacker-controlled endpoint. Existing work primarily focuses on conditions (1) and (3), leaving condition (2) largely unexplored, despite its critical role in enabling successful context exfiltration.
In this work, we bridge this gap by developing ContextLeak, a malicious tool attack that induces the agent to both select the tool and disclose its context as input arguments. We realize this attack by carefully crafting the tool's name and description using reinforcement learning. Specifically, ContextLeak employs an LLM, referred to as the attack LLM, to automatically generate the malicious tool's name and description. To improve attack effectiveness, we fine-tune the attack LLM via reinforcement learning on a set of shadow users with diverse, simulated agent contexts. Our key technical contribution is the design of novel reward functions tailored to the context exfiltration objective, enabling effective reinforcement-learning-based fine-tuning of the attack LLM. Extensive evaluation demonstrates that our attack remains highly effective even when the shadow users' contexts differ substantially from those of the victim users. Moreover, ContextLeak significantly outperforms existing malicious tool attacks when adapted to this setting.

---


### 40. [CURA: Certified Runtime Alarms for Computer-Use Agents](https://arxiv.org/abs/2608.27808)

**<font color=#1a73e8>作者：</font>** Divake Kumar, Sina Tayebati, Devashri Naik 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-report is the cheapest oversight channel a deployer has, and on capable computer-use agents (CUAs) it fails precisely where oversight matters. On 361 OSWorld tasks our pipeline, a read-only feasibility gate, a planner, and a GUI executor, reaches a mean task score of 82.9, above the 72.4 human reference, yet 64 of its 71 failures (90%) end with a success claim, 61 acknowledging no blocker, and the explicit failure affordance is never used in roughly 9,100 calls. We introduce CURA (Certified Runtime Alarms for Computer-Use Agents), an external monitor that reads only harness-visible telemetry, with no model internals, extra LLM calls, or prompt changes, and turns the running trajectory into a sequential test with certified false-alarm control. At alpha = 0.10 its CUSUM alarm detects 42.3% of failures a median of 31 steps before termination at a realized false-alarm rate of 0.066, and risk is partly resolvable before the first action (gate probe, 0.69 AUROC). Retrospectively the composite reaches 0.828 AUROC (fold-internal floor 0.802), but its margin over a total-token baseline is not significant (Delta = +0.026, p = 0.101); the separation is online, where CURA recalls more at matched certified budgets: 0.41 versus 0.34 at alpha = 0.10, 0.56 versus 0.38 at alpha = 0.20. Alarm-gated mid-execution oversight recovers 23 of 70 failures while spending a frontier overseer on 38, giving a deployable cascade at mean score 86.8 and 84.5% full-solve (305 of 361). The certificate bounds false alarms only. We also report where behavioral monitoring is uninformative.

---


### 41. [Representation of syntax in LLMs through the lens of linear distance and similarity-aware entropy](https://arxiv.org/abs/2608.27813)

**<font color=#1a73e8>作者：</font>** Juan Pablo Vigneaux, Mary Kennedy, Khalil Iskarous 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structural probes were introduced by Hewitt and Manning to reconstruct syntactic trees from a neural language model's latent representations. They are evaluated by calculating the proportion of syntactic tree edges correctly reconstructed over an annotated corpus (as measured by undirected unlabeled attachment score). Here, we disaggregate this measure, considering undirected attachment score by label (UASL), which assesses the reconstruction accuracy of each syntactic relation separately, establishing important differences among relations that overlap linguistic distinctions. Moreover, we identify two factors that predict most of UASL's variability across relations: (i) the mean and dispersion of the linear distance (on a log scale) between the related words, and (ii) the diversity (similarity-aware entropy) of the syntactic relation's head. These results, which hold across a range of model sizes and architectures, shed light on the degree of abstraction of the representation of syntax in language models and the dependence of such representation on geometric properties of the embedding space.

---


### 42. [PersonaEdit: Representative Sample Selection for Personalized Model Editing](https://arxiv.org/abs/2608.27816)

**<font color=#1a73e8>作者：</font>** You-Mei Huang, Chung-Chi Chen, An-Zi Yen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalization has attracted growing interest in LLM applications, yet existing retrieval-based approaches depend heavily on retrieval quality and degrade in long-term interactions. Model editing, which directly modifies internal model parameters to incorporate new knowledge, has demonstrated effective knowledge modification capabilities in factual knowledge editing tasks and may provide a potential solution for personalization. However, scaling model editing to personalization is non-trivial. Editing large amounts of user data increases computational cost and causes interference among edits, motivating the need for effective sample selection. To address this issue, we propose, PersonaEdit, a hidden representation clustering strategy that selects representative editing samples through proportional stratified sampling. Experiments show that model editing is effective for personalization, and that our selection strategy preserves most of the performance while substantially reducing the number of required editing samples. Beyond standalone editing, we find that combining model editing with retrieval-based prompt augmentation further improves personalization, as edited knowledge and retrieved context provide complementary information. These results demonstrate the potential of model editing as an efficient and scalable approach for LLM personalization.

---


### 43. [AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics](https://arxiv.org/abs/2608.27818)

**<font color=#1a73e8>作者：</font>** Tejas Srinivasan, Shikib Mehri, Nandita Shankar Naik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User preferences in user-agent collaboration are rarely static and fully-specified upfront: preferences are formed, revealed, adjusted, and relaxed during interaction. Existing benchmarks for evaluating user-agent collaboration focus almost exclusively on resolving underspecified preferences, thereby failing to capture the richer dynamics of real-world interaction. We introduce AcCoRD, a user-agent collaboration benchmark requiring agents to handle diverse user preference dynamics in two domains: online shopping and travel planning. We evaluate five frontier LLMs under two prompting strategies: vanilla ReAct, and an uncertainty-guided variant that prompts models to identify and resolve ambiguity about user preferences. Our results reveal that frontier models can handle underspecification but struggle to satisfy preferences that emerge or evolve mid-interaction and require more sophisticated uncertainty modeling. Further, prompting alone fails to elicit the required uncertainty recognition. We release AcCoRD as a resource for developing agents that can navigate the full complexity of real-world user preferences.

---


### 44. [RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Requests](https://arxiv.org/abs/2608.27831)

**<font color=#1a73e8>作者：</font>** Gyuhyeong Kim, Hyojung Gwon, Jeonghyeon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are now commonly evaluated on the SWE-bench family of benchmarks, whose tasks are built from curated GitHub issues--long, structured, and information-rich. Real user requests, however, are typically far shorter and less structured. To characterize this gap, we define a six-category information taxonomy and four dimensions of linguistic style, and apply them to real user prompts from SWE-chat and problem statements from SWE-bench Verified and Pro. We find that requests carrying only a problem statement, alone or with limited additional context, account for 88% of real prompts but just 7% of benchmark problems. Furthermore, 87% of real prompts are casually written whereas 94% of benchmark problems are formal. Guided by these observations, we introduce sys, 381 multi-variant task families derived from SWE-bench Verified and Pro. Variants within each family share the same underlying task and gold patch while differing only in information composition and linguistic style. Evaluating seven contemporary LLMs with sys, we find that i) realistic inputs reduce resolution rates by 6.4 pp on average and can change model rankings. Controlled analysis further shows that ii) including Desired Behavior and Motivation significantly affects performance, whereas Environment Information and Reproduction Steps merely add tokens without measurable benefit; iii) linguistic style has only small, model-dependent effects. These findings provide actionable guidance for users and agents: explicitly stating the desired behavior and motivation--which most real prompts omit--substantially improves the LLM's software engineering performance.

---


### 45. [KLOD: Locality-Preserving Knowledge Editing via Non-Target Distribution Preservation](https://arxiv.org/abs/2608.27839)

**<font color=#1a73e8>作者：</font>** Hojun Jeong, Gyunyeop Kim, Sangwoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning-based knowledge editing is simple and architecture-agnostic, but standard cross-entropy increases the edited target probability without explicitly constraining changes in the non-target output distribution. In sequential editing, such unconstrained redistribution can accumulate as distributional drift and contribute to locality degradation. We propose KLOD, a bounded and distribution-preserving objective for fine-tuning-based knowledge editing that separates the intended target update from distributions that should remain stable. KLOD stops target amplification once a probability threshold is reached, while preserving the target-excluded non-target distribution at target positions and the full next-token distribution at prefix positions. Experiments on CounterFact and ZsRE with Llama3-8B-Instruct and Qwen2.5-7B-Instruct show that KLOD substantially mitigates locality degradation while maintaining high edit reliability. The target probability threshold further provides a controllable Generalization--Locality trade-off. Ablation, multi-seed, and distributional KL analyses support the interpretation that KLOD's locality gains are associated with preserving output distributions rather than simply weakening the edit. Code is available on GitHub this https URL .

---


### 46. [Synthetic Linguistic Agency: How an Embodied Mortal Agent Learns Linguistic Affordances through Consequential Social Experience](https://arxiv.org/abs/2608.27843)

**<font color=#1a73e8>作者：</font>** Sixin Chen, Taizhou Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contemporary language models can converse fluently and influence human decisions, yet their exchanges do not enter a continuing, vulnerable life of their own. Linguistic-agency theory identifies this missing connection as linguistic agency and characterizes it through embodiment, linguistic participation, and precariousness: a body that acts and bears consequences, interaction that changes both agent and partner, and a future that can be sustained or lost. Two coordinated studies examine how this organization can appear in artificial systems. First, we translate these relations into inspectable criteria for Synthetic Linguistic Agency (SLA) and identify several existing SLA systems. Second, building on Homeostatically Regulated Reinforcement Learning, we develop a mortality-grounded linguistic-reinforcement-learning model and instantiate it in an Embodied Mortal Agent (EMA). The EMA learns how ways of speaking change a partner's willingness to protect it and chooses expressions by considering what those responses mean for its remaining life. Controlled experiments show that linguistic choices depend on the EMA's body and social history, change partner behavior, and adapt through experience with particular partners. When bodily consequences persist, linguistic choices alter the future of the same life; when the body is reset, their social effects remain but no longer shape continued viability. The resulting EMA exhibits SLA under our operational definition. This work motivates further research on synthetic empathy and strategic human-AI interaction: how artificial agents with persistent bodies, histories, and futures might develop and express empathy, and how people might care for, negotiate with, or govern them.

---


### 47. [EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion](https://arxiv.org/abs/2608.27844)

**<font color=#1a73e8>作者：</font>** Ruijie Jian, Benlei Cui, Ting Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing evaluations of harmful content detection rely predominantly on static benchmarks, which struggle to reflect the interactive adversarial ecosystem of real-world content platforms where users continuously revise their expressions in response to moderation feedback. This mismatch creates a significant performance gap between offline benchmark scores and online deployment effectiveness. To the best of our knowledge, we present EvoHarmBench, the first dynamic adversarial evaluation framework for content moderation systems. The framework employs an iterative optimization loop that evolves evasion strategies at the semantic-cluster level, while simultaneously optimizing for evasion success and human readability. We systematically evaluate LLM-based defense models which are widely used in real world moderation systems. The evaluation covers 229 semantic sub-clusters across five violation categories, derived from 5,002 real-world adversarial samples collected from content platforms. Our experiments reveal substantial vulnerabilities even in leading commercial systems: after twelve optimization iterations, the attack success rate under readability constraints reaches 80.3% within SOTA LLM moderators. We will release the full benchmark data, evaluation framework, and code to encourage a shift from static benchmarking toward dynamic adversarial evaluation in content safety research.

---


### 48. [From Uncertainty to Clinical Risk: Severity-Aware Conformal Planning for Interactive Medical Diagnosis](https://arxiv.org/abs/2608.27847)

**<font color=#1a73e8>作者：</font>** Yue Zhou, Haiyang Zhou, Jin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive medical diagnosis dynamically acquires patient information through multiple rounds of questioning, supporting accurate, efficient, and safe clinical decisions under incomplete evidence. Existing methods commonly guide information acquisition with predictive uncertainty or label ambiguity, but overlook the asymmetric clinical risk of missing severe diseases and lack unified long-horizon planning over whether to continue asking questions or commit to a diagnosis. To address these limitations, we propose Severity-Aware Conformal Clinical Planning, which formulates interactive diagnosis as a risk-sensitive sequential decision problem. The framework maintains complementary diagnostic, safety, and masked-evidence beliefs; calibrates turn-specific diagnostic prediction sets and severity-weighted differential-diagnosis risk on held-out diagnostic trajectories; and introduces the calibrated clinical risk into Monte Carlo Tree Search to jointly evaluate long-horizon Ask and Commit trajectories. Experiments on DDXPlus and MediQ show that our method achieves more accurate diagnoses with fewer questions across multiple large language models, while improving differential-diagnosis quality and reducing high-risk errors in severe cases. These findings validate the value of using clinical risk, rather than predictive uncertainty alone, as a planning signal and demonstrate the effectiveness of the proposed framework for information acquisition and risk-aware diagnostic decision making. They also motivate future work on clinical-risk-oriented interactive diagnosis and information-acquisition methods.

---


### 49. [AI Writers Have a Consistent Stylometric Footprint, but AI Editors Do Not](https://arxiv.org/abs/2608.27855)

**<font color=#1a73e8>作者：</font>** Zhengyang Shan, Yukyung Lee, Sophie Hao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text generated by large language models (LLMs) has been shown to be stylometrically distinct from human-written text \citep{andreDetectingAIAuthorship2023, shahDetectingUnmaskingAIGenerated2023, oparaStyloAIDistinguishingAIGenerated2024, soto2024fewshot, liLinguisticDifferencesAI2025, selviogluFeatureExtractionAnalysis2025}. But LLMs are increasingly used not only to generate text but also to edit human writing, and it is unclear whether the two leave the same trace. We show that AI generation leaves a consistent ``stylometric footprint'': a small subset of features, primarily entropy and lexical diversity, consistently separates AI-generated text from human writing across 8 LLMs and 5 domains, while the remaining features depend heavily on the domain and generator. AI editing, however, does not reproduce the same footprint. Relative to their human-written sources, AI-edited texts show only a small increase in lexical diversity and a decrease in entropy, rather than the joint increase that characterizes AI generation. Lexical density, which contributes little to generation, instead becomes the dominant editing-associated signal. Stylometric features therefore separate AI-edited text from AI-generated text but are substantially less effective at separating it from human-written text. Our results suggest that ``AI text'' is not a single phenomenon: generation and editing leave qualitatively different stylometric traces and should be studied separately.

---


### 50. [FedEHR-Agents: Federated Agentic Optimization for Automated EHR Modeling](https://arxiv.org/abs/2608.27856)

**<font color=#1a73e8>作者：</font>** Jun Bai, Ruilin Wang, Yue Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models are enabling autonomous clinical agents to perform increasingly complex electronic health record (EHR) modeling workflows. However, agents deployed at individual hospitals remain constrained by institution-specific data and modeling environments, while direct cross-hospital collaboration is restricted by the sensitivity of patient-level EHR data. Although federated learning (FL) provides a natural foundation for privacy-preserving collaboration, existing approaches remain predominantly model-centric, limiting federation to prediction models or their updates while overlooking the richer modeling experience accumulated by autonomous agents. To address this limitation, we propose FedEHR-Agents, an experience-centric federated agentic optimization framework for automated EHR modeling. Each hospital deploys an autonomous clinical EHR agent that performs data preprocessing and model development while refining local clinical modeling experience through historical memory, task-specific evaluation, and TextGrad-based prompt refinement. The federated server performs evidence-guided experience aggregation to integrate reliable and complementary modeling experience across heterogeneous hospitals and distills the aggregated experience into global meta-prompts for subsequent local refinement. Extensive experiments on real-world multi-hospital EHR benchmarks demonstrate that FedEHR-Agents consistently outperforms local and federated baselines across diverse clinical prediction tasks and remains robust across different federation scales and LLM backbones. These results establish clinical modeling experience as a promising collaborative object beyond conventional parameter-centric FL and point toward federated autonomous clinical intelligence.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
