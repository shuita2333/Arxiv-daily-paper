# 🧠 大模型相关研究 | 2026年09月09日

> 本类共 **179** 篇论文：已确认 **171** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-179**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-179**

---

### 151. [Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference](https://arxiv.org/abs/2609.05275)

**<font color=#1a73e8>作者：</font>** Mostafa Elhoushi, Alex Pretko, Nolan Dey 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Layer dropout (a.k.a. stochastic depth) has been shown to enable faster training, higher accuracy, and robustness to zero-shot layer pruning in both language and vision transformers. However, as models and datasets have scaled, dropout - particularly layer dropout - has largely disappeared from large language models (LLMs) pre-training recipes. While some prior work has reported that dropout can degrade accuracy, no comprehensive study has quantified, let alone mitigated, this effect. In this study, we show that layer dropout should be used in state-of-the-art LLM training, establishing best practices and scaling analysis for both training and post-training benefits. Concretely, with optimal layer distribution, time schedule, and optimizer hyperparameters, we observe that at the same training FLOPs layer dropout leads to lower loss. For a given number of training steps, LLMs can achieve lower or similar validation loss while saving upto 25% of training FLOPs. Moreover, layer dropout enables significant post-training optimizations, such as early exit, intermediate-layer skipping, and self-speculative decoding, yielding up to 1.5x inference speedup with negligible accuracy loss. Across more than 2400 training experiments, spanning models from 271M to 8.2B parameters and datasets up to 160B tokens, we demonstrate that these findings extend reliably to large-scale training regimes. All pre-training experiments were run on Cerebras CS-3 systems.

---


### 152. [Testing Interchangeability in LLM Agent Teams](https://arxiv.org/abs/2609.05279)

**<font color=#1a73e8>作者：</font>** Jianxin Gao, Tianyi Yu, Linna Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production multi-agent systems replace agents constantly, on the assumption that an agent filling a role is interchangeable with any other agent that can do the job. We test that assumption. Eight teams per setting are formed independently from one base model on the same tasks, each agent keeping a private notebook across ten formation episodes; we then trade role-matched agents between teams and measure what changes on held-out tasks. Against a placebo that reproduces the disruption of a roster change without changing who occupies the seat, a swap costs little in task score but raises the communication a team spends per unit of progress by 16 to 63 percent, and in Hanabi a swapped agent is more expensive than an inexperienced one, consistent with interference from conventions learned with its former partner. In Collab-Overcooked, when the agent that sets the agenda is replaced, most of the extra communication comes from the agent that stayed. Three ablations, over base models, decoding temperature and formation length, move the swap penalty alongside one other quantity: how far independently formed teams drift apart. Greedy decoding lowers both; doubling a team's history raises both. In these settings, agents are more fungible in task outcome than in coordination efficiency, with larger swap effects after longer formation histories.

---


### 153. [GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity](https://arxiv.org/abs/2609.05284)

**<font color=#1a73e8>作者：</font>** Shuang Liang, Xin-Yu Hu, Xiang-Jun Ou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed great advances in the reasoning ability of Large Language Models (LLMs). However, the reasoning processes of LLMs often exhibit uncertainty, where LLMs often produce a proliferation of divergent branches at each reasoning step even when fed the same prompting inputs, and certain branches exhibit evidently incredible, even nonsensical, reasoning chains and results. In this paper, we propose the Graph-complexity-based UncerTainty (GUT) method for investigating the reasoning uncertainty of LLMs. The key idea of GUT is to characterize the potential branches of each reasoning chain with a directed acyclic graph, thereby ensuring that all potential branches are comprehensively covered within the graph space. Building upon this recognition, we further build two modules of GUT, that is, a Quantification (GUT-Q) module and an Optimization (GUT-O) module, for quantifying and reducing the reasoning uncertainty of LLMs, respectively. GUT-Q measures LLM reasoning uncertainty by approximating the reasoning space complexity with graph complexity. GUT-O implements uncertainty optimization by treating negative uncertainty as the reward function in reinforcement learning. Experimental results conducted on four LLMs and five datasets validate the effectiveness of GUT.

---


### 154. [Beyond Aggregate Scores: Behavioral Correctness Assumptions for Assessing Reference-Based Automatic Evaluation Methods](https://arxiv.org/abs/2609.05289)

**<font color=#1a73e8>作者：</font>** Maria Mahbub, Ashley Rice, Michael R. Munroe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated reference-based evaluation methods play a critical role in assessing natural language generation systems. Existing meta-evaluation primarily measures agreement with human judgments or benchmark labels, providing limited insight into evaluator behavior under controlled conditions. We introduce behavioral correctness assumptions, a complementary framework for evaluating reference-based automatic evaluation methods. We define a taxonomy of correctness-preserving and correctness-altering assumptions and operationalize them through controlled response transformations that specify expected scoring behaviors. We evaluate diverse lexical, character-level, semantic, LLM-based, and hybrid evaluators and analyze their assumption-level behavior, stability, sensitivity, repeat-run variability, configuration sensitivity, and reproducibility. Our experiments reveal distinct behavioral trade-offs across evaluation paradigms: no evaluator satisfies all proposed correctness assumptions, and evaluators with similar aggregate performance can exhibit substantially different behavioral profiles. These findings demonstrate that behavioral correctness assumptions provide diagnostic information obscured by conventional aggregate meta-evaluation.

---


### 155. [RISE: Recursive Improvement via Self-Extrapolating Policy Distillation](https://arxiv.org/abs/2609.05295)

**<font color=#1a73e8>作者：</font>** Yang Li, Semih Yavuz, Shafiq Joty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides dense, per-token supervision for language model post-training, but its effectiveness is bottlenecked by teacher quality: external teachers suffer from distribution mismatch, while self-distillation with privileged conditioning is limited by in-context learning capacity. We propose \textbf{RISE} (\textbf{R}ecursive \textbf{I}mprovement via \textbf{S}elf-\textbf{E}xtrapolating Policy Distillation), which constructs a synthetic teacher directly from the model's own RLVR training trajectory. By extrapolating the displacement between the current checkpoint and a trailing anchor---in parameter space or output logit space---RISE converts a sparse outcome-induced parameter update into a dense token-level target, without any external model or privileged conditioning. RISE combines RLVR and OPD in a complementary loop: outcome rewards ground the extrapolation toward correct reasoning, while the extrapolated teacher refines token-level decisions. Moreover, since the teacher is refreshed every iteration as the student improves, distillation becomes a recursive improvement mechanism rather than a one-shot compression step. Experiments spanning mathematical reasoning, multi-domain STEM, code generation, and multi-turn agentic tasks show that RISE outperforms RLVR-only training and on-policy self-distillation across all settings.

---


### 156. [How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity Mixing](https://arxiv.org/abs/2609.05309)

**<font color=#1a73e8>作者：</font>** Pengxiang Zhao, Xing Li, Xianzhi Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyper-Connections and their manifold-constrained variant mHC widen a residual pathway from one stream to n, yet how trained models use this capacity remains unclear: how broadly blocks read and write, how strongly the residual pathway mixes streams, and whether the streams carry distinct representations. We examine these properties in the four-stream residual pathway of DeepSeek-V4-Flash using effective stream counts, cross-stream residual weights, and inter-stream cosine similarity. Read/write routing is concentrated but varies across depth: a typical attention or FFN site effectively uses about two streams, while the dominant stream changes across layers and the representations remain directionally distinct. Residual mixing is modest and occurs primarily in early layers; in layers 22-42, the pathway mostly carries each stream forward separately. Targeted interventions establish the functional significance of these patterns. Replacing the late mixers by identity increases C4 perplexity by only 1.9% and preserves the six-task average score, whereas replacing the early mixers increases perplexity by 41%. Fixing each early mixer to its C4 diagnostic mean increases perplexity by only 0.2% and reduces the average score by 0.25 percentage points, showing that its site-specific structure matters more than its token-wise variation on the evaluated metrics. Likewise, retaining the three largest routing weights per token at every site increases perplexity by at most 2.7% and changes the average score by at most 0.4 points. Thus, the studied model realizes only part of the flexibility afforded by four-stream mHC: individual blocks rarely require all four streams, and late residual mixing provides little measured benefit.

---


### 157. [Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness](https://arxiv.org/abs/2609.05314)

**<font color=#1a73e8>作者：</font>** Alexander Neubauer, Tianzhen Hong, Han Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building automation systems generate rich sensor data yet remain insight-poor because heterogeneous point naming, missing metadata, and fragmented documentation obstruct their operational use. This systematic review analyses and codes 66 peer-reviewed studies on large language models (LLMs) for HVAC operations published between 2023 and March 2026. Each study is classified across five application families and three LLM method families and assessed for evidence realism, deployment readiness, and the responsibility boundary between the LLM and physical HVAC decisions. The corpus is concentrated in building energy modelling (BEM, 32 of 66 papers), while load forecasting remains too sparse for subfield-level conclusions. Only four studies reach pilot-level evidence, and none reports sustained operational deployment. No study was classified as ready-now for industry adoption; three were near-term and 63 research-only. Nevertheless, several bounded, human-in-the-loop uses merit near-term trials, including point-name normalisation, document-grounded operator support, BEM workflow assistance, and advisory interfaces around physics-based controllers. Conventional machine learning (ML), model predictive control (MPC), reinforcement learning (RL) and ontology-based tools remain more adopted for high-frequency control, short-horizon numerical forecasting, and well-posed ontology mapping, while autonomous agentic operation and unvalidated occupant proxies remain research-stage. Current evidence therefore supports LLMs primarily as semantic and workflow layers rather than autonomous HVAC controllers. Future work should prioritise field-validated benchmarks, orchestration evaluation under operational constraints, and LLM-MPC/RL architectures with bounded latency and verifiable safety properties.

---


### 158. [LLM-Driven Algorithm Design for Quantum Circuit Synthesis based on Binary Decision Diagrams](https://arxiv.org/abs/2609.05327)

**<font color=#1a73e8>作者：</font>** Yoonju Sim, Federico Berto, Chuanbo Hua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantum circuits are central to implementing quantum algorithms on quantum devices, where quantum gates must be reversible. Many quantum algorithms rely on Boolean functions, which must therefore be implemented reversibly within quantum circuits. Reversible circuit synthesis provides a way to translate such Boolean functions into reversible circuits. Binary decision diagrams (BDDs) offer a scalable approach to this task, but the resulting BDDs and circuits depend heavily on variable ordering. Existing ordering heuristics commonly minimize BDD size because it is closely tied to the circuit size. However, BDD size is an imperfect proxy for the quantum cost of the synthesized circuit (QCC). We propose \texttt{QuantumEvo}, an evolutionary framework that uses an LLM as a heuristic generator for QCC-aware BDD variable ordering. Instead of predicting orderings directly, \texttt{QuantumEvo} searches over ordering heuristics initialized from multiple heuristic families. Candidate heuristics directly manipulate variable orderings using standard BDD operations and are selected by downstream QCC. The discovered heuristic, HGA-QE, modifies the sifting step inside a genetic algorithm so that the procedure is better aligned with QCC. Across the benchmark set, HGA-QE achieves a 70.9\% tie-or-win rate against the per-function best baseline and is strictly best on 13.5\% of the functions. The results demonstrate broadly competitive QCC performance, with HGA-QE showing a clearer relative advantage in strict wins on the two benchmark suites drawn from sources different from the data used for heuristic discovery.

---


### 159. [Technical Manual for a Toolkit for Measuring Contextual Individuation in Transformer Language Models](https://arxiv.org/abs/2609.05333)

**<font color=#1a73e8>作者：</font>** José Luciano Verçosa Marques, Frederico Jorge Heitmann, Daniel Omar Perez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A transformer language model assigns a single, context-independent vector to a word type at its embedding layer, yet is widely believed to individuate that word's occurrences by context in its later layers. Testing this belief cleanly requires a construct that holds the word form fixed while its context and intended sense vary in a controlled, labeled way. This manual documents an open toolkit built around such a construct, which we call a bridge form: a single written word that recurs, unchanged, across two or more subject domains with a different sense in each. We describe, and justify, every stage of the pipeline: the declarative specification of bridge forms and their source domains, corpus acquisition from Wikipedia, occurrence localization, layer-wise representation extraction, a domain-pairwise silhouette measurement of separation in the model's representation space, and a paired visualization protocol. Each design choice is presented together with the methodological failure mode it is meant to avoid (sense contamination from overly broad category labels, the multi-group bias of the silhouette coefficient, subword-tokenization misalignment, and axis-comparability artifacts in dimensionality-reduced plots, among others). This manuscript is a methodological and implementation reference: it does not report or interpret empirical outcomes of running the toolkit on any particular model or bridge-form set. The toolkit, its full source, and the corpora used to exercise it are archived separately (Section 9) under a persistent identifier, and are intended to be cited as an instrument by studies that use it to produce and interpret empirical results.

---


### 160. [The History Is the Detector: Executing CVE Patch History, End-to-End](https://arxiv.org/abs/2609.05335)

**<font color=#1a73e8>作者：</font>** Qiushi Wu, Kevin Eykholt, Youngja Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public vulnerability databases collect rich information about known software flaws, including their weakness types, affected components, and related patches. Fixing commits provide the exact code changes that removed these flaws. While these records capture why the original code was unsafe, they are documented mainly for human inspection rather than automated reuse. Consequently, the same unsafe conditions may still exist elsewhere in code without a known advisory, leaving much of this detection knowledge unused.
We present BUGSTONE-E2E, a framework that transforms vulnerability history into executable detection rules and validates their findings. First, BUGSTONE-E2E mines reusable rules from verified fixing commits, capturing scan anchors, fix semantics, and CVE provenance and organizing them by CWE and language. Second, detection follows a funnel-shaped pipeline: early stages process a large pool of candidates using lightweight analysis, while later stages apply increasingly capable and expensive models to a shrinking set of targets. Specifically, BUGSTONE-E2E first enumerates call sites matching rule anchors using Tree-sitter, then removes benign sites using lightweight heuristics without LLM calls. Next, LLM-based agents inspect the remaining candidates guided by the rule. Following this inspection, the system re-triages surviving candidates and builds runtime verifications, then generates scope-checked patches validated via two-sided differential tests. Using 19,325 high-severity CVEs from 2022 to 2026, BUGSTONE-E2E identifies 2,710 fixing commits and constructs 1,033 detection rules across 56 CWE families, packaged into 172 skills. When applied across 14 programs, it produced runtime evidence for 644 findings. These results demonstrate that CVE history can be turned into an executable workflow, transforming past vulnerabilities into reproducible detection and repair.

---


### 161. [Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability](https://arxiv.org/abs/2609.05339)

**<font color=#1a73e8>作者：</font>** Ankit Goyal, Jaideep Ray  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model upgrades are routine; memory migrations are not. An agent can keep the same memory store and still forget: a new model may interpret old notes differently, mixed embedding versions may break retrieval, and repair may fail without the original evidence. We compare memory as the same history is preserved verbatim for long-context reading (LC-RAW), divided into chunks for retrieval-augmented generation (RAG), compressed by a model into natural-language notes (NOTES), or normalized into a fixed-schema knowledge graph (KG-fixed). The study uses 48 synthetic histories with randomized answer codes, exact scoring, and two open-weight models with sub 10 billion parameters.
Our measurements show that fixed-schema structures transfer reliably, with KG-fixed accuracy changing by only $+0.0004 \pm 0.0020$ following a writer swap. Conversely, compressed NOTES exhibit high model coupling, with accuracy shifting asymmetrically by $+9.91$ or $-13.28$ percentage points depending on the specific migration direction. In RAG systems, partial embedding migrations using a 50/50 mixed index capture only a 4.96-point accuracy improvement, forfeiting the majority of the 11.90-point gain achieved through full re-embedding. Diagnostic decomposition attributes 80% ($0.467 \pm 0.014$) of the NOTES accuracy deficit to information lost during initial construction, whereas retrieval failures drive 81% ($0.364 \pm 0.012$) of the RAG deficit. Finally, store-only repair of NOTES fails to reach a 90% performance recovery target in all 48 test cases, whereas retaining the raw source history enables successful recovery in 34 of 48 cases for one tested direction. These findings highlight the necessity of direction-specific migration testing, strict embedding space isolation, and the retention of source histories for memory repair.

---


### 162. [Who Should Grade My Work? Student Perspectives on Transparent AI-Assisted Writing Assessment in Higher Education](https://arxiv.org/abs/2609.05346)

**<font color=#1a73e8>作者：</font>** Rayed AlGhamdi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of GenAI tools into higher education assessment raises important questions about how students understand, interpret, and respond to AI-mediated evaluation. As instructors increasingly explore AI tools for providing feedback, prior research has examined whether GenAI-generated feedback improves writing performance and how students perceive its usefulness; comparatively little is known, however, about how students interpret such evaluation when they are explicitly informed that an AI system, rather than a human instructor, produced the feedback and the score. This study reports findings from a qualitative pedagogical inquiry conducted in an undergraduate technical communication course for computing students at a Saudi public university. Thirteen male undergraduate computing students completed an in-class handwritten writing task; the scanned submissions were evaluated by ChatGPT using a rubric-based prompt aligned with the task objectives. Students were then explicitly informed that ChatGPT had generated the score and feedback and were invited to reflect on the evaluation in writing. Inductive thematic analysis of these reflections identified four themes: perceived usefulness of feedback; awareness of AI's contextual and pedagogical limitations; conditional trust, distinguishing feedback utility from evaluative authority; and reflection on the institutional and pedagogical role of the human instructor. Participants accepted GenAI feedback as useful for surface-level revision but consistently positioned the human instructor as the appropriate authority over grading decisions. The study identifies this as a distinction between feedback utility and evaluative authority, two judgments that students treat as analytically separate rather than as opposite ends of a single approval scale...

---


### 163. [MEOX: Compact Multimodal Mixture-of-Experts for Earth Observation](https://arxiv.org/abs/2609.05351)

**<font color=#1a73e8>作者：</font>** Mohanad Albughdadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Earth Observation representation learning accommodate heterogeneous sensors and missing observations, often through larger architectures. We present MEOX (Multimodal Earth Observation with eXperts), a multimodal masked autoencoder with a 2.939 million-parameter encoder and 3.115 million parameters in total. Sensor-specific adapters, explicit validity signals, and a shared sparse-expert block preserve modality-dependent processing before a learned patch-wise fusion. Four metadata tokens then accompany a single spatial sequence through fourteen further encoder blocks. Shared expert projections with private low-rank residuals constrain parameter growth, while rotary attention supports downstream spatial grids different from pretraining. The model is pretrained on 1.228 million MMEarth64 samples using modality-balanced masked reconstruction and structured sensor dropout. Frozen transfer is evaluated on six GEO-Bench tasks at both 64 and 224 pixels. The model reaches 64.42% mean intersection-over-union on cashew segmentation at 64 pixels and 90.56% average accuracy on EuroSAT at 224 pixels, exceeding the corresponding reported CSMoE results. BigEarthNet finetuning reaches 72.95% micro-average precision. Routing diagnostics distinguish expert participation, spatial dependence, modality association, and functional contribution. A held-out WorldCover probe measures a 0.64-percentage-point benefit from metadata, while retrieval separates same-sensor semantics from cross-sensor alignment. These results demonstrate sensor-flexible representation learning and strong task transfer using a compact parameter budget.

---


### 164. [Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time Training for Scalable Trade-Up Recommendation](https://arxiv.org/abs/2609.05363)

**<font color=#1a73e8>作者：</font>** Siliang Liu, Mohammad Ghasemi, Sapan Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trade-up recommendation identifies higher-quality alternatives that preserve a customer's purchase intent while offering upgraded benefits. Large language models (LLMs) can reason about such distinctions, but applying them directly to hundreds of millions of product pairs is operationally impractical. We introduce a two-level framework that distills LLM reasoning into an efficient non-generative student and adapts its decision boundary to product-type-specific trade-up criteria. At Level 1, a retrieval-augmented few-shot LLM teacher generates structured relation labels and natural-language rationales. These rationales supervise a compact embedding-pair classifier through alignment and contrastive objectives; at inference, the student uses only two precomputed 768-dimensional product embeddings, with no LLM calls or text generation. On a fixed human-annotated benchmark of 8,352 pairs, a 15.5M-parameter four-class reasoning-distilled student achieves AUC 0.924 (95% CI [0.918, 0.929]), compared with 0.912 for the four-class label-only student. At Level 2, product-type test-time training (PT-TTT) uses few-shot demonstrations to optimize lightweight category-specific adapters over the frozen student. PT-TTT improves AUC from 0.924 to 0.941 and average precision from 0.920 to 0.940. On a 100K-pair proxy catalog, the distilled student on a single eight-GPU machine is approximately 5,000x faster and 10,000x lower in estimated cost than direct LLM inference.

---


### 165. [When LLM Decompilers Recompile More and Preserve Less](https://arxiv.org/abs/2609.05370)

**<font color=#1a73e8>作者：</font>** Chang Liu, Edward Raff, Kristopher Micinski  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decompilation recovers high-level source from compiled machine code and serves as a foundation for security tasks such as vulnerability detection and malware analysis. Traditional decompilers like Ghidra and Hex-Rays expose whatever they cannot resolve as visible placeholders and often emit pseudocode that will not compile or execute; LLM-based decompilers produce clean, idiomatic C and are now judged almost entirely by recompilability and re-executability: whether the output builds and passes its shipped input/output tests. We show that these metrics can reward the wrong path: a function may recompile and pass every shipped test yet diverge on other legitimate inputs, and a disclosed vulnerability may disappear from the recompiled code with no visible trace of the crash. Neither failure is caught by existing suites.
To address this gap, we propose Decompile-Diverge, a behavioral comparison oracle not relying on fixed or hand-crafted tests: for each function it synthesizes a driver, grows a fuzzing corpus from the reference, and reruns the decompiled code on the same inputs to detect changes in the function's behavior. Across eight systems in nine configurations on established LLM decompilation corpora, candidates that pass every shipped test still diverge from the original on our input corpus: 4.9% overall, and as many as 13% for a single system. On 300 real GitHub library functions and 287 CVE-grounded functions, recompilability and behavioral agreement can come apart: the strongest refinement LLM lifts Ghidra's build rate from 75% to 90%, while its Matched rate falls from 74% to 62%; on disclosed vulnerabilities, up to one tenth exhibit Crash Absence in its output. Source-level analysis traces this divergence to introduced fields, types, callees, and guards that replace the visible unknowns traditional tools leave behind.

---


### 166. [CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents](https://arxiv.org/abs/2609.05374)

**<font color=#1a73e8>作者：</font>** Haoting Shi, Wenhao Wang, Weicheng Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents have advanced on benchmarks like OSWorld and AndroidWorld, but still act mostly through the GUI, often producing inefficient trajectories. Real-world computer work is hybrid, combining visual-state inspection with precise, high-throughput command-line operations, so capable agents must coordinate both modalities over shared application state. Yet scalable hybrid environments remain scarce because supporting both GUI and CLI over real applications typically requires substantial manual engineering for each application. Existing agents also struggle to use the two interfaces complementarily: CLI-native agents lack visual perception for tasks involving interface state or layout, while GUI-native agents are inefficient for operations better executed through commands. We introduce CUA-Universe, a scalable environment-to-data pipeline that turns real desktop software into hybrid GUI+CLI environments. App-Forge adapts applications into reproducible VMs and command-line surfaces it discovers, wraps, or generates, scaling to 16 applications; Task-Weave synthesizes diverse hybrid tasks of controllable difficulty from reusable operations over seed files; and Path-Steer steers rollouts along efficient hybrid paths and harvests verified trajectories for post-training. Training on this data shifts behavior from inefficient GUI interaction and brittle CLI scripting toward effective GUI+CLI orchestration. Our 9B model improves both success and efficiency on CUA-Verse (Score +39.3 pts; -37% steps, -60% tokens), OSWorld (SR +16.8 pts; -57% steps, -44% tokens), and OSWorld-MCP (Score +7.84 pts; -27% steps, -30% tokens). CUA-Universe provides a scalable path toward more capable and efficient computer-use agents.

---


### 167. [Molecular Déjà Vu: Digit-Level Retrieval of Published Values in Frontier Language Models](https://arxiv.org/abs/2609.05381)

**<font color=#1a73e8>作者：</font>** Matthias Busch, Marius Tacke, Sviatlana V. Lamaka 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly evaluated on molecular property benchmarks, but accuracy cannot distinguish a model that predicts a property from one that retrieves a published number. We audit 22 frontier models on 12 regression benchmarks for verbatim retrieval and find that it is widespread but relatively benchmark-specific: on five datasets more than $50\%$ of the LLMs show verbatim retrieval, while on the remaining datasets it appears only in isolated cells. We run our experiments at two reasoning levels and find that reasoning changes retrieval. The same experiments, on the same molecules and with the same prompt, are flagged $89\%$ more often at the higher reasoning level than at the lowest one. Finally, we test a way to interrupt retrieval in our most contaminated cases, and find that the strongest models in some cases still recognise a combination of transformed SMILES strings and original labels. Furthermore, suppressing retrieval moves the prediction errors of the different models closer together in relative terms, while their differing use of verbatim retrieval spreads them apart. This indicates that the general predictive capability of an LLM is not determined solely by the amount of memorised values. This work provides an overview of the amount and depth of verbatim retrieval in molecular regression benchmarks using LLMs.

---


### 168. [Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence](https://arxiv.org/abs/2609.05385)

**<font color=#1a73e8>作者：</font>** Urja Pawar, Rajitha Ramanayake, Nabeel Kemal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM decision components that can operate within agent workflows often produce action-relevant recommendations or judgements together with explanations. Operators may use the named factors to monitor a system, diagnose errors, or decide when to escalate an output. Such use assumes that the explanations agree with the component's observable decision behaviour. We test two interpretations of the named factors: necessity, meaning that changing a factor would change the output, and sufficiency, meaning that retaining it while removing other changeable information would preserve the output. We evaluate these interpretations in two synthetic use cases: recommending advisors to clients and judging prompts for harmfulness or risk. Models return an output and the top three factors that most influenced it. Controlled black-box interventions estimate a necessity score for each factor by measuring how often changing it changes the output, and a sufficiency score by measuring how often retaining it preserves the output. Across eight models from the Claude, GPT, and Gemini families, the mean Spearman correlations between the cited ranking and the necessity and sufficiency scores are 0.349 and 0.354 for advisor recommendation, and 0.431 and 0.580 for prompt monitoring. Furthermore, an uncited factor scores above the lowest-scoring cited factor in 57.6% of advisor responses under necessity and 58.1% under sufficiency; the corresponding prompt-monitoring rates are 25.8% and 8.9%. The cited top three contain useful information but do not reliably identify the three factors with the strongest measured influence under necessity or sufficiency. The framework provides a black-box reliability check for explanations used in agent oversight while remaining scoped to individual LLM decisions.

---


### 169. [Think-Verify-Revise: Neuro-Symbolic Visual Reasoning with Vision-Language Models and Dynamic Logic Tensor Networks](https://arxiv.org/abs/2609.05388)

**<font color=#1a73e8>作者：</font>** Homayoun Afshari, Pietro Basci, Alessandro Russo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reasoning tasks require a system to jointly perceive visual content and apply formal relational constraints---a combination that neither pure neural nor purely symbolic approaches handle well in isolation. This paper proposes a Neuro-Symbolic (NeSy) framework that closes this gap by tightly coupling a Vision-Language Model (VLM) for automatic First-Order Logic (FOL) rule induction with a Dynamic Logic Tensor Network (D-LTN) for differentiable rule verification, in a closed iterative feedback loop. The VLM receives a small set of labelled visual examples and proposes candidate FOL rules conforming to a strict grammar (Think); the D-LTN is automatically assembled from these rules at runtime and evaluates them grounding on CNN-produced visual embeddings (Verify); and verification failures are fed back to guide the VLM's next hypothesis (Revise). Evaluated on the ViSudo-PC benchmark across four visual domains (MNIST, EMNIST, KMNIST, FMNIST), the system induces valid Sudoku constraint rules using only three training examples as visual context. The proposed method achieves AUC scores matching or outperforming previous methods (NeuPSL, LTN), showing the potential for automatic rule discovery through VLM. Code is available at this https URL.

---


### 170. [Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe](https://arxiv.org/abs/2609.05395)

**<font color=#1a73e8>作者：</font>** Dain Kim, Eungi Cho, Kyumin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data-sovereignty regulations increasingly require public institutions to deploy open-source, on-premise LLM agents that chain multiple tool-calls across live government APIs. However, open-source models consistently underperform in this multi-step setting, and no existing benchmark measures the gap. We introduce the Korean Open Public API Benchmark (KOPA-Bench), comprising 145 real-world tasks. To close this gap, we present EDGE, an Execution-grounded Dynamic Graph for tool-calling data synthEsis driven by live execution. EDGE builds a graph of how each tool's output can feed another's input, keeps only the links that succeed when actually called against the live APIs, and traverses these verified links to synthesize executable multi-step trajectories. Fine-tuned via GRPO on the resulting dataset, our 9B model nearly matches the untuned 27B model from the same family, improving substantially not only on KOPA-Bench but also on the BFCL benchmark.

---


### 171. [WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data](https://arxiv.org/abs/2609.05405)

**<font color=#1a73e8>作者：</font>** Ji Soo Lee, Xilun Chen, Pierce Chuang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in wearable sensing enable continuous monitoring of physiological and behavioral signals, yet existing benchmarks rarely evaluate whether AI systems can reason over a real user's longitudinal wearable record. We introduce WearableQA, a benchmark comprising 4,084 10-option multiple-choice questions constructed from the wearable time series, blood biomarkers, and demographics of 200 real users, each with up to 500 days of daily measurements. WearableQA preserves authentic wearable distributions that include device noise and inter-individual variability. To evaluate distinct reasoning capabilities, we introduce 16 question types organized along two complementary axes: data versus health reasoning, which distinguishes computation over longitudinal measurements from physiological interpretation; and single- versus cross-signal reasoning, which separates reasoning about individual signals from the integration of multiple signals. To construct reliable questions at scale, we adopt a dual-grounding framework that combines literature-grounded physiological findings with statistically validated population-grounded physiological patterns. This enables the capture of meaningful relationships observed in real-world wearable data. Evaluation of 14 proprietary and open-source LLMs demonstrates that WearableQA effectively differentiates model capabilities, with performance ranging from 19.6% to 72.9% against a 10% chance baseline. Moreover, WearableQA remains far from solved: most models achieve accuracies below 60%. Overall, WearableQA provides a realistic and diagnostic benchmark for evaluating LLM reasoning over real-world wearable data.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 172. [Step Back to Move Forward: Reflection-Aware Preference Optimization for Visual Generation](https://arxiv.org/abs/2609.04282)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junlong Wu, Jiuzhou Lin, Jia Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become the mainstream paradigm for modern visual generation and have substantially advanced multimedia content synthesis, especially in text-to-image and text-to-video tasks. To further align such generative models with human preferences, reinforcement learning (RL) has recently shown strong potential as a post-training strategy. Nevertheless, existing policy gradient-based methods often explore inefficiently, making them vulnerable to local optima that may degrade semantic faithfulness and visual realism. To address these challenges, we present Reflection-Aware GRPO (RA-GRPO), a new RL-based preference alignment framework for diffusion generative models. The core idea is to improve "forward" generation by incorporating "backward" reflection during optimization. We first introduce Diffusion Reflection, which rectifies intermediate sampling trajectories by inverting the diffusion process with a weak estimator, guiding latent states toward higher-probability regions of the true data manifold. Furthermore, we introduce Counterfactual Path Synthesis to implicitly distill these rectified trajectories into the policy, enabling the model to internalize the benefits of search-based exploration without incurring inference-time overhead. Extensive experiments on T2I and T2V models demonstrate that RA-GRPO significantly outperforms existing methods, particularly in mitigating reward hacking and improving generalization. The method remains architecture-agnostic and integrates seamlessly with standard pipelines, suggesting a promising direction for stable preference alignment.

---


### 173. [Joint Alignment and Distillation for Video Generation via Sample-Guided Distribution Matching](https://arxiv.org/abs/2609.04283)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiuzhou Lin, Junlong Wu, Fei Zuo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning video generative models to human preferences heavily relies on Reinforcement Learning (RL), which suffers from extensive computational overhead. Existing workflows typically treat RL and distillation as disconnected stages: applying RL before distillation incurs prohibitive computational costs, whereas applying RL after distillation frequently leads to model collapse. To overcome these limitations, we propose a unified, single-stage optimization framework grounded in Distribution Matching (DM). In the standard DM framework, distillation updates the model via a gradient direction that minimizes the gap between the real and fake models, guiding generations toward clarity and high fidelity. Building upon this, we introduce DM-Align, which derives a complementary gradient direction to guide the model toward human-preferred samples. Inspired by DPO and GRPO, our method leverages the distributional gap -- formulated from either preference pairs or intra-group exploration -- to directly construct this preference-guided gradient. By synergizing these two gradient directions, our approach eliminates the need for multi-step reward evaluation and complex ODE-SDE conversions inherent in traditional RL. Comprehensive experiments across multiple foundational video models demonstrate that this sample-guided framework robustly enhances both distillation quality and preference alignment, consistently outperforming both standalone variants and sequential two-stage pipelines.

---


### 174. [Where Appearance Fails, Geometry Recognizes: A CAD-Free 3D Shape Prior That Complements Vision Foundation Models](https://arxiv.org/abs/2609.04381)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chenxi Tao, Seung-Kyum Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing specific objects onboarded without a labeled training set recurs across manufacturing and service robotics, yet the conventional renderable prior, a computer-aided-design (CAD) model, is often unavailable. Two-dimensional capture supplies no shape prior, and frozen foundation features fail on geometrically similar, low-texture industrial parts. We ask what a short object-centric scan buys for recognition beyond the captured images themselves: each object is reconstructed with 3D Gaussian Splatting (3DGS), summarized into a per-class shape prototype, and fused with frozen DINOv2 image features. First, the scan recovers the recognition value of CAD without CAD: geometry from RGB-D depth (on T-LESS), 3DGS, and CAD gives comparable recognition (tied on HOPE, within 1.6 points on T-LESS); 3DGS is only a convenient route to a point cloud. Second, the payoff is governed by how recognizable the shape is: on shape-distinctive household objects (HOPE) geometry alone reaches 0.920 versus image-only 0.832, a ceiling below which fixed-weight fusion (0.872) sits. On shape-confusable textureless industrial parts (T-LESS) the gain is modest but consistent (0.560 to 0.591 fused, above both single signals). Third, the prior is complementary, not uniformly additive: it rescues far more image failures than it breaks successes, and its benefit grows under partial occlusion. Finally, the worth lies in geometry, not rendered pixels: 3DGS renderings do not help the image side, and frozen-feature recognition is nearly lighting-invariant (within 2.5 points). The study is scoped to recognition, not the BOP pose benchmark.

---


### 175. [DART: Depth-as-Target Pretraining for Surgical Vision Foundation Models](https://arxiv.org/abs/2609.04555)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** John J. Han, Adam Schmidt, Muhammad Abdullah Jamal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models (VFMs) are valuable in data-scarce domains such as surgery, where a single pretrained backbone can provide rich representations for many downstream tasks. Yet the dominant self-supervised pretraining paradigm uses only RGB images, leaving readily available complementary signals, such as depth maps, unused. This is a particular missed opportunity in surgery, where natural-image VFMs transfer poorly while the scene geometry is rich and informative. With strong off-the-shelf models now able to produce pseudo-labeled dense depth for any image corpus, we hypothesize that such signals can be folded into pretraining to learn better representations. We present DART, an RGB-D pretraining recipe that builds on DINOv2 with a simple modification: a pixel-space depth reconstruction objective applied to masked iBOT patches, supervised by pseudo-labeled depth. Depth is used only during pretraining, so fine-tuning and inference remain RGB-only. We find that this pixel-level reconstruction head improves representation quality rather than disrupting it. We further show that depth, which encodes scene geometry, is more effective as a target than alternative dense signals such as Canny edges, confirming that the gains stem from depth rather than added supervision alone. Across eight surgical benchmarks spanning segmentation, depth estimation, and image-level recognition, DART outperforms both natural-image and in-domain baselines, including a vanilla DINOv2 trained on identical data, improving dense prediction while also strengthening image-level understanding. More broadly, DART shows that freely available geometric pseudo-labels can strengthen foundation model pretraining without extra labels or added inference cost, pointing toward stronger backbones for surgery.

---


### 176. [Adaptation Interfaces for In-Context Tabular Foundation Models in Time-to-Event Prediction](https://arxiv.org/abs/2609.04901)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Minh-Khoi Pham, Luca Cotugno, Dan Cernei 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TabFMs) achieve strong performance on structured data, particularly for standard classification and regression problems. Yet, extending them to censored time-to-event prediction is challenging because it requires properly handling censoring and event-time dynamics. Building on our prior work, we further link TabFMs with CoxPH and DeepHit and revise the context-resampled training procedure. We evaluate temporal zero-shot reformulation, classification-based fine-tuning, and survival-head adaptation using frozen TabFM backbones on 74 single-risk data sets, and we additionally study 4 competing-risk data sets. Zero-shot inference is effective on smaller single-risk data sets, whereas supervised adaptation becomes increasingly advantageous as data sets scale. Cox provides the most reliably strong interface, especially for Integrated Brier Score (IBS) on larger data sets. DeepHit is relatively stronger for the time-dependent Concordance Index than for IBS, while cause-specific MTLR ranks highest among the TabFM survival heads in the four-data-set competing-risk analysis. Classification fine-tuning becomes more competitive with zero-shot inference as data sets grow but remains weaker for probabilistic prediction. Overall, our results indicate that effective TabFM transfer depends on the data regime and on the statistical structure represented by the chosen adaptation interface. The implementation scripts used for this work are available at this https URL.

---


### 177. [Fractal basins trap latent reasoning](https://arxiv.org/abs/2609.04963)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jeffrey Lai, Anthony Bao, John Quinn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning allows artificial intelligence models to revisit and correct their mistakes, enabling recent frontier advances in mathematical theorem solving, software engineering, and autonomous task planning. Reasoning models are widely observed to reason for longer on harder tasks, but the general mechanism responsible for these slowdowns is unknown. Here, we show that reasoning models exhibit transient chaos, a physical consequence of the computational complexity of difficult tasks. As a consequence, we show that diverse leading reasoning models are dynamical systems with fractal basins, with fractality increasing with task difficulty across diverse tasks like Sudoku and maze solving, visual puzzles, and mathematical logic. We show that transient chaos emerges due to reasoning becoming trapped for extended durations near saddle points, which we show correspond to nearly-correct attempted solutions of the underlying problem. Our results show that reasoning slowdowns are an inevitable consequence of problem hardness in modern artificial intelligence models, and establish reasoning traces as a rich new class of dynamical system.

---


### 178. [Influence Score and Transformers interpretability: Measure of the Effective Impact of Attention Heads at inference time](https://arxiv.org/abs/2609.05074)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lisa Bouger, Yannick Teglia, Philippe Loubet Moundi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose an influence score to quantify the contribution of attention heads to classification decisions in Transformer-based models designed for prompt injection detection. The score combines directional influence on the logits with structural contribution within the residual stream, enabling a multi-scale analysis at the head, layer, and network levels. Applied to a DeBERTa model specialized for prompt injection detection, our framework reveals distinct decision behaviours between correct and erroneous predictions. Our method provides an effective compromise between fine-grained circuit analysis and global output-based methods, and offers a systematic way to study decision mechanisms in Transformer classifiers.

---


### 179. [Conserved Immune Topology Improves Pathology Foundation Model Generalization for Cross-Cancer MSI-H Prediction](https://arxiv.org/abs/2609.05182)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dasari Naga Raju  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models integrated with multiple instance learning achieve competitive accuracy within single-cancer cohorts, yet cross-cancer generalization remains unresolved due to organ-specific histological and architectural differences. In this paper, we propose Conserved Immune Topology (CIT), a lightweight spatial representation for cross-cancer MSI-H prediction that augments foundation-model embeddings with biologically motivated immune descriptors. CIT uses unsupervised clustering to identify immune-associated tiles, then encodes tertiary lymphoid structures, peritumoral immune reactions, multi-scale tumor-infiltrating lymphocyte density, and immune-tumor mixing from frozen foundation-model embeddings and tile coordinates without requiring annotations or target-domain data. The proposed method was evaluated under cross-site and cross-cancer settings using CPTAC-COAD and TCGA-STAD cohorts, which introduce scanner variability, distribution shifts, and organ-specific architectural variations. Zero-shot cross-cancer transfer with CIT increased TransMIL AUC from 0.6627 to 0.7161, an absolute gain of 0.0534 (p=0.003), with consistent improvements across all three MIL aggregators. These results suggest that spatial immune topology provides potentially an organ-invariant representation for MSI-H prediction, supporting cross-cancer generalization of pathology foundation models.

---


> [!TIP]
> 当前位于：**151-179**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-179**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
