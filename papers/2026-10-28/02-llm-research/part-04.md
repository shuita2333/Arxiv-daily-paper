# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

---

### 151. [HerHealthGPT: An Evidence-Grounded Conversational AI System for Women's Reproductive Health Copy title](https://arxiv.org/abs/2610.33931)

**<font color=#1a73e8>作者：</font>** Hassan Saeed Hassan Albattra, Mazen Mohammed Bahgat, Rahatara Ferdousi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> "Why is my period late?" Sometimes, the most useful response begins with another question. Yet conversational AI systems may respond to incomplete health queries without seeking essential context or grounding their guidance in verifiable evidence. This paper introduces HerHealthGPT, an evidence-grounded conversational AI system designed to address these challenges in women's reproductive health. HerHealthGPT integrates retrieval-augmented generation (RAG), context-aware clarification, and source validation within an interactive web interface. Rather than responding immediately to incomplete queries, the system maintains conversational context, asks targeted follow-up questions, checks for premature conclusions, and grounds its responses in retrieved evidence. We evaluate the AI components using 540 English messages derived from 90 reproductive-health cases and conduct a prototype questionnaire study with 30 adults. Evidence retrieval improves concern-category accuracy from 54.1% to 59.3% compared with fine-tuning alone. The clarification router achieves 85.6% recall and 86.2% specificity on constructed targets. In the user study, 83.3% of participants preferred the retrieval-enabled configuration, while 25 of 30 considered its follow-up questions relevant. These findings suggest that integrating evidence retrieval with interactive clarification offers a promising approach to more transparent, context-aware reproductive-health information systems, while further clinical validation remains necessary.

---


### 152. [What Makes a Question Curious? Measuring Model Curiosity in Human-LLM Interactions](https://arxiv.org/abs/2610.33950)

**<font color=#1a73e8>作者：</font>** Angana Borah, Rachana Ramchandar, Inderjeet Nair 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly act as partners in everyday communication. In these interactions, useful assistance may require not only answering, but also asking the right questions that surface knowledge gaps, assumptions, and alternatives. In this study, we refer to such epistemic question-asking as model curiosity, and introduce a theory-grounded taxonomy that distinguishes curiosity-oriented questions from generic model questioning. Across four conversation datasets, we find that curiosity-oriented questions remain rare (17-28% of all questions), but are associated with more exploratory and epistemically rich subsequent user responses, with varying patterns across datasets. We further conduct a human study to evaluate the usefulness of model curiosity, finding that curiosity can encourage exploration, especially in advice, creative, and research contexts. These findings have implications for building LLMs that ask more selectively to support deeper exploration and human-AI collaboration.

---


### 153. [Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents](https://arxiv.org/abs/2610.33956)

**<font color=#1a73e8>作者：</font>** Haoyu Zhao, Sitian Tu, Yuxuan Huang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning is the ability of LLM agents to improve over time by acquiring, refining, and applying knowledge from experience while retaining useful prior knowledge. It is essential for agents learning over long time horizons, yet current evaluations largely assess individual task performance rather than improvement through accumulated experience. We introduce Continual Learning Exam (CLE), a large-scale benchmark developed by 50+ domain experts to measure experience-driven improvement in realistic professional workflows. CLE comprises 120 human-authored tasks, each organised as a five-level ladder, yielding 600 levels spanning 89 professional roles across 12 occupational domains. Agents must pass each level to unlock the next, with later levels building on experience accumulated during earlier assignments. An evaluation agent assesses each submission against human-authored rubrics. We compare a single-submission setting with one that provides diagnostic feedback after failure and allows one revision. Across 17 harness-model configurations using frontier LLMs, feedback and revision yield a median completion gain of 5.3 percentage points. Yet the best-performing system clears only 47.7% of levels and completes all five levels in just 23.3% of tasks, highlighting the difficulty of sustained learning from experience for existing frontier LLMs. As such, the dataset can also be used to post-train LLMs to strengthen their continual learning capabilities.

---


### 154. [Beyond Belief: Evaluating and Mitigating LLM Susceptibility to Misinformation](https://arxiv.org/abs/2610.33962)

**<font color=#1a73e8>作者：</font>** Emran Kanaan, Jiho Lee, Ibrahim Odat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-using large language models (LLMs) must decide whether external information warrants action. We investigate whether their expressed credibility judgments reliably indicate behavioral resistance to misinformation. We evaluate five LLMs on 196 constructed false notices paired with legitimate counterparts and 204 archived attacks adapted to simulated tool use. When asked to act on the constructed notices, models issue harmful tool calls in 27%--99% of cases they have rated untrustworthy. Removing the preliminary rating step increases harmful execution by 15 percentage points on average, showing that credibility elicitation itself changes the behavior being evaluated. Interventions that improve credibility discrimination do not consistently yield safer actions. A simple forewarning significantly reduces harmful execution in four of five models, but neither tested generated-example prebunk outperforms it in the main evaluation. These reductions can also compromise legitimate task completion. Supervised fine-tuning on generated false notices reduces harmful execution on held-out archived attacks under the rating-first protocol, with model-dependent utility costs and weaker protection without rating elicitation. Our findings motivate evaluating misinformation defenses through both harmful actions and legitimate task completion, while accounting for the behavioral effects of the evaluation protocol.

---


### 155. [QECGBERT: A Scalable ECG Foundation Model Based on Self-Supervised Language Learning via VQ-VAE Waveform Tokenization](https://arxiv.org/abs/2610.33964)

**<font color=#1a73e8>作者：</font>** Aruna Mohan, Burcu Ozek, Or Zilbershot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI foundation models play a pivotal role in advancing heart disease diagnosis from electrocardiogram (ECG) data, particularly for rare diseases where the lack of sufficient labeled data hinders supervised learning. However, most self-supervised learning methods treat ECGs as generic sequence or image data without exploiting underlying physiological structure. To address this limitation, we propose QECGBERT, a self-supervised ECG language model that explicitly encodes physiological semantics by tokenizing the P, QRS, T, and isoelectric background waveforms. Vector-quantized variational autoencoder (VQ-VAE) tokenization is applied to each 12-lead ECG, with tokens enriched by continuous waveform features to preserve morphology lost during quantization without increasing sequence length. This design enables compact BERT masked language modeling with short sequences, improving scalability and reducing computational cost relative to long-sequence approaches. QECGBERT applies BERT pre-training to the MIMIC-IV dataset containing over 800,000 unlabeled ECG recordings, and fine-tuning on labeled PTB-XL, CPSC2018, and Chapman--Shaoxing--Ningbo datasets for evaluation. The results demonstrate that QECGBERT achieves comparable or superior performance to published benchmarks, offering a scalable, physiologically aware approach to ECG foundation modeling for cardiac diagnosis.

---


### 156. [InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants](https://arxiv.org/abs/2610.33966)

**<font color=#1a73e8>作者：</font>** Qinsi Wang, Wei Wen, Chong Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People have long dreamed of an assistant that is always there to guide them and remind what they forget, from new dishes to lost keys. Powered by multimodal large language models (MLLMs), egocentric AI assistants on wearable devices are bringing this dream within reach: they see what the user sees and give instructions for user's physical work when necessary. However, testing such assistance is challenging and usually requires real people. The expensive and rare real interaction data leaves a key question unanswered: Can today's MLLMs truly help people in physical world? To answer this question, we propose InteractiveWorld, the first verifiable environment for closed-loop interaction between human and AI assistant. Unlike existing robot-centric simulators, InteractiveWorld lets the assistant guide a human agent who observes the scene, understands instructions, and acts independently. It thus realistically simulates how AI assistant collaborates with human: the assistant instructs, the human acts, and the environment executes actions and updates what they see next. Building on it, we introduce InteractiveBench, the first dynamic benchmark for egocentric AI assistants, with 120 multi-turn tasks across six categories. In each task, the assistant guides the human in real time, and every instruction shapes the outcome, which is scored by verifiable, state-based rewards. Experiments with 12 frontier MLLMs show they are still far from reliable assistants. Even the strongest model, Claude Fable 5.1, achieves at most 20% and 25% on long-horizon Guidance and Planning tasks, respectively. Overall, our work offers a verifiable platform and a rigorous evaluation set, laying a solid foundation for research on interactive MLLM assistants that truly help people in the physical world.

---


### 157. ["High-Quality" Data for Early-Stage Instruction Tuning: An Empirical Study of Data Quality Metrics](https://arxiv.org/abs/2610.33969)

**<font color=#1a73e8>作者：</font>** Vladimir Necula, David Gvadzabia, Sofia Serrano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> "Data quality" is widely invoked in instruction tuning, but the term is often underspecified. We study it as an operational property by asking which simple example-level metrics, drawn from prior work on data selection, text quality, and instruction tuning, best predict training utility under a fixed finetuning budget. For each metric, we sort instruction-response examples by score, partition them into low, middle, and high bins with roughly equal token mass, finetune separately on each bin, and compare validation perplexity and LLM-as-judge scores for the models' generated answers as a function of cumulative training tokens. Our results suggest that answer-dense supervision, as captured by response ratio, is a stronger and more portable predictor of instruction-tuning utility than commonly used alternative proxies.

---


### 158. [Detecting and Understanding Ambiguity in Visualizations with Role-Playing Vision Language Model Interpretations](https://arxiv.org/abs/2610.33997)

**<font color=#1a73e8>作者：</font>** Garrick Chan, Yun-Hsin Kuo, Sam Yu-Te Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Communicative visualizations can support multiple chart-grounded takeaways, including divergent or conflicting ones; we refer to this variation as interpretive ambiguity. Such ambiguity can undermine a visualization's communicative goal when the supported takeaways diverge from its intended message. Evaluating visualizations with target audiences can surface this variation, but such evaluations can be costly and difficult to scale. In this work, we explore persona-conditioned Vision Language Models (VLMs) as a complementary evaluation tool for interpretive ambiguity. For a given visualization, our pipeline uses topic-relevant personas to elicit candidate contextual takeaways supported by interpretations of perceived visual patterns, such as trends and clusters. We derive a Target--Pattern--Scope framework for comparing these interpretations, use LLM judges to assign Compatible, Disjoint, or Opposing ambiguity labels to statement pairs, and summarize their distribution in an ambiguity profile. To improve chart grounding, we benchmark candidate VLMs on chart comprehension and select the highest-performing model for each chart type. We evaluate statement-pair labeling against human-authored annotations and apply the approach to real-world, public-facing visualizations curated from established datasets. Through case studies, we examine how perceived visual patterns relate to contextual takeaways and how a visualization redesign changes the sampled interpretations. Our findings show how persona-conditioned VLMs can complement human feedback by generating candidate contextual takeaways and surfacing potential ambiguity for further inspection.

---


### 159. [Fed-Universe: A Semantic-Geometric-Topological-Human (S-G-T-H) Stack for Negotiated Alignment in Federated Systems](https://arxiv.org/abs/2610.34009)

**<font color=#1a73e8>作者：</font>** Ting Xu, Henry Leung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional federated learners implicitly optimize for global means, creating a "one-size-fits-all" paradigm that inevitably suppresses the minority under cross-site heterogeneity. To bridge this critical gap, we present Fed-Universe, a generalizable Semantic-Geometric-Topological-Human (S-G-T-H) architecture that transforms passive averaging into an active negotiation for decentralized alignment. The S-layer deploys an edge-capable LLM as a semantic surrogate to translate heterogeneous inputs into standardized patient profile prompts. The G-layer enforces geometric quality assurance (GQA) via a mapping f: Theta -> Q from the statistical parameter space to a physically interpretable quality domain, employing a cosine similarity gate to retain minority updates based on physical geometry rather than statistical proximity. The T-layer executes topological Pareto control, identifying a sensitivity-based knee point (lambda_k) to balance multi-objective aggregation without majority degradation. Finally, the H-layer operationalizes a cognitive twin dynamic to mirror the user's real-time psychological state, dynamically adapting human-computer interaction modes via active intent alignment. To ground this theoretical architecture empirically, we validated the S-G-T core on a binational synthetic clinical network simulation. This proof-of-concept demonstrated a "zero-sum escape": a minority node (<3% data volume) achieved utility parity (loss reduction from 0.857 to 0.340) alongside dominant hubs. Our Fed-Universe framework is being expanded along two focused pillars: institutional multimodal alignment (Fed-Ultra) and individual cognitive intent alignment (Fed-Human).

---


### 160. [Reversible Pseudonymisation of Documents Sent to External LLMs: an Open Bilingual Benchmark and an Engine](https://arxiv.org/abs/2610.34012)

**<font color=#1a73e8>作者：</font>** Vladimir Beskorovainyi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Professionals send working documents to external large language models. A common safeguard is reversible pseudonymisation: personal data are replaced with placeholders before the request and restored locally in the answer. We present an open benchmark of five existing open tools and a regular-expression baseline on Russian and UK English, and an open engine built on the two strongest tools. The benchmark excludes each tool's own authors' dataset from its verdict, compares the engine with each tool on identical datasets for detection, reports masking precision, and tests on a held-out set of synthetic documents whose files, hashes, decision rules, run plan and stopping rule were published before any run. Two local LLMs test whether placeholders survive. All evaluation data are synthetic, and the benchmark was run by the author of the engine; code, data, predictions and raw answers are released. On external datasets no existing tool meets all predefined thresholds: in UK English the identifier and leak thresholds are not met, in Russian the identifier threshold is borderline. On the last held-out set of 1,000 documents per language, the best existing tools leave a whole value visible in 61% (Russian) and 58% (UK) of documents. On these documents, from the generator it was developed on, the engine does so in 0.3% [0.1; 0.9] and 0.2% [0.1; 0.7], leaves any part of a value visible in 0.8% and 0.2%, and meets all detection thresholds in both languages. In UK English it also restores at least 99% of its placeholders after 760 answers. In Russian it restores only 94.6% [93.6; 95.6] of name placeholders, against a 99% threshold, mainly because the inflection it borrows from pii-guard produces wrong surname forms. The engine was developed over six earlier held-out sets from the same generator; real documents were not tested.

---


### 161. [BriLLM-MetaPred: A Representation-Prediction Unity Language Model with Adaptive Self-Measurement](https://arxiv.org/abs/2610.34018)

**<font color=#1a73e8>作者：</font>** Junyuan Liu, Hongyue Lin, Jiale Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present BriLLM-MetaPred, the first engineering implementation of the MetaPred machine-learning framework established by a mathematical theory of AGI, instantiated for language modeling. The theory argues that MetaPred is both necessary and sufficient as a machine-learning primitive for general cognition. Taking this theoretical conclusion as a design premise, we report an implementation of the primitive for language modeling. A single continuously evolving dynamical state serves as both the context representation and the state from which predictions are read out. Continuous measurement of its own state reduces finite-depth inconsistency, maintains internal consistency, and provides an endogenous dynamical self-supervision signal in fixed-point form. The single dynamical state of MetaPred intrinsically couples training and inference. MetaPred therefore exhibits symmetry across almost all key elements of machine learning, an intuitive and observable property of the mathematical optimum over the space of all machine-learning paradigms. BriLLM-MetaPred is neither another recurrent language model nor an extension of BriLLM. It provides a bridge between two prior contributions: the construction and motivation of the MetaPred primitive provided by AGI theory, and the SiFu learning paradigm provided by BriLLM (Zhao et al., 2025). The latter's node-signal-flow design enables the primitive to run on available software and hardware accelerators. Our implementation of BriLLM-MetaPred achieves predictive performance comparable to a GPT baseline of the same size. This provides initial evidence for the engineering feasibility of the MetaPred framework established by the mathematical theory of AGI. MetaPred is the first machine-learning paradigm derived entirely from mathematical theory rather than assembled and incrementally improved through human design---and perhaps the last such paradigm.

---


### 162. [When Does GEPA Merge Help? A Mechanism-Level Diagnostic](https://arxiv.org/abs/2610.34027)

**<font color=#1a73e8>作者：</font>** Chong Zhao, Ruyi Yang, Changming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GEPA is among the strongest reflective prompt optimizers for language-model programs, but its system-aware merge operator is unstable across models: merge improves gpt-4.1-mini on average while degrading Qwen3-8B, an asymmetry noted but left unexplained by the GEPA paper. We investigate this instability across five datasets and two models. Our nine-configuration sweep over merge timing and merge operator shows that merge can improve both models when configured appropriately. This suggests that merge instability is better explained by configuration sensitivity than by an inherent flaw in the merge operator. We then test whether prompt-level features predict GEPA's merge-accept decisions and find that they do not, ruling out static-feature gating. As a proof of concept, a behavior-based probe built from these diagnostics avoids large merge failures in our multi-seed runs by abstaining on high-risk tasks, although it does not consistently outperform NoMerge. Code is available as GEPA-MergeProbe at this https URL .

---


### 163. [Explaining Navigation Decisions: Stage-Aware Visual Attribution for Vision-Language Navigation](https://arxiv.org/abs/2610.34028)

**<font color=#1a73e8>作者：</font>** Yiyuan Yao, Xinpeng Ding, Minglei Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Vision-Language Models (VLMs) increasingly enable robots to follow language instructions, understanding their navigation decisions becomes important for reliable deployment. Existing explainability methods overlook a key challenge in Vision-Language Navigation (VLN): evidence for the current action may be distributed across historical and current observations and associated with different instruction stages. We identify instruction-stage insensitivity, where existing methods produce similar explanations despite changes across different navigation stages. To address this issue, we propose a stage-aware attribution framework for VLN. We first construct action-conditioned temporal instruction--visual attributions across observations. These attributions are projected into instruction space to estimate stage associations, which guide the aggregation of relevant historical evidence for refining the current explanation. An instruction-guided spatial filter further suppresses isolated responses while preserving compact, instruction-relevant regions. Experiments across multiple VLN policies and benchmarks show improved attribution quality over existing methods. We further demonstrate that our method acts as a diagnostic tool for analyzing failure cases, and validate its applicability to real-world navigation on a Unitree G1 robot.

---


### 164. [Fovea-JEPA: Overcoming Geometric Blind Spots in V-JEPA for Camera Motion Recognition](https://arxiv.org/abs/2610.34033)

**<font color=#1a73e8>作者：</font>** Xiangkun Shi, Hanhui Li, Shiyue Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera motion recognition requires separating viewpoint changes caused by camera translation, rotation, or zoom from object motion and scene dynamics. Video-language models often rely on semantic cues and struggle with the geometric evidence needed for this task. Joint-Embedding Predictive Architectures such as V-JEPA offer strong spatio-temporal representations, but our experiments suggest that they underrepresent geometric cues in some regions. Under temporal-reversal supervision, V-JEPA improves overall but degrades on several motion families, whereas a weaker geometry-oriented VGGT predictor improves across all families. We refer to these geometrically underrepresented regions as geometric blind spots and propose Fovea-JEPA to identify and address them. Using V-JEPA as the base model and VGGT as a geometry expert, we construct intervention pseudo-labels from their prediction errors to weakly supervise a blind-spot predictor. The predictor produces token-wise response maps, which are aggregated into a clip-level intervention score to guide adaptive fusion of visual and geometric features. This selective intervention introduces complementary geometric information while preserving reliable visual predictions. Experiments on CameraMotionDataset, CameraBench, and ShotBench demonstrate the effectiveness of Fovea-JEPA, with gains of 9.67, 8.67, and 24.38 percentage points over previously reported state-of-the-art baselines, respectively. Code and models will be released upon acceptance.

---


### 165. [What Sketches Tell Us about LVLMs: Conventions, Grounding, and Localisation](https://arxiv.org/abs/2610.34037)

**<font color=#1a73e8>作者：</font>** Chaitat Utintu, Ahmed Bourouis, Arkaprabha Basu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LVLM benchmarks tell us whether a model answers correctly, but not which visual conventions it has retained, nor where those conventions live. Sketches expose this hidden structure. A sketch removes texture, lighting, and photographic context while preserving the strokes humans judged sufficient for recognition. If an LVLM can operate on that abstraction, the surviving signal is structural rather than merely photometric. We introduce a training-free sketch probe with three readouts: temporal part-construction order, spatial attention-based grounding, and the mechanistic layer/head locus of grounding. We evaluate nine LVLMs on part order and five on the attention readouts, over two part-annotated sketch datasets. Three findings emerge. First, LVLM part order tracks human convention: models reproduce canonical orderings where human drawings converge, and become correspondingly variable where human orderings vary. Controls that blank, withhold, and mismatch the sketch locate this convention in the language model. Second, part-level grounding survives the abstraction: attention heads selected from the frozen model with an existing recipe recover part and object regions on object and scene sketches, with no grounding supervision. Third, the grounding signal concentrates in a narrow mid-network band whose location follows the base language model rather than parameter count in the two families we compare, and remains stable across object and scene sketches. The result is a practical diagnostic for sketch-driven LVLMs: no fine-tuning, no auxiliary segmenter, and a layer band that doubles as a head-selection prior, matching or improving grounding mAcc@0.1 in every model and dataset we tested.

---


### 166. [INTRA: Interleaved Non-contiguous Token spaRse Attention](https://arxiv.org/abs/2610.34056)

**<font color=#1a73e8>作者：</font>** Yuxuan Xia, Wenbo Lu, Shaoyi Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers achieve strong performance across modalities but are bottlenecked by the quadratic cost of attention. Sparse attention can reduce this cost, but effective sparsity must preserve useful long-range communication and map well to GPU hardware. We introduce INTRA--Interleaved Non-contiguous Token spaRse Attention--a hardware-aware static sparse attention design based on a relay-communication view under Computational Query Set (CQS) constraints. Rather than directly covering all token-to-token interactions within each sparse layer, INTRA uses complementary sparse groups to provide short mediated communication paths across layers. Scatter forms relay groups that sample broadly across local neighborhoods, while Gather reconnects these groups in subsequent layers. Under a partition model, this structure guides CQS-compatible sparse patterns with global reachability. Our CQS-aware FlashAttention-style kernel computes structured indices at runtime, loads selected non-contiguous tokens, and packs them densely for computation. On an A100, INTRA achieves a $1.53\times$ speedup in $2K$ FLUX.1-dev generation, with better measured image quality than evaluated CLEAR configurations after LoRA self-distillation. On LLaMA-3.1-8B, it improves long-context prefill efficiency with strong teacher-forced retrieval performance under matched LoRA adaptation. Attention-only benchmarks further show up to $8.4\times$ and $10.4\times$ speedups over MoBA and density-constrained NSA, respectively.

---


### 167. [Memory Tax: Dissecting the Net Value of Agent Memory](https://arxiv.org/abs/2610.34073)

**<font color=#1a73e8>作者：</font>** Xuan He, Sining Zhoubian, Ruozhen Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems underperform naive RAG in many cases, indicating a negative net value. Taking RAG as a reference, we dissect the net value of memory into the gains and losses over direct retrieval, termed memory benefit and memory tax. These gains and losses arise because memory process changes how the raw information is organized and accessed. We view such changes as the double-edged deviations from the raw history. They are originally designed and introduced to benefit the task, for example by reorganizing facts or distilling preferences, but some may also remove or obscure evidence, giving rise to memory tax. Since memory benefit reflects the expected gains of its design, we then focus more on the overlooked memory tax, study how it arises from the system and evaluation side, and generalize the concept to more application scenarios of memory. We hope the notion of memory tax can provide a new lens and shift more attention from standalone performance to the net value of memory, informing more reliable memory designs and evaluations. We will open-source the code and results to the community. Project Page: this https URL

---


### 168. [The LALA Benchmark: Evaluating Literary and Linguistic Analysis in LLMs](https://arxiv.org/abs/2610.34080)

**<font color=#1a73e8>作者：</font>** Michael Foster, Barbara McGillivray, Gard B. Jenset 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the Literature and Linguistics Analysis Benchmark (LALA), comprising 236 open-ended questions written by experts in linguistics and literary studies, together with expert-provided ideal answers. By comparing models within families and at similar training scales using human and LLM judges, LALA identifies differences in linguistic competence associated with post-training, offering a framework for evaluating future models and guiding targeted improvements. We administered questions to 17 language models and evaluated their responses using both human expert assessment and two LLM evaluators, Sol and Qwen. Base models displayed little of the linguistic competence assessed by the benchmark, whereas their post-trained versions performed markedly better, suggesting that post-training plays a central role in making linguistic knowledge accessible and usable. Parameter count, by contrast, showed no statistically significant association with partial-credit performance, and competencies remained unevenly distributed across linguistic domains. We interpret this pattern as evidence that post-training adds linguistic competencies piecemeal, without producing a general linguistic intelligence capable of extending them beyond the learned policies that support them. Models performed best on logical relations between statements and selected discourse-level tasks, while even the strongest post-trained models continued to struggle with ambiguity, literary style, reference, and misleading assumptions. Human and Sol evaluations produced nearly identical model rankings in both the original and ReliableEval runs, supporting the replicability of the comparative results.

---


### 169. [From Document Layout to Causal Topology: An End-to-End Architecture for Temporal Causal Reasoning](https://arxiv.org/abs/2610.34094)

**<font color=#1a73e8>作者：</font>** Zhifeng Yang, Wei Luo, Yongjian Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) generally lack deep causal reasoning capabilities in temporal reasoning. Inspired by document layout reordering, this paper proposes a paradigm shift from discrete narratives to causal topologies. It constructs two architectures: a training-free neuro-symbolic framework, temporal causal reasoning agent (TCR-Agent), which achieves interpretable causal deduction and counterfactual truncation through external causal graph instantiation and a symbolic intervention engine; and an end-to-end model, temporal causal reasoning former (TCR-Former), which internalizes these mechanisms into the Transformer attention space via a Causal-Topological Attention Mask and temporal span biases. Experiments on the TempoCausal benchmark demonstrate that TCR-Agent comprehensively surpasses existing training-free baselines. At the same time, TCR-Former achieves an accuracy 16.5% higher than that of state-of-the-art (SOTA) methods, outperforming large-scale models such as GPT-5.4 and DeepSeek-V3.2 with only approximately 8.6B parameters. Further analysis reveals a structure-reasoning disconnection phenomenon in existing methods: external symbolic constraints and chain-of-thought reasoning can improve reasoning steps, yet fail to enhance deep causal deductive capability. By internalizing temporal causal reasoning capabilities into the model, TCR-Former effectively bridges this gap, providing an efficient and reliable end-to-end foundation for complex reasoning scenarios.

---


### 170. [T2D: Target-to-Draft Model Pruning & Adaptation for Efficient Speculative Decoding](https://arxiv.org/abs/2610.34103)

**<font color=#1a73e8>作者：</font>** Shahriar Kabir Nahin, Xiao Ye, Muhao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding significantly accelerates autoregressive text generation in Large Language Models (LLMs), but its efficacy depends largely on two key factors: the distributional alignment between the draft and the target model, and the draft model's latency during inference. However, existing approaches typically utilize independently pretrained small draft models or seek to prune the target model to a manually chosen architecture, thereby failing to explicitly balance the trade-off between draft model alignment and token generation efficiency. To address this gap, we formulate draft model design as an optimization problem and propose T2D, a framework that constructs draft models directly from the target model using latency-aware structured pruning and knowledge distillation. In this manner, T2D obtains draft models that are jointly optimized for both measured inference latency and cross-entropy loss on the target model's responses, resulting in superlative speculative decoding performance. Through extensive experiments on multi-domain speculative decoding benchmarks and across several target model families of differing scale, we demonstrate how T2D prunes up to 92\% of the target model to obtain highly performant draft models compared to competitive baselines. Moreover, draft models obtained via T2D can also be utilized by other speculative decoding token-alignment and knowledge distillation methods in a plug-and-play fashion, leading to further gains. Our findings underscore the importance of jointly navigating the draft model architecture-alignment frontier to unlock the full potential of speculative decoding for LLMs.

---


### 171. [Can LLMs Trust Appropriately? Evaluating Calibrated Reliance on Imperfect Partners](https://arxiv.org/abs/2610.34107)

**<font color=#1a73e8>作者：</font>** Mengdi Chu, Jintao Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly collaborate with humans and peer AI agents whose contributions may be incomplete, inconsistent, or incorrect. Effective collaboration requires calibrated trust, whereby decisions to rely on, verify, or assist a partner adapt rationally as empirical evidence accumulates. We investigate whether models translate partner evidence into appropriate reliance policies. We introduce a benchmark of 324 scenarios across 23 collaboration categories. Each scenario involves three sequential decisions with explicit transition dynamics, feedback emissions, and cost schedules, permitting exact analytical evaluation of choices against their expected consequences over the remaining interaction. Evaluating seven models alongside 36 controlled-history probes, we dissociate evidence sensitivity from normatively appropriate action. While the strongest frontier model approaches near-optimal decisions, other models exhibit recurring pathologies: procuring excessive safeguards, purchasing verification tests with zero expected value of information, prioritizing immediate savings over cooperative learning, and misallocating assistance to suboptimal channels. Supplying explicit posterior distributions resolves certain errors while introducing new failure modes. Calibrated trust in autonomous agents critically demands coupling empirical evidence with forward-looking decision utility.

---


### 172. [Self-Evolution Reasoner: Continuous Optimization via Policy-Intrinsic Exploration and Exploitation](https://arxiv.org/abs/2610.34137)

**<font color=#1a73e8>作者：</font>** Wenhang Shi, Yiren Chen, Zhe Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) enables large language models (LLMs) to continuously self-improve their reasoning capabilities. Compared to RLVR's scalar rewards, recent self-supervised on-policy distillation methods leverage denser supervision signals. However, both paradigms suffer from exploration bottlenecks, struggling to escape local optima when the policy fails to sample valid solutions. Relying on external demonstrations can bypass this issue; however, the off-policy nature hinders genuine self-improvement and the mismatched-distribution reasoning can not be fully exploited. In this work, we propose Self-Evolution Policy Optimization (SEPO), a framework that drives continuous reasoning capability evolution via guided exploration and in-distribution exploitation. Specifically, SEPO utilizes labels to elicit correct reasoning from the policy, unlocking the exploration potential. By treating current policy conditioned on this in-distribution reasoning as a self-teacher, SEPO distills the newly discovered solution back into the policy. Through this iterative cycle of policy-intrinsic exploration and exploitation, SEPO achieves robust and continuous capability evolution. Across scientific, tool-use, and complex logical reasoning domains, SEPO consistently achieves the best performance under identical training time or steps, demonstrating superior efficiency and convergence ceilings. Notably, SEPO maintains stable improvements even in scenarios where baselines severely underperform or fail entirely, such as on complex tasks or with small-scale models. Our code is available at this https URL.

---


### 173. [Rethinking Retrieval in the Long-Context Era: Training-Free Semantic Trees for Adaptive Context Construction](https://arxiv.org/abs/2610.34146)

**<font color=#1a73e8>作者：</font>** Zhe Xu, Tianhao Liao, Zhenqing Ling 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context language models can increasingly process entire documents, making full-context prompting a practical alternative to passage retrieval. However, greater capacity determines how much information a model can receive, but not which information best supports a query. This distinction motivates rethinking retrieval: when the full document already fits, can selecting and organizing its evidence improve answering? The challenge is to retain supporting facts and relations while keeping the context focused on the question. To reconcile these goals, we introduce \ours, a training-free framework that uses semantic abstraction to guide selection while retaining original text for answering. \ours constructs a reusable semantic hierarchy from the full document in a single generation, linking node descriptions to source spans. Given a query, structural--semantic scoring and fine-grained lexical attribution nominate shared source nodes; their union with ancestor context preserves structural relations and complete local text. Across four frontier answer models, \ours improves average QA-F1 by 1.72 points over full-context prompting on three LongBench tasks, surpassing the evaluated baselines on the four-model average while reducing answer-context length by 58.55\%. Our code is available at the $\href{this https URL}{repository}$.

---


### 174. [Humans in Space: Can MLLMs Construct Human-Centric Spatial Understanding via Active Exocentric Exploration?](https://arxiv.org/abs/2610.34149)

**<font color=#1a73e8>作者：</font>** Tianchen Guo, Tengyue Zhang, Chen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) excel at zero-shot reasoning, their spatial capabilities are primarily evaluated through static, passive observation. In complex, human-centric scenes, occlusion often hides crucial geometric evidence, and passive benchmarks force models to guess rather than recognize their own visual uncertainty. To bridge this gap, we introduce SATE-Bench, a novel interactive benchmark comprising 316 real-world scenes and 2,525 multi-turn QA pairs to evaluate visual self-awareness and active exocentric view-exploration. It combines a Passive multi-view control with an Active exploration setting, where models start from a severely occluded view and must iteratively query adjacent viewpoints until they gather enough evidence to fully ``sate'' the question, scored by a step-penalized efficiency reward. Evaluating state-of-the-art MLLMs reveals that they terminate exploration prematurely while reporting high confidence, and struggle with fine-grained 3D geometric tasks; matched-view controls further attribute the Active--Passive gap primarily to insufficient evidence acquisition. Moreover, fine-tuning with Group Relative Policy Optimization (GRPO) shows that rewarding view-seeking increases active exploration but lowers overall accuracy, as models over-explore and fail to fuse expanding multi-view contexts across turns. These findings indicate that scaling passive multi-view perception does not intrinsically yield active spatial reasoning, highlighting the need for models that know where to look, how to integrate what they see, and when to stop. Code and data are available at this https URL

---


### 175. [Execution Logs Sway VLM Judges of Robot Progress](https://arxiv.org/abs/2610.34151)

**<font color=#1a73e8>作者：</font>** Weiyan Zhao, Sunny Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models now grade robot videos, and text placed beside the frames can change their verdicts. On clips where the robot is losing progress, we add one log line saying the robot is making progress. Across Gemini, Qwen and GPT judges, this flips correct verdicts to progress 10 to 35 percentage points more often than a neutral line does. A one-line warning that the log may be wrong removes most of this effect. Selected fake "task complete" claims flip half of Qwen's correct verdicts, against a tenth for unrelated log lines. They have no detectable effect on Gemini.

---


### 176. [Last-Iterate Stationarity of Muon with Finitely Many Newton-Schulz Iterations](https://arxiv.org/abs/2610.34158)

**<font color=#1a73e8>作者：</font>** Ping Li, Vincent Y. F. Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has achieved strong empirical performance in large-scale language-model training, motivating a better theoretical understanding of its practical implementation. Unlike the idealized polar-factor update, practical Muon uses a fixed number of quintic Newton--Schulz iterations. Existing analyses mainly establish average- or best-iterate stationarity guarantees, leaving last-iterate convergence less understood. We study last-iterate gradient convergence of practical finite-step Muon on smooth, lower-bounded nonconvex objectives.
For deterministic gradients, we show that without input stabilization, Muon can cycle even on a smooth convex quadratic. With positive stabilization, we establish last-iterate gradient convergence for any fixed momentum coefficient below one and a sufficiently small constant learning rate, together with square-summability of gradients. For stochastic gradients, we first show that persistent bounded, unbiased noise can prevent convergence with fixed learning rates and momentum, even with positive stabilization. We then establish almost-sure and mean-square last-iterate gradient convergence by combining decreasing learning rates with increasing momentum under bounded-variance stochastic gradients. Finally, we construct a smooth counterexample showing that neither convergence theorem guarantees a pointwise polynomial rate. We further establish density-one convergence rates, guaranteeing polynomial gradient decay for all but a vanishing fraction of iterations.

---


### 177. [Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents](https://arxiv.org/abs/2610.34167)

**<font color=#1a73e8>作者：</font>** Jiaju Huang, Shaobin Chen, Xinglong Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language model agents are usually evaluated by whether they finish the user's task. That metric misses a common failure: an agent can complete the requested work while also taking an unauthorized side-effecting action, such as writing to the wrong object, expanding the scope of the request, or contacting an unintended recipient. We call this failure mode collateral damage (CD). We introduce SABench (Side-effect-Aware Benchmark), a benchmark of 201 email, calendar, and ticket tasks. Each task crosses one of four state structures (independent, dependent, externally reachable, cross-tool) with one of four trap families (ambiguity, mis-targeting, cascade harm, overreach), and each task has a deterministic trace-based oracle for both goal satisfaction and authorization compliance. Across 2,211 model-task pairs from 11 frontier LLMs spanning major commercial and open model families, 15.2% of all runs incur CD, with risk concentrated in ambiguity tasks (38.8% violation rate) while non-ambiguous traps average 8.4% CD. Among goal-satisfied runs, 12.8% still produce unauthorized writes. Cross-tool and dependent states have about twice the CD rate of independent states. CD rates vary by 4.7x across models at comparable goal rates, which suggests that task success alone is a poor proxy for safe tool use. The SABench task corpus is released at this https URL the traces, oracle, code, and analysis pipeline are released at this https URL.

---


### 178. [Freeze What Is Settled, Cache What Is Smooth: Spatial Freezing Keeps Step Caching in Its Low-Error Regime](https://arxiv.org/abs/2610.34177)

**<font color=#1a73e8>作者：</font>** Baiyan Li, Ganxuan Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editors built on diffusion transformers run tens of denoising steps. Training-free acceleration either reuses features across steps (step caching) or stops computing the regions an edit leaves untouched (region freezing), and the two have been combined before. We ask how a high speed-up target should be split between them. On Qwen-Image-2.1, freezing does more than remove tokens: it lowers the cost of every step, so the step cache can reach the same overall speed-up with a conservative threshold that keeps its error small. A per-step cost model fitted on development runs predicts held-out latency with a median error of 4.0% and reproduces the speed ceilings of the region methods we re-implemented (2.73$\times$ predicted vs. 2.70$\times$ measured for RegionE). Driving frozen tokens to the model's one-step $x_0$ estimate beats returning them to the reference image on every development sample, and in 90% of measured cases the composed error stays below the sum of the two individual errors. The resulting method, FreezePlan, keeps five full steps and gives the rest of the budget to TaylorSeer. On a pre-registered test split it runs 5.05$\times$ faster end to end at 29.8 dB PSNR to the original output, with no significant drop in a VLM judge score; TaylorSeer at 5.02$\times$ reaches 23.5 dB. The curve extends to 5.99$\times$ at 28.0 dB. Swapping in the region selectors of prior methods under our schedule lowers median PSNR by only 0.5--0.6 dB, which places the gain in the schedule and budget split rather than in the selector.

---


### 179. [Entropic Control for Homeostatic Optimization: Pre-empting Catastrophic Forgetting via Dynamic Feedback](https://arxiv.org/abs/2610.34182)

**<font color=#1a73e8>作者：</font>** Shangxi Wu, Xiaorong Yan, Xiaojun Meng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised Fine-Tuning (SFT) of LLMs suffers from catastrophic forgetting, and prevailing mitigation strategies struggle to reconcile the plasticity-stability dilemma. To address this, we propose Entropic Control for Homeostatic Optimization (ECHO), a closed-loop control framework. By decomposing the KL divergence, we identify output entropy as a dominant observable component of KL variation. This enables us to leverage entropy as a computationally efficient online proxy to monitor forgetting risks in real-time, bypassing expensive reference-model inference. Consequently, ECHO employs an elastic controller that dynamically modulates the gradient weight of replay data via a proportional control law, using deviations from the pre-trained entropic equilibrium as an error signal. Empirical evaluations across 0.6B to 9B parameter architectures demonstrate that ECHO lies on, and in several comparisons extends, the observed plasticity-stability frontier and maintains high operational robustness against varying data mixing ratios.

---


### 180. [R2A-Sales: A Policy-Atom-Matched Benchmark for Rule-to-Action Gaps in Goal-Directed Sales Agents](https://arxiv.org/abs/2610.34185)

**<font color=#1a73e8>作者：</font>** Yihua Qin, Jiajie Jerry Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based sales agents are often evaluated on static policy questions or task success, but deployment asks a sharper question: when a model can state a rule, will it choose compliant, tool-grounded actions under commercial pressure? We introduce R2A-Sales (Rule-to-Action), a policy-atom-matched benchmark for this question. Each item pairs a static probe with a multi-turn sales scenario sharing the same versioned policy atom, facts, evidence, behavioral constraints, and tool contract, so differences cannot be attributed to policy-content mismatch. In the interactive arm, a code-owned ledger verifies committed tool effects and terminal states; unsupported action claims receive no credit. We report static compliance $K$, grounded action compliance $A=\Pr(\text{safe terminal}\land\text{no hard violation}\land\text{non-echo})$, and the matched gap $G=K-A$. The frozen release spans three controlled Chinese-language sales domains, 24 policy atoms, 42 semantic cores, and 2,016 matched pairs. The confirmatory study audits 21,888 runs over 19 cores, covering eight backbones plus four Qwen3-8B prompt treatments (12 configurations). Static compliance is near ceiling $(K=89.9\%\text{--}99.1\%)$, yet eight-backbone action compliance is only $A=3.0\%\text{--}17.3\%$, giving $G=80.4\text{--}92.5$ percentage points. Since $A$ also requires safe termination, $G$ upper-bounds rule-to-action degradation rather than isolating pressure alone. No prompt-only treatment dominates all metrics. R2A-Sales shows that sales-agent reliability must be measured at committed action, not rule recital or task completion alone.

---


### 181. [Timing Matters Twice: When to Query and When to Skip in Flow-Matching On-Policy Distillation](https://arxiv.org/abs/2610.34191)

**<font color=#1a73e8>作者：</font>** Renye Yan, Junyi Zhan, Jikang Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) enables flow-matching models to acquire complementary capabilities from specialized teachers through supervision on student-generated trajectories. However, different evaluation dimensions, such as aesthetics and OCR accuracy, and different tasks, such as image generation and editing, emphasize different aspects of the denoising process, suggesting that their effective supervision may occur at different stages. Existing methods typically select supervision states from predefined timestep distributions, which may overlook these phase-dependent differences and incur unnecessary computational overhead. This motivates two critical timing decisions: when to adaptively query teachers for effective supervision based on the evolving generative process, and when to skip the remaining rollout to avoid redundant computation.
In this paper, we introduce PhaseOPD, a phase-aware query-and-skip framework that identifies generative phases online from revisions of predicted-clean latents, using existing student velocity predictions without additional model evaluations. For each task-assigned teacher, PhaseOPD selects a supervision state based on its phase preference and skips the unused rollout suffix once all query decisions are finalized, preserving the single-query velocity-distillation objective. On SD3.5-M, PhaseOPD executes only 5.56 of 16 rollout positions per local batch, reducing training time by 41.3% relative to DanceOPD while improving Aesthetic, GenEval, and OCR scores.

---


### 182. [SRA: Selective Residual Adaptation for LLM Reasoning Enhancement](https://arxiv.org/abs/2610.34199)

**<font color=#1a73e8>作者：</font>** Zhenxing Dou, Kun He, Mingyang Yi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation transfers reasoning capabilities from large language models to lightweight students. However, distilled small models still struggle with multi-step reasoning. We observe that the distribution divergences between teacher and student models along reasoning paths are highly sparse, and target tokens almost always fall within the student top-$K$ candidate set. Based on this finding, unlike approaches updating student backbones or requiring runtime teacher computation, we propose Selective Residual Adaptation (SRA), a plug-and-play framework that internalizes localized corrections. Concretely, SRA employs a Discrepancy Gate to identify divergence positions alongside a Candidate Residual Adapter for top-$K$ logit calibration to correct the mismatch. Theoretically, we establish error bounds ensuring strict sequence level performance gains. Across mathematical benchmarks on Qwen3 models from 0.6B to 4B, SRA consistently enhances distilled student models, raising average Pass@16 by up to 4.37 percentage points while preserving general capabilities.

---


### 183. [MatOS: An Agent Operating System for Materials Research](https://arxiv.org/abs/2610.34203)

**<font color=#1a73e8>作者：</font>** Dingyang Lyu, Jing Gao, Zhonghao Chang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Materials research relies on scattered and growing data, knowledge, and simulation tools, and a single study often spans multi-day workflows across literature analysis, computation, and experiment. Large language model agents can now retrieve materials data, operate simulation codes, and close design-synthesis-characterization loops with autonomous laboratories. However, extending these agents with new capabilities, keeping long-running tasks on track, and letting them learn from past tasks and user feedback remain difficult. Here we present MatOS, an agent operating system for materials research with three core components: (1) a layered scientific asset graph that organizes data, knowledge, tools, skills, roles, and workflows as reusable assets; (2) a stateful adaptive workflow that runs tasks as explicit execution graphs with scientific checks, so that they can be resumed and traced; and (3) evidence-driven asset evolution, which revises these assets from execution records and user feedback. On ResearchClawBench, MatOS improves on the previously best-performing agent by 11.15% with the same base model and extends the cost-score Pareto frontier. With a common base model, it outperforms Codex CLI and Claude Code, exceeding Codex CLI by 2.13% on MatTools and 4.17% on SciAgentGym. In eight research cases, MatOS narrowed more than 30 million candidate structures to 97 solid-electrolyte candidates, identified 89 halide variants with higher computed conductivity than their parent structures, linked the force errors of 11 pretrained interatomic potentials to local atomic environments, and supported two new methods that reduce errors by 3.1% and 13.6% relative to their baselines. These results show that organizing research capabilities as reusable, evolving assets enables agents to carry out long, multistage materials studies. Code is available at this https URL.

---


### 184. [MIS-VQA: An Annotation-Driven Surgical Vision-Language Dataset for Complex Surgical Understanding](https://arxiv.org/abs/2610.34210)

**<font color=#1a73e8>作者：</font>** Mohamed Hamdy, Iheb Zouari, Fatmaelzahraa Ahmed 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern surgical AI increasingly requires multimodal understanding rather than isolated perception, yet existing datasets remain largely limited to single-task supervision such as recognition or templated question answering. Current medical VQA resources often rely on synthetic templates, lack natural descriptive supervision, or provide sparse annotations that hinder reasoning about spatial relations and procedural context. We introduce MIS-VQA, a surgical vision-language dataset generated through an annotation-driven pipeline that converts heterogeneous surgical annotations into structured textual scene representations. Using EndoVis18 and CholecT50, we transform phase, instrument, interaction, triplet, and segmentation labels into unified contexts that guide large language models to generate clinically coherent question-answer pairs. MIS-VQA supports four response types-concise and detailed descriptions, perception-level grounding, and multi-step reasoning-enabling hierarchical evaluation from atomic visual grounding to compositional reasoning. To address annotation sparsity, we incorporate confidence-filtered segmentation and cross-annotation consistency checks, enabling spatially grounded supervision at scale. MIS-VQA establishes a unified benchmark for surgical vision-language understanding with spatial supervision and multi-tier reasoning evaluation. To demonstrate its utility, we introduce LLaVA-SurgXpert, a family of surgical vision-language models with visual encoders to analyze how visual representations influence multimodal reasoning. Experiments show consistent improvements over existing surgical VQA baselines while revealing capability gaps between perceptual grounding and higher-level reasoning hidden in prior benchmarks.

---


### 185. [Higher Reasoning Effort Improves Reference Verifiability and Changes Reasoning Summaries in GPT-5.5](https://arxiv.org/abs/2610.34212)

**<font color=#1a73e8>作者：</font>** Melika Mobini, Andres Algaba, Vincent Ginis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly being used in different stages of scientific knowledge production, including the suggestion of references. These models can operate at different levels of reasoning effort and provide summaries of their reasoning processes. This raises two questions: Does increasing reasoning effort improve the verifiability of generated references, and do the resulting reasoning summaries reveal how the model's behavior changes with greater effort? We examined summaries from GPT-5.5 as it generated scholarly references for 1,000 papers under paired low- and high-effort settings. Generated references were matched to external bibliographic records, and reasoning summaries were scored for four predefined features and explored for additional features discovered by GPT-5.5. High effort increased the mean paper-level resolver-verified reference rate from 78.3% to 84.8%, and produced longer reasoning summaries. All four predefined features received higher scores under high effort. The discovered features changed less uniformly: some appeared equally often in both conditions, whereas others were more common under high effort. Within each effort condition, neither feature set showed a consistent increase in verification rates with higher scores.

---


### 186. [From Presence Labels to Bounding Boxes: Can Multimodal Large Language Models Scale Surgical Instrument Localization?](https://arxiv.org/abs/2610.34218)

**<font color=#1a73e8>作者：</font>** Mohamed Hamdy, Muraam Abdel-Ghani, Fatmaelzahraa Ahmed 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial localization of surgical instruments through bounding-box annotations is a foundational component of surgical scene understanding, supporting detection, tracking, interaction analysis, and grounded vision-language applications. Yet existing annotations often cover selected frames, video subsets, or dataset variants rather than complete procedures. Manual extension is time-consuming and expert-dependent. Additionally, weakly supervised and detector-based pseudo-labels require task-specific training and may be imprecise. In this study, we design a scalable MLLM-based annotation framework that converts surgical frames and existing instrument-presence labels into accurate bounding boxes, and systematically analyze its reliability, cost, and design sensitivity. We instantiate the framework using six MLLMs and a multi-call configuration on laparoscopic cholecystectomy in Cholec80. Using a carefully designed stratification scheme, two annotators independently label 1,000 frames, and an expert surgeon reviews one annotation set to establish the reference. Results show that instrument-set F1 ranges from 88.2 to 92.7,whereas mIoU ranges from 0.180 to 0.735, showing that comparable recognition can conceal large localization differences. A structured multi-stage annotation pipeline achieves 0.784 mIoU, compared with 0.735 for the best single-call baseline and 0.814 human-human agreement. Using the best accuracy pipeline, we create and publicly release a spatial extension of Cholec80 comprising 285,977 bounding boxes across all 184,498 annotated frames from the 80 videos. The annotations and human references are made available on GitHub

---


### 187. [CropReward: A Human-Preference Benchmark and Reward Model for Aesthetic Image Cropping](https://arxiv.org/abs/2610.34221)

**<font color=#1a73e8>作者：</font>** Xiangfei Sheng, Xiaofeng Pan, Leida Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aesthetic image cropping (AIC) aims to improve image composition and aesthetic quality by removing extraneous or distracting content. Over the past decade, AIC methods have evolved from specialized vision models to multimodal large language models(MLLMs). Reliable evaluation that reflects human preferences is essential for benchmarking AIC methods and guiding model optimization. However, the current AIC evaluation relies largely on geometry-based metrics such as intersection over union (IoU), as well as image aesthetic assessment(IAA) models. Although inconsistencies with human preferences have long been observed, the robustness and reliability of these evaluation criteria remain underexplored. To bridge this gap, we first construct CropBench, a large-scale benchmark comprising 106,995 human preference pairs for 1,019 images, with each candidate set containing the original image and candidate crops produced by 14 AIC methods. A systematic study on CropBench reveals that the existing criteria, ranging from IoU to off-the-shelf IAA assessment models, only exhibit limited alignment with human preferences. Building upon CropBench, we further propose CropReward, an MLLM-based reward model that evaluates a candidate crop by comparing with the original uncropped image and outputs a score indicating explicit aesthetic improvement or degradation relative to the original. In addition, we employ CropReward to construct CropReward-300k, the largest AIC dataset to date, and further develop CropAlign, a preference-aligned AIC model trained solely with CropReward supervision, without human-annotated crop boxes. Experimental results demonstrate that CropReward aligns with human preferences significantly better than existing criteria. CropAlign also surpasses the state-of-the-art AIC methods, demonstrating the advantage of CropReward in guiding AIC model optimization.

---


### 188. [Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models](https://arxiv.org/abs/2610.34251)

**<font color=#1a73e8>作者：</font>** Xinyu Liu, Daiying Tian, Chenwei Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have shown remarkable success in robotic manipulation, yet their ability to execute long-horizon tasks remains limited by insufficient long- term memory modeling. Existing methods either rely on implicit temporal representations within policy networks, where historical information can be gradually diluted, or maintain explicit memory buffers that suffer from redundancy, noise accumulation, and inefficient retrieval. In this paper, we propose CogMemory, a novel variational cognitive memory framework that enables VLA systems to selectively preserve and reuse task-relevant historical information. Our approach encodes multimodal trajectories into compact latent memory representations through a selective state- space memory encoder, multi-slot temporal abstraction, and variational information compression. During action generation, dynamic cross-attention retrieval with gated fusion adaptively incorporates relevant memories into policy prediction. With merely 3.45M additional parameters, CogMemory stays lightweight and seamlessly fits both early- and intermediate-fusion VLA backbones. Extensive experiments on long-horizon robotic manipulation benchmarks demonstrate consistent improvements across diverse VLA backbones.

---


### 189. [NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names](https://arxiv.org/abs/2610.34253)

**<font color=#1a73e8>作者：</font>** Chieh-Yuan Chang, Guan-Wei Chen, Chia-Yi Hsu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents routinely clone repositories, install packages, and read source code obtained from the Web, so publicly hosted code becomes part of the context that shapes the code they write. We show that this Web-borne context can be weaponized without any explicit instruction. We present NameTrap, a source-code poisoning attack that only renames identifiers in third-party Python files to steer AI coding agents toward attacker-targeted Common Weakness Enumeration (CWE) vulnerabilities. An attacker-side coding agent iteratively aligns identifiers with a CWE-specific naming convention and confirms through local probe completions that the renamed file elicits the target weakness, while the released bait contains neither instructions nor vulnerable statements. We evaluate NameTrap across six AI coding agents, ten underlying language models, and four vulnerability categories: CWE-78, CWE-79, CWE-327, and CWE-502. Starting from files whose clean versions never yield the targeted CWE, identifier-level manipulation achieves overall attack success rates of 22.5\% to 56.0\% across the six agents, reaching 75.0\% for certain agent--model configurations, and substantially outperforms random renaming, neutral renaming, and the prior identifier-poisoning attack XOXO. The attack remains effective under Traditional Chinese prompts and transfers across models, while a security-reminder defense fails to consistently prevent vulnerability introduction. Moreover, three AI-based security analyzers and four static analyzers report none of the targeted weaknesses in the poisoned files. These findings expose an overlooked attack surface of agents that consume Web content: seemingly harmless variable names in untrusted, Web-hosted code can compromise the security of downstream software.

---


### 190. [Recovering Business Rules as Cascade Lookups for Enterprise Field Prediction](https://arxiv.org/abs/2610.34258)

**<font color=#1a73e8>作者：</font>** Changxu Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enterprise sales-order systems rely on manually maintained configuration rules to determine fields such as payment terms, shipping points, and sales ownership. When these rules are incomplete or stale, operators must enter values by hand, and downstream errors spread into billing, logistics, and reporting. This paper studies whether missing or outdated rules can be recovered from historical transactions instead of being relearned as opaque statistical patterns. We introduce a knowledge-graph-guided workflow in which an LLM agent proposes candidate business keys, meaning column combinations such as customer and document type, validates them through SQL profiling, and compiles the resulting evidence into deterministic cascade lookups. The LLM is used only during offline rule discovery. At inference time, prediction is a transparent key lookup with no model-serving requirement. Experiments on enterprise sales-order prediction and public relational benchmarks show that cascades are most effective when fields follow stable business rules, while learned graph models remain preferable when prediction depends on temporal or neighborhood patterns. Drift analysis further turns residual errors into diagnostics for configuration maintenance. Code and data: this https URL.

---


### 191. [MultiEvoSkill: Structure-Aware Multi-Agent Skill Evolution for Generalizable Skill Artifacts](https://arxiv.org/abs/2610.34260)

**<font color=#1a73e8>作者：</font>** Kounianhua Du, Jianxing Liu, Ruoshui Shan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill documents are becoming the default adaptation surface for frozen large language model (LLM) agents, but current skill generators face two key limitations. First, humans and different LLMs differ in how they organize procedural knowledge and approach task solving. Skills authored from a human or single-model perspective may therefore fail to align with the reasoning behaviors of other backbones, limiting cross-model generalization. Second, sequential skill descriptions inadequately represent procedures with parallel branches and explicit dependencies, while existing skill optimizers primarily operate on prose and lack explicit support for graph-structured skill evolution. We introduce MultiEvoSkill, a skill-optimization framework comprising three core components: 1) Skill compiler casts the skill as a typed graph with tailored operators, producing a compact, informative representation with explicit procedural topology; 2) Heterogeneous agent system proposes revision advices using collective intelligence, where minimal and informative issues are identified based on multiple sets of experiences. 3) Structure-aware debate and evolution mechanism organizes candidate edits into a heterogeneous graph, resolves them under dependency and importance constraints, and distills the collective proposal into the artifact. Multi-dimensional gating ensures the information gain and topological correctness of each evolution. Optimal skills are then obtained when the system converges at a consistent state. Various experiments and ablations against SOTA methods validate the effectiveness and generalization of MultiEvoSkill.

---


### 192. [DoubleFree:Exploiting Exploration History for Rollout-Free Multi-Task LLMs Training](https://arxiv.org/abs/2610.34272)

**<font color=#1a73e8>作者：</font>** Yingping Wang, Min Cai, Chenyu Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task post-training can develop domain specialists through independent reinforcement learning (RL) and consolidate their capabilities through multi-teacher on-policy distillation (MOPD). However, standard MOPD generates on-policy student responses and keeps multiple teachers online throughout consolidation, introducing substantial system costs. We view this pipeline as domain-wise exploration followed by cross-domain exploitation. Domain RL produces not only the final specialists, but also the trajectories collected throughout their training. Existing methods primarily use the former while leaving the latter underutilized. We introduce DoubleFree, which reuses these historical trajectories for rollout-free consolidation and precomputes teacher supervision for online-teacher-free student training. To understand why this works, we analyze when updates from historical trajectories can approximate on-policy distillation updates and how combining trajectories across exploration stages can better support an evolving student. DoubleFree requires only minimal changes to existing post-training frameworks. Across math, code, and instruction following on Qwen3-4B, Qwen3-8B, and SmolLM3-3B, DoubleFree achieves $2.99$-$5.75\times$ consolidation speedups and reduces GPU-hours by $80.9$-$90.1\%$, while maintaining comparable multi-domain performance.

---


### 193. [A Russian, a Brazilian, and a German Walk into a Bar, Ask the Same Question-- And Get Three Different Answers: Profiling LLM Perspective Diversity on Contested Topics](https://arxiv.org/abs/2610.34278)

**<font color=#1a73e8>作者：</font>** Wiem Ben Rim, Yao Lu, Pontus Stenetorp 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models(LLMs) have shown strong performance on tasks with verifiable answers, but many real-world queries involve subjectivity, disagreement, and conflicting evidence. Most existing benchmarks for such queries remain English-centric, overlooking the vast diversity of perspectives held by users worldwide. To systematically study how LLM perspectives vary across languages, we curate PerspectivesQA, a manually verified multilingual dataset of globally contested topics covering 18 languages, and propose ROOTS, a framework that profiles linguistic, perspective, and framing diversity. We evaluate a diverse set of eight models covering both open-source and proprietary families at varying scales, establishing that LLMs hedge their answers in English but commit to positions in lower-resource languages. Larger models maintain a more consistent cross-lingual worldview, while smaller models are more easily swayed. All models also exhibit high sensitivity to minor surface-level input variations, producing notable stance even in larger models.

---


### 194. [Transformer to GPT-5: Advancements, Limitations, and Future Directions in Large Language Model Design](https://arxiv.org/abs/2610.34281)

**<font color=#1a73e8>作者：</font>** Harsidak Singh Banwait, Chander Prabha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have revolutionized Artificial Intelligence (AI) by their extraordinary capabilities, like contextual understanding, few-shot/zero-shot learning, code generation, ability to reason and problem-solving. Recent studies have shown immense work on LLMs. Yet, there is limited work on the thorough taxonomy of LLMs. This study would showcase a detailed classification of LLMs, starting with the earlier models like BERT and leading to LLMs like GPT, Gemini, Claude and Grok. We would delve into topics like datasets used to train LLMs, computational power used during training, their hardware specifications, architecture and parameters. Further, we would also look at the limitations, computational challenges and open problems as well. This study would primarily focus on the timeline of LLMs, signifying their growth over the period. Findings reveal a clear pattern: models that optimize the ratio between architectural complexity and data quality exhibit stronger reasoning stability and better alignment, without proportionally increasing the computational load. This desired balance between scaling and sustainability is the defining characteristic of the current generation of AI.

---


### 195. [ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence](https://arxiv.org/abs/2610.34283)

**<font color=#1a73e8>作者：</font>** Yihao Hu, Yitong Lin, Pan Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training a spatial VLM to answer which side an object lies on does not require it to preserve the metric displacement that determines that answer, while supervision for a distance estimate may leave categorical relations largely unconstrained. When post-training emphasizes one readout, improvements can therefore concentrate on that interface while transfer to others remains weak or even degrades; we call this observed specialization interface lock-in. ChronoReplay addresses it by replaying heterogeneous spatial supervision as chronologically ordered episodes, retaining source-native targets, and balancing supervision across families. Under the same observation access, a single ChronoReplay checkpoint improves OVO-S-Bench, OST-Bench, and UCS-Bench together, including a 13.41-point gain on OST-Bench, and achieves the highest three-benchmark mean among the supervision settings compared here. Same-data controls further separate the ingredients of this transfer: answer serialization redistributes gains across OST and UCS, family-balanced learning improves over ordinary joint SFT and natural turn weighting, and chronological replay exceeds a shifted-order control by about 2.41 OST points across two paired seeds. Adaptive frame selection then changes evidence access while keeping the trained model fixed, providing an additional inference-time gain at lower visual cost. Streaming spatial performance depends on what distinctions supervision preserves, how heterogeneous histories are organized during learning, and what causal evidence inference makes available at test time.

---


### 196. [Repairing Broken Access Control in Web Applications with LLMs: An Empirical Benchmark Study](https://arxiv.org/abs/2610.34290)

**<font color=#1a73e8>作者：</font>** Mingrui Liu, Liang He, Xinchu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Broken access control (BAC) ranks among the most severe web-application vulnerability classes, yet its automated repair remains largely unexplored. Unlike memory-safety vulnerabilities, BAC is a logic vulnerability whose repair demands a deep understanding of an application's access-control model and business semantics, which traditional automated vulnerability repair techniques handle poorly. Large language models (LLMs) open a promising avenue for this problem, but no standard benchmark exists for studying how well they repair BAC vulnerabilities. We construct BAC-Bench, the first benchmark for BAC repair, consisting of 46 real-world BAC vulnerabilities drawn from six widely used web applications spanning four programming languages. Each vulnerability is equipped with a sandboxed runtime environment, a PoC validation program and a functional test program. We further propose a BAC repair-strategy framework that characterizes any BAC patch along four dimensions, Position, Coverage, Mechanism, and Content. Evaluating eight base LLMs and two commercial LLM agents on BAC-Bench, we find that single-turn base LLMs repair 37.68% of the vulnerabilities on average, while two minimal scaffolds, Apply-Feedback and Navigate-and-Locate, raise this average to 66.03%, with the best base LLM reaching 75.36%, close to the 78.99% of the best agent. Notably, some LLM-generated patches surpass the official patches, and one incidentally closed a zero-day vulnerability that had lain dormant for three years. Our findings delineate the current capability boundary of LLM-based BAC repair and offer guidance toward its practical adoption.

---


### 197. [Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents](https://arxiv.org/abs/2610.34298)

**<font color=#1a73e8>作者：</font>** Zhenning Shi, Liang Pang, Yongqi Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents increasingly act through external tools and interactive environments, making the interface between the model and its executable capabilities part of the decision process. Model Context Protocol (MCP) and command-line interfaces (CLI) can expose the same semantic operations through markedly different model-facing representations. We study whether these representational differences change agent behavior when executable capabilities are matched. We introduce Matched Interface Comparison and Analysis (MICA), which renders MCP and CLI from a shared semantic action contract and routes decoded actions through the same runtime. Across six models and three interactive environments, matched interfaces produce substantial differences in task performance and interaction cost. These effects extend beyond surface validity to semantic action selection, failure pathways, and recovery. Matched-state probes localize sensitivity to capability presentation, realization, and feedback. Paired natural trajectories reveal structured divergence in 94.3% of 2,004 episodes and show that early differences propagate through subsequent interaction. This analysis identifies interface realization as a direct intervention boundary. We therefore introduce Decoupled Action Realization and Targeted Repair (DART), which preserves validated semantic commitments while repairing interface-specific realization. DART improves benchmark score in all six evaluated settings by up to 9.0 points and reduces MCP token cost in all three environments by up to 27.1k tokens per task. Together, these results establish interface representation as part of the closed-loop decision environment shaping agent behavior.

---


### 198. [SHIFT-JEV: Certified Abstention and Gain-Gated Continual Adaptation for LLM-Based Decision Models under Distribution Shift](https://arxiv.org/abs/2610.34329)

**<font color=#1a73e8>作者：</font>** Muhammad Atif Saeed, Azka Atiq, Adarsh Kumar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can act as decision models that return a probability distribution over a fixed set of options, but deployed decision models face domain, label-prior, emerging-class and candidate-set shift. We study how such models fail under shift and propose SHIFT-Jev, a monitoring, abstention and continual-adaptation procedure for them. It scores the risk of each decision from uncertainty, format and option-consistency signals, certifies abstention thresholds with Learn-then-Test, monitors the decision stream with drift and label-shift detectors, and accepts a model update only when an expected-gain gate finds a significant held-out improvement without loss on earlier regimes. On a benchmark of ten shifted test environments with Qwen3-0.6B and Qwen3-4B (three seeds each) and Phi-4-mini, fine-tuning with KL anchors and temperature scaling lowers calibration error under shift from 0.289 to 0.087. At a target risk of 10%, a learned uncertainty score with a certified threshold exceeds the target in 3 to 5 of 27 environment-seed tests, against 5 to 15 for a max-probability score with the same certification and 9 to 14 for conformal prediction sets; drift-based routing changes little. A chi-squared test on predicted labels detects 95 to 99% of class-prior shifts that confidence- and embedding-based detectors miss. In continual adaptation, SHIFT-Jev reaches 70.5% accuracy on Qwen3-0.6B, above replay, LwF, EWC and fine-tuning baselines in every seed, whereas on Qwen3-4B its conservative gate leaves it 0.4 to 1.4 points behind them.

---


### 199. [CrossPair: Unlocking Generalist Visual Transformation Learning in Image Editors](https://arxiv.org/abs/2610.34333)

**<font color=#1a73e8>作者：</font>** Yibo Zhao, Lifan Jiang, Senlin cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language models switch tasks from demonstrations, but vision still often relies on separate systems for restoration, editing, and stylization. A before--after example offers a shared instruction only if the transferable change can be separated from the scene that demonstrates it. We introduce CrossPair, which adapts a pretrained multimodal image editor to transfer diverse transformations from one exemplar pair. Exemplar-before, exemplar-after, and query images take fixed roles in its native VLM and VAE pathways: the VLM extracts operation semantics, while the VAE retains fine appearance and structure. A training-only, change-aware DINOv3 objective aligns feature-change directions across content-distinct scenes, guiding the output to follow the demonstrated relation without an inference-time encoder. We construct Transform-360K by grouping filtered pairs from conditional representations, restoration, editing, virtual try-on, and stylization under shared transformations. On Relation252K-derived seen and held-out transformations, \method improves target agreement and edit-direction similarity over released systems. Ablations show that the semantic and visual exemplar routes are complementary and that DINO relation alignment further strengthens transfer; Transform-360K training also improves aggregate held-out-operation scores.

---


### 200. [CoLink: Global Compression and Knowledge Linking for Multi-Turn Dialogue Modeling](https://arxiv.org/abs/2610.34335)

**<font color=#1a73e8>作者：</font>** Lian Yan, Zhenbo Xia, Haotian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting salient information from long-horizon dialogue histories remains a significant challenge for Large Language Models (LLMs) due to the restricted context windows and efficient retrieval challenges. Current methods typically rely on history organization or local token-level optimization, suffering from information loss, retrieval redundancy, and myopic attention. Inspired by the view in cognitive science that dialogue constitutes sense-making and memory association, we propose CoLink, a framework that enhances LLMs' global context awareness in domain-specific multi-turn dialogues through information linking and compression. CoLink first clusters historical contexts into topic graphs to establish cross-semantic associations with external knowledge. Guided by the adaptive control of thought, it then retrieves and activates knowledge via synergizing semantic relevance and graph-structural topology. Crucially, to achieve effective compression of history and knowledge, we ground multi-turn dialogues in information theory and derive a principled optimization objective for extracting the core sense-making information. Coupled with a competitive slot mechanism, CoLink condenses the global context into dedicated memory and knowledge slots, efficiently distilling lengthy, redundant inputs into an extremely compact latent representation. Extensive empirical results on both public and our MMD datasets validate CoLink's superiority and generalizability in knowledge linking and sense modeling.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
