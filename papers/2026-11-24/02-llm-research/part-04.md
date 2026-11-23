# 🧠 大模型相关研究 | 2026年11月24日

> 本类共 **200** 篇论文：已确认 **182** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200**

---

### 151. [Beyond Sample Hardness: Adaptive Data Selection through Learning Dynamics](https://arxiv.org/abs/2611.27656)

**<font color=#1a73e8>作者：</font>** Hai Gan, Suorong Yang, Guang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data selection has emerged as an effective approach to reducing the model training costs. However, most existing methods often rely heavily on sample hardness, which may overlook differences in sample learning dynamics and lead to suboptimal sample selection. In this paper, we propose LeDAS, an end-to-end Learning Dynamics-Aware Selection framework for dynamic data selection, which jointly characterizes sample importance through hardness, learning progress, and deterioration, enabling adaptive sample prioritization throughout training with marginal additional computational overhead. Specifically, we track per-sample loss dynamics using exponential moving averages (EMA) to obtain three complementary signals that capture current learning difficulty, ongoing learning improvements, and potential degradation. To accommodate evolving training dynamics, we introduce Adaptive Metric Fusion, a contextual bandit-based mechanism that dynamically adjusts the relative importance of these signals based on training feedback. Furthermore, a bounded staleness compensation mechanism accounts for historical selection patterns by increasing the selection priority of samples that have not been selected for extended periods. Extensive experiments across diverse vision and language tasks demonstrate the effectiveness and generality of LeDAS. Compared with state-of-the-art baselines, LeDAS consistently achieves superior performance, matching or surpassing full-dataset training at a 50\% selection ratio on ImageNet-1K and in LLM supervised fine-tuning. Moreover, its modular and task-agnostic design enables the integration of complementary selection signals, demonstrating strong robustness to noisy and corrupted datasets.

---


### 152. [Hy-MT3: More Accurate, Robust and Practical Multilingual Translation Models in the Wild](https://arxiv.org/abs/2611.27673)

**<font color=#1a73e8>作者：</font>** Mao Zheng, Zheng Li, Fangxu Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hy-MT3 is the third generation of the Hunyuan multilingual translation model family, including \textbf{Hy-MT3-1.8B}, \textbf{Hy-MT3-7B} and \textbf{Hy-MT3-30B-A3B (MoE)}. Compared with Hy-MT2, Hy-MT3 translates \textbf{more accurately, more completely and more faithfully to user constraints}: on real-world scenario data, the share of samples with mistranslations is reduced by \textbf{43\%}, omissions or additions by \textbf{74\%}, and instruction-following errors by \textbf{40\%}, while language coverage is expanded from \textbf{38 to 102} languages. With only 3B activated parameters, \textbf{Hy-MT3-30B-A3B achieves the best overall performance among all evaluated models in non-thinking mode}, including flagship models such as Qwen3.8-Max, Kimi-K3.1-Pro and DeepSeek-V4.1-Flash, and approaches the strongest closed-source thinking models such as GPT-6.1-Sol and Gemini-4-Argon, while surpassing models that consume \textbf{more than 30$\times$} its inference compute. Beyond general translation, Hy-MT3 is optimized for two industrial scenarios. For \textbf{game localization}, built with high-quality game-domain data and a professional evaluation system from the Honor of Kings team, Hy-MT3-30B-A3B matches or outperforms strong closed-source models such as Gemini 3.1 Pro on all core metrics, and can be plugged into game development pipelines through an open-source toolchain. For \textbf{image translation}, Hy-MT3 improves context understanding and error correction to better tolerate OCR errors, achieving the best result among models of comparable size. Finally, we open-source \textbf{TransRubric}, a rubric-based automatic evaluation suite for translation, which outperforms other evaluation schemes on the WMT26 metrics shared task test set and is more stable with respect to human evaluation.

---


### 153. [Too Fast to Doubt? Skipping Reasoning Leaves Jev-like Models Vulnerable](https://arxiv.org/abs/2611.27679)

**<font color=#1a73e8>作者：</font>** Yue Li, Hao Wu, Zenan Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fast decision models offer low-latency actions and explicit confidence estimates. We audit four state-of-the-art decision models on 1,440 paired synthetic browser tasks, injecting false conclusions or evidence interpretations through external comments. Across models, clean accuracy averages 91.0%, yet two-shot attack success reaches 81.2%. Mean expected calibration error rises from 2.6% on clean inputs to 36.7% under conclusion poisoning and 36.1% under evidence poisoning. Clean accuracy and calibration therefore do not ensure reliable decisions under injection. We further compare GPT-6 Luna and Luna Decisions, which share the same base model, on 48 matched tasks. With a chain of thought averaging fewer than 30 reasoning tokens per response, low-effort GPT-6 Luna answers 95.83% of poisoned inputs correctly, versus 38.54% for native Luna Decisions, while mean selected-generation latency increases from 0.29 to 1.94 seconds. These results expose a sharp latency-robustness trade-off: skipping reasoning for sub-second speed leaves fast decision models substantially more vulnerable to deceptive web content.

---


### 154. [Abstract What Varies, Reuse Longer Patterns: Efficient Offline Chain-of-Thought Compression](https://arxiv.org/abs/2611.27710)

**<font color=#1a73e8>作者：</font>** Shibo Wang, Yuzhe He, Yifeng Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline chain-of-thought (CoT) compression creates shorter supervision for efficient reasoning, but per-example compressors repeatedly process similar expressions across traces, wasting compressor budget. Methods that reuse identical text across examples miss longer shared expressions when names, numbers, or formulas change from one question to another. We introduce CRAFT, which abstracts problem-specific details into slots to uncover partially lexicalized expression templates (PLETs) and clusters wording variants into families. Compressing each family representative once yields shared deletion or rewriting edits, which are applied with each occurrence's own details to construct compact, ordinary-text training targets. Compared with per-example rewriting, CRAFT Rewrite reduces weighted compressor budgets by a median 90.7% with a median accuracy loss of 1.21 percentage points, while generating shorter reasoning. Against cross-sample encoding, it shortens reasoning across all eight model-dataset settings by 25.3% on average and improves accuracy in five.

---


### 155. [MetaRigor: From Agentic Automation to Verifiable End-to-End Meta-Analysis Through Scientific Decision Boundaries](https://arxiv.org/abs/2611.27713)

**<font color=#1a73e8>作者：</font>** Yifeng Xie, Chenke Li, Yangshuo Miao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated meta-analysis requires not only accurate numerical extraction but also the consistent preservation of result identity across stages, including the associated study, comparison, population, outcome, time point, and analysis conditions. We present MetaRigor, an LLM workflow framework for verifiable end-to-end evidence synthesis. MetaRigor organizes study results as Study x Target units and operationalizes scientific decision boundaries at the task level through Task Contracts, programmatic rules, and source binding. The model performs semantic interpretation that depends on study context, whereas programs execute formalizable rules, computations, validation, and source verification. We conducted controlled evaluations across five stages: evidence acquisition, data extraction, risk of bias assessment, certainty of evidence assessment, and manuscript generation. MetaRigor achieved an F1 score of 86.29% for complete result delivery and 80.20% agreement for domain-level certainty of evidence judgments. Generated manuscripts received scores of 86.00 under human evaluation, exceeding all three baselines. A seven-case downstream end-to-end evaluation further yielded an aggregate F1 score of 77.01%, exceeding the strongest baseline by 9.78 percentage points. Cross-system tracing of archived outputs from three systems further showed that local mismatches or omissions in result identity could alter statistical inputs and the objects subjected to risk of bias assessment, with these errors subsequently propagating into the final report. Ablation experiments showed that task constraints and programmatic rules played distinct roles across different stages. These findings indicate that, in LLM-driven evidence synthesis workflows, consistently maintaining explicit result identity, decision boundaries, and provenance relationships is critical to improving end-to-end verifiability.

---


### 156. [Decision Models for Multilingual Emotion Classification: A Comparative Study Against LLMs and Encoders](https://arxiv.org/abs/2611.27721)

**<font color=#1a73e8>作者：</font>** Alessandro Piccolo, Francesco De Nicolò, Francesco Manco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision models receive a question with a closed list of answers and return a probability for each answer instead of free text. They promise low latency and robustness to prompt wording, but no study has compared several of them with fine-tuned encoders across languages. We ask whether systems used without training on labelled data (zero-shot) can replace fine-tuning, and what the decision format adds over a general-purpose large language model (LLM). We compare three decision models (Jev, OpenAI Decisions, Strands Decider 2B) and two LLMs (GPT-6 Luna, Qwen3.5-2B), given Italian instructions, with two fine-tuned multilingual encoders (tabularisai, XLM-EMO) on four emotions (joy, sadness, anger, fear) in 10 social-media datasets in five languages, with paired difference and equivalence tests. The three best zero-shot systems (two decision models and one LLM) score on average about one macro-F1 point below an encoder fine-tuned on the target dataset; our test sets cannot exclude a gap of 4-5 points, and on single datasets either approach wins by up to 22 points. They beat encoders fine-tuned on another dataset by 8-15 points, though against XLM-EMO this may not extend to new datasets, and instructions in each text's language change their results by under 1 point. Exploratorily, they beat the strongest public emotion model used as is by about 6 points. OpenAI's decision endpoint matches GPT-6 Luna, the LLM it runs on, at a fifth of its median latency, and a 2-billion-parameter decision model beats a same-size general LLM by 10 points, owing to its training, not the decision format. The best zero-shot systems, the LLM included, have an SD of about 1 point across prompts. Without labelled data they are a strong default, and decision models add lower latency and, unlike generative LLM use, per-option probabilities. Fine-tuning won by a wide margin only on the largest dataset, GoEmotions.

---


### 157. [Beyond Math, Code, and Logic: Do Reasoning Models Transfer to Scientific Argumentation?](https://arxiv.org/abs/2611.27722)

**<font color=#1a73e8>作者：</font>** Buse Sibel Korkmaz, Antonio del Rio Chanona  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discourse depends on argumentative reasoning: identifying claims, evaluating evidence, and constructing coherent responses. While recent advances in reasoning-capable language models have demonstrated strong performance on mathematical, coding, and logical benchmarks, their ability to engage in scientific argumentation remains unclear. We present the first systematic evaluation of language models across seven tasks spanning argument mining, rebuttal generation, and discourse-level reasoning using research papers, peer reviews, and grant proposals. Our study reveals that even frontier models with strong general reasoning skills struggle with domain-specific argumentative tasks, highlighting a fundamental capability gap. To address this, we introduce a training framework that explicitly scaffolds the argumentative reasoning process in language models, substantially improving their competence in scientific discourse. The resulting compact models approach or exceed the performance of much larger proprietary systems and generalize to unseen conversational settings, demonstrating reasoning transfer beyond task-specific supervision. These findings underscore that effective scientific argumentation is not an emergent property of scale, but requires explicit reasoning-aware training, and they point toward practical pathways for building AI systems that can contribute meaningfully to scientific discourse.

---


### 158. [A Cognitive Agentic AI Framework for Interactive Process Analysis and Optimization](https://arxiv.org/abs/2611.27725)

**<font color=#1a73e8>作者：</font>** Trung Ngoc Trinha, Roman Tschentscher, Trong Dong Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Complex multivariable process analysis and optimization require coordinated access to simulation, structured data, machine learning (ML), optimization, and scientific literature, often across disconnected software tools. We present a Cognitive Agentic AI Framework (CAAF) that enables interactive, iterative process investigation through natural-language prompts within an established flowsheet. Following harness-engineering principles, CAAF assigns task interpretation, planning, knowledge synthesis, and context management to a large language model while delegating numerical calculations to specialized tools. Dedicated providers connect databases, scientific-document retrieval, ML-assisted Bayesian optimization (BO), and COCO process simulation. The framework is demonstrated on methyl acetate production. Guided by successive prompts, an engineer explored multivariable relationships, conducted 4,000 BO iterations to maximize carbon conversion yield (C-Yield) and minimize specific energy cost (C-SEC), refined operating bounds, and verified selected candidates through process simulation. Re-simulation of 16 candidates within the restricted domain showed close agreement with ML predictions, with a mean absolute C-Yield error of 0.0085 (0.85 percentage points). The highest BO-derived C-Yield, verified by COCO, was 0.921 versus approximately 0.81 in the initial dataset, an improvement of about 11 percentage points. CAAF also detects and reports non-converged simulations, excludes invalid outputs, and continues subsequent evaluations. The results demonstrate how human-guided agentic coordination can combine engineering tools for iterative analysis and optimization with rigorous simulation-based verification under a fixed process topology.

---


### 159. [Average-Depth Variable Execution via Request-Local Token Routing](https://arxiv.org/abs/2611.27738)

**<font color=#1a73e8>作者：</font>** Pengjie Zheng, Mengwei Xie, Huan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Layer skipping can reduce large language model inference costs, but a request budget does not specify how to allocate layer execution across generated tokens. We introduce \method{}, which allows tokens to execute different numbers of layers while matching each request's mean executed depth to a continuous budget. At each routed layer, a router reads the current token state and its request's budget and decides whether to execute the Transformer block. Tokens that skip the block pass through a lightweight residual adapter and write no key/value (K/V) entry at that layer. A single checkpoint serves requests with different budgets in the same batch. Across three LLaMA backbones, six quality metrics, and 13 budgets, AVERT is best or tied for best in 206 of 234 comparisons. Across single- and mixed-budget batches, the mean absolute per-request budget error is at most 1.15 percentage points. When grouping requests by budget leaves batches underfilled, mixing budgets reduces decode time per output token (TPOT) by 4.3--21.2%.

---


### 160. [Can Vision-Language Models Synthesize Executable Game-Playing Programs?](https://arxiv.org/abs/2611.27741)

**<font color=#1a73e8>作者：</font>** Yao Tong, Jiaxin Qi, Dingyu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models (VLMs) have endowed multimodal agents with increasingly strong visual perception and long-horizon reasoning capabilities, making VLM-based autonomous game playing feasible. Existing game benchmarks primarily evaluate whether an agent can select appropriate actions from the current visual state across different scenarios and games. However, most of them adopt a step-by-step interaction paradigm where the current visual observation is sent to the agent before each action. In practical deployment, this paradigm introduces two fundamental limitations: the game loop must wait for model inference, making real-time interaction impractical, and repeated VLM calls incur substantial cost. Therefore, we propose PlayScriptBench, a script-based game benchmark that evaluates whether VLMs can synthesize an executable game-playing program from game states. This setting jointly evaluates visual grounding, understanding of game dynamics, long-horizon strategic reasoning, and executable program synthesis, providing a more comprehensive assessment of game-playing agents. To support more tractable evaluation for current general-purpose VLMs, we further introduce a four-stage pipeline --- Explore, Perception, API Construction, and Strategy Composition --- that decomposes controller synthesis into game exploration, state perception, interface construction, and strategic control, enabling agents to progressively construct an executable program. Experiments on 16 games spanning 4 genres show that even strong VLMs struggle on our benchmark, revealing a substantial gap between passive visual game understanding and executable closed-loop game control. These results establish script-based controller synthesis as a complementary direction for benchmarking VLM-based game-playing agents.

---


### 161. [RoSci: Exploring Robustness in Science VLMs](https://arxiv.org/abs/2611.27750)

**<font color=#1a73e8>作者：</font>** Junying Wang, Yijin Guo, Yalun Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Vision-Language Models (VLMs) enable significant progress in scientific tasks. However, these models are generally assumed to be presented with complete and accurate information, overlooking the challenges of erroneous/missing information in wild scenarios. To address this gap, we introduce the concept of Scientific Model Robustness, which defines a model's ability to detect anomalies, assess solvability, and perform self-calibration when faced with Information Error (inconsistencies) or Information Loss (insufficiency). Specifically, we present RoSci-Bench, a diagnostic benchmark of 1,220 samples using a seed-variant strategy across six degradation types. To address VLM fragility, we further propose RoSci-Agent, a framework that employs a Parse-Verify-Decide pipeline to vet premises before reasoning. The evaluated VLMs sometimes answer questions whose premises are invalid or incomplete. RoSci-Agent achieves a higher Overall Robustness Score than the evaluated standalone VLMs. RoSci-Bench gives the multimodal reasoning community a common test of when models answer, request clarification, or reject a scientific question.

---


### 162. [DPMA: Learning to Compress Mixture-of-Experts Models](https://arxiv.org/abs/2611.27759)

**<font color=#1a73e8>作者：</font>** Jon Irureta, Jon Imaz, Philipp Wiesner 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures offer high computational efficiency, but storing all experts requires substantial memory and limits deployment on resource-constrained hardware. Most retraining-free MoE compression methods commit to either pruning or merging experts, often with a uniform compression ratio across layers. We introduce DPMA (Differentiable Prune Merge Absorb), which jointly learns compression operations and layer-wise expert allocation through gradient descent under a global expert budget. Separate learnable coefficients allow DPMA to prune experts, merge their parameters, and absorb their routing contributions by forwarding routing weights to retained experts. These coefficients and expert assignments are optimised to match the original model's outputs on calibration data while its weights remain frozen. Across four MoE models, eight multiple-choice benchmarks, and five compression ratios, DPMA achieves the highest accuracy averaged over benchmarks and compression ratios on each model among the evaluated methods. At $75\%$ expert reduction, it outperforms the strongest baseline on every model, with gains of up to $6.7$ percentage points.

---


### 163. [Enhancing Attention with Higher-Order Attention](https://arxiv.org/abs/2611.27764)

**<font color=#1a73e8>作者：</font>** R. I. Cukier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current decoder large language models rely on a combination of attention, feed forward and residual layers. The attention used is autoregressive (AR) though this is not strictly correct, as we note. That motivates the introduction of other attention methods that, while also not strictly AR, do enhance the AR character. One is based on a decomposition of mutual information (MI) into a set of Conditional MIs (CMIs) that correlate key tokens with pairs of query tokens. A second, higher-order attention, introduces correlations between contiguous key and query tokens. A third introduces correlations between a set of key and query tokens and uses a Generalized Maximum Entropy Principle to obtain an attention expression spanning a sequence of tokens. All these methods may enhance the information content of the autoregressive probabilities that are used in inference/generation. Applications to contrastive decoding and a systematic analysis of autoregressive probabilities are presented.

---


### 164. [QuASAR: Toward an LLM-Assisted Framework for Screening, Prototyping, and Assessing Quantum-Advantage Opportunities in Scientific Computing](https://arxiv.org/abs/2611.27778)

**<font color=#1a73e8>作者：</font>** Mark L. Carroll, Jordan A. Caraballo-Vega, Brian P. Powell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying scientific computations that could benefit from quantum algorithms requires both domain knowledge and fluency in quantum algorithm design, expertise that rarely resides in one person. We report results from QuASAR, an experimental, two-agent, LLM-driven pipeline intended to bridge this gap. One agent screens scientific literature for computational kernels with a plausible quantum-algorithmic analogue and proposes candidates, each backed by citations. A second agent independently verifies those citations. For candidates that survive verification, it reconstructs the source's computational structure, formulates a quantum mapping, builds and executes a prototype, and benchmarks it against classical baselines. We applied this pipeline to ten candidate computations drawn from the astrophysics literature. Nine candidates were carried through to a small-scale, benchmarked prototype. We report three in detail, chosen as the clearest examples with the least redundancy across the set. They span combinatorial optimization, stochastic simulation, and Bayesian inference. The pipeline attempted to supply quantum-design expertise a domain scientist might lack, reconstructing source algorithms where one existed and building original, disclosed mappings where none did. None of the three case studies achieved quantum advantage at the tested scales, and their astrophysical framing has not yet undergone expert validation. What the experiment does show is that the pipeline can turn a published idea into a runnable prototype, which a scientist can then inspect, test against classical methods, and decide whether to pursue. QuASAR is an exploratory framework, offered to the community for evaluation, critique, and further development, with an approach that could broaden the use of quantum computing in scientific research and extend to computational improvements more generally.

---


### 165. [ChildAI-Gov: An Evidence-Linked AI System for Assessing EdTech Policies Against Children's Digital Rights](https://arxiv.org/abs/2611.27799)

**<font color=#1a73e8>作者：</font>** Naveen Sigalapalli, Huizhi Liang, Clara Crivellaro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ChildAI-Gov, an explainable AI system for assessing whether education-technology (EdTech) policies respect children's digital rights. Generative AI is reaching children's education faster than its governance can keep pace, yet checking a tool against children's rights remains manual, expert-dependent, and slow. We propose the Child Rights Impact Score (CRIS), an evidence-linked measure across five dimensions: safety, privacy, transparency, autonomy, and non-discrimination. ChildAI-Gov reads an EdTech tool's privacy or AI policy and scores each dimension by combining a large-language-model judgement (gpt-4o-mini) with a deterministic rule check. A retrieval-augmented generation (RAG) component grounds every score in the governing provisions, retrieved from a curated knowledge base of children's rights frameworks (the EU AI Act, UNICEF guidance, and others), so each score is tied to the evidence behind it and an auditor can trace which provision it rests on. We also construct AIPolicy-EdTech, a dataset of 57 real EdTech policies. On it, the five dimensions cohered as a single measure (Cronbach's alpha = 0.79), and grounding made scoring stricter while preserving rankings; an ungrounded baseline was far more lenient, passing nearly half the policies where ChildAI-Gov passed none. It offers evidence-linked decision support on documented commitments, not observation of real-world behaviour or determinations of legal compliance.

---


### 166. [Evaluating Prompting Strategies for Zero-Shot Multilingual Aspect-Based Sentiment Analysis with Large Language Models](https://arxiv.org/abs/2611.27807)

**<font color=#1a73e8>作者：</font>** Jakub Šm{í}d, Pavel Kr{á}l  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) have advanced natural language understanding, their ability to perform complex target-aspect-sentiment detection (TASD) -- a key task within aspect-based sentiment analysis (ABSA) -- in zero-shot multilingual settings remains underexplored. Existing ABSA research predominantly focuses on English or relies on fine-tuned task-specific models, leaving a gap in understanding how open-weight LLMs handle compound sentiment triplet extraction across diverse language families and domains. We present a systematic evaluation of zero-shot multilingual TASD across 12 languages and three domains using seven instruction-tuned open-weight models -- ranging from 8B to 35B parameters across dense and mixture-of-experts (MoE) architectures -- under four prompting paradigms: monolithic, chain-of-thought, sequential, and sequential refine. Our results show that direct monolithic prompting achieves strong zero-shot performance, outperforming multi-step pipelines, while dense models consistently outperform sparse MoE architectures. Through fine-grained error taxonomy profiling and step-level pipeline tracking, we demonstrate that initial aspect term recall forms a hard bottleneck, whereas multi-step decomposition degrades extraction quality; iterative refinement only partially recovers this loss on larger models while inducing net-negative over-refinement on smaller architectures. Finally, generation volume analysis shows that multi-step strategies incur up to 2.38x token overhead without F1 gains, establishing monolithic prompting as the most effective and efficient paradigm for multilingual ABSA.

---


### 167. [SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech](https://arxiv.org/abs/2611.27810)

**<font color=#1a73e8>作者：</font>** Côme Hosxe, Rachid Riad, Quentin Spinat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio language models (ALMs) can answer clinical questions from speech, outperforming baselines built on handcrafted acoustic features. Reasoning ALMs generate a chain of thought that refers to properties of the speaker's voice before predicting. Each statement the model makes about the voice needs to be checked against clinicians' perceptual ratings of the same recording. On clinical speech, existing evaluations score only the final answer. We introduce Speech Language Pathologist Bench (SLP-Bench), a benchmark grading each acoustic claim in the chain of thought against clinicians' perceptual ratings of the same recording. It covers five clinician-rated datasets and 25 perceptual dimensions, and assesses claims for factuality, stability under resampling, and consistency across reworded and different questions. Across ten open-weight reasoning ALMs evaluated zero-shot, claim balanced accuracy ranges from 0.52 to 0.58, claims change under resampling and rewording, and the most consistent models are not the most factual. Fine-tuning a 7B ALM with GRPO on a reward for claims that agree with clinicians raises its claim balanced accuracy from 0.54 to 0.60 and its mean kappa from 0.39 to 0.61, while preserving answer accuracy on per-dimension questions. SLP-Bench is available upon request, subject to approval by the providers of each dataset.

---


### 168. [BinXSight: Fast Binary Program Summarization via Hierarchical Modular Decomposition](https://arxiv.org/abs/2611.27816)

**<font color=#1a73e8>作者：</font>** Zhijie Liu, Zhipeng Xue, Zhipeng Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Binary code summarization (BCS) is crucial in fields such as cybersecurity. Particularly, program-level BCS can quickly provide a comprehensive overview of an entire stripped binary without in-depth manual reverse engineering. However, a binary often contains numerous functions with complex interactions, making it challenging to extract its functionality efficiently. Moreover, existing methods focus solely on function-level without considering contextual information, limiting their applicability to program-level analysis. Towards comprehensive and fast program-level BCS, we propose BinXSight, an LLM-powered framework based on hierarchical modular decomposition. Specifically, we first propose binary graph, a new data structure composed of four graphs, to comprehensively represent a binary. Then, based on the binary graph, we hierarchically decompose functions into modules and select the most significant ones. Finally, BinXSight generates a program-level summary from these module summaries. We evaluate BinXSight on stripped binaries across various sizes, fields, platforms, and architectures. Results show that BinXSight outperforms baselines by 23.18% to 46.99%, and summarizes a binary with about 3K functions in 24.3 seconds on average. In addition, a user study with 27 experts shows that BinXSight's high-quality summaries help users quickly understand the whole binary. Our case analysis on recent real-world malware further demonstrates its practical utility.

---


### 169. [DistDNA: Language Model Fingerprinting under Stochastic Decoding](https://arxiv.org/abs/2611.27831)

**<font color=#1a73e8>作者：</font>** Lifan Hu, Qian Yu, Zhaomin Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavioral fingerprints identify a large language model (LLM) from its responses to a shared set of prompts, enabling applications such as verifying whether a deployed model corresponds to the checkpoint it claims to be. Deployed models, however, are commonly served with stochastic decoding, under which the same model may produce different responses to an identical prompt, depending on an unknown temperature and top-$p$ setting. Existing representations such as LLM DNA provide limited treatment of this variation. A natural remedy is to characterize models by their response distributions, which, however, raises two challenges. First, each distribution must be estimated from only a small number of sampled responses. Second, a change in decoding setting can alter responses to the same extent as a change of checkpoint. Consequently, fingerprint distances alone provide an incomplete basis for model identity, and identification typically relies on a classifier trained jointly on fingerprints from many checkpoints. We propose DistDNA, which represents a model by its prompt-conditional response distributions and compares models by promptwise maximum mean discrepancy (MMD). The model under examination is assigned to the known checkpoint whose reference fingerprints, collected at several decoding settings, lie nearest to its own, without training a classifier. We show that finite sampling adds variance-dependent terms to the expected squared fingerprint distance, with these terms decreasing as $O(1/R)$ for equal response counts, where $R$ is the number of responses per prompt. Experiments across 115 model checkpoint entries demonstrate that DistDNA improves identification accuracy over the strongest baseline, LLM DNA, by 10.36%.

---


### 170. [Auditable Financial Knowledge Graphs: Schema-Driven Construction and Intrinsic Quality Evaluation](https://arxiv.org/abs/2611.27835)

**<font color=#1a73e8>作者：</font>** Samarth Sarin, Lovepreet Singh, Dhagash Mehta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial documents combine narrative disclosures, accounting metrics, corporate structures, management commentary, and time-dependent facts, making them difficult to represent using conventional chunk-based retrieval-augmented generation systems. This paper presents an auditable, schema-driven methodology for constructing temporal financial knowledge graphs from page-delimited documents parsed using a general purpose document intelligence service. Overlapping document windows undergo phased large language model extraction of structural entities, quantitative observations, and domain-specific relationships. Candidate graph elements are validated against predefined schemas and consolidated through scope-aware exact, normalized, fuzzy, embedding-based, and LLM-assisted entity resolution. Temporal merge constraints, deterministic edge deduplication, conflict-aware property management, and fine-grained provenance preserve issuer identity, reporting-period validity, and traceability to source evidence. The contributions of this work comprise the proposed methodology for financial knowledge graph construction, the creation of an evidence-grounded temporal knowledge graph from heterogeneous financial documents, and an intrinsic framework for evaluating the quality of the resulting graph. The evaluation framework assesses seven weighted dimensions, two hard validation gates, and structural diagnostics. By separating graph-quality assessment from downstream retrieval and answer generation, the framework supports systematic diagnosis and iterative refinement of the constructed graph.

---


### 171. [Beyond Self-Critique: Epistemic Convergence Control for Multi-Agent Research Verification](https://arxiv.org/abs/2611.27839)

**<font color=#1a73e8>作者：</font>** Chrisantus Eze  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems for scientific claim verification increasingly rely on role-structured LLM debate to pressure-test hypotheses. However, when debating agents are instantiated from the same underlying base model, they share identical latent representations, making self-critique bias structurally inevitable. Static fixed-iteration protocols compound this by either halting prematurely before evidence stabilizes or wasting inference compute after convergence. We present \sys{}, a multi-agent research verification framework that addresses both failure modes. First, we introduce an asymmetric role architecture comprising an Advocate, Skeptic, and Arbitrator with opposing epistemic directives, producing significantly lower role-embedding similarity (0.852 vs.\ 0.918 for symmetric Multi-Agent Debate [MAD], $p = 5.82 \times 10^{-8}$) and surfacing more contested claims (22.0\% vs.\ 15.4\%). Second, we propose the Belief-Delta ($\DB$) convergence criterion, an evidence-grounded stopping rule that eliminates over-iteration (0.0\% vs.\ 62.5\% for Fixed-$3$) while cutting LLM calls by 2.4$\times$. Third, each supported claim is anchored to a verbatim literature snippet audited by an independent NLI classifier, achieving a 21.7\% hallucination rate (comparable to 25.9\% for a Self-Refine critic, $p = 0.61$) while establishing auditable evidence grounding. Across 200 runs on 40 research hypotheses evaluated with DeepSeek-R1-32B, \sys{} balances compute efficiency with rigorous epistemic verification.

---


### 172. [ENC-QA: A Diagnostic Benchmark for Vision-Language Models on Electronic Navigational Charts](https://arxiv.org/abs/2611.27858)

**<font color=#1a73e8>作者：</font>** Jiyoon Pyo, Jacob Arndt, Yao-Yi Chiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nautical charts encode safety-critical maritime information through standardized symbols, attributes, text, and heterogeneous geometries. Interpreting these charts and assessing the navigational significance of successive chart updates requires recognizing nautical features, determining their spatial relationships, and applying navigational knowledge. Vision-language models (VLMs) offer a promising approach to nautical-chart interpretation, yet systematic evaluation of their fine-grained nautical feature recognition, chart-based spatial reasoning, and application of navigational knowledge to assessing chart changes remains limited. We introduce ENC-QA, a diagnostic benchmark comprising 77,312 questions derived from 6,612 National Oceanic and Atmospheric Administration (NOAA) Electronic Navigational Charts (ENCs). The benchmark evaluates four complementary capabilities: ENC Perception, Spatial Reasoning, Joint Perception and Spatial Reasoning, and Application. Of these, 8,227 questions form a progressive subset that decomposes selected chart-change cases into linked questions progressing from change detection to criticality assessment, enabling case-level analysis of how models use perceptual and spatial evidence to determine the navigational significance of chart changes. Evaluations of 10 open-weight VLMs reveal substantial limitations in fine-grained nautical feature recognition and feature-grounded spatial reasoning. Controlled evidence interventions show that relevant perceptual and spatial information improves change-criticality accuracy. Our findings establish ENC-QA as a diagnostic resource for nautical-chart understanding and safety-critical navigational decisions. We will release the benchmark and evaluation code upon publication.

---


### 173. [Who Grades the Agent? Privilege Separation for Coding-Agent Benchmarks](https://arxiv.org/abs/2611.27860)

**<font color=#1a73e8>作者：</font>** Nathan Nour Houlamy, Mattia Favretto, Earlence Fernandes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Benchmarks for AI-based coding agents are a staple of the current AI landscape, because they are the leading way to measure the performance of LLMs. Their scores guide business and research decisions. Evaluating coding agents is challenging, since they are able to manipulate their evaluation infrastructure to artificially achieve better scores. Grading an agent's solution often requires running its code, which can then manipulate the evaluation process. BenchJack, an automated benchmark auditor, recently reached near-perfect scores on nine of ten popular agent benchmarks without actually solving their tasks. Agents already do this unprompted, as OpenAI's July 2026 Hugging Face incident showed.
Building on secure systems design, we introduce SplitBench, a privilege separation framework for evaluating coding agents and the first in the scientific literature to separate running a task's tests from judging their results. Even an agent whose code takes over the entire test environment cannot forge a pass, because a trusted grader holds the expected answers. We show that real-world benchmarks (e.g., Terminal-Bench, DeepSWE) can be ported to the SplitBench framework with minimal effort and high fidelity: 180 of 202 tasks convert, and SplitBench agrees with the native graders on 98.7% of agent attempts. We attack the converted tasks in the worst case, where adversarial agents can read all the grading code but not the expected answers. SplitBench blocked 75% of their attempts; the rest mostly reveal weaknesses in the original tasks' tests rather than flaws in SplitBench.

---


### 174. [Integrating Generative Artificial Intelligence with Learning Style Models: Opportunities, Challenges, and Future Directions](https://arxiv.org/abs/2611.27868)

**<font color=#1a73e8>作者：</font>** Malithi Nawarathne, Prasanna Haddela, Nuwan Kodagoda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative Artificial Intelligence (Generative AI) has emerged as a powerful tool for transforming learning. This review examines how Generative AI can be integrated with established learning style models (VARK, Kolb, Felder-Silverman, and Honey & Mumford) to support student engagement in large online classes. Following PRISMA 2020 guidelines, we searched Scopus, IEEE Xplore, and Google Scholar (2015 to 2026) and included 41 studies that met the eligibility criteria. The review maps Generative AI capabilities to learning style preferences, synthesizes existing implementations, highlights benefits and challenges, and proposes pathways for future research and practice. Despite ongoing debates regarding the empirical validity of learning styles, Generative AI enables flexible, multimodal, and real-time adaptation. This study offers practical insights for educators and developers seeking to build more effective, learner centered learning systems

---


### 175. [LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT](https://arxiv.org/abs/2611.27876)

**<font color=#1a73e8>作者：</font>** Maximilian Rokuss, Jeya Maria Jose Valanarasu, Alejandro Lozano 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Every few months, a cancer patient's CT scans decide whether treatment continues. 3D foundation models can now detect, segment, register and track lesions, yet none of them reads the scans as a radiologist does. A radiologist decides which findings are lesions, which are the same lesion months later and whether a new spot means progression, and checks each decision against the extensive rules of a clinical guideline. We introduce LesionAgent, an LLM agent that performs this read end to end without task-specific training. It operates frozen 3D models as tools, acts in 3D through coordinate-labelled views, remembers every lesion across visits in a registry, verifies every model output it relies on, and leaves every number to a deterministic guideline engine. On four public longitudinal CT datasets, LesionAgent tracks more lesions and measures them more accurately than every automatic baseline, and where the same 3D models chained by fixed rules call progression falsely at 33 of 56 follow-ups, it does so twice. On clinical follow-up CTs, it agrees with the radiologists' response at 20 of 23 follow-ups, including every change in response, and without training on DeepLesion, it retrieves more of its lesions than every tracker trained on it (89.0% vs. 87.4%). Its harness, not its LLM, makes the difference: given the same LLM and 3D models but not the harness, Claude Code reaches a detection F1 of 41% and LesionAgent 78%, and an open-weight LLM that can run inside the hospital rises from 6% to 73%. LesionAgent and a napari reading app for any LLM are available at this https URL.

---


### 176. [Speculative Decoding Is Less Speculative Than You Think](https://arxiv.org/abs/2611.27891)

**<font color=#1a73e8>作者：</font>** Guanning Zeng, Andrea Zanette  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates language-model inference by preparing candidate continuations before the target model generates them. Its efficiency depends on how well limited drafting computation anticipates the path the target will actually follow. Anticipating this path involves two sources of uncertainty: the target model's predictions and the randomness of sampling. Yet the former requires a target-model forward pass, while the latter can be fixed before drafting. Building on this observation, we introduce DICE (Draw-Informed Candidate Selection), which pre-samples and synchronizes verification randomness across drafting and verification. By combining these known draws with predictions from an existing drafter, DICE allocates computation toward continuations more likely to be used in the current sampling run. This principle guides node selection throughout draft-tree construction and extends to asynchronous prefetching, where DICE predicts which next-round drafts to prepare. Without additional drafter training or changes to the target sampling distribution, DICE achieves state-of-the-art decoding throughput across diverse settings, with speedups of up to 24.6pp over strong baselines.

---


### 177. [The Dual-Tier Sentiment Framework: Scalable Multimodal UX Attribution in Web Search](https://arxiv.org/abs/2611.27899)

**<font color=#1a73e8>作者：</font>** Yi Ding, Gaurav Kumar, Rui Min 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sustaining user experience (UX) quality in large-scale web search requires scalable evaluation. Traditional surveys are slow and bottleneck rapid A/B testing, while automated metrics often lack the granularity to diagnose visual-spatial UX anomalies. To address this, we introduce the Dual-Tier Sentiment Framework, a novel industrial architecture for automated UX attribution. Tier 1 (Macro System) acts as a scalable user sentiment regression detector, utilizing a fine-tuned encoder-decoder LLM (based on Gemini XS) on telemetry features. Through multi-task regularization and contextual feature engineering, this tier achieves a +9.8% PR-AUC gain on over 500,000 held-out records, matching baseline recall on all validated regressions with $\sim$20% relative precision gain among the 12 held-out experiments. In production, it reduces measurement latency from weeks to hours and cuts survey overhead by over 40%. Tier 2 (Micro System) provides granular diagnostics by employing a Multimodal LLM (Gemini 3.0 Pro) to natively assess visual renderings and spatial layout of web result blocks, quantifying "User Toil" as the estimated effort required to reach a satisfactory result. Enhanced by RL-based automated prompt optimization and an AI judge for win/loss patterns, the MLLM yields a $>$6.5% F1 score improvement, offering deep insights into content quality and layout friction. Ultimately, this framework enables scalable, accurate, and diagnostic UX attribution, processing O(100k) live experiment queries daily.

---


### 178. [QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers](https://arxiv.org/abs/2611.27901)

**<font color=#1a73e8>作者：</font>** Zunhai Su, Keyu Fan, Ruishan Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming visual geometry transformers retain historical key-value (KV) states as cross-view geometric memory, but growing caches constrain long-sequence inference. We systematically characterize KV quantization in streaming geometry and uncover two linked challenges: Nonuniform Geometric Sensitivity and Cache-Geometry Mismatch. Quantization sensitivity varies across precision choices and cache locations, while perturbed retrieval changes geometry-head inputs and propagates through subsequent predictions and KV writes. Guided by these findings, we propose QuantStream3D, to our knowledge the first dedicated KV quantization framework for streaming visual geometry transformers. Geometry-Guided Mixed-Precision KV Quantization protects sensitive cross-view evidence, while Geometry-Aligned Quantization-Aware Distillation jointly adapts transformer blocks and geometry heads on student-generated quantized history. Across five benchmarks and two backbones, QuantStream3D achieves near-lossless geometric accuracy in most settings with predominantly 2-bit KV caches, and many configurations surpass unquantized inference. Compared with LLM-oriented KV quantizers, it reduces TUM absolute trajectory error and NeuralRGBD completeness error by up to 57.4% and 69.7%, respectively. Integration with existing native cache-pruning methods further pushes compression while improving reconstruction quality on NeuralRGBD. Our optimized StreamVGGT backend achieves $5.05\times$ physical KV compression and 23.1% lower latency at batch size one. Under a fixed memory budget on the same GPU, it supports $5.4\times$ the maximum batch size and up to $1.67\times$ the peak throughput of unquantized inference. Code and pretrained checkpoints will be made publicly available.

---


### 179. [AnimalFarm: Auditing the Generation and Detection of Hateful Images Featuring Anthropomorphic Characters](https://arxiv.org/abs/2611.27905)

**<font color=#1a73e8>作者：</font>** Junjie Chu, Ye Leng, Mingjie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anthropomorphic non-human characters have long been used to convey hateful messages targeting human groups, from Nazi-era propaganda to recent AI-generated imagery on social media. However, the safety risks posed by such imagery remain largely unexplored. We thus conduct the first systematic study of hateful image generation and detection involving anthropomorphic non-human characters. We construct a benchmark from conservatively screened source scenes, covering five character types and three image generation tasks: text-to-image generation, image editing, and conversational image generation. Across 14,250 scheduled queries, image generation systems produce images for 92.1\% of queries, of which 95.9\% contain hateful content. We further collect 4,370 hateful images and evaluate five popular hateful-content detectors. Even the strongest detector, GPT-5.5, identifies only 73.9\% of hateful images, while most detect fewer than 58\%. Our analysis reveals that existing detectors often misclassify hateful images as benign when their main subjects are non-human characters. We explore two effective mitigation approaches: a training-free pipeline that maps non-human characters back to human representations before classification and a detector fine-tuned for this type of hateful content. These approaches achieve F1 scores of 0.962 and 0.979, respectively. Our findings expose significant safety gaps in both image generation and hateful-content detection.
Disclaimer: This paper contains hateful text and imagery.

---


### 180. [StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning](https://arxiv.org/abs/2611.27915)

**<font color=#1a73e8>作者：</font>** Chi Yan, Guoyang Zhao, Wentao Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) exhibit strong semantic understanding but remain limited in their ability to reason about metric 3D space in the physical world. Existing VLMs typically infer 3D scene structure from one or more images without known camera calibration or cross-view geometric constraints. This makes metric 3D inference inherently ambiguous and leaves it unclear whether their spatial predictions are grounded in visual evidence or driven primarily by semantic priors. In contrast, calibrated stereo provides explicit cross-view geometry that resolves this ambiguity and offers a more reliable foundation for metric 3D perception and geometric generalization. We investigate how VLMs can learn transferable 3D representations directly from calibrated binocular observations. To this end, we introduce StereoVLM, the first geometry-aware binocular VLM for metric 3D spatial reasoning. StereoVLM follows a hierarchical learning paradigm spanning from cross-view correspondence and disparity estimation to calibration-conditioned metric depth perception and semantic spatial reasoning. We further find that disparity supervision generalizes substantially better than direct binocular depth supervision on unseen environments. To evaluate these capabilities, we introduce Stereo3D-Bench, a comprehensive benchmark across three levels, from point-level geometry to object-level spatial reasoning. StereoVLM-8B achieves 95.17% depth accuracy ($\delta_1$) and a 66.98 average object-level score on Stereo3D-Bench. Intervention results further indicate that the model's performance on Stereo3D-Bench benefits from valid cross-view geometry and cannot be explained solely by additional visual tokens or semantic priors. Hierarchical geometric supervision also yields average gains of 3.54 points across five spatial benchmarks and 4.3 percentage points in RoboCasa manipulation success.

---


### 181. [DiTraR: Diverse Scorers and Transcript-Guided Re-ranking for Video Corpus Moment Retrieval](https://arxiv.org/abs/2611.27931)

**<font color=#1a73e8>作者：</font>** Mohammad Alijanpour Shalmani, Alale Rezvani Boroujeni, Ali Amini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video corpus moment retrieval asks a system to find, in a large collection of untrimmed videos with subtitles, the video and the time interval that a natural-language query describes. We find that most top-ranked errors of a strong corpus-level scorer come from choosing the wrong video, not from imprecise boundaries, and that re-weighting the evidence the scorer already uses does not fix them. We present DiTraR, which addresses video selection from two complementary directions. A witness-interval scorer decomposes the query into probes and scores every candidate interval of every corpus video exactly; a multi-scorer energy ensemble averages the energies of independently trained scorers before one exhaustive search; and a transcript verifier, a frozen language model that reads the time-stamped dialogue of the highest-ranked videos, re-orders the moments without changing their boundaries. With all settings frozen on development data and a single evaluation, DiTraR reaches 24.36 and 13.55 R@1 at IoU 0.5 and 0.7 on the TVR validation split. The ensemble improves queries about visual content, the verifier improves queries about dialogue, and their gains largely add up.

---


### 182. [MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973)

**<font color=#1a73e8>作者：</font>** Chang Nie, Chaoyou Fu, Songlin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) in long-horizon and continual interactions requires maintaining reusable memory states for future inference, posing challenges for existing architectures. Standard Transformers accumulate layer-wise, token-level KV caches, incurring linear GPU memory growth and quadratic computational complexity as the context expands. In contrast, linear-time architectures compress history into fixed-size states, but struggle to retain fine-grained details. We introduce MemOnce, a foundation architecture that learns scalable memory states for language models. MemOnce is based on two core designs: (a) Memory encoder-decoder: it caches only a small subset of final-layer hidden states as compact memory representations and dynamically decodes them back into KV caches for attention layers; (b) Memory sparse attention: for each continual input, MemOnce adaptively retrieves relevant memory representations, with the sparse indices computed only once across layers. Coupling these two designs enables efficient on-the-fly memory loading and KV cache decoding, drastically reducing the GPU memory footprint and achieving linear-time complexity. We conduct extensive experiments to show that MemOnce outperforms Transformers and other architectures across varying model sizes, context lengths, and training paradigms (pretraining and post-training adaptation). In particular, adapting Qwen3.5-4B with MemOnce reduces memory state cache by 1313$\times$ and prefill latency by 6.9$\times$ at 1M context, and improves throughput by 3.5$\times$ and overall memory performance by +5.77%. Finally, MemOnce generalizes zero-shot to downstream representation tasks, achieving competitive results against specialized models.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 183. [SkillPrivus: Uncovering PRIVacy of USe Harms in Agentic Skills](https://arxiv.org/abs/2611.26747)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mariana Fernandez-Espinosa, Ivoline Ngong, Keerthiram Murugesan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent skills extend AI assistants through installable instructions and code that can access users' files, accounts, and data. Even when performing their advertised tasks, skills may infer sensitive attributes, retain unnecessary information, or disclose data to unexpected recipients. We study these potential privacy-of-use harms through SkillPrivus, a static audit framework that analyzes skills before installation without executing them. SkillPrivus extracts data operations from code and natural-language instructions, grounds them in source evidence, and adapts Contextual Integrity to assess their appropriateness. Applied to 726 real skills from public marketplaces, 563 of which handle personal data, SkillPrivus flags at least one potential violation in 307 of these skills (54.5%), and its judgments agree with three blind human annotators on 83.2% of resolvable moves. The flagged behaviors include sensitive inferences, information use beyond the stated task, and disclosures to unexpected recipients, suggesting that privacy harms can arise from ordinary skill functionality.

---


### 184. [Reinforcement Learning Unlearns Corrupted SFT Reasoning](https://arxiv.org/abs/2611.26756)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Anika Misra, Shreyas Vinod, Huteng Dai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We show that reinforcement learning (RL) in reasoning tasks can succeed even when the supervised fine-tuning (SFT) data is severely corrupted. In a mathematical reasoning dataset (GSM8K), we systematically corrupt training trajectories across 361 configurations by injecting realistic error types, varying error locations, trace-answer consistency, and corruption ratios up to 100%. While aggregated SFT-only performance steadily deteriorates under corruption (dropping from 43.61% to 13.80%), Group Relative Policy Optimization (GRPO) post-training consistently restores model accuracy back to gold-baseline levels (approximately 60%). Crucially, initializing RL with as few as N = 8 minimal, incorrect, three-line "form-only" traces boosts post-RL performance to 69.30%, outperforming standard gold SFT initialization (60.71%) and GRPO without SFT (35.00%). Further, we show that SFT accuracy is largely uncorrelated with post-RL accuracy (r approximately 0), demonstrating a fundamental asymmetry in post-training: SFT primarily establishes structural layout (form), while RL independently discovers functional reasoning (function).

---


### 185. [Don't Discard Your Rollouts: Reusing Teacher RL Traces for Student Distillation](https://arxiv.org/abs/2611.26803)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Vashisth Tiwari, Emma Strubell, J. Zico Kolter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL post-training methods such as PPO and GRPO are computationally expensive, with substantial resources devoted to sampling rollouts, which contain multiple completions per prompt along with their respective rewards. Canonical distillation, however, discards these traces and uses more compute to regenerate data from the final teacher. We ask if and how we can reuse the saved teacher RL rollouts to distil student models. Reusing rollouts is non-trivial: naive SFT on the rollouts underperforms canonical distillation, and naive DPO, while performant, is unstable, collapsing on weaker students. We show that treating rollout reuse as a data selection problem using metadata already recorded during GRPO substantially reduces this gap. We use prompt pass rates to order the data, using the easiest prompts for an SFT warm start prior to using mixed-success prompts for DPO. For each prompt, we use saved teacher log-likelihoods as a proxy for selecting student-compatible completions. Across mathematical reasoning and Python coding tasks, with students from multiple model families, our two-stage recipe achieves comparable average performance to canonical distillation, while incurring no additional inference cost for dataset construction.

---


### 186. [Disentangling Verbalized Evaluation Awareness and Refusal through Neuron-Level Intervention](https://arxiv.org/abs/2611.27032)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jingyuan Feng, Gouki Minegishi, Andrew Gambardella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large reasoning models (LRMs) become more capable, reliable evaluation becomes essential. LRMs can sometimes recognize that they are being evaluated, a phenomenon known as \emph{evaluation awareness}. This phenomenon raises concerns about whether safety behavior, particularly refusal behavior, generalizes from evaluation to deployment. Prior work manipulates \emph{verbalized evaluation awareness (VEA)} through activation steering and observes higher refusal rates when VEA is present, but the mechanisms underlying this connection remain poorly understood. We identify \emph{VEA neurons} by contrasting their activations in VEA and non-VEA reasoning segments. Intervening on 5,000 VEA neurons reduces the VEA rate from 12.6--51.8\% to at most 1.4\% across the model benchmark combinations in our main experiments, and lowers a probe score for unverbalized evaluation awareness (unVEA). In QwQ-32B, VEA-neuron intervention also reduces refusal even in rollouts without VEA; VEA text itself explains only 4--10\% of the decrease. We further show that their down-projection vectors contain refusal components, and preserving these components during intervention partially restores refusal while maintaining VEA suppression, accounting for about half of the refusal decrease and providing a mechanistic explanation for the connection between evaluation awareness and refusal. Finally, across the OLMo 3 SFT, DPO, and RLVR checkpoints, the VEA rate on SorryBench and StrongREJECT is similar after SFT and DPO but substantially higher after RLVR, alongside an increase in the number of VEA neurons. Together, these findings show that VEA text itself has a limited effect on refusal, and that VEA neurons integrate evaluation awarenss and refusal.

---


### 187. [V2VFusion: Text-Controlled Video-to-Video Diffusion for Degradation-Aware Video Fusion](https://arxiv.org/abs/2611.27063)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiajun Chen, Han Xu, Yunfei Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video fusion integrates complementary information in multiple source video streams into a single sequence for complete scene perception. Existing methods perform frame-wise fusion and lack unified spatio-temporal modeling across sequences, damaging temporal coherence across sequences. When dealing with degradations, they also ignore temporal dynamics and overload a single network with diverse degradations, leading to limited and imbalanced degradation suppression. To address these issues, we propose V2VFusion, the first unified video-to-video fusion framework that directly generates temporally coherent, high-quality fused videos from degraded multi-source inputs. By reformulating video fusion as a video-to-video conditional generation problem in latent diffusion space, our approach holistically models spatio-temporal dependencies across entire sequences and intrinsically ensures sequence-level consistency. On this basis, a text-guided degradation-conditioned ControlNet bridges high-level textual degradation descriptions with low-level visual priors, enabling interpretable and controllable guidance for structure-preserving fusion beyond purely data-driven conditioning. To handle heterogeneous and compound degradations, a state-modulated degradation-aware hierarchical mixture-of-experts module decouples expert selection into diffusion-state-aware filtering and degradation-aware routing. It prevents unreliable routing and fosters expert specialization to mitigate representation conflicts among diverse degradations. Experiments on infrared-visible, multi-exposure, and multi-focus video fusion tasks and complex degradations validate that V2VFusion surpasses existing methods in fusion quality and temporal stability. The code is available at this https URL.

---


### 188. [Hindsight Forcing: Learning Better History from the Future in Autoregressive Video Diffusion](https://arxiv.org/abs/2611.27074)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haonan An, Yihang Tao, Yu Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive video diffusion enables real-time streaming generation, with each generated chunk serving as historical context for subsequent generation. To avoid the memory explosion of backpropagation through time, previous self-rollout methods typically truncate cross-chunk gradients or detach historical latents. As a result, earlier denoising computations receive no downstream feedback through the generated history on how to synthesize frames that facilitate subsequent generation, leading to visual drift and structural collapse as rollouts extend. To address this limitation, we propose Hindsight Forcing, which allows historical chunks to learn directly from future outcomes by decoupling forward generation from backward credit assignment via a latent straight-through bridge. In the forward pass, each chunk completes a full multi-step rollout to update the KV cache. In the backward pass, the bridge routes gradients from future losses back to a single selected denoising step per historical chunk, training both the context writer and historical denoiser on shared parameters without retaining the full trajectory graph. Remarkably, Hindsight Forcing requires no additional model parameters, architecture modifications, or separate trajectory replay. Extensive experiments on VBench demonstrate that Hindsight Forcing outperforms existing baselines in overall visual quality and dynamic motion, while ablation studies validate the benefit of supervising historical denoising. Code is available at this https URL.

---


### 189. [Distillation with Errors: Sparse Unbiased Backpropagation for Knowledge Distillation](https://arxiv.org/abs/2611.27131)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuyang Zhang, Yuxin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) trains a student to match a teacher's output distribution. However, full-vocabulary KD requires costly output-head backpropagation. To reduce this cost, we introduce Distillation with Errors (DWE). Our key insight is that minibatch training already approximates the training gradient, so per-position backpropagation does not need to be exact. DWE therefore exploits the zero-sum structure of logit gradients to construct sparse paired gradient estimates whose expectation matches the full-vocabulary gradient. It then uses geometry-aware pairing and stratified sampling to further reduce estimation variance. We prove that the estimator is unbiased and evaluate DWE's gradient estimation accuracy and training efficiency. At the same sampling budget, DWE reduces hidden-state and output-weight gradient MSE by 63.5% and 57.9%, respectively, compared with importance sampling. In off-policy KD, it achieves up to a $1.95\times$ output-head speedup and reduces training time by 10.4-15.7% relative to full-vocabulary KD. In on-policy distillation (OPD), it achieves up to a $2.20\times$ output-head speedup. DWE maintains competitive downstream performance in both settings. Our code is available at this https URL.

---


### 190. [Structure Over Scale: Rethinking Adaptation for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2611.27148)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Allan Kazakov, Abdurrahman Javat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) is often framed as a choice between the expressivity of Full Fine-Tuning (FFT) and the efficiency of Low-Rank Adaptation (LoRA). We find that this framing misses an important variable: the geometry of the update. Under a common cold-start GRPO protocol, LoRA exhibits rank collapse: performance remains broadly stable at low rank, then fails abruptly as rank increases. On DeepMath-Hard, for example, accuracy drops from 73.1% at r=64 to 4.7% at r=128. In contrast, Weight-Decomposed Low-Rank Adaptation (DoRA) and Quantum-Informed Tensor Adaptation (QuanTA) remain stable over a wider tested optimization region and are competitive with FFT while updating less than 0.6% of the model parameters. Spectral analysis reveals a corresponding difference in learned update structure: collapsed LoRA concentrates its update energy into relatively few effective directions, whereas structured adapters produce substantially more distributed updates. These results suggest that nominal rank and parameter count alone are insufficient to characterize adaptation in RLVR - the structure imposed on the reachable update manifold also matters. Finally, across three 8B base models, adapter behavior aligns with both frozen-weight spectral structure and reported pre-training scale, motivating the Model Maturity Hypothesis: the adaptation geometry that works best may depend on properties already encoded during pre-training. We present this as a falsifiable hypothesis rather than a causal conclusion. The code can be found here this https URL

---


### 191. [cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction](https://arxiv.org/abs/2611.27193)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haowei He, Ziwen Zhao, Chenshuo Pan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Manifold-constrained Hyper-Connections (mHC) extends residual connections to multiple streams and stabilizes residual propagation by constraining stream-mixing residual matrices to the Birkhoff polytope, the set of doubly stochastic matrices. In this work, we investigate how to effectively mix residual streams within the Birkhoff polytope. We reveal a mixing trade-off: when under-mixed residual matrices stay close to the vertices of the Birkhoff polytope, hyper-connections will degenerate into a set of nearly independent streams; when over-mixed residual matrices are concentrated around the uniform barycenter of the polytope, streams will become less distinguishable from each other. We theoretically validate our findings by bounding the cumulative residual mixing, stream difference and gradient difference of mixing coefficients across layers. Motivated by these findings, we propose Contraction for Manifold-Constrained Hyper-Connections (cmHC), an exact doubly stochastic method which geometrically contracts the Birkhoff polytope toward its interior. This contraction mitigates under-mixing by forcing the residual matrices to explore deeper into the polytope, with a provable stream mixing bound and no new parameterization. Moreover, we apply a moderate contraction at the shallow layers to prevent over-mixing, enabling stable gradient propagation on extremely large-scale model pretraining. Extensive experiments across dense and mixture-of-experts models at various parameter scales demonstrate the effectiveness and scalability of cmHC. We also develop fused operators for cmHC on Ascend NPUs, reducing hyper-connection execution latency by up to 44.8%.

---


### 192. [InterBand-EMG: A Cross-Band Foundation Model for Generalizable Hand-Pose Estimation](https://arxiv.org/abs/2611.27289)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zongheng Guo, Tao Chen, Dalong Du 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surface electromyography (sEMG) enables continuous hand-pose estimation, but learning representations that generalize across users and movements remains challenging. We introduce InterBand-EMG, which combines band-specific quantization with cross-band reconstruction and structured masked code prediction to learn transferable EMG representations for hand-pose tracking. We also introduce SynapMyo, an eight-channel EMG-to-pose dataset comprising 1,227.74 hand-hours from 499 users across 68 movement categories. Experiments on emg2pose and SynapMyo show that InterBand-EMG outperforms state-of-the-art baselines in joint-angle accuracy across all three generalization settings on both datasets. The source code and the SynapMyo dataset will be publicly released upon acceptance of this paper.

---


### 193. [H-MSAE: Hierarchical Sparse Concept Coverage for Efficient and Diverse Instruction Data Selection](https://arxiv.org/abs/2611.27329)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bohan Cui, Jingyi Cui, Hongwei Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large instruction-tuning corpora contain substantial semantic redundancy, motivating the selection of compact subsets that preserve useful supervision while reducing training cost. Existing diversity-aware selectors often rely on generated semantic tags and explicit graph structures, introducing considerable annotation and preprocessing overhead. We introduce H-MSAE, a hierarchical sparse instruction selection framework that organizes multi-resolution concepts learned by a Matryoshka sparse autoencoder into a coarse-to-fine hierarchy. Quality-weighted, diminishing-return coverage with ancestor propagation promotes high-quality and non-redundant semantic coverage, while pool-relative length constraints regulate subset composition. We motivate this design through a local quality-diversity analysis of subset SFT utility and examine it using example-quality and representation-space diversity diagnostics. On Tulu 3 data pool, H-MSAE achieves the highest Final Avg among the evaluated 50K selectors across scales and initialization. The selected subset also exhibits the highest mean quality and effective rank among the evaluated methods. By avoiding full-pool generative tagging and supporting efficient sparse selection, H-MSAE reduces measured end-to-end runtime by approximately $5\times$ relative to MIG.

---


### 194. [Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training](https://arxiv.org/abs/2611.27376)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhen Zhang, Changyi Yang, Xuehai He 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL post-training typically produces domain experts that must then be consolidated into one model, and as new experts keep arriving, this consolidation becomes a continual process. Weight merging and multi-teacher on-policy distillation (MOPD) must re-consolidate the whole model whenever an expert is added, and can erode capabilities outside the target domains. We propose Composable Soft-Prompt Distillation (CSPD), which keeps the pre-RL model frozen, distills each RL expert independently into a soft prompt, and composes experts by concatenating their prompts without joint training. A single soft prompt suffices to distill an RL expert, recovering at least 90% of the teacher's gain in 22 of 23 math, code, and agent settings. Independently trained prompts compose well. In a multi-expert setting, the average rises with every expert added, and the full composition matches MOPD (67.83 vs. 67.79). The composition generalizes best across six held-out benchmarks. Input-space adaptation adds little serving overhead, keeping throughput within 1.5% of the unadapted backbone and reaching 2.40x that of rank-4 LoRA. These results point toward continual post-training on a fixed backbone.

---


### 195. [Detecting Word-Substitution Poisoning of a RAG Knowledge Base with Relative Entropy and Runtime Verification](https://arxiv.org/abs/2611.27410)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ali Yousefi, Nikos Komninos, Hafizul Asad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A retrieval-augmented generation (RAG) system answers questions using passages it retrieves from a knowledge base, so users must trust that knowledge base. We study an attacker who quietly edits existing passages by swapping words for synonyms (PWWS, TextFooler) in a cybersecurity RAG system built from MITRE ATT&CK and CAPEC. Using a reviewed 44-question benchmark, repeated paired runs and a control corpus in which only the layout changes, we find that poisoning lowers judged answer correctness from 0.714 to 0.555. The damage comes mostly from lost evidence and refusals, not from false statements. To find the edited passages, we use relative entropy. Comparing a whole passage with normal text is a weak signal. Still, one term of the relative entropy, the log-ratio between a word and its most probable synonym, works well: with a small language model as the reference, it reaches an AUROC of 0.95 and stays near chance on the control. Used as a retrieval filter, it halves how often edited text reaches the generator, and an attacker who must keep each passage as probable under the language model fails on all 57 sections it tries. Filtering does not restore correctness, because the edited passage is usually the one that held the answer. We therefore add a runtime monitor that checks each answer against trusted MITRE STIX data and remembers the passages it rejects. On its own, it reduces exposure to edited text from 0.41 to 0.26; when it may add the trusted MITRE entry as a source, correctness rises to 0.786. We report the costs and failure cases of every defence alongside its gains.

---


### 196. [Poisoning Attacks and Collaborative Defense Framework for LightRAG-Based Construction Regulation Knowledge](https://arxiv.org/abs/2611.27460)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yingyan He  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is widely used in construction, yet the security of building-regulation knowledge bases has received little study. This thesis reports a pre-registered experiment on one fully instrumented LightRAG system built on the UK Approved Documents. Using a 150-item benchmark labeled with safety consequences and tampering directions, it evaluates four attacks (text layer, graph layer, fabricated amendment narrative and a defense-aware adaptive attacker) together with a three-layer retrieval-graph-generation defense in a full factorial design. Text-level poisoning succeeded, with success rising with the budget; graph-level poisoning was less effective, contrary to the registered hypothesis. The full defense met the registered criterion and six of the seven configurations met its threshold, but those containing the generation layer did so by refusing 69-80 percent of poisoned queries, costing up to 74 points of clean accuracy, whereas provenance-based retrieval filtering cost no measurable clean accuracy in the configuration used. A second experimental batch showed that excluding a legitimate unregistered amendment caused no measurable loss of accuracy either, as its wording reached the generator through the graph's entity and relationship descriptions, the route the poison took, which no layer inspects. Interactions were strong, so no layer's contribution can be isolated. A reported zero attack success rate is not evidence of detection unless the refusal rate is reported with it: zero arises either because provenance filtering removes every document outside the manifest without judging its content, or because the system refuses. Layered defenses must therefore be evaluated factorially, and regulatory RAG assistants require corpus admission control and version-aware verification before they can support safety-critical decisions.

---


### 197. [Typhoon OCR 2: From Thai Document Transcription to Multilingual, Multi-Task OCR](https://arxiv.org/abs/2611.27494)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Surapon Nonesung, Natapong Nitarach, Sittipong Sripaisarnmongkol 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typhoon OCR 1.5 focused on reading Thai documents. However, in real-world workflows, users often need to extract specific information or preserve the structure of an entire page for further processing. Typhoon OCR 2 handles both tasks in a single model, with prompt-driven extraction and structured full-page parsing. Full-page parsing covers Thai, English, and Chinese. We release compact 2B and 0.8B models adapted from open document parsers through supervised fine-tuning on curated Thai and public multilingual data, followed by Group Relative Policy Optimization (GRPO) with task rewards and a rule penalizing unfinished responses. Among evaluated open models, Typhoon OCR 2 2B scores highest on Thai MDPBench (80.7 versus 68.9 for Typhoon OCR 1.5) and on ThaiOCRBench (59.91 versus 40.45), which covers recognition, extraction, and document understanding. The 2B model remains close to its base on English olmOCR-bench (84.7 versus 84.4) and on OmniDocBench, which evaluates English and Chinese together (90.97 versus 91.03). On MDPBench, GRPO reduces the mean share of pages with repetition loops for the 2B model from 3.2% to 0.7%, with a smaller and statistically uncertain score gain for the 0.8B model. We release the model weights, Python package, and evaluation suite.

---


### 198. [EchoAlign: Echocardiography foundation model with multilevel report alignment](https://arxiv.org/abs/2611.27517)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ahmed Aly, Darya Taratynova, Lotfi Abdelkrim Mecharbat 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Echocardiography assesses the structure and function of the heart. Cardiologists read each study across several standard views and report the findings visible in those views by cardiac structure. AI foundation models can learn to analyze these studies from clinical reports, reducing annotation burden and supporting clinical interpretation. However, existing models are trained by pairing each video with the full clinical report, including structures and findings its view does not show. This mismatch lets a model associate a finding with incidental or spurious signals rather than its visual evidence, which limits accuracy, anatomical grounding and clinical trust. Here we introduce EchoAlign, a vision-language foundation model developed on 2.87 million echocardiographic videos and images from 159 clinical centers. EchoAlign aligns each cardiac structure, video and study with its report text, and a visibility matrix restricts supervision to the views that actually depict each structure. We compare it with five public foundation models on 0.47 million test videos across ten unseen external datasets from more than 25 clinical centers. EchoAlign achieves the highest mean AUROC of 0.890 (95% CI, 0.881 to 0.897) for classification and the highest mean quadratic weighted kappa of 0.530 (95% CI, 0.511 to 0.544) for severity grading. Across 62 clinical findings, EchoAlign provides one model that detects findings, grades their severity, estimates measurements and segments cardiac structures.

---


### 199. [Adapting AI Weather Foundation Models to a Changing Climate](https://arxiv.org/abs/2611.27605)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinlei Xiong, Wenbo Hu, Shuxun Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI weather foundation models learn from historical archives, while the climate distribution encountered during deployment continues to evolve. This growing model--climate mismatch motivates continual adaptation without repeated full-model retraining, but the structure of weather forecast errors determines how such adaptation should be performed. We develop an online adaptation framework that exploits two complementary error structures: geographically persistent biases and flow-dependent errors that vary with the atmospheric state. Analysis of Aurora-1.3B reveals strongly concentrated forecast-loss sensitivity in its decoder, motivating flow-dependent corrections within fixed low-dimensional sensitivity subspaces. A residual memory tracks persistent errors remaining after this correction, while a variable-wise online gate controls the contribution of the persistent component. We evaluate Aurora-1.3B using ERA5 from 1959--1968 for offline initialization and a strictly chronological 1969--2022 stream for online evaluation, with updates restricted to previously available verification targets. For 2-metre temperature, distributional departure from the historical reference, measured directly from ERA5, is associated with larger frozen-model errors and greater adaptation gains, while the adapted model maintains more stable skill across evaluation periods. Across 69 output fields and five lead times from 6 to 72 hours, our method reduces MSE and MAE by 6.90\% and 6.45\%, respectively, relative to $\delta$-Adapter, the strongest of six online adaptation baselines.

---


### 200. [Interpretable Tissue Architecture Complements Pathology Foundation Models](https://arxiv.org/abs/2611.27881)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zeeshan Shahid, Hammam M. AlGhamdi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tissue architecture provides important information for histopathological assessment, yet its complementary predictive value alongside pathology foundation-model representations remains insufficiently understood. This study investigates whether interpretable measurements of cellular and multicellular tissue organization provide additional predictive information beyond learned representations. We introduce a 139-dimensional cellular-to-community representation comprising nine feature groups characterizing nuclear morphology, cellular composition, spatial connectivity, community organization, and cell-cell interactions. Their predictive contributions are systematically evaluated independently and through feature-level fusion with CTransPath and PLIP embeddings using multiple-instance learning (MIL). On the BCNB dataset, estrogen receptor (ER) and progesterone receptor (PR) classification is evaluated across four MIL architectures using five-fold patient-disjoint cross-validation. Selected CTransPath fusion configurations achieved mean ROC-AUC values of 0.9144 (ER) and 0.8360 (PR), while PLIP fusion achieved 0.8791 and 0.8015, respectively. Patient-level analyses identified ER-associated differences in nuclear morphology, graph connectivity, cellular communities, and cell-cell interactions. On LungHist700, selected fusion configurations achieved higher mean ROC-AUC across four classification tasks, including adenocarcinoma versus squamous cell carcinoma (0.7967 versus 0.7137 for CTransPath alone). Overall, these findings suggest that interpretable tissue-architecture descriptors can complement foundation-model representations while providing measurable insights into histopathological organization.

---


> [!TIP]
> 当前位于：**151-200**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
