# 🧠 大模型相关研究 | 2026年09月29日

> 本类共 **183** 篇论文：已确认 **174** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-183](./part-04.md)

---

### 51. [Causal Retention in Interactive Agents: Interface Factorization and Selective Adaptation](https://arxiv.org/abs/2609.30650)

**<font color=#1a73e8>作者：</font>** Shengjun Zhang, Tingyi Liu, Dong Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task performance need not determine which intervention mechanism an agent retains. We study causal retention: whether a frozen learned state answers a mechanism-probe map fixed independently of training, including action, context, direct target, value, and delay. For finite structural causal model classes, the optimal probe error is a Bayes decision risk. It vanishes exactly when every learning-interface fiber lies within one probe-answer fiber; any state obtained by post-processing that interface inherits the same lower bound. A posterior-coverage theorem characterizes budgeted retesting, while an exact edit decomposition shows that the shifted set is the unique support of an error-free target update. Causal Core implements these conditions through evidence-gated writing, readout filtering, temporal credit, hidden-context setup, and local diagnostic updates. Experiments cover finite causal systems, continuous simulators, an official TD-MPC2 world model, and Qwen2.5-7B-Instruct. A frozen Qwen last-layer probe reaches 0.958 balanced accuracy on source mechanisms but 0.583 on changed delays; the gated mechanism state reaches 1.000 and accepts only 0.056 of synchronized-readout candidates. In TD-MPC2, five target states per actuator recover effect-sign accuracy from 0.057 to 0.948 without degrading stable responses. Causal retention is therefore distinct from task sufficiency and source-domain decodability.

---


### 52. [Recursive Self-Improvement via On-Policy Distillation for Reasoning](https://arxiv.org/abs/2609.30652)

**<font color=#1a73e8>作者：</font>** Shangjian Yin, Zehao Zhao, Kavosh Asadi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student model by having it generate trajectories, then matching its next-token predictions with an external teacher's next-token predictions. This provides dense, token-level supervision to the student. On-policy self-distillation (OPSD) eliminates the need for the external teacher. Specifically, a second frozen copy of the student model, now given the ground truth in its context, serves as the teacher. The student model only receives the problem and learns to mimic the privileged teacher model, while the teacher remains frozen throughout training. Previous work showed that freezing the teacher is useful for training stability, but we argue that this can prevent the teacher from incorporating the improvements learned by the student during training. Our primary contribution is to address this limitation with a recursive framework built around two complementary components. First, we let the privileged teacher co-evolve with the student so that revision learned in one round can guide the next, a process we refer to as Dynamic Co-Evolution (DCE). Second, because stronger revision can also make responses too verbose and self-critical, we additionally train on shorter, verified rewrites of the model's own on-policy responses. We call this complementary objective Self-Refined Concise Learning (SRCL). Overall, our comprehensive evaluations show that DCE+SRCL outperforms OPSD across multiple model scales and four competition-level mathematics benchmarks. Specifically, on Qwen3-8B, DCE+SRCL reaches 65.97% Average@12, outperforming OPSD by 35.62 percentage points while reducing mean output length by 7.80% relative to DCE alone.

---


### 53. [LLM Parkinsonism: Executive-Control Failure, Token-Inefficient Persistence, and an Uncertainty-Aware Global Executive Control Architecture for Autonomous Language-Model Agents](https://arxiv.org/abs/2609.30662)

**<font color=#1a73e8>作者：</font>** Dongsheng Xiao, Zeyuan Wang, Xuzhe Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can plan, use tools, write code, and execute long-horizon workflows, yet strong local competence does not guarantee project-level executive control. Agents may continue acting after the original objective is satisfied, producing low-value refinements, repeated verification, and repairs to self-created complexity. We use LLM Parkinsonism as a narrowly defined, non-clinical metaphor for this pattern of persistent action despite diminishing task-level value. We argue that the problem is not explained by autoregressive next-token prediction alone, but more directly by concentrating proposal generation, scope interpretation, progress assessment, and stopping authority within the same self-conditioned loop. We therefore introduce Global Executive Control (GEC) v0.2, an uncertainty-aware governance architecture that separates action generation from project-level control. In a 24,000-episode matched-candidate benchmark under a common 40,000-token ceiling, a first-candidate baseline achieved 67.42% hard-goal success, a candidate-set local control achieved 96.53%, and GEC achieved 96.57%. The candidate-set control shows that access to multiple candidate actions explains most of the success gain; relative to that control, GEC preserved success while reducing mean token use from 19,782 to 12,574 (36.4%) and restricted mean tokens to completion at the 40,000-token ceiling from 16,136 to 13,114 (18.7%), while eliminating measured pre-completion drift and sharply reducing gross complexity. Governance-overhead sensitivity remained favorable through an additional 500 synthetic governance tokens per cycle. These mechanistic simulations support explicit governance of scope, evidence, resource use, and stopping, while live-model validation remains necessary.

---


### 54. [A Large-Scale Empirical Study of Modern Phishing Email Content](https://arxiv.org/abs/2609.30683)

**<font color=#1a73e8>作者：</font>** Jaehwan Park, Woonghee Lee, Fujiao Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing remains one of the most pervasive threats to Internet users, and email remains its predominant delivery channel. Email content is the attack surface of phishing: it is what the victim reads and what automated defenses inspect. Yet the composition of modern phishing content is poorly measured. Prior work has characterized dimensions such as theme, call-to-action (CTA), and impersonation, but not at scale, and their associations and temporal changes remain unclear, owing to small or source-specific corpora, bag-of-words topic models, and a focus on text alone.
We present a content-focused measurement study of 2.9M distinct real-world phishing emails collected over 13 months (June 2025 - June 2026) in collaboration with the Anti-Phishing Working Group (APWG). We treat each email as a composite artifact comprising message text and its attachments: 272K images, 143K PDFs, and 57K calendar invitations. Using an LLM pipeline validated against human-annotated samples, we analyze these components along three dimensions (theme, CTA, and impersonation), examine the associations among them, and measure longer-term change against a historical dataset.
We find that attackers diversify what they use to deceive but converge on how victims should respond: no theme exceeds 21.3% of emails, while a single CTA, URL navigation, accounts for 73.0%. CTA and impersonation choices are conditioned on theme. Attachments play three roles: images supplement the message text, PDFs substitute for it by carrying the pretext, and calendar invitations reinforce it by replicating interaction endpoints into a persistent medium. Over the longer term, the dominant CTA for invoice-themed phishing shifted from URL navigation to offline communication, rising from 6.7% in 2015 to 46.9% in 2025.

---


### 55. [ADF-EA: A Unified Execution Assurance System for Agent Device Foundation](https://arxiv.org/abs/2609.30691)

**<font color=#1a73e8>作者：</font>** Xuechun Li, Jiaxin Liang, Jie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agents based on large language models (LLMs) can access heterogeneous devices through tools and APIs, but reliable execution must account for unmet effects, uncertain outcomes, and changing prerequisites. A command may be acknowledged without producing its intended effect, while missing feedback may obscure an action that has already succeeded. We present Agent Device Foundation--Execution Assurance (ADF-EA), an architecture that connects agent planning and device execution through shared capability contracts. Device Capability Contracts (DCCs) unify invocation conditions, intended effects, evidence requirements, and recovery rules across heterogeneous interfaces. Agents use these contracts to plan, while the runtime applies the same semantics to authorize actions, verify effects, and govern continuation and completion. Persistent execution state retains verified progress, unresolved outcomes, and remaining budgets across plan revisions, enabling observation-based recovery, authorized retries, and necessary state repair. We formalize the execution lifecycle and establish conditional soundness properties for completion and recovery authorization. Evaluations span multiple LLMs, five agent frameworks, and simulated process-control, household, and robotic manipulation domains. Compared with direct invocation and existing execution-checking approaches, ADF-EA reduces false completion and unnecessary repetition, supports necessary state repair, prevents calls to unavailable capabilities, and preserves permitted task completion and recovery. These results demonstrate DCCs as a reusable semantic foundation for agent autonomy across heterogeneous devices, unifying capability-based planning, evidence-grounded execution, and authorized recovery within one architecture.

---


### 56. [LUMO (Lightweight Unified Multilingual Orchestrator): A Privacy Preserving Offline Voice Assistant](https://arxiv.org/abs/2609.30692)

**<font color=#1a73e8>作者：</font>** Md. Mehedi Hasan Naeem, Mst. Kamrunnahar Ruma, Nafiza Anjum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable voice interaction is essential in environments with limited internet connectivity and strong privacy. However, most existing voice assistants depend on cloud-based services, which leads to latency issues, dependency on internet access, and privacy vulnerabilities. This research presents LUMO (Lightweight Unified Multilingual Orchestrator), a privacy preserving offline voice assistant designed for edge computing environments. This system integrates local Automatic Speech Recognition (ASR), locally deployed quantized Large Language Model (LLM), and Text-to-Speech (TTS) synthesis into a fully offline pipeline running on a Raspberry Pi 5 with 8 GB RAM.
To enable efficient operation on resource constrained hardware, the language model is compressed using 4-bit GGUF quantization, which reduces memory usage while preserving practical conversational capability. Existing edge based voice assistants Mycroft provides partial offline functionality without a generative LLM, with an approximate latency of ~5 s and power consumption of ~12 W, while Rhasspy supports full offline operation but lacks generative capabilities, with ~3 s latency and ~11 W power usage. In contrast, LUMO achieves a Word Error Rate (WER) of 6.8% for short English utterances in low noise conditions, an end-to-end response latency of 2.0-4.0 s, and a lower peak power consumption of approximately 9.0 W. The system also achieves effective offline recognition for Bangla speech, supporting multilingual accessibility in low resource settings. By operating entirely offline, LUMO provides strong data privacy, reduced need for cloud connectivity, and suitability for privacy sensitive edge execution such as rural healthcare, education, and disaster response scenarios.

---


### 57. [MM-VeriAgent: Learning to Use Extensive Tools to Verify Multimodal Misinformation with Reinforcement Learning](https://arxiv.org/abs/2609.30698)

**<font color=#1a73e8>作者：</font>** Peipei Li, Shuhan Xia, Shengyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world multimodal misinformation often involves mixed forgery sources, requiring sample-specific detection strategies. Existing tool-augmented methods rely on predefined workflows or inference-time planning, limiting adaptability or increasing inference cost. To address this issue, we introduce \textbf{MM-VeriAgent}, which learns to verify mixed-source multimodal misinformation with tools. We first build \textbf{MM-VeriTools}, a specialized toolkit for misinformation detection agents. By benchmarking various candidate models and methods on the sub-tasks required by mixed-source detection, we select the strongest for textual, visual, and cross-modal forgery analysis and encapsulate them as callable tools with a unified interface. On top of this toolkit, we train the LVLM agent with reinforcement learning to teach it how to use these tools to better solve mixed-source detection. Since many of the tools are specialized models whose online execution at every rollout severely limits RL efficiency, we further introduce \textbf{Tool-Execution Cache}, which pre-executes candidate tool calls and reuses their cached outputs during training. This preserves multi-step rollouts while reducing online tool execution, largely improving the training this http URL on MMFakeBench demonstrate substantial accuracy gains over the base model without explicit tool search at inference time. Ablation and efficiency analyses further validate the learned tool-use policy and show that Tool-Execution Cache reduces online tool executions during training.

---


### 58. ["If You're Not Doing It, Somebody Else Is": Active Negotiation and the Invisible Labor of Sustained LLM Use](https://arxiv.org/abs/2609.30699)

**<font color=#1a73e8>作者：</font>** Matt Viana, Patrick Erickson, Shomir Wilson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become fixtures of academic work even as their users describe them as degrading their writing, thinking, and skills. Dominant adoption frameworks read continued use as evidence of satisfaction, and cannot explain continued use of a distrusted tool. We interviewed 36 graduate student workers, balanced between English-as-a-foreign-language (EFL) and non-EFL speakers, and introduce the Active Negotiation framework: a model of sustained LLM use as a recurring cycle of risk, mitigation, and justification. A failure surfaces a risk, mitigation labor addresses it, and a justification renders the residual risk tolerable until the next failure reopens the cycle. The cycle runs across three dimensions: practical, auditing output; internal, auditing one's own cognition and identity; and social, managing how peers and institutions perceive use. EFL participants invoke linguistic parity as a further justification. We reframe continued adoption as compliance sustained by invisible labor.

---


### 59. [The Price of Thought: Does Test-Time Reasoning Pay in LLM Trading?](https://arxiv.org/abs/2609.30705)

**<font color=#1a73e8>作者：</font>** Jiayi Chen, Guiling Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While inference-time reasoning in large language models (LLMs) promises better decision making, its higher computational cost may not yield better economic outcomes. Yet reasoning controls are rarely evaluated as economic interventions, where changes in model outputs must translate into better portfolios after trading costs. We conduct a controlled study of representative LLMs from the DeepSeek, GPT, and Gemini families. We vary reasoning effort while holding information available at each formation date, prompts, output formats, and portfolio construction fixed. Our evaluation covers a full year of U.S. equities under three input conditions: numerical, identifiable news, and masked news. It includes more than 800,000 asset predictions and repeated model generations. Across all three model families, additional reasoning does not produce a reliable improvement in net portfolio returns. For DeepSeek, where we examine the full progression from no reasoning to maximum reasoning, performance is nonmonotonic. Repeated generations also produce unstable treatment effects and portfolio selections, even when overall scores remain similar. These findings show that additional reasoning can change financial decisions without reliably improving their economic value, motivating validation for each task before deployment.

---


### 60. [LAVOIR: Teaching a Single-Pass Decision Encoder When and What to Ask with Amortized Value of Information](https://arxiv.org/abs/2609.30706)

**<font color=#1a73e8>作者：</font>** Furkan Yilmaz, Habibe Aleyna Tasdemir, Muhammed Faruk Gozay  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> "System One" decision models such as TypeSafe's Jev and its open counterpart Laya answer typed questions about a text in a single forward pass with calibrated probabilities, but they cannot ask for missing information: when a first message does not say what separates two departments, they guess. We present LAVOIR (Laya with Value-Of-Information Routing), which places the candidate pieces of missing information (slots) in the input next to the answer options, so that one forward pass returns both the decision distribution and, for every slot, the expected gain in the probability of the correct decision if the user were asked about it. VOI targets need no human labels: gold decisions come from schema rules, an LLM only verbalizes messages and answers, a model from another family checks every text, and pairing each message with several profiles makes regression on realized gains estimate the expected gain. A Gini-impurity cap bounds the predicted value by what a calibrated model can still gain. In a controlled study, decisions on seen schemas are statistically indistinguishable from the Bayes ceiling. The final model's question policy matches a greedy oracle VOI policy on seen schemas (AUC 0.799 vs. 0.797), and with at most 0.5 questions per conversation it is 14.1 points more accurate than never asking. On real ABCD conversations, one real exchange raises accuracy by 8.3 points where LAVOIR asks and leaves it unchanged where it does not; on SGD the cap lowers the asking rate from 93% to 8.6%. On Laya's twelve benchmarks LAVOIR is above Laya's reported scores on seven, and it answers a question in 31 ms (median, GH200).

---


### 61. [VLALight: Lightweight Vision-Language-Action Models for Emergency-Aware Traffic Signal Control](https://arxiv.org/abs/2609.30709)

**<font color=#1a73e8>作者：</font>** Kemou Jiang, Maonan Wang, Xingchen Zou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic signal control (TSC) is essential for mitigating urban congestion. Recent advances in vision-language models (VLMs) enable richer interpretation of intersection scenes, opening new opportunities for visual-context-aware TSC. However, the loose coupling and repeated information conversion between modules can lead to the loss of fine-grained visual details, while sequential inference introduces substantial latency. To address these limitations, we propose VLALight, a lightweight end-to-end vision-language-action framework that directly maps intersection observations and signal-phase information to discrete signal actions. To handle the multi-view nature of TSC, VLALight combines multiple directional camera views into a unified visual input and uses textual instructions to establish their correspondence with traffic movements and signal phases. This design enables direct action prediction with a compact 0.5 B-parameter model, without intermediate image-to-text descriptions or handcrafted traffic-state representations. Experiments show that VLALight delivers the best emergency-vehicle service of all compared methods, reducing pooled emergency waiting time by 21.1% over the cascaded VLMLight while running in real time on local hardware and generalizing to unseen intersection topologies and traffic-flow patterns.

---


### 62. [Words Speak Louder Than Order: A Behavioral Evaluation of Gemma 4](https://arxiv.org/abs/2609.30716)

**<font color=#1a73e8>作者：</font>** Amanda Fitch  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model receives two conflicting documents as input, how does it decide which one to prioritize? Does it rely on how the sources are framed or the presentation order of the documents? We evaluated this behavior on Google's pre-trained Gemma 4-e4b model across a targeted behavioral suite (n = 13 items, 784 forward passes in short, single-turn contexts) using a completely counterbalanced experimental design. This setup allowed us to mathematically isolate the specific effects of source framing and reading position, while ensuring the model's natural vocabulary biases were canceled out.
Across ten test conditions, we discovered the following:
1. Source framing heavily overpowers reading position. When directly competing, the semantic framing of a source (such as presenting it as an official guideline or a fresh update) had a significantly stronger impact on the model's final answer than the presentation order of the document.
2. The model favors the first document it reads, but this bias is highly variable. While the model consistently demonstrated a primacy effect (preferring the first document presented), the actual strength of this bias fluctuated by at least a factor of 5 based solely on the surface wording.
3. Overall structural repetition, not short copy-cues, drives positional bias. The model's preference for the first document is not a mechanical reaction to short, repetitive trigger phrases, such as "is [Answer]". However, the primacy effect does increase significantly when the two competing documents are structurally identical, using word-for-word verbatim templates. Introducing variation in the overall wording between the two sources reduces this positional bias.

---


### 63. [Analyzing and Mitigating Cost-Inefficient Behaviors in Coding Agents](https://arxiv.org/abs/2609.30725)

**<font color=#1a73e8>作者：</font>** Yiran Hu, Nan Jiang, Shanchao Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although effective, coding agents often incur substantial monetary costs. Their recurring cost-inefficient behaviors remain underexplored. We conduct the first study of behavioral cost inefficiencies in coding agents, analyzing 1,200 trajectories from Claude Code and Mini-SWE-Agent across four configurations on SWE-bench Verified. We identify three cost-inefficient behaviors: subsumed retrieval, similar script generation, and test re-execution. We then evaluate three mitigation strategies: structure-aware retrieval, agent-synthesized skills, and developer-designed skills, over 10k trajectories on held-out SWE-bench Verified and Pro tasks. Our main findings are: (1) The three behaviors affect 79.00\%--98.00\% of coding tasks and account for up to 22.75\% of task cost. (2) Structure-aware retrieval can introduce retrieval overhead and alter agent delegation, causing inconsistent improvements in retrieval efficiency and cost increases of up to 28.14\%. (3) Agent-synthesized skills tend to produce low-level, trace-specific guidance, limiting their effectiveness and generality. (4) In contrast, developer-designed skills provide high-level, trace-agnostic guidance, reducing cost by up to 41.73\%, roughly twice the maximum gain from agent-synthesized skills.

---


### 64. [Learning What to Skip: Counterfactual Credit Assignment for Efficient Multi-Agent LLM Workflows](https://arxiv.org/abs/2609.30734)

**<font color=#1a73e8>作者：</font>** Jinfeng Xu, Zheyu Chen, Ziyue Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM workflows use planning, execution, verification, and summarization to improve task performance, yet the value of each component depends on the state already produced. Executing every component can waste computation or overwrite a correct intermediate answer. We formulate component omission as counterfactual credit assignment: full-workflow logs reveal the executed trajectory's reward, while controlled skip interventions reveal the consequences of omitting a future step. We introduce Learning What to Skip (LW2S), which learns action-specific safety models from these interventions and combines held-out calibration with domain-native guards to select skips. When an early skip is rejected, the controller can continue execution and reconsider a later component. Across mathematical reasoning, multiple-choice QA, and code generation with two instruction-model families, LW2S reduces recorded token cost while matching or improving aggregate full-workflow accuracy in the evaluated settings. Scale-up and second-topology experiments further examine component redundancy, while shared-error cases reveal why agreement alone is insufficient for skip selection. These findings connect efficient workflow execution to learning the conditional utility of individual components.

---


### 65. [Beyond Mean Attention: Diversity-Aware, Layer-Wise Scoring for KV Cache Eviction](https://arxiv.org/abs/2609.30738)

**<font color=#1a73e8>作者：</font>** Tianfang Xie, Wei Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KV cache eviction methods such as SnapKV and PyramidKV rank tokens solely by mean attention over a small observation window. We study a unified score, $\mu_i+\lambda_1\sigma_i+\lambda_2\mathrm{corr}(i,S)$, adding attention dispersion across window queries and redundancy relative to selected tokens. For $\lambda_2<0$, the score penalizes similarity to selected tokens as in maximal marginal relevance (MMR), without extra forward passes. To test whether this relevance-diversity balance should vary with depth, we compare fixed global coefficients with three-segment and quadratic profiles. Only these depth profiles are searched on a development split under a $\sinh$ reparameterization. On all 16 English LongBench datasets with Mistral-7B at a budget of 64 entries per layer, a single global diversification constant improves 13 of 16 datasets (macro +1.1); the gain holds at budget 32 and narrows at 128. Per-dataset search finds no detectable layer structure on most datasets; on passage retrieval it finds a large one: a mid-layer sign flip that rewards similarity and is worth +9.6 over the baseline at budget 64 and, without re-tuning, +13.2 over the global constant at budget 128. Ablations attribute the gain to the redundancy term; replaying every accepted search state on the held-out test set separates genuine structure from tuning noise.

---


### 66. [ORCA: Evaluating LLMs on Data Science Code Translation](https://arxiv.org/abs/2609.30749)

**<font color=#1a73e8>作者：</font>** Xiaolong Li, Jinyang Li, Bowen Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data Science Code Translation (DSCT) is the process of converting code between data science libraries while preserving functional equivalence and enabling interoperability across data science ecosystems. While Large Language Models (LLMs) have demonstrated considerable progress in Data Science Code Generation (DSCG), their performance in DSCT remains insufficiently studied. To address this gap, we introduce ORCA, a comprehensive benchmark with two complementary settings: ORCA-MAIN, which comprises 1,600 carefully curated grounding-level tasks across 3 representative domains: Data Querying, Data Manipulation, and Deep Learning; and ORCA-PROJECT, which contains 200 translation tasks over complete data science projects across 7 data science task types. Each task is accompanied by annotated reference translations and test cases for validating functional equivalence. We further incorporate a multi-stage quality verification process that thoroughly verifies task correctness and test case robustness. Experimental results demonstrate challenges in DSCT, with even frontier LLMs showing limited performance. Specifically, Claude-Opus-4.6 achieves a success rate of 56.92% on ORCA-MAIN and 33.67% on ORCA-PROJECT, indicating considerable room for improvement in DSCT. We also observe a clear directional preference in DSCT, where translation is consistently easier when the source code expresses the task through more explicit, fine-grained operations. Motivated by this, we propose an intent-augmented method, in which the model first infers source-code intent and then uses it as additional context for translation, achieving average absolute success-rate gains of 4.80% and 5.33% on ORCA-MAIN and ORCA-PROJECT, respectively.

---


### 67. [Backbone-Adaptive Evidence Routing for Robust Pairwise LLM Judging](https://arxiv.org/abs/2609.30751)

**<font color=#1a73e8>作者：</font>** Zeyan Li, Jing Peng, Jianfeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pairwise language-model judges can gather evidence through direct comparison, reasoning, or reference-based verification, but no single protocol is best across benchmarks and judge backbones. We introduce Backbone-Adaptive Evidence Routing (BAER), which adapts the evidence mechanism while preserving candidate symmetry: swapping the two responses may reverse the preference but cannot change its strength. BAER separates each expert's signed preference from candidate-invariant reliability and builds three symmetric heads: evidence stacking, reliability-based expert routing, and candidate-blind reference verification. Development data select one head for each benchmark--backbone condition, and that choice is frozen before testing. Across four benchmarks and two 8B judge backbones, BAER achieves the highest test accuracy among the compared methods in all eight conditions, with full prediction coverage and gains of 0.87--7.32 points over the strongest external baseline. The results show that adapting how evidence is gathered is more reliable than fixing one judging protocol everywhere.

---


### 68. [HCOE: Hyperbolic Clinical Ontology Embeddings from Biomedical Language Models](https://arxiv.org/abs/2609.30763)

**<font color=#1a73e8>作者：</font>** Yixuan Li, Weihao Li, Ziyang Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical language models (LMs) encode textual semantics but do not explicitly preserve medical code hierarchies. We present Hyperbolic Clinical Ontology Embeddings (HCOE) for hierarchy-aware clinical concept representation. HCOE maps frozen BioBERT embeddings into a Poincare ball, combining parent-side and child-side ontology-guided contrastive learning with coarse-to-fine ontology-path aggregation. It uses International Classification of Diseases (ICD) codes organized by Clinical Classifications Software (CCS) and Anatomical Therapeutic Chemical (ATC) medication hierarchies. Evaluations show that HCOE performs best on ICD/ATC clinical relation prediction and CCS-to-PheCode hierarchy transfer. On the MIMIC-IV dataset, HCOE also achieves the best performance on mortality prediction, readmission prediction, medication recommendation, and rare drug prediction.

---


### 69. [Does Thinking Help Fairness? Reasoning Tokens Resolve Some Biases but Create More](https://arxiv.org/abs/2609.30768)

**<font color=#1a73e8>作者：</font>** Deng Pan, Joe Germino, Yihong Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Thinking in reasoning language models (RLMs) has been subject to debate on whether it resolves or amplifies bias. Prior works have shown competing conclusions in both directions. Using a within-model thinking-vs.-non-thinking ablation across QwQ-32B, DeepSeek-R1-Distill-Qwen-32B, and Qwen3-32B on three high-stakes decision tasks (Adult, COMPAS, Credit), we show that thinking has an asymmetric dual effect on counterfactual fairness: it both resolves counterfactual flips produced by the non-thinking baseline and creates new flips at near-saturating model confidence. In all nine (model, dataset) combinations, the created flips outnumber the resolved flips by roughly 5 times. To explain the effect, we treat the thinking trace itself as a measurable site of fairness change and study it through two dynamic instruments: 1) We propose Counterfactual Depth Probability Gap (CDPG) to track bias evolution along thinking depth, and observe that bias propagates and amplifies with thinking. 2) We also formulate the Bias Transition Matrix (BTM) to show how predictions of counterfactual pairs change from non-thinking to thinking, and find that the asymmetric dual effect originates in the pair-state joint transition.

---


### 70. [Learning Natural Conversational Behavior in Tandem Speech-to-Speech Models with Randomized Guidance](https://arxiv.org/abs/2609.30773)

**<font color=#1a73e8>作者：</font>** Manato Yaguchi, Yotaro Kubo, Hikaru Asano 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tandem speech-to-speech architectures couple a responsive speech frontend with an asynchronous text backend. In KAME, a large language model (LLM) serves as the backend, supplying candidate responses as guidance to the speech frontend while the user is still speaking. Ordinary conversation recordings capture the eventual response but not the guidance the backend would supply during the user's utterance. Generating the missing guidance with a simulator LLM adds substantial data-preparation overhead when training on real conversations. We propose randomized intermediate guidance, which derives guidance directly from the conversation corpus rather than simulating backend LLM behavior. During training, target responses provide informative guidance, while randomly sampled responses provide potentially irrelevant updates during the utterance. This combination aims to teach the frontend to use backend information selectively. On synthetic dialogues, KAME trained with this recipe achieves response quality comparable to that of the LLM-generated and similarity-based baselines. Training on 3.8k hours of real conversations improves smooth turn-taking and audio-judge naturalness over synthetic-data KAME while retaining a response-quality advantage over Moshi. These results show that randomized guidance offers a practical route to combining the response-quality benefits of tandem models with natural conversational behavior learned from real speech.

---


### 71. [Skip the Talk, Re-Focus on Vision: Latent Reasoning for Reasoning Segmentation in Multimodal Large Language Models](https://arxiv.org/abs/2609.30783)

**<font color=#1a73e8>作者：</font>** Tianhang Guo, Yulin He, Wei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning segmentation aims to interpret implicit textual queries and enable fine-grained visual perception, which is critical for applications such as human-computer interaction and embodied agents. Existing methods typically generate explicit Chain-of-Thought (CoT) by multimodal large language models (MLLMs) before localizing the target. Although intuitive, such explicit verbal reasoning introduces substantial attention interference: redundant textual tokens disrupt attention during perception-token generation and also increase the effective distance between visual tokens. To address this issue, we propose LIRSeg, which fully replaces explicit CoT with a compact set of learnable latent tokens for reasoning segmentation. LIRSeg is trained in two stages: spatial alignment grounds the latent tokens in object-relevant visual evidence, and GRPO further optimizes them with segmentation rewards. To make these compact latent tokens more informative, we introduce three complementary mechanisms from an information perspective: extreme-advantage sampling for selecting informative training signals, decoupled exploration-stability updates for learning complementary representations, and latent diversity amplification for preventing representational collapse. Extensive experiments on benchmarks demonstrate that LIRSeg consistently improves both segmentation accuracy and reasoning efficiency. Compared with the VisionReasoner baseline, LIRSeg achieves absolute gIoU improvements of 4.9% on ReasonSeg, 7.1% on MUSE, and 4.7% on MMR, while achieving a approximately 16x reduction in reasoning tokens. Code is available in supplementary materials.

---


### 72. [ConsultMind:Towards Automated Diagnostic Consultation via Uncertainty-Aware Reasoning](https://arxiv.org/abs/2609.30796)

**<font color=#1a73e8>作者：</font>** Xiao Sun, Yuming Yang, Yun Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diagnostic consultation is an online sequential decision-making process in which clinicians gather evidence through patient interaction until a diagnosis is sufficiently supported. Automating this process requires adaptive inquiry and interpretable decisions. Bayesian networks offer a natural foundation by updating diagnostic posteriors as evidence accumulates, but their use in open-ended consultation raises two challenges: linking diagnostic hypotheses to potential inquiries and translating evolving posteriors into consultation decisions. We introduce AutoDisym, an automated pipeline that integrates diagnostic knowledge with heterogeneous diagnosis-labeled clinical narratives to construct a Disorder--Symptom Bayesian Network (DSBN). Building on the DSBN, we propose ConsultMind, an uncertainty-aware framework that updates disorder posteriors after each response and uses posterior uncertainty to guide inquiry and diagnosis. We evaluate both methods across psychiatry, respiratory medicine, fever clinics, and three public datasets. The results show that AutoDisym can automatically construct high-quality DSBNs and that ConsultMind consistently improves diagnostic performance and explanation soundness. For example, AutoDisym achieves macro-averaged F1 scores of 81.37 for canonical symptoms and 72.19 for manifestations using GPT-5.6-Sol. ConsultMind improves Top-1 and Top-3 diagnostic accuracy by up to 22.15 and 37.89 percentage points, respectively. Physician evaluation further shows that ConsultMind improves the quality of ranking explanations, differential diagnoses, and diagnosis rationales across LLMs of different scales. This work offers a promising approach to automatic diagnostic consultation.

---


### 73. [HasMem: Hard-Origin Adaptively Softened Memory for Long-Term LLM Agents](https://arxiv.org/abs/2609.30797)

**<font color=#1a73e8>作者：</font>** Zihong He, Junxiao Shen, Chen Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-based memory and context compression support reuse of past interactions. Resizing continuous memory changes the input to a frozen LLM, coupling capacity allocation with readout. We propose Hard-Origin Adaptively Softened Memory (HasMem). Frozen hard-prompt embeddings provide a verifiable initial state. A controller adjusts memory widths, a Writer re-encodes resized entries, and Reader and Global provide readout adaptation and cross-turn state. On all $535$ questions in a reconstruction probe derived from the Multi-Session Chat (MSC) development split, the main configuration achieves lexical F1 of $95.3$ ($+4.4$ percentage points) at $93.6\%$ of the hard reference's framed memory positions. With approximately matched per-question target body budgets, six configurations at mean per-entry retention around $0.83$--$0.91$ exceed rule-based re-encoding by $8.0$--$23.6$ exact-match (EM) percentage points. With fixed model parameters and rule target width ratio $0.75$, Global's EM gain passes a user-level exact paired test with Bonferroni correction over eight comparisons. On all $500$ LongMemEval-S questions, local lexical F1 rises from the hard reference's $3.4$ to $8.9$, and answer negative log-likelihood (NLL) falls from $12.257$ to $5.274$. F1 gains accompany lower EM on both evaluations.

---


### 74. [A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory](https://arxiv.org/abs/2609.30813)

**<font color=#1a73e8>作者：</font>** Xiaoyang Li, Yiqi Wang, Chencheng Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating claim admission in shared agent memory is challenging because repeated claims may be mistaken for independent evidence. An agent may copy or paraphrase a retrieved belief, while admitting a false claim exposes subsequent agents to it. To study this problem, we introduce the Correlated Promotion Benchmark (CPB), which evaluates whether candidate claims should be admitted to shared this http URL-Static constructs a frozen test split from publicly annotated sources with fixed gold actions. CPB-Live runs multi-agent teams over a shared store, records all writes and retrievals, and tracks source lineage defined by each scenario. A separate consumer answers from the store alone. We evaluate eight admission policies across four agent families. Our results show that policies which deduplicate sources reject many true claims alongside false ones, whereas policies preserving answer coverage admit nearly as many false claims as unrestricted sharing. Gating on declared source type reduces false adoption to 0.06--0.09, compared with 0.22--0.47 for other answering policies. Once an uncontested false belief enters memory, the consumer asserts it in 0.97--0.99 of probes across all families. No non-oracle policy consistently rejects false claims across verbatim copies, paraphrases, and paraphrases declared authoritative. These findings reveal the limitations of admission policies without access to source lineage.

---


### 75. [Quantizing Looped Transformers: Feedback Exposure and Calibration Blindness](https://arxiv.org/abs/2609.30820)

**<font color=#1a73e8>作者：</font>** Nux Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers reuse weights across recurrence steps, making low-bit quantization especially attractive. We identify two distinct failure modes of standard post-training quantization. On Huginn-3.5B, per-channel INT4 fails primarily at the non-residual loop-entry adapter, while quantizing the residual core is much less damaging. We call this feedback exposure: a quantized layer perturbs the recurrent state without an identity path, and the resulting error is fed back at later steps. Controlled experiments on linear filters and Mamba state-space models show that feedback exposure also occurs outside transformers. Grouped INT4 reveals a separate failure, calibration blindness: our one-step GPTQ baseline builds its Hessian from step-0 activations, leaving input directions used later in the recurrence nearly unweighted. Across nine checkpoints from seven looped architectures, one-step GPTQ is worse than round-to-nearest (RTN) on the primary task metric for five checkpoints. Accumulating the GPTQ Hessian across recurrence steps outperforms both one-step GPTQ and RTN on all nine checkpoints and recovers bf16-level accuracy on Huginn. These results separate two questions for PTQ on looped models: where quantization error enters the recurrence, and which states calibration sees.

---


### 76. [Crypto-bound identity-verified capability tokens for coordinating distributed AI agents: A proposal](https://arxiv.org/abs/2609.30824)

**<font color=#1a73e8>作者：</font>** Srikumar Subramanian, Shubhashis Sengupta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The prospect of fully autonomous transactional agents did not appear on the horizon until the advent of high capability language models. With such models, the operational benefits of adaptive task orchestration and independent (but constrained) decision making are tantalizing for enterprises and individuals alike. However, each such agent carries with it a serious attack surface in the form of prompt injection which can compromise any soft "guard rails" that may have been placed in context. The consequences of these attacks include credential ex-filtration which, if left unmitigated, renders the whole category of such agents unusable due to breach of trust. Furthermore, expecting a growth of autonomous agents, a security framework for them would require a form of decentralization to scale. Drawing on the proposed OAuth Agent Authorization Profile and the W3C DID and VC standards, we propose a framework based on the principles of capability based security with decentralized agent identity whereby agents access services based on tokens that are cryptographically bound to the agent's and issuer's identities and specify their scope. Services can validate that the delegation chain only involves scope attenuation before acting on any given token. We show that such a layer that lives outside the language model's context window in a secure module can enable agents to act within enforceable security boundaries.

---


### 77. [PTC-Decoder: Towards Intelligent SLMs on Offline Resource-Constrained Edge Devices](https://arxiv.org/abs/2609.30836)

**<font color=#1a73e8>作者：</font>** Minghui Yu, Ke Mu, Gang Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying small language models (SLMs) on offline, resource-constrained edge devices such as remote sensing satellites presents a fundamental challenge: their limited reasoning capacity hinders reliable execution of multi-step agent tasks requiring complex tool orchestration. Existing plan-solve paradigms rely on prompt-based enforcement, which our experiments show SLMs almost entirely disregard: weak models fail to invoke the plan. We propose PTC-Decoder (Plan-Tool Constrained Decoder), a training-free, plug-and-play decoder framework that combines (1) a Plan-to-Act paradigm, which elevates planning to an atomic tool and forces its invocation at the first inference step, and (2) TC-Decoder, a deterministic finite automaton that imposes token-level hard constraints on tool names while preserving freedom over parameter generation, thereby retaining SLM reasoning capability. Evaluated on 200 real remote-sensing satellite tasks across 7 SLMs, PTC-Decoder yields a statistically significant mean overall score gain of +1.21 (p<0.01), 95% CI [+1.13, +1.29]), with consistent improvements across models and other datasets. An ablation study that removes TC-Decoder causes substantial performance degradation across all quality metrics without reducing computational cost, confirming TC-Decoder as the primary driver. PTC-Decoder thus offers a lightweight yet effective solution for improving step-level reliability, with final-answer accuracy remaining an open challenge. In essence, we enforce plan adherence by constraining the permissible output vocabulary during inference, without requiring retraining.

---


### 78. [MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.30837)

**<font color=#1a73e8>作者：</font>** Tianze Xu, Yanzhao Zheng, Zhentao Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) integrates specialized capabilities into a single student, but existing practice typically hard-routes each prompt to a domain-matched teacher for the entire rollout. This dependence on prompt-level domain labels restricts using unlabeled training mixtures and leaves complementary signals from other teachers unused. We introduce MOPD-Router, a framework that routes supervision over the full teacher pool at each token, without domain labels or training a separate routing model. Its plug-in interface supports different metrics for selecting and weighting teacher-specific OPD signals. Within this interface, we propose ExpertAlign, which scores each teacher by whether its correction to the student at the current token expresses the specialization that teacher acquired during post-training, and compare it against two reference metrics built on teacher confidence (Entropy) and teacher-student discrepancy (Novelty). Experiments on unlabeled and domain-labeled training mixtures under strong-to-weak and same-size distillation scenarios show that ExpertAlign achieves the strongest overall performance in all four settings. On unlabeled data, it improves the overall score by 5.88 (+12.3%) points over Mean aggregation; on domain-labeled data, it outperforms standard MOPD by 3.95 (+7.8%) points without using available domain labels. These results demonstrate token-level routing can exploit cross-domain complementary supervision, and reduce exclusive reliance on prompt-level domain assignment. Code is available at: this https URL.

---


### 79. [Enhancing Assessment of Self-Consistency in LLM Explanations using Perturbation Strength](https://arxiv.org/abs/2609.30849)

**<font color=#1a73e8>作者：</font>** Phuong Q. Le, Kemal Kurniawan, Jey Han Lau  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work has examined the self-consistency of LLM-generated explanations using surface-level perturbation methods. However, the strength of these perturbations is not explicitly measured and controlled. In this work, we propose an LLM-as-a-judge approach to measure perturbation strength in a unified manner across input and CoT perturbations. We then evaluate the self-consistency in explanations generated from various LLMs under controlled strength conditions, ensuring a fair comparison across perturbation types. Experiments show that our proposed LLM-based perturbation strength measure outperforms other embedding- and probability-based approaches and that input perturbations generally affect LLMs more strongly than CoT perturbations. Our work suggests that judgments about a model's self-consistency is fair only within the same perturbation type.

---


### 80. [SkillEvoReg: Regularizing Agent Skill Evolution Against Overfitting](https://arxiv.org/abs/2609.30861)

**<font color=#1a73e8>作者：</font>** Guanyu Nie, Fangzhou Zhu, Shixiong Kai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly improve by converting execution experience into reusable external skills. Yet repeated skill updates form a learning process of their own: locally useful edits can accumulate into redundant or task-specific instructions, while new updates can disrupt behavior that previously worked. We study this problem as skill-evolution overfitting and introduce SkillEvoReg, a general regularization framework for skill evolution inspired by anti-overfitting techniques in neural-network training. SkillEvoReg combines training-time skill dropout, which perturbs update generation, and complexity-aware local regularization, which controls unnecessary structural growth, with causal counterexample validation (CCV), which provides targeted behavioral validation of candidate-specific regressions. We instantiate the framework across heterogeneous skill-evolution systems while retaining each system's native skill evolver and task evaluator. Across SkillOpt, SkillEvolBench, and ContinualSkillBench, SkillEvoReg consistently controls skill-state growth while preserving competitive downstream capability, improves several transfer and later-stage evolution outcomes, and identifies update-level regressions that structural metrics alone cannot reveal. These results suggest that explicit regularization is a useful complement to increasingly capable skill updaters.

---


### 81. [Persistent Negatives for Adversarial Black-Box On-Policy Distillation](https://arxiv.org/abs/2609.30864)

**<font color=#1a73e8>作者：</font>** Haixu Ma, Saad Lahrichi, Weiwei Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Black-box On-Policy Distillation (OPD) seeks to improve a student from its own generations when the teacher provides sampled responses but not token probabilities. Adversarial distillation offers one route: it learns a discriminator over prompt-matched teacher and student responses and uses its score as the policy reward. However, sampling discriminator negatives from the latest student at each step couples the learned reward to a negative distribution that changes after every policy update. We address this moving-target problem with persistent-negative adversarial distillation, a live-pool method that replaces a fraction of each discriminator batch with historical, prompt-matched teacher--student comparisons. Under matched discriminator compute, historical comparisons train the discriminator, while GRPO remains on-policy with fresh student responses. Our analysis identifies the Bayes-optimal reward as a teacher-to-negative log-density ratio and, under explicit assumptions, shows how persistent negatives anchor the discriminator and reduce reward-estimation MSE relative to fresh-negative training. Across two student families, three judges, and four judged-chat benchmarks, persistent-negative adversarial distillation consistently improves performance over current methods at matched discriminator compute. It also yields smoother fresh-policy discriminator trajectories, with fewer below-chance dips. These findings identify the discriminator's negative distribution as an important design axis in black-box on-policy distillation.

---


### 82. [Evidence-Grounded Auditing of Identification Assumptions in Climate-Policy Causal Evaluations](https://arxiv.org/abs/2609.30867)

**<font color=#1a73e8>作者：</font>** Yonghong Zhang, Yong Xie, Isabel M. Parra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Difference-in-differences (DID) studies are widely used to evaluate climate policy, but assessing the evidence supporting their identification assumptions remains challenging. We introduce ARGUS, a structured language-model pipeline that audits reported evidence against an eleven-dimension assumption-implication-evidence rubric and abstains when relevant evidence cannot be retrieved. We evaluate ARGUS using injected flaws, economics papers, and a small pilot with reconciled labels. On the 11-flaw benchmark, ARGUS detects 73% of planted flaws, compared with 18% for a keyword-based pipeline. Across 26 economics papers, ARGUS abstains on about 40% of paper-dimension assessments for lack of retrievable evidence. In a five-paper pilot with labels reconciled by two annotators, it assigns a higher risk level than the labels on 25 of the 33 assessments it completes. A rule fixed before the labels arrived removes most of this in-sample; weighted agreement stays low. ARGUS provides evidence-linked risk reports that localize potential weaknesses for expert review, without adjudicating causal claims. Code and data: this https URL

---


### 83. [Effects of Transcript Compression on LLM-based Medical Misinformation Detection in Japanese YouTube Videos](https://arxiv.org/abs/2609.30882)

**<font color=#1a73e8>作者：</font>** Yuya Wake, Sho Tsugawa, Toshiyuki Amagasa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to assess long-form medical videos, but their effectiveness may depend on whether transcripts are provided in full or compressed through summarization, retrieval, or claim screening. This study examines how such transcript compression affects LLM-based veracity classification of Japanese medical YouTube videos. We compare four transcript input designs: full transcripts, LLM-generated summaries, RAPTOR-based retrievalaugmented generation (RAG), and Screening, which extracts candidate medical and health-related sentences. Using 74 long-form videos labeled as Real or Fake, we evaluate classification performance and analyze linguistic changes using J-LIWC, hedge expressions, and institutional or technical terms. The full-transcript Baseline achieved the best performance, whereas all compressed inputs increased false negatives, meaning that Fake videos were more likely to be misclassified as Real. Summary caused the largest performance drop, while Screening performed best among the compressed inputs but still omitted many medically relevant sentences. Linguistic analyses showed that these errors were not explained by a simple increase in certainty. Instead, Summary reduced affective, social, temporal, cognitive, and conversational cues, while Summary and RAG made institutional and technical terms more salient. These findings suggest that transcript compression can represent Fake videos as more coherent and authoritative inputs, thereby weakening cues needed for misinformation detection

---


### 84. [CacheReforge: Bounded Recovery for Stale KV Caches under Evolving Adapters](https://arxiv.org/abs/2609.30884)

**<font color=#1a73e8>作者：</font>** Yuhang Cao, Yanzhou Mu, Chunrong Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models rely on KV caching to reduce repeated prefill computation in long context and interactive applications. As lightweight adapters evolve, cached states reflect earlier versions, so stale reuse distorts current model outputs, while complete affected suffix recomputation restores fidelity at substantial cost. We seek minimal recomputation that recovers current adapter behavior. Existing systems track token, context, or stable adapter identity, but neither represent caches from earlier adapter versions nor distinguish update propagation from the recomputation required for behavioral recovery. To address these gaps, we introduce CacheReforge, which represents stale KV caches as layerwise mixed-version objects. It combines per-layer adapter anchors, calibrated sensitivity, accumulated drift, and executable restart boundaries to select direct reuse, bounded recomputation, or complete affected-suffix recovery. We distinguish dependency depth from the functional recomputation horizon and use cumulative tail influence to characterize when bounded recovery preserves current-model behavior. We evaluate CacheReforge on Qwen2.5-1.5B and Qwen2.5-7B with continual LoRA updates, including 16K HotpotQA and 2WikiMQA workloads. CacheReforge reduces mean KL divergence by 92.4% relative to stale reuse, while recomputing only 5.44% of layers and reducing cache-maintenance time by 93.2% relative to fresh full prefill. These results show that version-aware recovery preserves model fidelity and most KV caching gains.

---


### 85. [Training Graph Foundation Models on The Web Graph](https://arxiv.org/abs/2609.30894)

**<font color=#1a73e8>作者：</font>** Ryoma Sato  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Acacia, a graph foundation model, trained on the web graph. Acacia (i) supports arbitrary feature dimensionalities and semantics without additional training, (ii) supports a wide range of tasks, including node classification, link prediction, node clustering, and graph generation, without additional training, (iii) has in-context learning capabilities, and (iv) does not rely on pretrained LLMs. In particular, existing graph foundation models often require training additional classification heads or feature projectors to accommodate new graphs or new labels, whereas Acacia does not. Moreover, existing graph foundation models often gain their capabilities by being stitched together with pretrained LLMs, whereas Acacia is trained from scratch using only the Common Crawl web graph. This is also an important result because it provides evidence that graph models can acquire emergent capabilities from scratch like LLMs.

---


### 86. [From annotation to reasoning: Culture in language models](https://arxiv.org/abs/2609.30897)

**<font color=#1a73e8>作者：</font>** Daniel Hershcovich, Alexander Conroy, Jens Bjerring-Hansen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How should we evaluate language models when more than one interpretation can be right? Cultural benchmarks often test factual knowledge, agreement with survey responses, or recognition of a predefined meaning. These tasks leave open whether a model can explain how a cultural reference works in a particular text, support a reading with evidence, or revise it after criticism. This is a question of interpretive depth, complementary to the breadth of cultural coverage. We argue that literary interpretation offers a useful setting for studying these capabilities. We focus on cultural referencing and reuse: how texts invoke, repeat, and transform earlier expressions across historical and linguistic contexts. Our central claim is that literary scholars can disagree about an interpretation while recognizing the quality of its support. We propose linking evidence-centered benchmarks, evaluation that preserves scholarly disagreement, and model-development experiments on literary data, contextual resources, and scholarly feedback. Danish literature provides a concrete starting point, with implications for other languages and domains. The aim is to develop alternative evaluation strategies that go beyond conventional benchmark metrics and guide model development toward cultural robustness in AI systems.

---


### 87. [ToolSearcher: Optimizing Tool Selection at Scale via Reinforcement Learning](https://arxiv.org/abs/2609.30906)

**<font color=#1a73e8>作者：</font>** Zhenlong Dai, Xujie Song, Zitong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at natural language processing but struggle to interact with external environments. Tool learning provides a promising way to extend LLMs into actionable agents, where tool selection is a critical prerequisite for successful tool use. Existing work often assumes a small or predefined set of tools, leaving large-scale tool selection underexplored. Real-world repositories contain a vast and diverse array of tools, making it difficult for LLMs to effectively search, distinguish, and compose tools under context-length constraints. We identify large-scale tool selection as a new challenge for agentic reinforcement learning, highlighting that existing RL methods for knowledge-based question answering are inadequate for selecting tools while considering compatibility. To address this challenge, we propose ToolSearcher, a novel RL framework for effective multi-turn search and fine-grained optimization in large-scale tool selection. Specifically, we introduce category-constrained tool discrimination to improve the model's ability to distinguish functionally similar tools, event-level search modeling to explicitly optimize the discovery of target tools during multi-turn search, and trajectory-aligned credit allocation to provide fine-grained reward signals for different stages of the search-selection process. Extensive experiments on large-scale tool selection benchmarks demonstrate that ToolSearcher consistently outperforms a set of strong baselines in challenging settings involving iterative search and complex tool composition.

---


### 88. [Machine Unlearning for Large Language Models: Foundations, Advances, and Agentic Extensions](https://arxiv.org/abs/2609.30909)

**<font color=#1a73e8>作者：</font>** Xiaoyu Xu, Minxin Du, Li Bai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove target influence while preserving other capabilities. This survey compares methods, benchmarks, and evidence across large language models and systems using retrieval, memory, tools, and interacting agents. A five-layer framework connects removal requests, system boundaries, target locations, interventions, and supported claims. A seven-stage lifecycle and six evidence dimensions guide comparison. The review shows that target construction, retained data, and recovery tests affect reported outcomes. Evidence from model evaluations remains insufficient to establish removal across external state and subsequent updates, motivating evaluation that tracks dependencies and tests whether target influence returns.

---


### 89. [JevSoup: System-One Routing for Training-Free LoRA Composition](https://arxiv.org/abs/2609.30922)

**<font color=#1a73e8>作者：</font>** Xiuying Wang, Jiahua Cheng, Shuotian Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building adaptable AI systems requires effective coordination of specialized capabilities across diverse tasks. Low-rank adaptation (LoRA) enables modular expertise, but existing routing approaches may require auxiliary data, additional training, or autoregressive decoding. We propose JevSoup, a training-free framework separating System One expert routing from System Two execution. Using only the input and expert descriptions, Jev selects two experts through structured probabilities. JevSoup retains the leading expert's update, projects the second onto the orthogonal complement of the first update's row space, and combines them with equal weights. Across 14 PorTAL tasks and three Qwen3 scales, JepSoup achieves absolute gains of up to 1.19\% in task-macro and 1.21\% in sample-micro accuracy over the strongest evaluated external baselines. Our code is available at this https URL.

---


### 90. [Training-Free Pronunciation Transcription via Text-Constrained Acoustic Rescoring](https://arxiv.org/abs/2609.30924)

**<font color=#1a73e8>作者：</font>** Hikaru Asano, Yotaro Kubo, So Kuroki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate and efficient pronunciation transcription is essential for preparing text-to-speech training data at scale. Existing approaches have different limitations: grapheme-to-pronunciation (G2P) and speech-to-pronunciation (S2P) methods each capture only partial information, using only text or only speech, while speech-and-text-to-pronunciation (ST2P) methods use both but require costly pronunciation-annotated data. To address this problem, we propose a training-free ST2P pipeline that integrates both lexical and acoustic information at inference time. Lexical resources and G2P tools generate text-constrained candidates, and a left-to-right greedy search selects the best one using whole-sequence negative log-likelihoods from frozen pretrained S2P models. On three Japanese corpora, our method reduces Character Error Rate (CER) from 0.60--1.40\% (text-only baseline) to 0.04--0.17\% with reference transcripts, and 0.64--1.58\% with ASR transcripts. It outperforms all baselines, including a trained ST2P model and commercial multimodal LLMs. Our greedy search method is 3--3.5$\times$ faster than beam search at similar CER, and the cascade is 2$\times$ faster than direct decoding ensuring the efficiency and accuracy. In Spanish, French, and preliminary English, it also surpasses four open multimodal LLMs and the best traditional methods.

---


### 91. [UltraG-Bench: A Multi-task Benchmark for assessing Large Vision-Language Models on Pixel-level Evidence Grounding in Ultrasound](https://arxiv.org/abs/2609.30928)

**<font color=#1a73e8>作者：</font>** Quanhao Zhu, Bo Xu, Rui Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound is one of the most widely used medical imaging modalities, and recent large vision-language models(VLMs) have shown increasing capabilities in ultrasound image understanding. However, these models fail to provide pixel-level visual evidence aligned with their semantic predictions, and their fine-grained grounding capability in ultrasound remains largely unclear. We introduce UltraG-Bench, a large-scale multi-task benchmark for evaluating pixel-level evidence grounding in ultrasound. UltraG-Bench is built by annotating 40 public ultrasound segmentation datasets spanning 13 anatomical categories, and comprises three progressive tasks: instruction-guided segmentation, evidence-grounded VQA, and evidence-grounded report generation, with 331125, 666779, and 138832 annotations, respectively. Comprehensive evaluation of 14 state-of-the-art models reveals a substantial gap between semantic understanding and fine-grained pixel-level localization. We further propose UltraG-Agent, which combines the semantic reasoning capabilities of a VLM with the ultrasound-specific segmentation capability of UltraSAM3. Experiments show that UltraG-Agent substantially improves both semantic prediction and pixel-level visual grounding. Our dataset and code are available at this https URL.

---


### 92. [ManiVid: Unified and Explainable Forensic Analysis of Manipulated Videos](https://arxiv.org/abs/2609.30934)

**<font color=#1a73e8>作者：</font>** Hengrui Kang, Zhonghao Yan, Yuxuan Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid advances in AI-generated video (AIGV) have increased the risks posed by deceptive video manipulation. Unlike fully synthetic videos, manipulated videos retain most source content and alter only localized regions, making forensic analysis particularly challenging. Existing video forgery research faces two limitations in both data and methodology: (1) High-quality datasets and benchmarks tailored for manipulated videos remain scarce. (2) Multimodal large language models (MLLMs) extend forgery analysis beyond binary classification but struggle to use low-level forensic cues and provide precise pixel-level grounding. Specifically, we introduce ManiVid, a unified forensic analysis task covering forgery detection, artifact grounding, and anomaly explanation for manipulated videos. We construct ManiVid-38K, the first dataset to combine paired, open-vocabulary localized manipulations of general videos with authenticity labels, forgery masks, and anomaly explanations. It comprises about 19K manually verified real-fake video pairs, mostly at 1080P resolution, generated under 2 paradigms with 15 powerful generation models. We sample 1K pairs for ManiVidBench, balanced across six manipulation types and generation models for fair evaluation. We further propose ManiVidLens, a unified framework for explainable video forgery analysis. Its Forensic Evidence Router supplies shared low-level forensic evidence for multimodal reasoning and video segmentation. Its Prompt Distill Module converts grounding states into semantic and geometric prompts and distills spatial priors for mask decoding and full-video propagation. ManiVidLens achieves relative gains over the strongest comparison methods in artifact grounding (+21.1% mIoU; +21.3% J&F) and anomaly explanation (+131.3% ROUGE-L; +9.9% CSS). Its forgery detection remains comparable to dedicated classifiers (0.914 Acc; 0.913 F1).

---


### 93. [Estimating and Orthogonalizing Unknown Pre-training Gradients for Continual Fine-tuning of Large Language Models](https://arxiv.org/abs/2609.30935)

**<font color=#1a73e8>作者：</font>** Bing Wang, Changchun Li, Xin-Qiang Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual fine-tuning is essential for large language models (LLMs) to dynamically adapt to real-world environments, yet it inevitably suffers from catastrophic forgetting, particularly the performance degradation of previous tasks and LLMs' general-purpose knowledge. Although existing methods, such as orthogonal gradient projection, mitigate the forgetting across various fine-tuning tasks, they fundamentally fail to preserve pre-training LLMs' inherent general-purpose knowledge because the original data and gradients of off-the-shelf pre-training LLMs required by these methods are strictly unknown and highly diverse. To bridge this critical gap, we propose EoupCT, a novel framework designed to Estimate and Orthogonalize Unknown Pre-training gradients for Continual LLM fine-Tuning. Specifically, EoupCT estimates pre-training gradients by dynamically generating pseudo data that is most susceptible to forgetting for new tasks through a learnable soft prompt equipped with Gumbel-Softmax relaxation. Furthermore, we formulate a multi-objective optimization problem and introduce a first-order efficient Pareto optimizer that jointly optimizes LLM parameters and the soft prompt, rigorously enforcing orthogonality between new task updates and the estimated pre-training gradients. Extensive experiments across multiple LLMs demonstrate that EoupCT effectively preserves both task-specific proficiency and inherent general-purpose knowledge, successfully mitigating the catastrophic forgetting.

---


### 94. [Self-Play Search Distillation for Large Language Model Reasoning](https://arxiv.org/abs/2609.30936)

**<font color=#1a73e8>作者：</font>** Lorenzo Molfetta, Wai-Chung Kwan, Giacomo Frisoni 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving reasoning abilities in Large Language Models (LLMs) requires high-quality data that exposes difficult decisions, competing alternatives, and their consequences. Data scarcity is driven by the low quality of synthetic data and the cost of human labeling. We introduce Self-Play Search Distillation (SPSD), a framework for generating superhuman synthetic data via self-play of MuZero-like networks trained on board games. SPSD uses executable environments to turn search into structured reasoning problems. At each state, the expert identifies a preferred decision, plausible alternatives, plausible opponent replies, and value estimates. By converting the self-play search records into superhuman chains-of-thought, we train LLMs with environment-grounded supervision. Although trained only on self-play search records, SPSD transfers to unseen mathematics. On Qwen3-4B-Base, it raises the mean over six mathematics benchmarks from 24.1 to 36.6 while increasing the held-out-game win rate from 15% to 45%. SPSD offers an annotation-efficient way to create high-quality synthetic data for improving LLM performance in reasoning tasks.

---


### 95. [MACBT: A Multi-Agent Cognitive Behavioral Therapy Decision Support System with Longitudinal Memory](https://arxiv.org/abs/2609.30939)

**<font color=#1a73e8>作者：</font>** De Jiang, Shuo Zhang, Weiwei Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive behavioral therapy (CBT) is an evidence-based first-line treatment for depression, yet its scale is constrained by the time clinicians spend on pre-session preparation, post-session documentation, and longitudinal cognitive-pathology tracking. We present a clinician-facing AI decision-support system that combines a multi-agent CBT framework (MACBT) with a CBT-specific longitudinal memory module (CD Memory). MACBT encodes the five-stage CBT workflow (assessment, Socratic questioning, cognitive restructuring, behavioral experiments, and treatment monitoring) into five collaborative agents. CD Memory tracks cognitive-distortion type, frequency, severity, and restructuring efficacy across sessions to generate pre-session pathology reports and intervention-priority recommendations. We construct a Chinese CBT dialogue corpus via dual-role large language model simulation and train a Qwen3-14B backbone with supervised fine-tuning and direct preference optimization. Evaluation with GPT-4 judges shows MACBT outperforms MeChat, SoulChat, PsyChat, and CPsyCounX in professionalism (2.62) and clinical authenticity (2.25). The full memory-augmented system further improves session quality by 12.6% and achieves a longitudinal mean of 2.29 on cross-session continuity, intervention progression, and personalization.

---


### 96. [Financial Fragility in Societies of LLM Agents: Coordination Failures and Stabilizing Mechanisms](https://arxiv.org/abs/2609.30940)

**<font color=#1a73e8>作者：</font>** Zhenhao Fu, Ruipeng Xu, Qibing Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Individually protective decisions can produce avoidable collective failures. As large language model (LLM) agents take on greater roles in financial decision-making, financial AI safety must therefore be considered not only at the level of individual agents, but also at the level of the systems they jointly create. We study this problem with FRAIL, a controlled experimental framework that places LLM agents in three dynamic financial environments---bank runs, debt rollover, and reward crowdfunding---where agents' decisions reshape the financial conditions faced by others. Across seven leading LLMs, we find widespread collective fragility even when no agent is instructed to destabilize the system: 77\% of baseline bank-run episodes and 83\% of debt-rollover episodes end in failure. We then compare three interaction mechanisms based on compensated commitments, centralized commitment agreements, and participant-led coalitions. All three improve aggregate outcomes, but no single mechanism performs best across all financial structures. Across mechanisms, successful stabilization shares a common temporal pattern: broad commitment forms early, before defensive behavior becomes self-reinforcing. Our findings show that individually capable agents do not automatically form safe financial systems, highlighting system-level evaluation and interaction design as central problems for financial AI safety. Code is available at this https URL.

---


### 97. [LogicTree-RAG: Logic Tree-guided Retrieval-Augmented Generation for Long-form Patent Drafting](https://arxiv.org/abs/2609.30943)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhu, Naili Xing, Hexiang Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-form technical text generation underpins knowledge-intensive workflows, yet remains challenging for large language models (LLMs) due to the need for globally consistent logical structuring and faithful technical reasoning beyond local coherence. Patent drafting is a canonical instance of this challenge, demanding holistic generation of a legally compliant and technically exhaustive document through sustained multi-expert collaboration. Existing approaches often focus on partial section generation or rely on manually crafted outlines, limiting scalable automation in realistic settings. In this work, we propose LogicTree-RAG, a logic tree-guided retrieval-augmented generation framework that induces a hierarchical logic tree as a global organizational backbone to organize and ground technical disclosures, without relying on expert-defined drafting priors. Each node in the logic tree represents a technical element and is constructed through evidence-guided recursive generation. A hybrid traversal mechanism then maps the logic tree into patent sections, enabling controllable and section-balanced generation. Extensive experiments show that LogicTree-RAG consistently improves content quality and language conformity over strong LLM-based baselines and achieves longer structured generation with high token efficiency, demonstrating the effectiveness of logic-centric generation for complex technical document drafting.

---


### 98. [Low-Bit Recurrent States in Hybrid Language Models](https://arxiv.org/abs/2609.30950)

**<font color=#1a73e8>作者：</font>** Hongren Chen, Jiayang He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid language models maintain fixed-size recurrent states, but existing quantizers typically use eight bits or more. Quantization errors persist according to channel decay rates. We derive distortion weights from the observability Gramian and combine them with normalized state ranges for mixed-precision bit allocation, without calibration data, rotation, or training. We also quantize decay rates logarithmically. With per-token state quantization, a four-bit mean payload reduces excess negative log-likelihood by factors of 3.3--27.9 relative to the best of seven baselines across three hybrid models; metadata costs vary. At six bits, negative log-likelihood differs from the FP32-state baseline by less than 0.005 nats. Ablations separate gains from variable bit widths, decay weighting, and range normalization. With less frequent write-backs, gains diminish and depend on the model and budget.

---


### 99. [MVVBench: Benchmarking 4D Reasoning in Vision-Language Models](https://arxiv.org/abs/2609.30952)

**<font color=#1a73e8>作者：</font>** Hyungjin Chung, Byeongjun Park, Joonseok Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view video understanding requires integrating spatial and temporal evidence across multiple, often non-overlapping camera streams: tracking entities as they transition between viewpoints, aligning events across time, and reasoning about latent 4D continuity rather than any single visible frame. We introduce MVVBench, a benchmark for multi-view video reasoning built from real world multi camera datasets. Questions are curated to be monocular-ambiguous along both the view and the temporal axis: each question is unanswerable from any single view in the designated input set, and the majority are further unanswerable from any single moment. Each question becomes uniquely solvable only by jointly reasoning across views and across time. MVVBench spans diverse dynamic scenes and probes six capabilities: implicit/explicit attribute identification, implicit/explicit relative distance, relative camera pose, and compositional counting, with human-authored QA and rigorous verification. Beyond benchmarking, we provide an extensive analysis of when and why current vision language models succeed or fail, characterizing errors due to temporal mis-localization, cross-view identity breaks, and brittle multi-hop reasoning. We then study inference-time elicitation strategies that unlock latent multi-view competence---task-specific chain-of-thought scaffolds and structured cross-view evidence aggregation---yielding substantial gains without retraining. Finally, we present preliminary evidence that reinforcement learning with verifiable rewards can elicit some latent multi-view competence in the base model, pointing to training-time approaches as a promising direction for future work. Together, MVVBench offers a rigorous evaluation of 4D multi-view reasoning and a foundation for future progress toward reliable embodied perception.

---


### 100. [FTB Graph: Determining and Validating First-token Broadcasters and Language-Identity Head Circuits in Multilingual Language Models](https://arxiv.org/abs/2609.30954)

**<font color=#1a73e8>作者：</font>** Arjun Pillai, Christian Hoang, Anjelo Laroza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models operating in multilingual contexts must resolve target response languages early in generation, yet the causal circuitry governing first-token language identity decisions remains poorly mapped. We present an end-to-end structural circuit analysis across six model architectures spanning four families: GPT-2, BLOOM-560M, Pythia-1B/2.8B, and Qwen2.5-1.5B Base/Instruct. Using Edge Attribution Patching (EAP) with FP16 active clamping, followed by exact activation patching verification with a 2,000-candidate-edge search ceiling, we extract directed acyclic graphs driving first-token language broadcasting. Across the standalone models, we observe deep or mid-to-deep broadcasting hubs, though the evidence is strongest for Pythia-2.8B and BLOOM-560M because GPT-2 and Pythia-1B leave few out-of-graph heads for comparison, while both Qwen2.5-1.5B variants invert the necessity check. Scaling from Pythia-1B to 2.8B expands node participation while maintaining a similar verified edge budget, producing sparser topology. The Qwen2.5-1.5B base and instruct circuits retain 84.7% Jaccard similarity, including the Layer 27 hub, indicating that first-token routing is largely established during pretraining and preserved by instruction tuning. Finally, EAP scores correlate weakly with exact patching deltas across most models, showing that linear gradient approximations can diverge from causal interventions in FP16 and motivating exact-patching verification for reliable circuit discovery.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-183](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
