# 🧠 大模型相关研究 | 2026年09月18日

> 本类共 **210** 篇论文：已确认 **198** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-210](./part-05.md)

---

### 151. [WaveTLM: Reliable Time-Series Language Modeling through Task Compilation](https://arxiv.org/abs/2609.18812)

**<font color=#1a73e8>作者：</font>** Jiahui Chen, Bingke Zhu, Hongyu Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series language models provide a shared natural-language interface across temporal tasks, but plausible text does not guarantee reliable task outputs. Responses may appear reasonable while hallucinating the required object: numerical sequences can violate shape, scale, channel order, or temporal alignment, and textual decisions can fall outside the legal label space. We formulate reliable time-series language modeling, separating task-object reliability from predictive quality. We introduce ExecTS-QA, a contract-grounded benchmark spanning forecasting, imputation, classification, anomaly detection, and waveform analysis. We further propose WaveTLM, a unified compiler-executor model whose task compiler transforms user requests, visible arguments, and wave-grounded evidence into typed task states, while task-native executors construct numerical tensors, legal decisions, or structured records. On ExecTS-QA, a single WaveTLM checkpoint achieves 99.40% contract-valid coverage, compared with 37.83% for the strongest evaluated string-first baseline, while retaining balanced predictive performance across all five task families. Evaluations on SciTS, TSQA, IRTS-ToolBench, and ARFBench provide additional evidence of transfer. The code, construction scripts, and ExecTS-QA dataset will be publicly released upon publication. These results show that task compilation can convert plausible language generation into reliable time-series outputs.

---


### 152. [Using OCR Heads to Verbalize Image Semantics](https://arxiv.org/abs/2609.18823)

**<font color=#1a73e8>作者：</font>** Sheridan Feucht, Benno Krojer, Sarah Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How do VLMs map from pixels to semantics? To understand this general question, we focus on a narrow one: studying how VLMs perform optical character recognition (OCR). Across four models, we identify attention heads causally necessary for OCR, and discover that these are in fact general-purpose heads that output interpretable semantic features across all image tokens. For example, pointing these heads at an image token containing the word "bike" causes Qwen3-VL-8B to output "bike," but pointing them at a bird wing causes the model to output the token "feathers." We collapse these heads' attention weights into a single verbalization lens transformation that reveals interpretable semantic features in hidden states across all layers. When combined with projection to vocabulary space, we can obtain interpretable labels starting from layer 0, showing that image representations are in fact aligned with language in early layers. We find that we can also use the inverse of this transformation to edit non-word concepts, e.g., replacing a tractor with a revolver in a naturalistic image, providing causal evidence that this subspace is useful for more than just OCR. Our results are an example of how the study of specific mechanisms can shed light on broader interpretability problems.

---


### 153. [Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data](https://arxiv.org/abs/2609.18842)

**<font color=#1a73e8>作者：</font>** Jinli Hu, Ross M. Clarke, Yichuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The scaling laws hold that a language model grows more capable with more parameters and more training data, and Mixture-of-Experts (MoE) architectures have ridden these laws to remarkable results, activating only a fraction of an enormous stored parameter bank for each token. That success is built on static pretraining data. A deployed model faces a different world, where much of the data that would make it more useful is not in its training set but in the live interaction it is currently handling, such as the facts a user supplies or the corrections they give. A conventional model cannot learn from this data, because its weights are frozen after training. Instead, the knowledge and behaviour supplied at run time are placed in the prompt, by retrieval or instruction, and re-read on every request only to be discarded once the request ends. We ask how an architecture could learn from live interaction by writing it into its weights. Taking inspiration from MoE, we propose the \textbf{Infinite-Parameter LLM}. A compact hypernetwork turns the data given at run time into a low-rank modulation of a shared base network, so the feed-forward weights are generated from live data rather than stored in a fixed bank. Where prior weight generators read the context once and freeze, we carry a Bayesian belief over the generator's latent code and update it online, so the effective weight is re-derived from that evolving belief as the session proceeds rather than fixed after one read. The stored footprint stays fixed, yet the weights the model can compile are effectively infinite. For the knowledge and behaviour supplied at run time, carrying them in the weights rather than the prompt is amortized in compute, frees the context window, persists across turns, and can generalise better than in-context use. We specify an evaluation protocol that tests exactly this against in-context learning and retrieval.

---


### 154. [ReFigBench: Benchmarking Scientific Figure Reconstruction as Editable PowerPoint Artifacts](https://arxiv.org/abs/2609.18844)

**<font color=#1a73e8>作者：</font>** Liyang Fan, Chi Wei, Yitai Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal coding agents are expected to turn visual inputs into usable artifacts, and they act through a harness, the layer of tools, context management, and execution environment around the model. Existing evaluations often isolate short tool calls, API traces, or screenshot resemblance, and a low score under these proxies cannot say whether the model saw poorly, planned poorly, or was failed by its harness. We study scientific overview figure reconstruction, an agent task in which a source image must become an editable PowerPoint slide that preserves text, topology, layout, and native document structure. We introduce ReFigBench, a benchmark and evaluation framework built on 1,000 real overview figures retrieved from arXiv papers with full provenance. Coding agents from four model families reconstruct every figure under two workflows, direct code generation and a specialized PPTX workflow, and the strongest model runs inside two commercial harnesses, yielding ten configurations. Evaluation combines deterministic artifact checks, repeated automated scoring by judges from two model families, and blinded human comparisons. Perception remains a bottleneck that iterative rendering only partly repays. Whether workflow effort converts into quality depends on the model together with its harness, since the same model gains from the specialized workflow inside one harness and loses inside the other, and the harness shifts scores even under an identical direct prompt. The specialized workflow erases native connectors in every configuration, human judges still prefer its renderings in most matchups, and even the strongest agent falls short of the rubric ceiling. These results expose the tension between fidelity and editability as the central challenge for practical multimodal document agents.

---


### 155. [EviGen: Predictive Evidence Scaffolding for Verifiable Clinical Rationale Generation](https://arxiv.org/abs/2609.18852)

**<font color=#1a73e8>作者：</font>** Fengnan Li, Heman Burre, Liwen Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Longitudinal electronic health records (EHRs) capture years of patient history across notes, codes, labs, and procedures, and contain evidence needed to reason about likely clinical outcomes. However, comprehensive clinician review of these records is impractical, and LLM-based processing is costly and often unreliable, missing some relevant observations while hallucinating others. We therefore propose EviGen, a three-layer framework for verifiable clinical rationale generation that addresses these challenges. The first layer is a patient-conditioned retriever that uses learnable queries to find evidence predictive of, not just textually relevant to, a clinical outcome and ranks it by prediction attribution scores. The second layer is an LLM generator that consumes this ranked evidence as a scaffold to produce a clinical rationale grounded in the retrieved spans. The third layer is a process-supervised verifier that checks the generated rationale at the reasoning-step level, flagging unreliable claims. Across three medical prediction datasets, EviGen improves prediction performance and rationale faithfulness over full-context LLM and RAG baselines, and is preferred by clinical reviewers in a usability evaluation.

---


### 156. [Decodable but Misrouted: Sparse Features Uncover a Readout Gap in Vision-Language Models for Harmful Meme Detection](https://arxiv.org/abs/2609.18860)

**<font color=#1a73e8>作者：</font>** Girish A. Koushik, Diptesh Kanojia, Helen Treharne  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a large vision-language model misclassifies a harmful meme, the failure may reflect missing internal evidence or an inability to route represented evidence to its output. We distinguish these cases in Gemma-3 and Qwen3.5 using sparse autoencoders, role-conditioned probes, causal interventions, and recovery experiments across six harmful content benchmarks, with additional Spanish and Hindi-English code-mixed evaluations. Sparse readouts outperform native prediction on all six primary binary tasks: Qwen averages $0.740$ versus $0.432$ native macro-F1, while residual reconstruction reaches $0.486$, whereas Gemma improves from $0.532$ to $0.714$. These differences reflect supervised accessibility rather than a pre-existing, native decision rule, and the most influential token role depends on the task. Under the evaluated score scales, Qwen silent-feature ablation is $24-63$ times more probe-sensitive, whereas routed-feature patching on literal yes/no tasks is $16-140$ times more output-sensitive. Calibration-only routing recovers $93.3$% of the mean gap, and probe-distilled LoRA improves native predictions, although shared multi-task adaptation causes negative transfer. A case study of Gemma-3-12B on Facebook Hateful Memes finds a distributed rank-32 image-prompt interaction, reaching $0.756$ versus $0.685$ native macro-F1. Robustness controls show that the signal extends beyond English, is not explained solely by accompanying OCR, and depends on paired visual evidence. Thus, routing, rather than representation alone, is a recurring bottleneck in harmful meme classification.

---


### 157. [PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning](https://arxiv.org/abs/2609.18861)

**<font color=#1a73e8>作者：</font>** Yu Liu, Zeming Liu, Tianle Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adaptive learning systems commonly formulate learning path planning as Exercise-Centric (EC) recommendation, where the next step is inferred from item-level interaction logs. Evaluating goal-oriented guidance additionally requires explicit learner goals and curriculum-scale prerequisites: learners with similar exercise records may need different paths toward their targets. We therefore study Knowledge-Centric (KC) personalized learning path planning, where a planner must reason over learner profiles, mastery states, and prerequisite knowledge structures to decide which textbook, unit, and concept should be studied next. To support this setting, we introduce PersonaPath, a benchmark that pairs 2,000 fine-grained learner personas with a hierarchical knowledge graph of 347 textbooks, 1,751 units, and 4,092 concepts across 77 subjects. We evaluate representative LLMs on PersonaPath. Results show that even the strongest LLM reaches only a 29.5% final pass rate in Basic Education, and that the main bottleneck lies in adaptivity, where no model exceeds 44.7% in tailoring paths to individual learners.

---


### 158. [CASHEWS: Source Preprocessor for LLM-based Malicious Package Detection](https://arxiv.org/abs/2609.18862)

**<font color=#1a73e8>作者：</font>** Jean-Charles Noirot Ferrand, David Adei, Anders Møller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malicious npm package detection tools now leverage LLMs' semantic understanding of source code to detect malicious intent at scale. This capability has proven invaluable in identifying packages involved in recent supply-chain attacks such as Shai-Hulud. However, threat actors exploit the limited context windows of LLMs through JavaScript techniques such as code obfuscation that yields high token density and bundling malicious code with benign packages, causing detectors to skip large files or miss malicious behavior. This creates an attack surface for evading detection. In this paper, we present CASHEWS, a JavaScript preprocessor that reduces file size by rewriting source code to remove code that is irrelevant to analysis or likely to mislead the model. Given a package source file, CASHEWS deobfuscates it through iterative decoding, extracts bundled modules and dynamically executed code, identifies malicious sinks and computes backward slices that reach them, and abbreviates long literals and identifiers to produce a compact representation for the detector. Across 512 large package files, two scanner types, and three LLMs, CASHEWS increases analysis coverage from 69.1--85.7% to 98.8--100% and reduces the false-negative rate by up to 18.6 percentage points. CASHEWS also has a median preprocessing time of 30 seconds while reducing net analysis cost by 34.6%, making registry-wide LLM-based analysis more practical. By preprocessing source code before analysis, CASHEWS enables researchers and industry practitioners to use more powerful models for malicious package detection at the same or lower analysis cost as less powerful models.

---


### 159. [ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions](https://arxiv.org/abs/2609.18864)

**<font color=#1a73e8>作者：</font>** Guosen Wu, Huizhen Huang, Guoxiong Long 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy evaluations of tool-using LLM agents often inspect a designated action, final response, or attacker report. These local proxies can miss unauthorized exposure elsewhere in a multi-step session and lack common ground truth across outlets, reports, and tool paths. We introduce privacy exposure displacement, the mismatch between a local evaluation proxy and target-grounded session exposure, and ASLEval, an authorization-aware framework that pre-registers a hidden target set, measures all declared visible exits, and reserves internal traces for diagnosis. Across multiple enterprise-style environments and independently implemented runtimes, we observe three recurring patterns. An expected-outlet-only view misses 46.9% of exposure recovered by the visible-exit union; attacker self-reports combine omissions with high false discovery; and schema-aligned internal evidence usually precedes visible exposure at the request/probe level. Reducing model-visible returns changes this path but can eliminate normal-task success. Independent human review supports the adjudication pipeline while identifying harder console and candidate cases. These findings motivate benchmarks that declare the complete visible boundary, ground claims in pre-specified targets and authorization, and report privacy together with task utility.

---


### 160. [Preventing Model Collapse: A Fisher-Rao Perspective on the Dynamics of Training with Synthetic Data](https://arxiv.org/abs/2609.18878)

**<font color=#1a73e8>作者：</font>** Matteo Marchi, João Pedro Silvestre, Bahman Gharesifard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are now routinely trained using synthetic data, since high-quality human data has been exhausted by the ever increasing needs of larger and larger models. However, recursive training on synthetic data frequently induces model collapse, a degenerative feedback loop where models progressively forget the true underlying data distribution. Training on a mixture of synthetic and fresh human data is a logical countermeasure and can prevent model collapse. However, it is an open question as to what is the exact minimum required ratio of human-to-synthetic data to maintain training stability. In this paper, we establish rigorous theoretical guarantees on the minimum rate of human data required to prevent model collapse. Although previous work established a formal lower bound for this ratio, such bound can be vacuous for very high dimensions, as the analysis relies on the usual Euclidean metric in R^n and is not adapted to the space of categorical probability distributions. Instead, in this paper we explicitly leverage the information-geometric structure of the probability simplex by analyzing the dynamics of the process under the Fisher-Rao metric. We derive quantitative contraction and invariance bounds that are stable and do not become trivial as the dimensions increase. Thus, we show that the effective required data ratio to prevent model collapse is different than previously implied.

---


### 161. [Structured Claim-Level Discourse Representations for Dense Health Narratives](https://arxiv.org/abs/2609.18905)

**<font color=#1a73e8>作者：</font>** Farnoushsadat Nilizadeh, Elham Pourabbas Vafa, Shirin Nilizadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Health discourse in social media videos often contains densely entangled claims spanning multiple thematic aspects, stances, evidential frames, and rhetorical functions within short conversational spans. Existing approaches largely rely on coarse topic-level, sentiment-based, or stance-oriented representations that do not adequately capture this structure. Our analysis identifies an average of 13.22 atomic claims per minute, motivating richer claim-level discourse representations. We introduce a structured framework for claim-level discourse analysis in dense health narratives. Our framework models discourse through tuples linking atomic claims with thematic aspects, stance, and multidimensional pragmatic discourse attributes. To support this setting, we construct a benchmark spanning four health domains with 1,191 manually annotated claims from 60 videos. Using this framework, we evaluate automated structured discourse analysis under different discourse context settings. Results show that current LLMs achieve strong performance on thematic categorization and stance prediction, but struggle with high-dimensional pragmatic profiling. We also find that different discourse tasks benefit from different forms of contextual reasoning, suggesting that future systems may require task decomposition and specialized inference strategies.

---


### 162. [How Much is a Human Right Worth? ECtHR-NPD: A Benchmark for Predicting Non-Pecuniary Damage Awards](https://arxiv.org/abs/2609.18908)

**<font color=#1a73e8>作者：</font>** Yanyi Pu, Damian A. Gonzalez-Salzberg, Zheng Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing legal benchmarks cover diverse tasks, while continuous monetary remedies remain comparatively underexplored. We introduce ECtHR-NPD, to the best of our knowledge, the first benchmark for predicting non-pecuniary damage (NPD) awards at the European Court of Human Rights (ECtHR) from case information when no statutory formula or explicit calculation rule determines the amount. ECtHR-NPD contains 14,575 cases with case-level awards in nominal euros, chronological splits, and a protocol separating target construction from model input. We evaluate a battery of methods, including constant predictors, gradient-boosted trees, retrieval methods, fine-tuned encoder language models (LMs), prompted decoder LMs, and knowledge-augmented agents. Our results show that more sophisticated LM and agentic approaches do not consistently outperform the strongest feature-based baseline. All model families struggle to identify zero awards and to calibrate high-award predictions, with further degradation on the Challenging test view, making ECtHR-NPD a challenging testbed for current state-of-the-art open-weight and proprietary LMs.

---


### 163. [Beyond Outcomes: Dual-View Relational Learning for Efficient Agent Benchmarking](https://arxiv.org/abs/2609.18909)

**<font color=#1a73e8>作者：</font>** Xinshuai Guo, Junjie Wu, Dolly Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks are substantially more costly to evaluate than conventional LLM benchmarks. Benchmark compression is therefore a natural solution, yet existing methods primarily model redundancy in task--model final-score distributions, which is important in agentic evaluation. To address this limitation, we analyze large-scale trajectories and identify six complementary process signals that are systematically associated with final agent performance. To disentangle agent performance redundancy from a complete perspective, we propose DualViewEval, an agent benchmark compression method that jointly exploits outcome and process relations to learn an exact-size miniset and predict the full-benchmark scores. Across five agent benchmarks and five representative baselines, DualViewEval achieves the best results in all datasets. With only 20 tasks, it achieves $24\times$--$40\times$ compression on APEX-Agents and BFCL, reducing mean absolute error (MAE) by $14.5\%$--$28.2\%$ over the strongest competitors while improving Kendall's $\tau$ by up to $7.2\%$ relative to EssenceBench on SWE-bench Verified. The selected minisets further reveal capability differences among different agents, providing compact and diagnostic feedback for efficient agentic model development.

---


### 164. [Higher-order pruning of experts in mixture-of-experts language models](https://arxiv.org/abs/2609.18916)

**<font color=#1a73e8>作者：</font>** Alex M. Tseng, Prannay Kaul, Luca Zancato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models suffer from large parameter counts, which create a significant memory bottleneck. Expert pruning is the most direct approach for reducing this parameter count, yet existing methods make pruning decisions for each expert independently, and assume experts' contributions are purely additive. In reality, expert usage in MoEs is inherently cooperative. We derive HOPE (Higher-Order Pruning of Experts), a second-order pruning objective which provably minimizes an upper bound on the error resulting from pruning. We show that REAP (a state-of-the-art first-order pruning method) is a special case of HOPE where interaction terms are ignored. Across three frontier MoE models (up to 122B parameters), two distinct calibration sets, and multiple benchmarks (including math, instruction following, coding, and an agentic suite), we demonstrate that HOPE produces better pruning decisions than existing methods, and its advantage is most pronounced at high pruning rates and on challenging agentic workloads. At 50% pruning, HOPE outperforms all baselines and achieves an average rank of 1.58 out of 5 methods (versus 2.42 for the next-best method, REAP), with gains of up to +6.1% on agentic coding. Over all conditions, HOPE again achieves the best average rank and surpasses every other method in the majority of head-to-head comparisons. By preserving cooperative expert structure that first-order methods ignore, HOPE enables aggressive compression with minimal degradation, particularly on complex tasks where diverse expert combinations are invoked over long sequences.

---


### 165. [PhysVGGT: Feed-Forward Dense Physical Property Estimation from A Single Image](https://arxiv.org/abs/2609.18920)

**<font color=#1a73e8>作者：</font>** Sneha Paul, Guile Wu, Bingbing Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical properties, such as friction, hardness, stiffness, and density, govern how robots should grasp, manipulate and interact with objects, yet estimating these properties from RGB images remains challenging. Existing methods typically employ per-object reconstruction augmented with physical properties or directly query vision-language models at test time, which results in substantial computational overhead that limits their applicability. In this work, we present PhysVGGT, a feed-forward model that predicts dense maps of friction coefficient, Shore hardness, Young's modulus, and density, together with object-level mass, from a single RGB image in one forward pass. The key idea of PhysVGGT is to formulate physical property estimation as a dense per-pixel prediction problem and employ a visual geometry transformer to extract geometry-aware tokens from the input image followed by a dense prediction branch for estimating local physical properties and a global prediction branch for estimating object-level mass. In addition, we introduce a scalable pseudo-label generation pipeline that enables large-scale weakly supervised training for dense physical property prediction, substantially reducing the need for expensive direct physical measurements. Extensive experiments show that PhysVGGT achieves state-of-the-art performance on the ABO-500 dataset and generalizes effectively to the out-of-distribution NeRF2Physics dataset. Moreover, PhysVGGT eliminates the need for per-object reconstruction and test-time optimization, achieving an inference latency of only 0.13s per image, making it $27\times$ faster than the previous state of the art.

---


### 166. [Long-Lived Characters, Local Inference: Incremental Memory Maintenance for Game NPCs](https://arxiv.org/abs/2609.18935)

**<font color=#1a73e8>作者：</font>** Zimu Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A game character should not have to reread its entire life before every conversation. For locally deployed language-model characters, however, revising a few memories can invalidate a long reusable prefix. The resulting preparation cost competes with both foreground dialogue and the maintenance of other characters. This matters especially when dialogue feeds game-defined actions and value judgments: a fluent but incorrect account of who owns an item, or whether a transfer has already happened, can corrupt the input to otherwise deterministic rules. We study incremental memory maintenance for long-lived game NPCs in a quantized Qwen hybrid recurrent-attention model. Our runtime removes superseded attention KV entries, computes replacement records at the true sequence tail, and preserves the continuing recurrent state and unchanged KV. Existing local experiments combine multi-update dialogue replays, fixed-input placement ablations, and attention diagnostics. Independent block composition weakens query-conditioned memory selection without a uniform chunk-initial attention collapse. True-tail updates preserve important current-state and historical bindings across eight scripted maintenance rounds; a placement case recovers the full-refill quantity in three reconstructions, while slot-preserving alternatives repeat a double-subtraction error. Attention-distribution proximity alone does not explain these semantic differences. The results motivate treating a character's inference state as a maintained, history-dependent resource, rather than only a disposable encoding of its latest memory text.

---


### 167. [StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction](https://arxiv.org/abs/2609.18949)

**<font color=#1a73e8>作者：</font>** Sean Wan, Dongping Liu, Luyao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce StableEval Arena, a cost-aware benchmark framework for evaluating agentic AI systems on stablecoin peg-risk prediction. StableEval Arena evaluates LLM-backed agentic systems on diagnosing peg stress and forecasting deviations from the one-dollar peg over a hidden seven-day horizon, using leakage-safe historical replay with exchange price-volume data and market-context features. We report two complementary experiment blocks: a 120-case stress-enriched validation block and a 507-case natural-distribution full-arena evaluation block. Across six LLM-backed agent configurations and baselines, StableEval Arena measures prediction quality, calibrated-label behavior, structured-output reliability, latency, token consumption, and estimated inference cost. Rather than ranking agents by accuracy alone, the framework treats trustworthiness as a joint property of forecast quality, operational reliability, and computational cost. The results show a gap between protocol-following reliability and financial-risk reliability: agents reliably produce valid structured outputs at modest measured cost, but still miss most rare severe-stress and sustained-depeg cases. To support auditing and replication, we release the benchmark dataset on Hugging Face and the source code on GitHub.

---


### 168. [LangSelect: Cost-Aware Target-Language Routing for LLM Code Generation](https://arxiv.org/abs/2609.18959)

**<font color=#1a73e8>作者：</font>** Son Ha Xuan, Phat T. Tran-Truong, Xuan-Bach Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM code-generation systems usually choose a target programming language before decoding and treat that choice as fixed. We show that, for language-flexible programming tasks -- tasks where several target languages are acceptable and checkable by the same tests -- this choice is a measurable cost lever: verified implementations of the same task can differ substantially in generated-token length. We introduce LangSelect, a verification-aware router that selects the target language before generation and falls back when the first attempt fails. To separate offline routing opportunity from end-to-end behavior, we evaluate verified-solution replay, which chooses among already accepted corpus solutions, and live GPT-5 generation, which charges every generation attempt, including failures and fallbacks. On MultiLang-Bench, a 3,000-task, 8-language verified corpus, replay shows substantial language-routing headroom. In live evaluation on 450 held-out tasks, a train-split Domain heuristic baseline reduces harness-proxy tokens, which include wrapper and entrypoint overhead, by 50.3\% at 92.9\% pass after fallback, while a learned CodeBERT+metadata selector reaches the highest pass after fallback, 93.8\%, with a 3.7\% token increase. These results show that output-language routing can define a practical cost-correctness frontier for unit-test-verifiable code generation.

---


### 169. [When Audit Quality Fails to Predict Downstream Utility: A Counterfactual Study of Synthetic-Data Selectors for Low-Resource African NLP](https://arxiv.org/abs/2609.18960)

**<font color=#1a73e8>作者：</font>** Son Ha Xuan, Phat T. Tran-Truong, Xuan-Bach Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quality-aware synthetic-data selection rests on a proxy: examples that an LLM judge rates as good should also help a downstream model learn. In a controlled replay in low-resource African-language classification, we show that this proxy breaks. Across four languages (Amharic, Hausa, Swahili, Yoruba), two classification tasks (MasakhaNEWS, AfriSenti), and five matched-budget selectors, audit rankings and downstream rankings diverge. Within each cell, the Spearman between judged label correctness and Macro-F1 across selectors has mean $\rho{=}0.04$ (median $0.00$), showing that the mismatch is not an aggregation artifact. \method{}-V2, our counterfactual audit framework, produces the cleanest selected pool on three audit channels at once: highest judged label correctness ($0.904$ vs.\ $0.767$ for naive, a $17.9\%$ relative gain), lowest shortcut score, and a hard-reject rate of $0.162$ vs.\ $0.486$ for naive. AlpaGasus nevertheless leads downstream Macro-F1 ($0.202$ vs.\ $0.163$ for \method{}-V2), and the inversion persists on the five non-degenerate cells. The lesson is methodological: in this controlled setting, audit quality is a property of the selected pool, not a guarantee of downstream utility. Synthetic-data evaluation should therefore report audit and downstream metrics on the same retained sets. We release the audit tables, per-selector retained pools, and a claim ledger that links every reported number to its source row.

---


### 170. [BadQubits: An LLM-Based Framework for Static Pre-Execution Detection of Structurally Harmful Quantum Circuits](https://arxiv.org/abs/2609.18965)

**<font color=#1a73e8>作者：</font>** Justin Woodring, Lamine Noureddine, Aisha Ali-Gombe  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents BadQubits, an LLM-based framework for static pre-execution detection of structurally harmful OpenQASM 2.0 circuits. The framework targets physical-execution-layer threats by analyzing submitted circuits prior to runtime, where dynamic inspection is constrained by measurement irreversibility and the exponential cost of classical quantum-state simulation. We evaluate four code-understanding LLM architectures on a dataset of 1,500 circuits consisting of 1,000 benign programs from MQTBench[33] and 500 synthetic attack circuits derived from three documented physical-layer threat primitives. Our fine-tuned Qwen Coder 2.5 7B model achieves 92.67% classification accuracy and 96.1% harmful-circuit recall. Two of the four evaluated base models fail to generalize under constrained LoRA fine-tuning, indicating that architecture-aware model selection is a necessary design consideration rather than a minor tuning choice. To characterize what the detector has learned, we compare it against a bag-of-gates CNN under progressive confound removal and adversarial syntactic perturbation. The CNN's harmful-circuit recall drops from 100% to 17%, while the fine-tuned LLM decreases only from 96.1% to 91.2%. We attribute this gap to the sequential structure retained in token-level LLM inputs but discarded by histogram-based baselines. A correlation analysis further shows that model decisions track threat-defining features, specifically SWAP density and measurement timing, rather than generator-specific artifacts such as register naming.

---


### 171. [LaSeD: Label-Semantic Self-Distillation for Visual-Only Surgical Phase Recognition](https://arxiv.org/abs/2609.18971)

**<font color=#1a73e8>作者：</font>** Ye Tao, Claudia Scherl, Sara Monji-Azad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical phase recognition maps each video frame to a clinically meaningful workflow phase, supporting context-aware assistance, documentation, and postoperative analysis. Most methods treat phase annotations only as class IDs, whereas recent surgical vision-language models often require additional video--text data, captions, or instruction tuning. We propose \emph{LaSeD}, a label-semantic self-distillation framework that uses phase names as privileged training-time context while retaining visual-only deployment without a ground-truth phase-name hint. LaSeD initializes a frozen teacher and a student from the same pretrained VLM checkpoint. The teacher receives the frame, a fixed task prompt, and the ground-truth phase-name hint; the student receives the same frame and prompt without the hint, and only its visual encoder is optimized. Training combines hard phase-token supervision with feature-level distillation from cached teacher representations. At inference, the teacher and hint are removed, and the student predicts one of the seven Cholec80 phases through constrained digit-token logits without an additional classifier head. On the Cholec80 evaluation split, LaSeD achieves 86.20\% accuracy, 77.75\% macro recall, 78.13\% macro precision, and 64.15\% macro Jaccard. Under the identical protocol, it improves a visual-only Qwen3-VL-4B baseline by 9.45, 9.42, 11.93, and 12.22 percentage points, respectively. Visual-only means that the image is the only sample-specific inference input, while all frames share the same fixed task prompt. These results suggest that phase names provide a useful low-cost signal for adapting VLMs to surgical workflow analysis. (The code will be published soon.)

---


### 172. [Instrument Classification of Solo Sheet Music Images](https://arxiv.org/abs/2609.18980)

**<font color=#1a73e8>作者：</font>** Kevin Ji, Daniel Yang, TJ Tsai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies instrument classification of solo sheet music. Whereas previous work has focused on instrument recognition in audio data, we instead approach the instrument classification problem using raw sheet music images. Our approach first converts the sheet music image into a sequence of musical "words" based on the bootleg score representation, and then treats the problem as a text classification task. We show that it is possible to significantly improve classifier performance by training a language model on unlabeled data, initializing a classifier with the pretrained language model weights, and then finetuning the classifier on labeled data. In this work, we train AWD-LSTM, GPT-2, and RoBERTa models on solo sheet music images from IMSLP for eight different instruments. We find that GPT-2 and RoBERTa slightly outperform AWD-LSTM, and that pretraining increases classification accuracy for RoBERTa from 34.5% to 42.9%. Furthermore, we propose two data augmentation methods that increase classification accuracy for RoBERTa by an additional 15%.

---


### 173. [Suppressed, Not Erased: A Representational Trace of Edited Facts Survives Even Weight-Free Knowledge Editing](https://arxiv.org/abs/2609.18985)

**<font color=#1a73e8>作者：</font>** Priyansh Srivastava, Romit Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge-editing benchmarks certify local correctness, whether an edited model produces the new fact on near-edit prompts but not how much of the original fact remains decodable inside the model. We study residual knowledge directly with a linear trace probe: after editing a fact, we ask whether the original object is still recoverable from the model's hidden states. On GPT-2-XL, across three mechanistically distinct editors applied to 50 CounterFact edits, the original object remains linearly decodable well above chance after a successful edit (probe accuracy 0.96 for ROME, 0.86 for constrained fine-tuning, and 0.79 for the memory-based editor GRACE, against a chance level of 0.50; all edits reach 100% generation-based success). The GRACE result is the most informative: GRACE changes zero base-model weights, overriding the fact through an external memory, yet the original object is still decodable from the underlying network, so the residual trace cannot be attributed to an incomplete weight update. We read this as evidence that editing, even when behaviorally successful, suppresses rather than erases the original association in representational space. We also report a relearning-savings instrument that did not behave reliably in our setting and discuss why; we treat it as a negative methodological result rather than evidence. Code and data are released.

---


### 174. [Function Lives Where Variance Doesn't: Task-Weighted Charts of a Language Model's Computation](https://arxiv.org/abs/2609.18989)

**<font color=#1a73e8>作者：</font>** Alexandre Quemy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How many dimensions does a language model's computation actually use? The question is ill-posed until one names a functional. Task-weighted charts make it well-posed: low-dimensional coordinate systems fit against a chosen functional of the representation, under the functional's own metric, turning distillation into plain least squares. Across six models from three families, spanning 70m to 7B parameters, next-token prediction needs 70--90% of the residual stream's width to stay within 5% of intact perplexity, a width consumed by the rare tail of language, and the variance profile predicts none of it: two directions carry 90% of GPT-2's activation variance and almost none of its function. Dimension is per-functional: the model's own uncertainty reads from six coordinates where the full predictive distribution needs hundreds; and it grows with depth. The dissociation is exploitable: when only a few dimensions can be kept, charts trained under the functional's metric preserve the model's predictions better than variance-based or optimal linear compression.

---


### 175. [Lost in Perception: Isolating Perceptual and Reasoning Failures in Multimodal Physics and Geometry Reasoning](https://arxiv.org/abs/2609.18991)

**<font color=#1a73e8>作者：</font>** Raj Jaiswal, Sree Krishna Uppalapati, Dhruvkumar Patel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs report strong performance on scientific reasoning benchmarks, yet most treat perception and reasoning as a single measurable process. We introduce a five-task diagnostic experiment across physics and geometry benchmarks that isolates failures to perception, reasoning, or both. Incorrect diagram interpretation degrades performance even on problems models solve correctly from text alone, and accuracy generally rises from raw images to human-authored captions. Recovery under corrected captions is high for some models, separating perception-blocked failures from genuine reasoning bottlenecks. Which reasoning error follows a perception failure depends on domain: physics failures resolve into calculation errors, geometry into conceptual misapplication. As a discussion beyond our core experiments, InternS1-mini, despite heavy scientific pretraining and thinking capabilities, falls below the weakest model from experiments on every task, with reasoning traces frequently truncating before completion.

---


### 176. [Compiled Agency: Frontier General-Purpose Coding Agents Build Winning Game Players from Bare Interaction - from Flappy Bird to StarCraft II and Civilization](https://arxiv.org/abs/2609.18996)

**<font color=#1a73e8>作者：</font>** Joey Xiao, Haonan Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents have repeatedly struggled to convert knowledge of a game into competent play, even when researchers build the agent around the model - supplying perception, memory, skill libraries, planners, or executable-policy scaffolds. Rapid progress in coding agents raises two sharper questions: can frontier models now win games at all, and can they win them unaided, building the entire player themselves? We introduce Gauntlet, a develop-freeze-evaluate framework that ports games from small arcades to full commercial-scale titles, behind one deliberately bare contract: a general-purpose coding agent receives a game description, a raw observation/action interface, and an empty policy file - no strategy, no algorithm, no architecture. In a single autonomous session the agent experiments with the live game and engineers a standalone controller; we freeze the result and score it on held-out instances with zero model calls during play. On an unpublished procedural roguelike, held-out success spans 0-86 percent and exposes a sharp generational threshold: every observed session of a newest-generation system outperforms the best session of its predecessor. At full-game scale, a compiled raw-API controller defeats every fair StarCraft II built-in AI and two cheating variants, and single-session programs win complete games of Civilization (Freeciv) by total conquest on held-out seeds. Though at modest rates against novice AI, this is a first: no prior language-agent system had won full games of this genre standalone, without per-turn model calls and a hand-crafted tactical layer. Frontier coding agents begin to track long-horizon strategy. The frozen programs are inspectable. We call this capability compiled agency: development experience compiled into a persistent executable agent whose architecture is built by the model.

---


### 177. [One Axis, No Brake: Self-Knowledge Limits the Filtering of Harmful Peer Conformity in LLMs](https://arxiv.org/abs/2609.18998)

**<font color=#1a73e8>作者：</font>** Yibo Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems are expected to be more reliable because agents can catch each other's mistakes. But peer pressure cuts both ways: the same correction that fixes a wrong answer can overturn a right one. The tempting safeguard is a brake that keeps the beneficial revisions and blocks the harmful ones. We show this brake is hard to build, for a simple reason: a revision is harmful exactly when the original answer was right, so deciding whether to block it is the same as knowing whether the model was already correct. This turns the open-ended hunt for a brake into one measurable quantity, the model's self-knowledge: any brake built from a deploy-time signal is a correctness probe in disguise, and self-knowledge is far from perfect (AUROC $\approx 0.64$--$0.89$ across six model families). We call this ceiling the wall. Even white-box steering of the model's own correctness direction does not breach it: it changes how often the model revises, but harmful and beneficial revisions move together. At population scale the wall becomes the cliff: when most agents start wrong, debate amplifies the shared mistake into a confident, wrong consensus. In our multiple-choice societies, more agents, more model diversity, and a stronger member do not fix it. What helps is adding information before the revision, not filtering after it. Local agreement is not global correctness.

---


### 178. [Capability Emergence Can Be Forecast: Per-Seed, In Advance, With Calibrated Intervals, Certified False Alarms, and a Blind Pre-Registered Gate](https://arxiv.org/abs/2609.19000)

**<font color=#1a73e8>作者：</font>** Gunner Levi Howe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emergent capabilities are widely treated as unpredictable: loss improves smoothly while abilities appear abruptly. Prior work offers early-warning indicators but never scores them as forecasts: no lead time at controlled false-alarm rate, no calibration, no negatives, no blind tests. We supply that discipline and show that, in grokking model systems and small language models, emergence timing is forecastable per run, in advance, with calibrated uncertainty. Across 30 transformers at identical configuration, the formation time of the previous-token head forecasts each seed's induction-head emergence at Spearman rho=0.977 with median lead 975 steps (~15% of training); a best-case loss rule ties the ranking with 50-step lead (a nowcast). Conformal intervals covered 15/15 held-out seeds, and the frozen rule passed blind pre-registered gates on TWO never-seen configurations (10/10 and 9/10 coverage). A trap-language rung then attacked our own rule as pre-registered: where previous-token context pays for the task itself, the bare precursor false-alarms on 10/10 capability-blocked runs, while the mechanism-composed conjunction is certified in both language classes (0 false alarms) and times emergence at rho=1.000. Finally, a gap-origin study broke the fixed offset (both lr and batch move the gap ~2.3x; no external clock owns it) and revealed the law beneath: across 80 valid-anchor runs the anchor fires at 0.843 of time-to-emergence -- t_event ~= 1.19 x t_anchor -- and this multiplicative rule passed its own blind gate (5/5) at a third unseen configuration. False alarms are certified against 33 manufactured negatives. The precursor leads across 3 public model families (Pythia, OLMo, OLMo-2; 7 suites), with OLMo-2 at 1B tokens showing precursor formed, capability absent. Four pre-registered kill criteria fired and are reported. Every freeze precedes its data in a public commit chain.

---


### 179. [CompileRover: Revolutionizing Virtual Machine Compiler Optimization with a Tri-Role LLM-Driven Framework](https://arxiv.org/abs/2609.19004)

**<font color=#1a73e8>作者：</font>** Mingqiao Mo, Yunlong Tan, Hao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Code optimization plays a crucial role in the development of virtual machine compilers, with optimization frameworks significantly enhancing the performance of generated assembly code. However, existing virtual machine compiler outputs frequently exhibit redundant computations, inefficient loop structures, and suboptimal function implementations, which collectively impair execution efficiency. To address these shortcomings, we propose CompileRover, an advanced optimization framework specifically designed for virtual machine compilers. CompileRover employs a sophisticated three-role collaboration mechanism, comprising a referee, an advisor, and an operator, effectively overcoming performance bottlenecks by leveraging comprehensive optimization algorithms and novel methodologies, including control flow analysis, code structure transformations, and dynamic execution pattern recognition. Extensive evaluations demonstrate that CompileRover consistently surpasses state-of-the-art virtual machine compilers, achieving significant improvements in execution performance across various benchmarks. Furthermore, performance analyses validate that the introduced optimizations notably reduce execution overhead, improve dataflow consistency, and robustly enhance compiler performance, showcasing CompileRover as an effective and reliable approach to optimizing virtual machine compilers.

---


### 180. [WordPolo: Evaluating Language Models Through Iterative Semantic Feedback](https://arxiv.org/abs/2609.19006)

**<font color=#1a73e8>作者：</font>** Tyler McDonald, Ali Emami  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) and Large Reasoning Models (LRMs) are typically evaluated on challenging benchmarks through dataset accuracy alone, providing no insight into the quality or faithfulness of their reasoning processes. We present WordPolo, a word-finding task where participants must discover an unknown target word using semantic similarity feedback. Players start with zero knowledge, make guesses, and receive distance scores (1 = correct, higher = further away). Success requires interpreting scores to navigate semantic space and systematically narrow the search. This design makes iterative reasoning and adaptive search strategies both directly observable and necessary for success. We evaluate recent LLMs (GPT-4.1, Llama 4, Claude 3.5 Haiku, Qwen 3), LRMs (o4-mini, Deepseek-R1), humans, and a novel heuristic on 1,500 puzzles. Beyond solve rates (which range from 4% to 62%), we introduce progression-based metrics that reveal models often make meaningful progress, insights that accuracy alone would miss. Our analysis shows how reasoning models can be hindered by overthinking and underthinking, while successful models exhibit human-like strategies. WordPolo demonstrates the need for benchmarks that test both reasoning process and outcomes, providing holistic measurements of model capabilities. Our code and dataset can be found at this https URL.

---


### 181. [TalkMatrix: Generating Character Dialogue that is Both Consistent and Diverse](https://arxiv.org/abs/2609.19022)

**<font color=#1a73e8>作者：</font>** Ayuto Tsutsumi, Yuu Jinnai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Candidate-based decoding typically selects a completion for each prompt independently, but many applications require a collection of outputs that satisfies global, non-decomposable requirements. We formulate this setting as structured multi-prompt, multi-completion selection: given a candidate pool for every prompt, select one completion per prompt to optimize a collection-level objective. We instantiate the problem in character dialogue, where each character should remain consistent across situations, each line should fit its situation, and characters and situations should remain distinguishable. Our method, TalkMatrix, generates multiple candidates for every character--situation pair and jointly selects a complete matrix using four embedding-based consistency and diversity objectives. Because a weighted sum can improve some dimensions by sacrificing another, TalkMatrix maximizes the worst-performing objective through a two-level minimax formulation. We approximately optimize the resulting discrete objective with multi-start coordinate ascent, and compare it with local, partial-matrix, and generic combinatorial search baselines. We run experiments on $50$ synthetic role-playing scenarios and $25$ curated board game scenarios where multiple characters interact in predefined situations. An LLM-as-a-judge rates matrix-level selection higher than random and independent cell-level selection baselines. These results show the value of structured selection for globally controlled dialogue generation, while our empirical validation remains specific to role-playing scenarios.

---


### 182. [Entropy in Conversational AI: Structured Unpredictability as Inferrable Interiority](https://arxiv.org/abs/2609.19044)

**<font color=#1a73e8>作者：</font>** Sebastian Cochinescu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sampling can increase response diversity without producing history-dependent behavior. We formalize a different design target, structured unpredictability, as conditional dependence between an output and a persistent hidden state beyond what an observer can infer from the transcript. A selection layer updates a low-dimensional style-and-attention state from a capacity-limited stream, generates several responses with a fixed base model, and selects for novelty and state affinity. Evaluation uses scripted sequences of independent prompt turns: the base model receives the current turn and rendered state, but not the preceding dialogue; cross-turn dependence resides in the wrapper state and response selector. A synthetic implementation validates the pipeline and matches four prospectively hash-frozen divergence features at point level. In the final real-model grid (mlx-community/Qwen2.5-1.5B-Instruct-4bit; 56 sequences per arm), the mechanism increased lexical novelty over the low-variance and consistency-only controls by 0.073 and 0.023, respectively. Its stylometric-consistency contrast with novelty-matched sampling was equivalent to zero under the registered smallest-effect rule, so the joint novelty-consistency criterion failed. The original two-part accumulation criterion also failed; a revised final-grid contrast, frozen after the powered grid, found higher consistency than the memory-reset ablation (0.028, 95% CI [0.018,0.039]), but does not establish path dependence. Twin separation was not established (0.003, 95% CI [-0.011,0.019]); the mean curve's saturating curvature matched the frozen prediction, which without separation does not support path dependence. Probe-level capability equivalence held within +/-0.10 on a near-ceiling battery, while output quality was not evaluated. All outcomes are machine-scored; no claims about perceived mind or consciousness are tested.

---


### 183. [MIRAGE: How Conversation State Shapes Historical Evidence Use in Multimodal Personal Agents](https://arxiv.org/abs/2609.19059)

**<font color=#1a73e8>作者：</font>** Yu Liu, Wenxiao Zhang, Cheng Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language model (MLLM) agents are increasingly used as personal assistants for long-running tasks. Their utility depends on continuity: agents must retrieve and use earlier evidence across dialogue, files, and workspace state. However, agents can generate plausible answers even when access to that history has degraded, causing outcome-only evaluation to overestimate true evidence use. We present MIRAGE (Multimodal Interaction Retrieval, Attribution, and Grounding Evaluation), a controlled study of historical evidence use under conversation-state variation in multimodal personal agents. MIRAGE holds evidence objects, questions, and scoring fixed while varying only conversation state, and evaluates whether an agent can determine answerability, recover the correct source, and answer from it. Across seven frontier and open-weight multimodal backbones, we find that: 1) pre-compaction depth and post-compaction continuation form distinct, non-monotonic failure regimes rather than a single degradation curve; 2) open-weight models rely heavily on context continuity and are reluctant to spontaneously switch to tool-mediated retrieval when provenance fails; and 3) retrieval pressure improves source attribution in deep pre-compaction states for tool-compliant models, but consistently regresses after compaction, where stored evidence has already degraded. These findings show that historical evidence use should be evaluated under state variation, rather than inferred from outcome-only correctness.

---


### 184. [Reading Between the Lines: Can LLMs Discover the Question Behind the Text?](https://arxiv.org/abs/2609.19070)

**<font color=#1a73e8>作者：</font>** Claudiu Creanga, Liviu P. Dinu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces ``question archaeology'', a specific evaluation task focused on inferring the single, authentic "genesis question" that motivated the creation of a complete text. Distinct from question generation, which targets any plausible question, or discourse frameworks that model utterance-level acts, our task assesses a model's grasp of authorial intent. We present a new dataset of commissioned texts paired with their original research questions and plausible distractors. Our evaluation of both proprietary models, like Gemini Flash and Pro, as well as open source models like Mistral and Qwen, reveals significant progress in this task, with the newer versions outperforming the earlier ones, while BERT-based models performed poorly. Notably, our findings indicate that current LLMs surpass human performance on this task, suggesting advanced understanding of authorial intent. This capability has important implications for AI's role in tasks requiring nuanced interpretation of human communication. Our work thus provides a new framework and a challenging benchmark for future models.

---


### 185. [Benchmarking Large Language Models for Biomedical Relation Extraction](https://arxiv.org/abs/2609.19071)

**<font color=#1a73e8>作者：</font>** Claudiu Creanga, Teodor Marchitan, Liviu P. Dinu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting SNP-phenotype associations from biomedical literature is vital but challenging. We benchmarked diverse NLP models, including MLMs, hybrid architectures, and state-of-the-art LLMs (Gemini 2.0, OpenAI O-series, Qwen, Mistral), on the SNPPhenA corpus across three tasks: sentence-level, abstract-level, and association strength classification. OpenAI O1 achieved state-of-the-art (SOTA) results using few-shot learning for non-finetuned sentence-level classification (F1 0.89) and established a new SOTA for abstract-level classification (F1 0.82). Association strength classification proved difficult, though fine-tuned Gemini 2.0 Pro performed best (F1 0.60) in the first LLM evaluation of this task. Proprietary LLMs, especially in few-shot (O1) or fine-tuned (Gemini 2.0 Pro) settings, significantly outperformed other models. These findings confirm the power of modern LLMs for genomic knowledge extraction.

---


### 186. [Safety-Flag: A Unified Benchmark for the Reliability and Calibration of LLM Content Moderators](https://arxiv.org/abs/2609.19072)

**<font color=#1a73e8>作者：</font>** Yibo Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for content moderation, but most evaluations still report aggregate accuracy on individual benchmarks. We introduce Safety-Flag, which places seven widely used safety benchmarks (BeaverTails, XSTest, Ethics, WildGuard, Aegis, ToxiChat, and ToxiGen) into a single balanced flag / do-not-flag protocol. We release item-level decisions and confidence scores for six general-purpose LLMs and four dedicated guards, together with three reference models, evaluated on the same items. Safety-Flag measures three dimensions of moderator reliability: error direction, probability calibration, and confidence-based error ranking for human review. They often disagree. Aggregate accuracy does not reveal error direction: one model flags $85\%$ of benign content, whereas another misses $54\%$ of harmful content. All six general-purpose models are overconfident; fitting one temperature per model reduces calibration error by $2.8$--$6.0\times$ without changing predicted labels or confidence ordering. Confidence-based abstention lowers selective risk for every model, although the gains depend on how well confidence ranks errors. Dedicated guards produce fewer false alarms and are better calibrated, but several have higher miss rates outside their documented coverage. We release the benchmark, fixed item lists, evaluation code, per-item model outputs, and leaderboard at: this https URL.

---


### 187. [MUSE: Benchmarking Large Vision-Language Models on Multi-Modal Understanding in Situated Education](https://arxiv.org/abs/2609.19088)

**<font color=#1a73e8>作者：</font>** Luyao Zhu, Xun Wei Yee, Wei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large vision-language models have achieved remarkable progress in multi-modal understanding, yet their capabilities in educational settings remain insufficiently evaluated. In AI-assisted language learning, models must interpret artistic imagery, understand its semantic, affective, and cultural content, and reason about visual context to support meaningful interaction. However, existing benchmarks primarily focus on real-world images or domain-specific educational reasoning, providing limited coverage of artistic educational content. To address this gap, we introduce MUSE, a benchmark for evaluating large vision-language models on artistic image understanding in situated educational applications. MUSE decouples image annotation from question generation, enabling diverse tasks with controllable difficulty while reducing annotation effort. It comprises twelve tasks spanning visual perception, semantic and affective interpretation, culture understanding, and compositional reasoning, together with diverse artistic images deliberately curated to center Singaporean and Southeast Asian multicultural contexts alongside Western art traditions, covering multiple themes and difficulty levels. Evaluation of open-source and proprietary models reveals substantial disparities across capability dimensions, particularly in affective interpretation and compositional reasoning. Our analysis further identifies common failure modes and key challenges for developing trustworthy multi-modal models for education. We hope MUSE will serve as a standardized benchmark for advancing multi-modal understanding in situated educational applications.

---


### 188. [When Agents Look Like Beacons: NIDS Evasion by Model Context Protocol Traffic](https://arxiv.org/abs/2609.19091)

**<font color=#1a73e8>作者：</font>** Muhammad Abdullah Sohail  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) standardizes communication between autonomous Artificial Intelligence (AI) agents and remote tools over Streamable HTTP. This shift introduces a class of machine-generated, authenticated, and high-frequency JSON-RPC traffic directly into enterprise networks. Enterprise network defenders have historically relied on machine-like cadence as an Indicator of Compromise (IoC). In this study, we show that without explicit network-layer indication, MCP traffic structurally and temporally resembles Command and Control (C2) beaconing behavior, specifically the polling architectures used by advanced persistent threats like Cobalt Strike. Counter to theoretical assumptions about machine-generated polling, our measurements reveal a visibility gap: standard enterprise Intrusion Detection Systems (IDS) and behavioral beacon-scoring frameworks do not classify MCP remote tool usage as anomalous within our testbed scope. Through a controlled Docker-based testbed simulating eleven mathematically defined traffic profiles across three TLS conditions (Opaque, TLS-Inspected, and Cleartext), we evaluate Suricata signature matching and RITA behavioral scoring against MCP JSON-RPC patterns. Our results show that MCP traffic, regardless of temporal smearing (jitter) or TLS inspection visibility, evades detection within this configuration, yielding a consistent 0.0 behavioral beacon score and near-zero IDS content alerts under the Emerging Threats (ET) Open ruleset. While opaque TLS obscures HTTP content, it exposes agent traffic to flow-level temporal analysis; however, NIDS heuristics tuned to identify traditional malware do not flag the lognormal inter-arrival distributions characteristic of generative AI reasoning loops. To address this gap, we propose an agent-native network indication standard including Agent-Native ALPN and standardized out-of-band headers.

---


### 189. [Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations](https://arxiv.org/abs/2609.19101)

**<font color=#1a73e8>作者：</font>** Leon Bergen, Usha Bhalla, Andrew Lee 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As models scale, reward hacking becomes more frequent, more sophisticated, and more consequential. Does it leave a telltale signature in model representations? This work analyzes how reward hacking is represented internally in frontier open source LLMs, and how those representations can be used to understand and discover the range of hacking behaviors a model displays. In particular, we find that simple difference of means vectors coherently represent reward hacking in Kimi K3, GLM 5.2, and Qwen 3.8 Max across a variety of behaviors in common evaluations. Despite their simplicity, these vectors are both generalizable and interpretable, and we can use them to reliably detect reward hacking. We first evaluate reward hacking in commonly reported benchmarks like DeepSWE and SWE-bench, finding that models reward hack excessively in these environments; GLM 5.2 hacks in 57.2% of rollouts on DeepSWE and in 73% of rollouts on SWE-bench. Catching these requires monitors; LLM monitors are effective, but expensive detectors. We show that DoM vectors are similarly effective but virtually free, catching 3.1% more hacks in Kimi K3 and 7.9% fewer hacks in GLM 5.2 on DeepSWE at a monitor matched false positive rate. DoM vectors run on the chain-of-thought also predict reward hacks in the model's subsequent actions, meaning we can run them online and catch potential hacks before they occur. Finally, we analyze probe-hits that LLM monitors do not catch and discover other undesirable behaviors, as well as show transfer to finding hacks in non-SWE evaluations. Together, these results provide evidence that simple, white-box methods can be used to scalably study and monitor reward hacking behaviors in frontier open source models

---


### 190. [How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents](https://arxiv.org/abs/2609.19107)

**<font color=#1a73e8>作者：</font>** Zixi Chen, Akshay Vegesna, Samip Dahal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws predict how loss decreases with increases in computation. We show, contrary to conventional wisdom, that architectural interventions can modify scaling exponents in pre-training, leading to exponential improvements in performance with increases in computation. As an anchoring point, we consider the architectural formulation of looped transformers. Although not typically used in this way, looping, also known as recursive depth, provides a mechanism for model growth, by increasing the number of loops during training. Model growth, with and without shared weights, provides the biggest changes to the scaling exponents. In particular, a 7.4B model growth architecture matches GPT-3 13B on CORE with roughly $20\times$ less compute, and has compute efficiency gains that increase with scale. Moreover, simply using a boundary operator in a vanilla transformer, which normalizes and injects an earlier block, also provides increasing compute-efficiency gains, although to a lesser extent. In the data-constrained, multi-epoch setting, standard looping has a useful regularizing effect, where we find it is compute-optimal to increase the number of loops with scale. These results can be understood through the lens of computational depth: for a given computational budget, we wish to increase the usable depth of the transformer, which can lead to efficiency gains that increase with scale.

---


### 191. [Playing log(N)-Questions over Wikipedia Abstracts: Communication Efficiency Between Paired Frontier Models](https://arxiv.org/abs/2609.19113)

**<font color=#1a73e8>作者：</font>** Peter Potash  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We evaluate six frontier language models on the two-agent $\log(N)$-Questions game. A questioner sees $N$ Wikipedia lead paragraphs and must identify a secretly chosen target using exactly $\log_2 N$ yes/no questions. An answerer sees only the target and the question, and replies with one word. Both roles run on the same provider, so the game measures how well a model communicates with itself across an information asymmetry. We run 408 games over document sets of 4 to 1024 paragraphs at a total API cost of \$363. One model finishes well behind the others: Claude Opus 5 wins 28 of 68 games, against 45 to 56 for GLM-5.3, GPT-5.6 Sol, Grok 4.6, Gemini 3.8 Flash and Kimi K3. The leading five are only marginally separable. Pooling those five, win rate declines with set size at $r=-0.973$ and is fit by a single per-round reliability parameter. The form is $\text{win}=p^{\log_2 N}$ with $p=0.928$. Losses divide into answer errors and discrimination failures in roughly equal measure, and models almost never name a document their own evidence excludes. Every unanimous answer error from the weakest model was inspected: 32 of 34 are ``No'' answers, on properties stated in the document's first sentence, under an instruction that explicitly warns against defaulting to ``No''. Information per question, estimated from answer balance, correlates with win rate at $r=+0.88$. The only two models to extract a full bit per question are the only two that partition on document titles, a strategy absent below $N{=}32$ and used in a quarter of questions above it. Reasoning-token expenditure varies $4.5\times$ across models with little relation to success, and the trace grows as the candidate set shrinks without a matching gain in reliability.

---


### 192. [Affora: A Design System for Agent-Friendly Interfaces](https://arxiv.org/abs/2609.19125)

**<font color=#1a73e8>作者：</font>** Jin Gao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computer-use agents increasingly operate software designed for people, but interfaces often leave actions or task state unclear to machine readers. We present Affora, a design system that supports both readers while preserving visual freedom and familiar human workflows. Three controlled studies examine component implementations, visual variation, and interaction-design principles. Their findings inform guidance from individual components to complete sites, supported by reusable implementations and executable checks. Agent performance depends on the interaction meaning available through its interface representation; substantial visual variation remains possible when that meaning is preserved. Evaluation on independently authored interfaces shows gains where Affora addresses existing deficits, but limited effects where those deficits are absent or outside its coverage. A workflow case provides preliminary evidence of reduced interaction cost. Affora connects user experience and agent experience through a shared interface rather than a separate agent-only surface.

---


### 193. [EarStreAM: A Closed-Loop Earable System for Personalized Stress-Adaptive Meditation](https://arxiv.org/abs/2609.19127)

**<font color=#1a73e8>作者：</font>** Jonas Hummel, Luisa Faust, Elias Müller 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present EarStreAM, a closed-loop earable system for stress-adaptive meditation that integrates in-ear physiological sensing with personalized, real-time intervention. Leveraging OpenEarable 2.0's multimodal sensing, EarStreAM continuously monitors physiological signals and detects elevated stress from heart rate and heart rate variability. Upon detection, the system initiates a personalized guided meditation generated by an LLM and adapted in real time to the user's stress state. The demo offers a hands-on experience of stress-adaptive meditation in two modes: a biosignal-adaptive meditation with optional stress induction to illustrate closed-loop adaptation, and a meditation-only mode focusing on EarStreAM's generative personalization capabilities. The demo highlights how in-ear sensing, closed-loop adaptation, and personalized generative meditation can be integrated into an earable system for real-time stress support in demanding office work contexts.

---


### 194. [Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection in Interactive Environments](https://arxiv.org/abs/2609.19128)

**<font color=#1a73e8>作者：</font>** João Meneses dos Santos, Arlindo L. Oliveira  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents remain brittle in interactive environments, where success requires long-horizon state tracking, valid action execution, and recovery from failed steps. We extend SwiftSage, a dual-process agent that combines a fast action proposer with a slower planner, using two modular cognitive extensions: an Adaptive Memory Module (AMM) for salience-gated episodic storage and trigger-driven retrieval, and a Self-Reflection Module (SRM) for bounded execution-time validation and corrective intervention. Both modules are implemented as feature-flagged extensions over the same execution substrate, enabling controlled ablations on ScienceWorld. Across four configurations---baseline, baseline+AMM, baseline+SRM, and the full system---the full system achieves the best mean final score (64.62), success rate (43.17%), and successful-step efficiency (19.33 steps), while SRM is the strongest standalone contributor. The results suggest that execution-time control is the dominant bottleneck in this setting, while episodic memory becomes most useful once the runtime loop is stabilized.

---


### 195. [In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138)

**<font color=#1a73e8>作者：</font>** Dongzhou Cheng, Taoran Yi, Ye Fang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Enabling robots to adapt to unfamiliar environments as readily as humans remains a moonshot goal of embodied AI. No finite collection of demonstrations can cover every task and situation a robot will encounter, making the ability to learn from context at deployment essential for generalization. Such in-context learning (ICL), however, remains largely beyond the reach of existing robotic policies. The broad agentic capabilities of commercial vision-language models (VLMs), such as GPT-6 Astra, raise a compelling question: can these models learn from demonstrations, examples, and interaction feedback, then translate that information into executable and verifiable robot behavior from a new initial state without gradient updates or persistent changes to task-specific parameters? We introduce GPT-Policy, a general-agent framework for in-context robot learning. GPT-Policy integrates a context compiler that preserves task-relevant visual transitions, a VLM that proposes robot-tool actions, and a constrained controller that verifies and executes each action and reports its outcome. We evaluate its reliability and limitations through task success and efficiency metrics, matched comparisons across models, and controlled context ablations. In real-robot trials, human video demonstrations improve task completion even without robot action labels, while aligned action references yield further gains on contact-sensitive tasks. These findings position GPT-Policy as a step toward robot adaptation through in-context learning, providing an empirical foundation for translating the general-purpose capabilities of VLMs into physical behavior and clarifying the challenges that must be overcome for reliable deployment.

---


### 196. [PANORAMA: Panoptic Grounded Captioning via Mask Proposal Selection](https://arxiv.org/abs/2609.19143)

**<font color=#1a73e8>作者：</font>** Sara Pieri, Evangelos Kazakos, Shizhe Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intelligent systems that act in the world require image understanding that is both comprehensive and spatially grounded. Current vision-language models (VLMs) can generate fluent and detailed image captions, but reliably associating them with image pixels remains challenging. Existing methods that combine dense captioning with pixel-level grounding often produce either incomplete descriptions or inaccurate segmentation masks. We study this problem through panoptic grounded captioning, a task that requires a VLM to describe both foreground objects and background regions while grounding each referring phrase with pixel-level masks. We make three contributions. First, we introduce PanoCaps, a human-annotated benchmark constructed from panoptic segmentation datasets. It provides dense captions with near-complete pixel coverage and image-text alignments at the entity level, supporting both training and evaluation. We further propose a phrase-mask matching protocol and a generalized Panoptic Quality (gPQ) metric that jointly evaluates textual and mask agreement. Second, we formulate phrase grounding as selection from a phrase-conditioned pool of mask proposals and introduce PANORAMA, a VLM that conditions a pretrained segmenter on contextualized phrase representations to obtain candidate masks and learns to select those corresponding to each phrase. Training this interface jointly with caption generation enables PANORAMA to produce high-quality masks while allowing each phrase to refer to a single region or multiple instances. Third, PANORAMA achieves the best overall grounding on PanoCaps and matches or exceeds specialized models across several pixel-level grounding tasks. Experiments show that our method produces precise entity-level segmentations while maintaining detailed, mask-consistent captions. Code, data and models are available at this https URL.

---


### 197. [A Zeroth-Order Paradigm for LLM Preference Alignment](https://arxiv.org/abs/2609.19144)

**<font color=#1a73e8>作者：</font>** Peter Chen, Xi Chen, Wotao Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct preference alignment methods are widely used to align large language models (LLMs) with human preferences because of their computational and memory efficiency. However, likelihood displacement motivates alternative ways to extract information from preference pairs with small likelihood margins. In this paper, we propose and analyze Comparison-based Preference Optimization (ComPO), a zeroth-order alignment method based on comparison oracles. ComPO extracts directional information from these pairs without directly optimizing a differentiable preference loss on them. We establish a convergence guarantee for its basic offline scheme under smoothness, gradient sparsity, and compatibility between the oracle and a latent objective. We further introduce online ComPO, which retains the offline comparison mechanism and uses unlabeled policy generations for reverse-KL control relative to a reference policy. Following the coverage perspective of preference fine-tuning, we establish a performance guarantee for a basic constrained scheme under local coverage and in-distribution pairwise reward accuracy. Experiments on Mistral, Llama, Gemma-2, Qwen3, and Gemma-3 models demonstrate improvements over existing direct alignment methods, including length-controlled win rates, with pair-level diagnostics providing evidence consistent with mitigating likelihood displacement.

---


### 198. [Objective vs. Search: Decomposing What Makes a Good Tokeniser](https://arxiv.org/abs/2609.19145)

**<font color=#1a73e8>作者：</font>** Ahmetcan Yavuz, Clara Meister, Tiago Pimentel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Two dominant tokenisation algorithms are used by modern language models: byte-pair encoding (BPE) and UnigramLM. These differ along two orthogonal axes: their optimisation objective (compression vs. log-likelihood) and their search procedure (bottom-up merging vs. top-down pruning). Existing comparisons confound these axes, making it unclear whether their observed differences stem from what is being optimised vs. how it is being optimised. We disentangle the two by introducing two new tokenisation algorithms that complete this 2x2 design space: BottomUpLL, a bottom-up likelihood-based tokeniser, and TopDownComp, a top-down compression-based tokeniser. We train language models with tokenisers produced by each algorithm, varying: model size, vocabulary sizes, and domain (English-only vs. multilingual). Evaluating models on bits-per-byte, we find that the search procedure -- not the objective -- is the dominant factor: bottom-up tokenisers consistently achieve lower bits-per-byte in most settings. Evaluating models on the BLiMP task, however, shows no consistent relationship between design choice and performance. Overall, our results disentangle the effect of tokeniser design choices on language modelling performance, offering concrete guidance for their more principled construction.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 199. [Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents](https://arxiv.org/abs/2609.17653)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bofan Chen, Boxuan Zhang, Fei Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GUI agents execute long-horizon tasks on dynamic graphical user interfaces, where pop-ups, delayed loads, and relocated widgets routinely invalidate plans fixed before execution. Recent agent-skill frameworks encapsulate reusable procedural knowledge to mitigate this, yet existing skill designs are largely developed without targeting GUI execution dynamics and treat skills as static artifacts produced before deployment rather than living procedural knowledge that improves through it. We argue that what GUI agents need is not better static skills, but skills that can be revised from execution feedback at deployment time, without additional training. We propose \textbf{EvoSkill-GUI}, a training-free framework in which each skill is a structured multi-file package containing retrieval metadata, executable plans, backup localization, failure-recovery rules, accessibility utilities, and failure cases. EvoSkill-GUI operates through a \textbf{\emph{reflect-revise-reuse}} loop: the executor performs instant in-rollout revisions, an isolated critic diagnoses failed trajectories under strict information isolation, and the executor edits specific skill files through a restricted tool interface. Across MobileWorld, AndroidWorld, and OSWorld, three mainstream GUI benchmarks spanning mobile and desktop platforms, EvoSkill-GUI consistently improves multiple base models without any training, with maximum gains of $+16.2\%$, $+6.0\%$, and $+10.5\%$ respectively, and evolved skill libraries continue to benefit related tasks rather than being rebuilt from scratch. Our code is available at this https URL.

---


### 200. [Dataset-Dependent Effects of Cross-Depth Aggregation and Soft-Routed Experts in EEG Foundation Model Fine-Tuning](https://arxiv.org/abs/2609.17886)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingyang Jiang, Yamin Li, Daniel Moyer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG decoding tasks can rely on different temporal dynamics and cross-channel relationships. We test whether specialized modules improve a fully fine-tuned EEG foundation model by augmenting CBraMod with cross-depth Attention Residuals (AttnRes) and two soft-routed expert banks. Across matched three-seed experiments on FACED, ISRUC, SEED-V, and PhysioNet-MI, the complete model changes mean balanced accuracy relative to full fine-tuning by -0.12, +1.27, +0.77, and -1.27 points, respectively. AttnRes alone improves mean balanced accuracy on three datasets, whereas adding experts on top of AttnRes helps only FACED and SEED-V. These gains come with substantial overhead: AttnRes requires 2.11 to 2.88x runtime and 1.78 to 2.67x memory, while the complete model requires 2.41 to 3.04x runtime and 1.86 to 2.85x memory. Overall, the added modules produce dataset-dependent, sometimes opposing effects rather than consistent gains over full fine-tuning.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-210](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
