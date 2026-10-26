# 🧠 大模型相关研究 | 2026年10月27日

> 本类共 **204** 篇论文：已确认 **185** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 1. [Validating the Comparison, Not Just the Scorer: Why Overall Accuracy Can Mislead in Interactive LLM Evaluation](https://arxiv.org/abs/2610.31678)

**<font color=#1a73e8>作者：</font>** Ancil Crayton  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many LLM studies compare how models respond to different follow-up prompts. For example, one prompt may neutrally ask a model to reconsider, while another insists that an invented film really exists. The difference is used to measure the effect of conversational pressure. An automatic scorer then labels whether each response makes an unsupported factual claim. Researchers commonly validate the scorer with one overall accuracy or $F_1$ score. However, high overall performance can hide prompt-specific mistakes: if the scorer makes more errors after one prompt, the measured difference can be too large, too small, or point in the wrong direction. An audit containing mostly difficult responses can also misrepresent performance in the full study. We derive how such errors alter a prompt comparison and examine the problem using six models, 180 invented-entity questions, and six prompt conditions. In a balanced audit of 288 responses, overall $F_1$ was $.916$. Yet, depending on the prompt, the scorer flagged 2.6%-33.3% of responses that the primary LLM rater judged not to contain an unsupported claim; these prompt-specific estimates were uncertain. In a second audit, the scorer and two separate LLM raters evaluated the same 300 model-question cases under each prompt. An apparent 9.3-point increase from asserting certainty rather than neutrally asking the model to reconsider fell to 2.3 points under both raters. The primary-rater interval included zero, so it did not establish an increase. Two other prompt comparisons kept their direction under both raters, while an attempted prompt-specific correction remained too uncertain for a firm conclusion. Researchers should therefore validate the exact difference they plan to report, not just the scorer as a whole: audit both prompts on matching cases and include scorer and rater uncertainty in the final result.

---


### 2. [MisconceptDialogue: Evaluation Criteria Shape Measured Success in LLM Math Tutoring](https://arxiv.org/abs/2610.31679)

**<font color=#1a73e8>作者：</font>** Woojin Lee, Yoonkyu Woo, Jinah Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as math tutors, raising two questions: can a single LLM detect a student's error, diagnose the underlying misconception, and remediate it through multi-turn dialogue - and can we trust the numbers that report how well it does? We address both with MISCONCEPTDIALOGUE, a fully automated framework that runs the full pipeline on five open-weight LLM tutors (7B-14B) interacting with LLM-simulated students over 5,000+ dialogues - a deliberately simulated protocol (paired conditions, a wrong-diagnosis control unsafe with real learners, scale) whose results do not establish real-student learning. On measurement, our headline finding is uncomfortable for the field: benchmark-style exact-match scoring common in standard math NLP - a lower-bound stress test - reports 42.1% measured Remediation Success Rate on identical dialogues where a human-calibrated LLM-as-judge reports 81.3%, a 39.2 percentage-point spread larger than the combined effects of tutor model, teaching strategy, and supplied diagnostic information. This is not a single-judge artifact: four independent LLM judges and 200 human annotations converge to within a few points (kappa up to 0.91). On capability, the verdict is equally striking: the score barely changes whether we tell the tutor the student's actual misconception or a deliberately swapped one - under the tested diagnosis-presentation format, these tutors show little evidence of reliably conditioning on the diagnostic information they are handed. For LLM tutoring evaluation to mature, multi-criterion scoring with multi-judge convergence and human anchoring should become standard practice - and the measurement question deserves as much scrutiny as the capability question it claims to answer.

---


### 3. [The Schema Coherence Inventory: Measuring Whether an Assigned Belief Organizes a Language Model's Cognition](https://arxiv.org/abs/2610.31683)

**<font color=#1a73e8>作者：</font>** Yuqi Wu, Deyang Li, Katharine Hibbard 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona-conditioned language models are used as simulated patients and affective agents, but there is no validated way to ask whether a belief assigned to such a model organizes its behaviour or whether the model has merely adopted a mood. We present the Schema Coherence Inventory (SCI): 96 forced-choice items at eight levels of Beck's cognitive model, each offering six replies keyed to three negative self-schemas and their positive counterparts, scored by length-normalized log-likelihood so that nothing is generated or parsed. Affect alone can move a model onto a default belief, so the discriminant criterion is target specificity: a condition built for one belief must select that belief more often than conditions built for the other beliefs of its pole. Six validation studies over 107 conditions on five backbones (1.7B-14B parameters) support this reading. Nine clinically trained raters recover the keyed belief at 79.5% (chance 16.7%). Belief adapters are target-specific on every backbone (+17.7 points; 30/30 belief cells positive), and a condition's SCI profile identifies its own free generations in 24/30 cases against 5 expected by chance. A 48-item short form correlates r = 0.73 with the other 48 items. Applied to six published patient simulators, none carries its formulation's core belief better than a one-sentence statement of it. The validation route, which separates a construct from the affect that accompanies it and checks model judges against clinicians, offers a template for affective measurement in language models; we outline its extension across task types, raters, sites and languages. We release the items, scoring code and short form.

---


### 4. [Knowledge Graphs Quality Assessment in the Era of LLMs: A Conceptual Framework](https://arxiv.org/abs/2610.31684)

**<font color=#1a73e8>作者：</font>** Elwin Huaman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs (KGs) have been popularized during the last few decades and are increasingly constructed and consumed by Large Language Models (LLMs). Various applications therefore rely on KGs to provide concise, complete, accurate, faithful, fresh, and traceable answers. However, what is the quality of those KGs? In which cases should a KG be used, and can it be trusted to ground an LLM? How might it be evaluated? We reviewed the literature on quality assessment (QA) of data, information, linked data, KGs, and the intersection of KGs and LLMs. We extended the current state-of-the-art frameworks to a catalog of 24 quality dimensions (QDs) and various quality metrics (QMs). Furthermore, we propose a general-purpose, customizable to a domain or task, and practical QA framework for assessing the quality of KGs.

---


### 5. [An Agentic Approach with Evidence-Grounded Verification for Multimodal Emotion Reasoning in Conversation](https://arxiv.org/abs/2610.31685)

**<font color=#1a73e8>作者：</font>** Elyas Rashno, Farhana Zulkernine  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based multimodal emotion reasoning systems perform well on standard benchmarks, but improving them through instruction tuning can be computationally expensive. Agentic pipelines built from frozen models avoid this cost, but introduce a different challenge: when a prediction is wrong, the system must identify which agent or stage caused the error. We address this problem with an agentic framework for traceable multimodal emotion reasoning and prompt-space adaptation. Modality-specific perception agents analyze visual, acoustic, and lexical inputs and post evidence-cited observations to a shared board. An integration agent combines these observations with retrieved multimodal examples to produce an emotion description, label set, and supporting citations, while an MLLM critic can request one revision before the output is finalized. For incorrect predictions, a separate evidence-grounded verification stage applies deterministic checks to verify that cited evidence and references are valid, and an entailment check to determine whether the final claims are supported by that evidence. Detected failures are then grouped by the responsible component and failure type, converted into targeted prompt patches, and accepted only after validation on a held-out set. This adapts the agent prompts without updating model weights. On the MER2025 dataset, targeted prompt adaptation outperforms the frozen static pipeline on all four MLLMs, ranging from 2B to 38B parameters, and matches or outperforms undifferentiated reflection baselines on each of them: VideoLLaMA3-2B, Phi-3.5-vision-instruct, Qwen2.5-VL-7B-Instruct, and InternVL2.5-38B. It improves F-score by 0.6--2.2 points depending on the backbone, including an increase from 52.3 to 54.5 on Qwen2.5-VL-7B.

---


### 6. [From Target Selection to Condition Reuse: Auditing Residual Interventions in Tool-Use Models](https://arxiv.org/abs/2610.31686)

**<font color=#1a73e8>作者：</font>** Tianda Sun, Dimitar Kazakov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation interventions can make a language model produce a target answer, but can the model use the intended condition in other computations? We study this question in Qwen3.5-27B on tool-use tasks where time or permissions determine eligibility and selection. Across 32 fresh worlds, two case-specific residual-writing variants raise familiar target-selection correctness from 35/128 to 119/128 and from 33/128 to 114/128. Yet these gains disappear when familiar facts and identifiers are recombined within the same selection task, while selection of previously rewarded identifiers increases. The gains persist across output formats but yield little improvement in independent judgments about whether a candidate is eligible or should be selected. Internal edits can nevertheless change how a source fact affects a judgment: in a prespecified secondary comparison, an early-layer source patch changes 50/64 judgments when that source is used, with one adverse change among 64 cases where it is not. This selective effect does not ensure correct complete actions. Together, these results separate target-selection control, condition-sensitive judgments, and complete-action correctness. Evaluating how an edited state is used, rather than only its trained answer, exposes these differences.

---


### 7. [Distributional Alignment of LLMs and Its Generalization Properties](https://arxiv.org/abs/2610.31687)

**<font color=#1a73e8>作者：</font>** Nelson Jo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to simulate and probe human behavior, e.g., for surveys. For these applications, a key property is that outputs satisfy distributional alignment: to match its output distribution with some reference (in this case, human) distribution. An obstacle in achieving distributional alignment is generalizing from small training data. In this work, we study (1) how to distributionally align LLMs; and (2) how aligned LLMs might generalize to unseen samples and unrelated topics and tasks. Using two large-scale benchmarks, we find that LLMs can indeed achieve distributional alignment and generalize to unseen questions of the same domain. Cross-topic generalization depends on the relationship between topics (e.g., questions about politics are related to trust in institutions). However, aligned LLMs can degrade in surprising ways (e.g., lose their creative ability), suggesting that its generalization properties are inherently unpredictable and unstable.

---


### 8. [Collaborative In-Context Learning for Indoor Radio Map Estimation](https://arxiv.org/abs/2610.31702)

**<font color=#1a73e8>作者：</font>** Yuanzhe Peng, Jie Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indoor radio map estimation (RME) is essential for wireless applications such as coverage planning, localization, and network deployment. However, most existing methods follow a supervised learning paradigm that requires costly labeled data and task-specific model training. Moreover, indoor environments involve privacy-sensitive information, such as building layouts and structures, that often cannot be centralized. To address these challenges, we make the first attempt to formulate indoor RME as a collaborative in-context learning (ICL) problem. We propose Poly-Ripple, a framework in which multiple clients perform ICL using large autoregressive vision models (LAVMs) without model updates. Each client is prompted by its private demonstrations and predicts the radio map for the same scene query. To capture the causal structure of wireless propagation outward from the transmitter (Tx), we adopt ripple-ordered autoregressive modeling. We further introduce importance-aware aggregation to exploit heterogeneous contextual knowledge distributed across clients under the context length constraint. We provide theoretical analysis and conduct extensive experiments on a public indoor RME benchmark. The experimental results show that Poly-Ripple consistently outperforms representative ICL baselines, while aligning with our theoretical analysis.

---


### 9. [Autoregressive Multimodal Anomaly Detection with Large Language Models for Microservice Systems](https://arxiv.org/abs/2610.31722)

**<font color=#1a73e8>作者：</font>** Yixiang Tang, Fagui Liu, Guoxiang Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Microservice systems have become a dominant architecture for large-scale cloud applications, enabling rapid deployment and elastic scaling. However, ensuring the reliability and availability of microservice systems critically relies on effective anomaly detection, as failures and performance anomalies can quickly propagate across services and severely impact end-to-end system behavior. Existing multimodal anomaly detection approaches for microservice systems often struggle with two fundamental limitations: (i) the neglect of modality-specific characteristics in favor of cross-modality fusion, and (ii) the "identity-shortcut" problem that affects the feature reconstruction process. To address these issues, we propose LLMMAD, an autoregressive multimodal anomaly detection framework for microservice systems based on Large Language Models (LLMs). Initially, to reconcile cross-modality fusion with modality-specific preservation, LLMMAD embeds and recombines multimodal data into a unified sequence for LLM processing to model inter-modality relationships, while employing modality-wise reconstruction heads to retain modality-specific information. Subsequently, to eliminate the identity-shortcut, we implement a prediction-driven autoregressive objective, under which the model predicts future states rather than copies current inputs. Finally, we conduct extensive experiments on three real-world datasets. The results demonstrate that LLMMAD consistently outperforms state-of-the-art methods, achieving F1-score improvements of 3.1%, 1.4%, and 0.9%, respectively, thereby providing a more reliable solution for microservice monitoring.

---


### 10. [LAMB: A Modern Contextual Language Model for Latin](https://arxiv.org/abs/2610.31723)

**<font color=#1a73e8>作者：</font>** Aidan McCarthy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article introduces Latin Modern BERT (LAMB), an encoder for the Latin language based on the ModernBERT architecture, pretrained in two phases on more than 74B Latin tokens using a novel morphologically informed masking regimen. We also present two corpora for the Latin language. Acervus contains 24B BERT WordPiece tokens, including over 760K samples from heavily damaged OCR transcriptions, repaired by a ByT5 model trained for Latin text repair. The second dataset, Corpus Trinum, contains a mixture of over 100M strong and weak Latin language semantic triplets. Corpus Trinum is the first Latin semantic triplet dataset, opening the door for Latin language models to be adapted to general sentence semantic similarity tasks. We construct an experimental grid using five tasks and seventeen subtasks, applying a variety of finetuning configurations and subword aggregation techniques for 15 pretrained encoders, 6 LAMB training checkpoints, and an ablation model designed to quantify the impact of different masking regimens. Using this benchmark, we rank Latin encoders and find that LAMB outperforms all other evaluated models on 16 of 17 subtasks, coming within 0.8 percentage points of state of the art on the seventeenth. We provide additional analyses relating Latin encoder performance to tokenizer behavior, syntactic structure, finetuning configuration, pretraining state, subword aggregation, and variation in source texts and domains. In these, we identify unique acquisition dynamics for Latin open class words during terminal decay phases, and establish that for some task categories, finetuning configuration selection can have a greater effect on downstream scores than additional pretraining tokens.

---


### 11. [When and How Does Muon Precondition? The Role of Structured Gradient Noise](https://arxiv.org/abs/2610.31728)

**<font color=#1a73e8>作者：</font>** Xiaoran Chen, Binghui Li, Liwei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has become a popular optimizer for large language model training, yet its theoretical foundations remain poorly understood. In this work, we study how gradient noise geometry shapes Muon's preconditioning benefits. We first show, theoretically and empirically, that under the classical isotropic noise assumption, Muon offers no acceleration beyond a rescaling of the learning rate. This motivates us to investigate structured noise arising from mini-batch sampling in associative memory with heterogeneous task frequencies. We establish an exact balancing threshold for two tasks and extend the analysis to multiple tasks, revealing how task coverage and gradient reliability jointly shape learning. Our analysis shows that Muon can soften the dependence on task frequency from linear to square-root, helping balance the learning of frequent and rare tasks. We further identify rotation-induced negative transfer in SignSGD that Muon avoids, and explain how momentum reduces sampling noise while tracking changing gradients. Controlled numerical experiments validate these mechanisms, and a preliminary LLM pretraining study illustrates the practical promise of fast-slow momentum.

---


### 12. [Learning to Be Monitored: Causal Bounds and Intervention-Aware Post-Training Recipes for Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.31733)

**<font color=#1a73e8>作者：</font>** Qiang Fu, Xinyue Li, Andre Wibisono 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring aims to detect potentially harmful behaviors in large language models (LLMs) from their CoTs. Intervention-based evaluations measure this property by asking whether a monitor can detect the role of an intervention from the CoT when the targeted behavior occurs, typically using minimal-criterion sensitivity ($\mathsf{TPR_{mc}}$) proposed by~\citep{guan2025monitoring}. However, a target behavior observed under intervention is not necessarily caused by it, and we show that this metric can overestimate how often a monitor detects target behaviors actually caused by the intervention. Specifically, we establish $\mathsf{TPR_{mc}}$ as an upper bound on this causal detection rate and derive a complementary lower bound, which provides a tighter evaluation framework for CoT monitorability. With this framework, we study whether LLMs can be trained to make their CoTs easier to monitor. We first construct a training dataset of paired control--intervention tasks spanning multiple intervention types. Using the dataset, we design and apply three intervention-specific training methods based on off-policy self-distillation, reinforcement learning, and on-policy self-distillation to train separate variants of each base model. Across various model-monitor configurations, all three methods generally improve CoT monitorability over the corresponding base models under our extended evaluation framework. Our code is available at this https URL.

---


### 13. [DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model](https://arxiv.org/abs/2610.31734)

**<font color=#1a73e8>作者：</font>** Zixian Gao, Lixin Xiu, Penghao Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A live esports broadcast needs a director who chooses which camera goes on air and a caster who talks over that choice, every second and without knowing what comes next. Streaming video language models have learned to commentate, but only over a broadcast that a human director has already produced. We study live broadcast production, in which a model receives the raw camera of every player and must both direct and commentate from the past alone. We present DirCast, a single streaming video language model that does both. Every second it scans all cameras at low resolution, decides with a hold-or-switch director whether and where to cut, and reads the chosen camera at high resolution before it speaks. Its context keeps what went on air and what was said and lets the other views expire, which bounds the cost of a stream of any length. We build a dataset of 27 professional Dota 2 matches with a camera for every hero, the human director's choices and the casters' commentary. DirCast directs better than rule-based and zero-shot directors including GPT-5, and its commentary wins 29.2 percent of comparisons against GPT-4o under the Proact-VL protocol, against 19.4 percent for the strongest of eleven streaming commentators that watch the human broadcast.

---


### 14. [Not Every Agent Needs the Strongest Model: Unified Prompt-Model Optimization for Heterogeneous LLM-based Multi-Agent Systems](https://arxiv.org/abs/2610.31743)

**<font color=#1a73e8>作者：</font>** Mingxiu Cai, Haoyang Xian, Xinyu Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) rely on role-specific prompts and execution models to solve complex tasks collaboratively. However, prompt optimization typically keeps model assignments fixed, leaving differences in role requirements and their associated inference costs outside the search. We present UniMASO, a Unified framework for heterogeneous Multi-Agent System Optimization through the joint adaptation of prompts and model assignments. UniMASO evaluates candidate updates through local, downstream, and global feedback, using cost-aware Pareto search to retain useful quality-cost trade-offs. Topology-aware co-evolution then coordinates these updates according to agent roles and dependencies. Cross-level trajectory memory further supplies historical successes and failures to guide subsequent optimization. Experiments on five benchmarks and five execution topologies show that UniMASO achieves competitive task performance at substantially lower deployment cost than the strongest homogeneous configurations. Under centralized execution, it improves the average score from 69.79 to 70.40 while reducing token-weighted deployment cost by 85.2% relative to DeepSeek-V4-Pro with MASPO. These results support joint prompt-model adaptation as an effective approach to efficient multi-agent collaboration. The code is available at this https URL.

---


### 15. [Efficient Omni-modal Large Language Model Inference via Per-Query Modality Selection](https://arxiv.org/abs/2610.31768)

**<font color=#1a73e8>作者：</font>** Shuqi Liu, Yuzhou Cao, Luke Ong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (Omni-LLMs) can jointly process a broad range of modalities, such as text, audio, and video, enabling stronger multimodal understanding and reasoning capabilities, but often at substantial inference cost. We observe that the benefit of additional modalities varies across queries, indicating that a fixed modality configuration can be inefficient. Motivated by this, we study query-wise modality selection, which keeps the underlying Omni-LLM fixed while adaptively selecting which modalities to provide for each query. We formulate the problem as an accuracy-cost optimization problem and develop a cost-sensitive learning approach for modality selection. We evaluate our approach on WorldSense using Qwen2.5-Omni and Qwen3-Omni under three inference-cost measures: input tokens, latency, and monetary cost. Across both models, query-wise modality selection consistently improves the accuracy-cost trade-off and can even outperform the standard setting in which all available modalities are provided to the Omni-LLM. For Qwen2.5-Omni, our cost-sensitive approach matches or exceeds this full-modality accuracy while requiring only approximately 41% of the input tokens, 39% of the latency, and 61% of the monetary cost.

---


### 16. [Benchmarks Are Surprisingly Compaction-Friendly](https://arxiv.org/abs/2610.31778)

**<font color=#1a73e8>作者：</font>** Jeanne Salle, Hardik Bhatnagar, Matthias Bethge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long horizon agentic tasks are now pushing LLM agents past their context window. To continue the task, the agent scaffold has to free up the context window, a process known as context compaction. Compaction is generally lossy by design: agents can silently lose task constraints, instructions, or their reasoning behind earlier decisions. Although compaction is a standard component of coding agent scaffolds, it has not been studied systematically with frontier models on realistic, long horizon agentic tasks. Previous work evaluate smaller open weight models on toy or synthetic trajectories. We fix the agent scaffold (OpenCode), implement five compaction strategies inside it, and evaluate three frontier models on three long horizon benchmarks (PaperBench, ProgramBench, PostTrainBench). For the two 1M context models, the compaction threshold does not measurably affect the task performance, whereas GPT-5.3-Codex, the model with the smallest context window, performs worse at lower thresholds on PaperBench and, less clearly, on PostTrainBench. No compaction method outperforms default self-summarization, and methods that discard more content cost some models up to 20 points while leaving other models the same. Compaction can, however, silently remove task constraints: on ProgramBench, the first compaction summary already drops about one third of the task's anticheating rules on average, and this rises monotonically with the number of compactions. On real user-agent sessions from SWE-chat, instructions about how the agent should work and what it should not do are dropped around 6 times more than specifications of what to build. We argue that current benchmarks are compaction-friendly: i.e., the objective is fixed and the agent's progress stays on disk, so most of what compaction discards can be recovered, except constraints that don't exist anywhere else.

---


### 17. [Phronix: The Capability-Centric Learning Paradigm for Agents](https://arxiv.org/abs/2610.31789)

**<font color=#1a73e8>作者：</font>** Hariharan Devarajan, Neeraj Rajesh, Aniruddha Marathe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific computing increasingly relies on large language model-based agents for performance engineering tasks such as instrumentation, analysis, and workflow porting. However, agent effectiveness depends heavily on the surrounding harness, which typically relies on manually written skills and curated memory. This limits autonomous learning, forcing agents to repeatedly rediscover solutions rather than retain and reuse knowledge from prior executions. We introduce Phronix, a capability-centric learning paradigm that enables agentic harnesses to acquire, validate, and refine reusable capabilities from their own executions. Phronix operates through a predictor-validator-corrector loop: MCP tools and associated skills propose solutions, tool executions validate them, and observed outcomes refine the stored capabilities. It distills every observed interaction into a capability store and researches a failing task rather than abandoning it. First, such learned capabilities solve a recurring task on the first attempt in 93-95% of cases across every model, significantly reducing solution non-determinism and improving reliability. Second, Phronix turns an agent's own execution into 7.6-30.8 durable capabilities per task without user instruction, and creation falls below two once the needed capability exists. Third, warm-start runs consume only 0.38-0.40 million tokens per task, which is three to four times less than a single baseline attempt, while a cold-start costs no more than the baseline. On the 1000 Genome Pegasus workflow, instrumenting a production application for I/O performance analysis, Phronix passes all 11 correctness checks against six for the baseline harness, and also lifts the task solving rates of two cheaper models from 29% and 27% of SWE-bench tasks solved to 91% and 87%, respectively, matching the performance of the most expensive evaluated model.

---


### 18. [CuraLoc: Repository-Level Fault Localization via Planned Code Inspection](https://arxiv.org/abs/2610.31809)

**<font color=#1a73e8>作者：</font>** Sangeeta Warrier, Anush Sankaran, Ryen White  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A bug report describes what went wrong, but rarely where the code should change. Existing repository-level localization methods often let language models iteratively decide what code to inspect next, requiring repeated model calls and substantial token usage. We investigate whether these inspection decisions can instead be planned before source retrieval. In this research, we introduce CuraLoc, which first selects candidate files and represents their symbols using compact behavioral and structural descriptions. In a single planning decision, the model jointly selects starting symbols, chooses code relationships to inspect from each, and forms hypotheses about likely edits. Deterministic retrieval collects the requested source for a final ranking informed by those hypotheses, concentrating model reasoning on choosing and comparing code rather than directing each retrieval step. We demonstrate the efficacy of our proposed approach on the SWE-Bench Lite and Verified datasets. On SWE Bench Verified with GPT-5.2, CuraLoc raises Func@1 from LocAgent's 53.8% to 59.3% while using 90.3% fewer recorded tokens, and also outperforms RepoSearcher (56.2%) and Agentless (39.6%) on Func@1. On SWE-bench Lite, CuraLoc achieves a high 83.8% Func@5 accuracy improving on Agentless by more than 15% in relative accuracy. Additionally, CuraLoc supports different model backbones, with strong localization accuracy demonstrated using both GPT-5.2 and GPT-6 Astra. These results provide evidence that repository-level code inspection can be planned effectively without iterative model-controlled navigation.

---


### 19. [PaperFormalizer: Author-in-the-Loop Autoformalization of Research Papers in Lean](https://arxiv.org/abs/2610.31810)

**<font color=#1a73e8>作者：</font>** Jiyuan Tan, Vasilis Syrgkanis, Jose Blanchet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Even a carefully proofread paper can leave small gaps in its proofs or its stated assumptions. We introduce PaperFormalizer, a Lean-based agentic pipeline that helps authors find and close such gaps in their own papers and turn each paper into a Lean-verified version. Starting from the LaTeX source, PaperFormalizer transcribes the paper into a dependency graph of statements, audits each statement in natural language for faithfulness, ambiguity and correctness, and then formalizes and proves the statements in Lean against Mathlib, optional domain libraries and the author's personal toolkit. Only the author knows what a statement is meant to say and how a formalization gap in a result is best fixed. The pipeline therefore stops and asks the author whenever a statement admits more than one reading, presents every repair, in natural language and TeX symbols, as a proposal that the author can accept, decline or redirect, and leaves to the author every decision that could potentially change what the paper claims. The output is an annotated and revised version of the paper, a report of the changes, and Lean code in which each declaration is linked to the statement it formalizes. The author's toolkit grows as more papers are formalized, and authors can share their verified papers so that researchers who build on them can reuse their Lean code. By making verified papers practical to produce, PaperFormalizer aims to make research that rests on mathematical proofs more robust. PaperFormalizer runs inside a coding agent (Claude Code or Codex) and is available at this https URL. Papers with Lean code shared by users are available at this https URL.

---


### 20. [Nested Sparsity for Scalable Pretraining and Continual Learning](https://arxiv.org/abs/2610.31818)

**<font color=#1a73e8>作者：</font>** Tianzhe Chu, Druv Pai, Yi Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) transformers, the standard backbone for modern large-scale deep learning, employ conditional computation: only a sparse subset of model weights is used in each forward pass. In MoE transformers, this sparsity arises in the MoE operator, which generalizes the multi-layer perceptron in the classical transformer. In this work, we explore an alternative mechanism for conditional computation that analogously generalizes the attention operator. The sparsity induced by this mechanism naturally nests (i.e., hierarchically composes) with the sparsity induced by the MoE operator. We show that a transformer employing this nested sparsity mechanism, which we call Nestor, performs better than a conventional MoE transformer at equal compute and equal sparsity in language model pretraining. We also show that Nestor is well-suited for continual pretraining: it can be adapted to longer contexts more effectively than conventional MoEs, as well as adapt more efficiently to new domains while forgetting less on old domains. Furthermore, we demonstrate that these benefits persist as model size, dataset size, and context length grow. Our results demonstrate the potential of alternative conditional computation mechanisms for deep neural network architectures. Code and checkpoints are available on GitHub at this https URL .

---


### 21. [Speculative Diffusion is a Tale of Two Tradeoffs](https://arxiv.org/abs/2610.31819)

**<font color=#1a73e8>作者：</font>** Aaron Zorel, Guy Van den Broeck, Aditya Grover 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding is a technique that accelerates the inference speed of autoregressive large language models (LLMs) by sampling from a faster, lower quality draft model. Traditionally, a fundamental characteristic of speculative decoding is that it is lossless with respect to the verifier distribution, guaranteeing speed without sacrificing quality. This differs from recently developed diffusion LLMs (dLLMs), which are notably able to achieve substantial speedups by degrading the quality of their outputs with less diffusion effort. Because diffusion models are able to sample faster than autoregressive models by generating tokens in parallel, they are considered strong candidates for draft models in speculative diffusion. While it is widely understood that diffusion models can sacrifice quality for speed, speculative decoding itself can also be generalized to generate lossy samples faster using more lenient acceptance criteria with respect to the verifier distribution. Presented with the two parameters of diffusion effort and speculative decoding leniency, this paper explores the full achievable Pareto frontier via joint variations of these parameters. Our experiments show that jointly varying diffusion effort and acceptance leniency can extend the speed-quality Pareto frontier over single step diffusion drafting.

---


### 22. [Free Lunch for LLMs Confidence: The RL Critic Already Knows](https://arxiv.org/abs/2610.31820)

**<font color=#1a73e8>作者：</font>** Shujin Wu, Heng Ji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable confidence estimation is essential for trustworthy deployment of large language models (LLMs), but dedicated confidence training stage requires additional data and compute. We ask a fundamental question: what prediction problem does confidence training actually solve? Inspired by prior work on external confidence estimation, we compare self- and external estimators of comparable capacity trained on the same (question, response, correctness) triples. We show that an external model trained solely on a policy's behavioral traces can estimate the policy's confidence as accurately as the policy itself, without accessing the policy's internal representations. This points to a deeper connection with value function learning in reinforcement learning (RL): under a correctness-based outcome, we prove that confidence estimation and critic training are equivalent, both predicting the likelihood that a policy's response will be correct from its trajectory. A simple consequence follows: for LLMs trained with value-based RL, the existing critic can be reused as an off-the-shelf confidence estimator with no additional training or data. The policy remains unchanged, so its task performance is preserved, and the critic provides confidence throughout generation, including intermediate reasoning steps. Across math, code, tool calling, and general reasoning spanning a dozen domains, the reused critic is the best confidence estimator on every in-distribution split and the best-calibrated on 14 of 16, without hurting the task performance.

---


### 23. [Ulysses: A Security Harness For Synthesizing Verifiable Web Exploits](https://arxiv.org/abs/2610.31831)

**<font color=#1a73e8>作者：</font>** Aditya Oke, André Vicente Duarte, Rui Melo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> How can an AI agent automatically discover security vulnerabilities in any software repository? Existing approaches use LLMs to generate software vulnerability exploits. However, it is challenging for an LLM to reliably verify its own generated exploits. In this paper, we propose Ulysses, a multi-agent security harness to synthesize verifiable vulnerability exploits for web applications. Ulysses converts candidate vulnerability findings into verified Proofs of Exploitability by iteratively exploring exploit hypotheses and establishing success in independently observed execution effects. We evaluated Ulysses on WebExploitGym, a curated benchmark of exploitable instances from 25 real-world web applications that span 5 languages and 7 frameworks. Ulysses produces verified proofs for 10 of 25 real-world advisories. It also discovered 4 new proofs of exploitability that have never been previously reported.

---


### 24. [Latent Coherence: Do Frontier Language Models' Probability Judgments Obey the Law of Total Probability?](https://arxiv.org/abs/2610.31833)

**<font color=#1a73e8>作者：</font>** Peter Potash  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LawZero's Scientist AI trains a Predictor toward the Bayesian posterior, with an objective that penalizes inconsistent probabilities among latent explanations. We ask whether current frontier language models, with no such training, are already consistent in this sense zero-shot: do their probability judgments satisfy the law of total probability, $P(X)=\sum_z P(z)P(X|z)$, when the latent $z$ must be inferred from records in the context? In separate single-turn calls, models are asked for $P(X)$, for $P(z)$ over the latent's states, and for $P(X|z)$; a causal family applies the same test to $P(y|do(x))$ and the back-door adjustment. Every query has an exact ground-truth probability, and a subset of items is asked in three wordings to separate persistent incoherence from rewording noise. Across seven models, GPT-6.1 Sol and Claude Opus 5.5 are the most coherent (mean absolute residual 0.08 and 0.12 log-odds, about 2 percentage points). Claude Haiku 5.5, Gemini 3.8 Flash and DeepSeek V4-Pro show persistent incoherence (0.27-0.35 log-odds) that is mostly item-specific rather than a shared offset. Within every model, larger residuals go with larger errors against the truth (Spearman 0.40-0.62), so the residual, which needs no ground truth, flags unreliable answers. Reasoning length does not predict coherence, across models or within a model across rewordings of the same question. Simple consistency checks pass almost everywhere; the failures are specific to reasoning through a latent variable. Code and data: this https URL

---


### 25. [SAGE: A hybrid vision-language and geometry framework for work-zone pathway prediction under temporary traffic control](https://arxiv.org/abs/2610.31835)

**<font color=#1a73e8>作者：</font>** Jiaxi Liu, Keshu Wu, Weizhe Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporary traffic control redirects vehicles through work zones, requiring automated vehicles to connect an interpretation of the visible devices to a continuous passing path. Geometric predictors can provide several plausible paths, yet selecting the one consistent with the temporary control remains difficult. We propose SAGE (Semantic-to-Action Grounded Execution), a read-decide-execute-check framework that separates path construction, path preference, and control compliance within a shared candidate space. The central idea is to use a vision-language model's (VLM's) trajectory as a preference over intact geometric candidates. A role-decoupled generator constructs the candidates, and rank fusion combines each candidate's geometric score with its agreement with the VLM trajectory. Supervision structured around the Manual on Uniform Traffic Control Devices (MUTCD) trains SAGE-VLM to state the lane status and hazard side before its passage decision and trajectory. The predicted hazard side enters image-space predicates derived from MUTCD provisions, which support a final intervention bounded in score and displacement. On 2,306 real-world ROADWork validation episodes, the candidates include a path within 10 px of the human demonstration in 87% of episodes, yet selection regret accounts for 53% of the geometric ranker's error. SAGE reduces average and final displacement errors by 8.3% and 12.0% relative to the ranker, mostly in the far field, and hard-constraint violations by 37%. The trajectory opinion improves all four tested generator-selector combinations. SAGE is comparable to state-of-the-art VLM modules in accuracy, with a faster-responding VLM, and outperforms four other adapted driving VLMs in displacement error and safety measures. Project page: this https URL.

---


### 26. [SAGE: Sense-Aligned Multimodal Grounding Evaluation with Gloss-Augmented Reasoning](https://arxiv.org/abs/2610.31838)

**<font color=#1a73e8>作者：</font>** Sunjae Kwon, Suhaas Kiran DG, Zonghai Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces Sense-Aligned Grounding Evaluation (SAGE), a unified 10-candidate image-selection benchmark that reformulates VWSD, VerSe, and WikiDiverse into a shared term-centric protocol covering noun-, verb-, and entity-centered grounding. SAGE includes confusable hard negatives and a context-swapped VerSe diagnostic to probe target-term grounding beyond direct caption--image compatibility. We further propose Gloss-Augmented Reasoning (GAR), a training-free framework combining definition grounding with constraint-guided semantic verification. Experiments show that strong VWSD performance does not transfer uniformly across grounding settings. With Gemma3-12B, definition augmentation improves all three subsets, while constraint-guided reasoning improves VWSD and yields particularly strong gains on VerSe, but is less effective on WikiDiverse. Combining the two signals achieves the best macro-average performance, improving Hits@1 from 65.90 to 71.22. These results show that SAGE supports both unified evaluation and fine-grained analysis of explicit semantic reasoning across grounding settings.

---


### 27. [Scaling cross-situational word learning on children's naturalistic experiences](https://arxiv.org/abs/2610.31842)

**<font color=#1a73e8>作者：</font>** Michael C. Frank, Alvin W. M. Tan, Khai Loong Aw 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do children learn the meanings of the simple, concrete words that form a majority of their early vocabulary? Statistical information about many word meanings can be recovered from the gradual accumulation of information about the co-occurrence of words with their referents, a proposal known as ``cross-situational learning''. Contrastive vision--language models allow this learning strategy to be tested on egocentric video data capturing children's early real-life experiences with visual and linguistic inputs. Initial successes of this method on small datasets provide a proof-of-concept, but vision models struggle to learn robust visual representations when trained on these same egocentric videos. How dependent is cross-situational word learning performance on the quality of the model's visual representations? And can cross-situational models scale to larger and more diverse datasets? To address these questions, we trained models on the BabyView corpus, including 2,441 hours of longitudinal egocentric video from 48 children. Models trained on this dataset learned object--label mappings, but performance was far higher when they used internet-pretrained visual representations as opposed to when visual representations were learned solely from the developmental video data. Further, the majority of the learning signal was carried by a small proportion of utterances that described a visible referent. Models learned lexical representations that showed recognizable human-like semantic structure, but model performance showed substantially different trajectories over training experiences than those observed in children. Cross-situational learning is a viable word learning strategy for early noun vocabulary, but constructing developmentally plausible models will require understanding how to learn high-quality visual representations from naturalistic data.

---


### 28. [SEMPRE: Semantic-Aware Protocol Reverse Engineering via Consistency-Driven Joint Optimization](https://arxiv.org/abs/2610.31844)

**<font color=#1a73e8>作者：</font>** Yihua Xu, Weijie Huang, Xiaofeng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Protocol reverse engineering (PRE) is essential for understanding undocumented or proprietary communication formats, enabling security-critical tasks such as vulnerability discovery, malware C2 analysis, and IDS signature generation. However, existing PRE techniques rely on brittle hand-written rules, under-model contextual dependencies among neighboring fields, and often fail on messages with nested sub-protocols. We present SEMPRE, a fully automated PRE framework that replaces ad-hoc heuristics with recursive LLM reasoning grounded in fine-grained dynamic program analysis. SEMPRE uses taint-flow and loop traces to guide an LLM-driven tree-of-thought search that slices messages into fields while detecting nested sub-payloads, producing a hierarchical layout. It then infers each field's type and role and iteratively refines boundaries by freezing high-confidence segments and re-running detection under semantic constraints, yielding an EM-style procedure that monotonically improves structure and semantics until convergence. Evaluated on a broad corpus of mainstream protocols against six state-of-the-art (vs. <0.4 for all baselines) and 0.72 for semantic inference (vs. 0.13 for BinPRE). Ablations confirm the contribution of each component, and a case study on a prolific real-world botnet demonstrates practical utility.

---


### 29. [Don't Forget What You Just Learned: Self-Directed Repair Turns Agent Mistakes Into Lasting Lessons](https://arxiv.org/abs/2610.31846)

**<font color=#1a73e8>作者：</font>** Yuval Kansal, Karen Ullrich, Polina Kirichenko 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intelligent agents should learn from their mistakes so that experience leads to continuous improvement. Yet today's agents recover from a mistake only temporarily: in-context reflections are easily forgotten across sessions and compete for limited context, while full-parameter fine-tuning is expensive and can interfere with existing capabilities. We introduce Self-Direction, a mechanism for agents to learn from mistakes that combines the benefits of temporary in-context retries and policy updates. When an agent fails a task, it reflects on its own trajectory in order to extract a lesson and immediately distills it into a lightweight low-rank adapter. By keeping the original weights frozen, Self-Direction prevents adapter training from overwriting base-model parameters while training additional parameters equivalent to ~0.02% of the base model's parameter count for each adapter. The agent then saves these adapters in a persistent library of lessons, automatically routing them to solve related problems later. Experiments with agents based on open-weight models from the Qwen family across open-ended research (GAIA), tool-use workflows (Claw-Eval), and terminal tasks (Terminal-Bench 2.1) show that our method improves overall success rates by 8.9 to 17.0 percentage points and performs competitively with frontier systems. We find that Self-Direction reduces repeated mistakes across future encounters of a task, nearly doubling the reliability of an agent's corrections. Learned lessons also transfer: a handful of adapters generalize to dozens of new tasks without additional training. Ultimately, this self-directed repair transforms everyday mistakes into lasting lessons.

---


### 30. [Aligning Large Language Models with Human Feedback: Mathematical Foundations and Algorithm Design](https://arxiv.org/abs/2610.31862)

**<font color=#1a73e8>作者：</font>** Siliang Zeng, Luca Viano, Chenliang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article provides an introduction to the mathematical foundations and algorithmic frameworks used to align Large Language Models (LLMs) with human intentions, preferences, and values. We discuss standard alignment techniques, such as fine-tuning (SFT), reinforcement learning with human feedback (RLHF), and direct preference optimization (DPO). We also explore the theoretical underpinnings of learning from human preferences, drawing connections to inverse reinforcement learning (IRL) and discrete choice models. We present state-of-the-art algorithms in a tutorial style, discuss their advantages and limitations, and offer insights into practical implementation. Our exposition is intended to serve as a comprehensive resource for researchers and practitioners, providing both a foundational understanding of alignment methodologies and a framework for developing more robust and scalable alignment techniques.

---


### 31. [Machine-Readable Operator Manuals over the ISO 11783 Network for Offline, Multilingual LLM Assistance](https://arxiv.org/abs/2610.31863)

**<font color=#1a73e8>作者：</font>** Timo Oksanen, Julius Gun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> If agricultural machinery is to support intelligent, offline assistance, then the system must access technical documentation dynamically. In this paper, the Semantic Synchronization of operator manuals over ISO 11783-based CAN buses is analyzed, defined as the process that brings the local knowledge base of a tractor-side assistant into agreement with the operator manual of the connected implement. Data transfer performance was benchmarked using Markdown, JSON, and XML; various open-weight Large Language Models (LLMs) were also evaluated in cross-lingual query tasks. The automatic evaluation of the answers was validated against four human raters. A complete manual was transferred over a physical ISO 11783 network in 31 to 89 s, depending on format and transport settings, which is comparable to the object pool upload that operators already wait for at the first coupling of an implement. Markdown produced the smallest files, while the question-answering performance was comparable across the three formats for most models. With retrieval-augmented generation, locally run models answered most questions on the English manual correctly, with no advantage of the largest model over 7B and 8B models, but performed worse on the five other language editions. Keyword retrieval failed across languages, whereas semantic retrieval provided the cross-lingual capability. The exchange requires only a new parameter group that uses the existing request and transport mechanisms of ISO 11783, which makes it a candidate for standardization. The study is a proof of concept with inference on PC-grade hardware; deployment on embedded agricultural hardware remains future work.

---


### 32. [Rewriting Scaling Laws for Synthetic Data with Compute and Data Constraints](https://arxiv.org/abs/2610.31867)

**<font color=#1a73e8>作者：</font>** Nicholas Roberts, Ahmed Ahmed, Suhas Kotha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic rewrites, where a language model rewrites a natural document e.g. into a target style, are now a standard ingredient of pretraining corpora. However, critical aspects of their use remain poorly understood, such as how much compute should be spent rewriting training data and whether a model trained on rewrites can outperform the rewriter. We study these two questions by proposing a rewriting scaling law that predicts loss from model size, training tokens, the fraction of training tokens that are rewrites, and the number of epochs over the natural data, charging the compute spent generating rewrites. We fit this scaling law in two settings. In the compute-limited setting, natural data is plentiful and rewrites come from a third-party rewriter trained with more compute than our largest run. We find that the estimated optimal rewrite fraction increases with compute, from under $10\%$ at $3\times10^{18}$ FLOPs to $32\%$ at $10^{22}$ FLOPs. Our scaling forecast extrapolates $33\times$ in FLOPs to train a 22B-parameter model, whose final loss is within $1.1\%$ of our prediction. This model achieves a better BPB than its rewriter on several web domains at one-tenth the rewriter's training compute. In the data-limited setting, we assume we only have a fixed seed set of natural data and that our rewriter is a model of the same size as the target, pretrained on that seed set. Again, we find the optimal rewrite fraction increases with the compute budget. We also demonstrate that a model trained on rewrites of its own pretraining data, generated by a rewriter of the same size, beats the best run on natural data alone at every model size up to 3B. Our results show that synthetic rewriting can be studied through the scaling law lens: that optimal methodological choices are predictable and scaling does not necessarily break down beyond the rewriter's capabilities.

---


### 33. [FSVL: Taxonomic Fast-Slow Vision-to-Language Collaborative Framework for Interpretable Confusable Fish Species Identification and Knowledge Generation in the Middle Yangtze River](https://arxiv.org/abs/2610.31880)

**<font color=#1a73e8>作者：</font>** Meng Liang, Fucheng Wang, Lang Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Yangtze River Basin is a critical region for freshwater biodiversity conservation. The implementation of the Yangtze River Ten-Year Fishing Ban has increased the importance of effective aquatic biodiversity monitoring and species-level identification. However, fine-grained identification of closely related freshwater fish species remains challenging due to subtle morphological differences. Existing deep learning methods often struggle to balance classification accuracy and inference efficiency, while LLMs may generate unsupported information when producing specialized biological knowledge. To address these challenges, this study proposes FSVL, a fast-slow dual-pathway framework integrating visual recognition with LLM-based Retrieval-Augmented Generation (RAG). A lightweight ResNet50 fast path performs preliminary classification across 51 fish species in the Middle Yangtze River Basin and routes predefined groups of easily confused species to a slow path for refined identification. Guided by taxonomic criteria, the slow path uses YOLOv8n to detect key morphological regions, including the head, dorsal fin, and tail, leveraging morphometric and outline traits to improve discrimination among closely related species. The framework further integrates a retrieval-enhanced Qwen3-14B backend, using soft tokens and Low-Rank Adaptation (LoRA) for parameter-efficient domain knowledge generation. On the evaluated test set of 607 images, the fast classifier achieved 99.67% accuracy, whereas the cascade corrected the two errors, yielding 100.00% overall accuracy; further validation on independent specimens and external conditions remains needed. Across 255 knowledge generation samples, scientific name accuracy rises from 91.37% to 100.00%, genus accuracy from 90.20% to 98.82%, and ROUGE-L from 0.335 to 0.655, supporting intelligent biodiversity monitoring and fisheries management.

---


### 34. [TACS-RF: Tool-driven Agentic Circuit Synthesis of RF and mmWave Modules](https://arxiv.org/abs/2610.31882)

**<font color=#1a73e8>作者：</font>** Tristan Liang, Aravind Nagulu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present the framework of TACS-RF - a Tool-driven Agentic Circuit Synthesis of RF and mmWave modules. In this framework, a large-language-model (LLM) coding agent (Claude Opus 4.8) directly drives industry-standard electronic-design-automation (EDA) tools such as Cadence Virtuoso/Spectre, Calibre, Cadence EMX, and Ansys HFSS to design RF and mmWave modules. We validate the framework through the agentic design of a 240-251 GHz sub-THz transmitter in a 90 nm SiGe BiCMOS process. The agent semi-autonomously designed the sub-blocks including a 60 GHz push-push Colpitts VCO with second-harmonic extraction, multistage differential cascode power drivers, a push-push frequency doubler, a differential bowtie antenna, and all the interstage matching networks. The transmitter chain with parasitic-extracted devices and EM-verified passives delivers +5.1 to +6.3 dBm across an 11 GHz varactor-only tuning range, phase noise of -80 to -88 dBc/Hz at 1 MHz offset while consuming a DC power of 361 mW. We describe the agent-driven design flow and the resulting division of labor between human and agent, taking a step toward a "text-to-ASIC" future for designing RF/mmWave hardware.

---


### 35. [TaxoSAE: Rethinking Sparse Autoencoders through Taxonomic Logic](https://arxiv.org/abs/2610.31894)

**<font color=#1a73e8>作者：</font>** Xinyu Guo, Minglai Yang, Clayton T. Morrison 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent Sparse Autoencoders (SAEs) decompose the representations of large language models (LLMs) into interpretable features, enabling precise readout and control of encoded knowledge. However, existing SAEs treat each feature as a standalone unit, whereas real-world knowledge is often taxonomically organized. As a result, readout carries no guarantee of taxonomic consistency, and control lacks the granularity to specify the scope of an edit. We propose TaxoSAE, which explicitly encodes taxonomical information, built on is-a (hypernym-hyponym) relations, into the SAE feature space. TaxoSAE mirrors a taxonomy with a stack of SAEs, one per taxonomy level, and introduces a taxonomic alignment loss that trains each concept to be active whenever one of its hyponyms is. On two factual QA taxonomies, one over biographical relations and one over animals, TaxoSAE enables (1) more accurate readout through the taxonomy with concentrated activations, e.g., +31.3 points in reading out the hypernyms of abstract concepts never queried in training; (2) more precise control, with +25.5 points in swap success, while suppressing a concept removes only its own answers (0-2% accuracy vs. 91-100% on other concepts); and, more importantly, (3) readout of unseen concepts through their hypernyms, with up to +37.9 points in hypernym readout accuracy.

---


### 36. [Learning Structured Sparsity for Large Models: Bridging Model Compressibility and Efficient Inference](https://arxiv.org/abs/2610.31897)

**<font color=#1a73e8>作者：</font>** Tianxiang Xia, Kai Lion, Niao He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws continue to reward increases in model scale, while the resulting computational and memory demands drive greater reliance on cloud infrastructure for inference. Yet unreliable network connectivity, communication delays, and privacy requirements can make such reliance impractical, motivating local execution on edge devices. Local deployment requires models to fit within limited memory and execute efficiently with the available computational resources. Recent work has shown that learning sparse-plus-low-rank representations enables elastic compression of a single checkpoint to multiple memory budgets. However, fewer parameters do not necessarily translate into faster inference. Indexing overhead and irregular memory access in unstructured sparse components can offset computational savings. To address this critical deployment barrier, we introduce S-SALAAD, a unified framework that jointly learns the model weights and their low-rank and structured sparse components during training. The framework supports a family of hardware-compatible structured sparsity patterns. It couples this structure learning with budget-aware compression and dedicated CPU and GPU kernels that exploit the learned structure for acceleration, enabling efficient inference from a single checkpoint across memory budgets. Experiments on Llama2 and Qwen3 models, covering both pretraining and distillation, show that S-SALAAD advances the empirical Pareto frontier in perplexity, memory, and inference latency across multiple hardware platforms relative to the evaluated baselines. These results show that structured learning can translate elastic compressibility into reduced memory requirements and lower inference latency, enabling practical deployment of large models on edge devices.

---


### 37. [StateBridge: Phase- and Track-Grounded Reasoning for Synthetic-to-Real Traffic Video Captioning and VQA](https://arxiv.org/abs/2610.31898)

**<font color=#1a73e8>作者：</font>** Blessing Agyei Kyem, Richard Dzinyela, Joshua Kofi Asamoah 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic safety videos provide rich evidence for understanding interactions between pedestrians and vehicles, but synthetic-to-real evaluation makes this setting challenging because models must learn from simulated scenes and generalize to real-world traffic. In this work, we present StateBridge, a traffic video-language framework designed to operate under this synthetic-only training protocol. Our approach uses phase-aware clip construction, pedestrian and vehicle track summaries, and structured prompts to ground vision-language models in stable traffic evidence rather than appearance alone. We fine-tune public vision-language models on synthetic captioning and visual question answering examples, then combine their outputs through fact-locked caption fusion and evidence-diverse VQA consensus to improve consistency across actor roles, behavioral phases, and question types. StateBridge achieves an official S2 score of 55.4679 on AI City Challenge 2026 Track 2 using only synthetic training data. These results demonstrate the effectiveness of structured evidence transfer for traffic safety captioning and visual question answering.

---


### 38. [LazyFlash: Forward-Dense, Backward-Sparse Attention for Accelerated Long-Context Fine-Tuning](https://arxiv.org/abs/2610.31911)

**<font color=#1a73e8>作者：</font>** Keqi Deng, Ruchao Fan, Jinyu Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) process increasingly long sequences, attention becomes a major computational bottleneck. Sparse attention mostly targets inference, yet many methods still train densely or cannot support sparse training, and their added complexity makes sparsity hard to turn into wall-clock speedups, leaving dense attention widely used in practice. This paper introduces LazyFlash, a forward-dense, backward-sparse attention method built on the observation that attention training is dominated by the backward pass. LazyFlash keeps the forward pass exactly dense, so the trained model remains a standard dense model that existing systems such as vLLM can serve without any change. For the backward pass, LazyFlash proposes a gradient-aware block sparsification design that ranks query blocks by their attention-output gradient norms and skips those contributing negligibly to parameter updates, turning the dense backward into a block-sparse one. A gradient-mass budget adapts the amount of skipped computation to each head and training step, while importance sampling preserves the dense gradient in expectation. These designs are implemented inside the tiled FlashAttention backward kernel, where skipped blocks are never loaded or computed, translating gradient sparsity into real wall-clock acceleration. Experiments on long-context text and speech LLMs show that LazyFlash maintains downstream performance while achieving up to 5.7x attention-backward speedup over FlashAttention and 1.7x end-to-end training speedup.

---


### 39. [Permission to Retry: A Study of Authorization and Recovery in AI Agent Workflows](https://arxiv.org/abs/2610.31916)

**<font color=#1a73e8>作者：</font>** Deekshith Marla, Kushagra Bhatnagar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A durable agent can resume a consequential action while its authority changes and the action's external outcome remains uncertain. We study execution-time reliability of tool-using AI agents, isolating recovery decisions from language-model behavior. Checkpoint state, permission to dispatch, evidence of an external effect and permission to reconcile are distinct obligations. We present a finite conformance study that checks these obligations through histories scored against a provider effect ledger hidden from the recovering application. A prospectively frozen campaign executes 336 histories on native LangGraph and Temporal hosts, crossing 14 schedules, three provider contracts and four matched application policies. All 168 paired host cells have identical checked outcomes. Per host, retained-ledger reconciliation passes all 42 histories: 21 checked completions, 15 denials and six unknown outcomes with reservations retained. Cached retry, revalidation before retry and stable-key retry pass 30, 36 and 31 histories respectively. A separate 16-case component study of InfinityOS, an enterprise AI platform developed by this http URL, exercises exported authority, worker, recovery and settlement code over repository fakes. The results isolate the roles of current authority, provider contracts and retained observations in recovery, with safety, completion and unresolved obligations reported separately for the declared application profile.

---


### 40. [Beyond On-Policy vs. Off-Policy: At What Level Should LLM Agent Distillation Follow the Student?](https://arxiv.org/abs/2610.31918)

**<font color=#1a73e8>作者：</font>** Ya Gao, Zhengtao Zou, Pekka Marttinen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distilling interactive LLM agents requires choosing between teacher-generated demonstrations and student-generated experience, corresponding broadly to off-policy and on-policy distillation. While both have proven effective, we argue that this distinction is inherently hierarchical: the policy that induces an interaction history need not be the same as the policy that generates the token prefix of the current action. We introduce a hierarchical agent distillation framework that formalizes these two levels of on-policiness and enables explicit control over their pairing, mixture proportions, and training schedule. We study this problem through self-distillation, where a frozen teacher has access to task guidance unavailable to the student, and conduct a three-stage controlled study across three models and four interactive environments. We find that student-induced histories paired with teacher-generated action prefixes generally provide the strongest standalone training signal, whereas following the student at both levels generally performs worst. Nevertheless, fully on-policy data becomes beneficial when incorporated into a mixture with other configurations. Moreover, mixtures with identical teacher/student proportions at each level can yield substantially different performance, showing that how the two levels are paired matters beyond the overall amount of on-policy data. Finally, front-loading fully teacher-generated contexts and delaying fully on-policy contexts improves over a static mixture. These findings provide practical principles for deciding where, how much, and when agent distillation should follow the student.

---


### 41. [Synthetic-to-Real Text-Based Person Anomaly Search via Multi-Model Retrieval Fusion and Cross-Encoder Reranking](https://arxiv.org/abs/2610.31930)

**<font color=#1a73e8>作者：</font>** Eugene Denteh, Blessing Agyei Kyem, Andrews Danyo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based person anomaly search requires a model to retrieve individuals from a large image gallery using natural-language descriptions of both appearance and behavior. This task is challenging because model training relies on synthetic image-text pairs, whereas evaluation is performed on real surveillance images containing domain differences, near-duplicate frames, and many visually similar distractors. We present a multi-model retrieval and reranking framework designed to improve synthetic-to-real transfer. The framework first adapts Qwen3-VL-Embedding-8B to synthetic person descriptions using bidirectional contrastive learning, explicit negative sampling, false-negative masking, and domain randomization. It then combines the normalized scores of six complementary Qwen3-VL checkpoints with those of a frozen SigLIP2 model using four-view gallery encoding. The fused retrieval scores identify the strongest candidates, which are jointly evaluated with the query using Qwen3-VL-Reranker-8B. The cross-encoder and retrieval scores are subsequently blended to produce the final ranking. We also construct a distractor-matched validation protocol entirely from synthetic data to select checkpoint weights, fusion coefficients, candidate depths, and reranking parameters without accessing the official test images. The final system achieves 94.7815% mAP and 90.8493% R@1 under the official AI City Challenge 2026 Track 4 test setting, with a reported eighth-place finish on the public leaderboard.

---


### 42. [Every Weight Is a Path of Shared Discrete Decisions](https://arxiv.org/abs/2610.31931)

**<font color=#1a73e8>作者：</font>** Ammar Ali, Stamatis Lefkimmiatis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TWIG (Tree-structured Weights with Inherited Gates), a representation in which every weight of a neural network is the end of a path of small discrete decisions: a sign, a shift by a power of two, a zero gate, an index into a shared table. Weights that belong together share the upper part of their paths, and each decision is inherited by every weight below it, so it is stored once and applied once. This simple change has three consequences. Any trained network can be written as a TWIG, and when the decisions are powers of two its weight layers become circuits made almost entirely of wires and adders, suited to chips whose weights are fixed at fabrication. Pruning, quantization, low-rank factorization, codebooks and weight sharing become edits of one object, so a single optimizer can choose among all of them for a whole network. And choosing the decisions is the ground-state problem of a higher-order Boltzmann machine whose interactions follow the paths of the tree, the problem class that annealers and quantum optimizers are built to solve. Today these questions are handled apart: each compression method brings its own format and solver, a circuit with fixed weights needs a dedicated constant multiplier for every weight, and discrete solvers reach only narrow subproblems such as rounding. Weight formats have long been moving toward shared decisions, through group scales, shared exponents, microexponents and sparse weights; TWIG takes this trend to its end, and every common format is a shallow TWIG at no extra cost. On five weight matrices of a large language model, a flat tree whose signed power-of-two terms are chosen per weight for circuit cost, with no group scales, needs 9--15\% fewer additions than GPTQ at equal layer error at 3- and 4-bit accuracy on typical matrices, and 20--55\% fewer on matrices with strong outliers.

---


### 43. [$M^3$: A Multi-LLM System for Multi-Turn Jailbreaking as a Markov Decision Process](https://arxiv.org/abs/2610.31937)

**<font color=#1a73e8>作者：</font>** Yuqing Huang, Jack Ji, Jithin Pradeep 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern Large Language Models (LLMs) remain vulnerable to carefully orchestrated multi-turn interactions that progressively bypass safety mechanisms. However, many existing red-teaming approaches rely on heuristics or impose strong assumptions that limit their applicability in fully black box settings. We address this gap by introducing $M^3$, an automated red-teaming framework that formalizes multi-turn jailbreaking as a finite-horizon Markov Decision Process (MDP). In $M^3$, an attacker LLM interacts with a target LLM while operating over a compact internal state produced by a state LLM. Across two benchmarks and six target models, $M^3$ consistently outperforms state-of-the-art multi-turn red-teaming methods in Attack Success Rates (ASR), achieving improvements of up to 53% in ASR@5. Even with lightweight attacker, $M^3$ attains gains up to 26% in ASR@1 and 34% in ASR@5, compared to baselines that use higher capacity attackers. Beyond improved effectiveness, $M^3$ exhibits steeper risk escalation over conversational turns and achieves more consistent performance across risk categories (up to 4.82 improvement in Gini index) without relying on predefined risk taxonomy, providing a scalable and principled framework for multi-turn red-teaming and safety evaluation.

---


### 44. [Agreement rather than normalisation keeps depth reusable in looped language models](https://arxiv.org/abs/2610.31943)

**<font color=#1a73e8>作者：</font>** Ivan Viakhirev, Kirill Borodin, Maxim Abramov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models apply one block of layers repeatedly, and the design pays off only if depth is reusable: loop steps beyond the trained budget must remain usable at inference. We ask whether that rests on normalising the state between loop steps, as the released Ouro models do, or on agreement between the loop a model is trained with and the loop it is run with. On released weights this loop-boundary normalisation can be removed without adding parameters and with the readout path bit-identical, and the operation is an identity at one loop step, which serves as an implementation check. Removing it takes Ouro-1.4B and Ouro-2.6B to zero accuracy by the trained budget on a balanced binary task (chance 0.500). State-norm growth, the failure that prior accounts predict, is not the cause: the norm stays within a factor of 2.021 while the head commits to a single wrong token. Yet in 19M-parameter models trained from scratch on two synthetic tasks, 16 seeds per configuration, training without the normalisation is never worse than training with it and extrapolates better: the two are closest at the trained depth and separate on both sides of it (Cliff's delta up to 0.867 beyond the budget). Both results follow if agreement, and not the normalisation itself, is what keeps depth reusable. The damage sits in the readout together with the last layer of the block: in the models trained from scratch, refitting the head over the frozen modified loop recovers a third of the lost accuracy and plateaus, while refitting the last block layer with it recovers all of it. Finally, comparing looped with stacked depth at an equal inference loop count is confounded by unequal overshoot of the trained budget; at matched overshoot the advantage of looping vanishes on one task and shrinks on the other.

---


### 45. [Which Answer Did the Seventeen-Year-Old Write? A Behavioral Case Study of Author-Age Misattribution, Miscalibrated Confidence, and Non-Corrective Self-Explanation in Six Frontier Language Models](https://arxiv.org/abs/2610.31946)

**<font color=#1a73e8>作者：</font>** Brianne Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Three students answered the same exam prompt by hand: "What is happiness? Are you happy?" Their ages, recorded at collection, are 17, 28, and 45. The 17-year-old's answer is hedged and formally phrased. Asked to match each answer to an age and gender label, most frontier language models confidently assign it to an adult. This paper reports a structured case study of that failure across six models: Claude Fable 5, Gemini 3.1 Pro, GPT-5.6 Sol, Grok 4.5, GPT-4o (2024), and DeepSeek V4. We ran 1,081 API sessions and scored 3,225 responses across six experimental conditions that manipulate framing, disclosure format, and audience-awareness instruction. Three of six models perform at or near chance (1/3) on the matching task while reporting 73-88% mean confidence. The youngest writer's answer is misattributed to an adult in up to 90% of trials. Removing the multiple-choice scaffold collapses accuracy further: three models never place within three years of the true age once open-ended estimation is required. Institutional framing ("a community-college biology final") significantly degrades the best-performing model's accuracy; a neutral label does not. A single audience-awareness instruction significantly improves one model (+21 points) and moves another to ceiling, with no detectable effect on the three weakest models. Stated confidence is uncorrelated or inversely correlated with correctness for five of six models. After ground truth is revealed, one model names its own stereotyping in 68 of 114 explanations, yet shows the lowest accuracy and highest confidence of any model under blind presentation: articulate retrospective diagnosis that does not track the quality of its judgments. This is a three-item, single-topic, single-language case study meant to isolate a mechanism, not to estimate a population bias rate. Data, code, and raw model outputs are publicly released.

---


### 46. [Sharp Bounds on the Winner's Bias under Independent and Nonnegatively Correlated Noise](https://arxiv.org/abs/2610.31948)

**<font color=#1a73e8>作者：</font>** Ivan Viakhirev, Kirill Borodin, Grach Mkrtchian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reporting the best of $M$ noisy, unbiased scores overstates the winner's value by up to $c\sqrt{V}$, where $V$ is the total noise variance and the sharp constant $c$ depends on how the noise is dependent. It was known only at the two extremes, arbitrary dependence ($\sqrt{(M-1)/M}$) and i.i.d. noise. We determine it for two classes in between: for independent, not identically distributed noise it is $\sqrt{(M-1)/(2M)}$, and for pairwise nonnegatively correlated noise it is $(M-1)/M$; for uncorrelated noise this answers the maximum version of an open question about the expected range. Explicit finite constructions attain both. As a corollary, the bias of the cross-validation estimator is bounded sharply within each class. All theorems are formally verified in Lean 4. Across 448 language-model and classifier selection pipelines, designs with per-candidate items realize a median 0.75 of the independent-class ceiling. At a fixed item budget, scoring all candidates on shared items is markedly less optimistic than giving each candidate its own items.

---


### 47. [A Mathematical Theory of the Jacobian Lens](https://arxiv.org/abs/2610.31955)

**<font color=#1a73e8>作者：</font>** Mitchell Ostrow, Daoyuan Qian, Toni Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work from Anthropic introduced a new interpretability tool, called the Jacobian lens (J-lens, Gurnee et al., 2026). This method identified linear directions in the hidden states of frontier language models that had properties reminiscent of working memory-like representations. However, it is unclear what mechanistic properties of such features make them detectable to the J-lens. To this end, we introduce a mathematical theory of the J-lens, and show that it preferentially identifies coherent features -- directions that act like leading, spatially coherent Lyapunov modes. Small perturbations along these directions amplify across layers, remain roughly constant across token positions, and are consistent across different contexts. While we are agnostic to whether these properties are necessarily associated with a ``Global Workspace'', the analytically derived preferences of the J-lens nevertheless explain prior empirical applied to both model classes. We validate our analysis on a Bayes filter and a toy transformer, each optimally predicting next tokens emitted from a Hidden Markov Model (HMM). We show how modulating task parameters that change the coherence of features in the Bayes filter correspondingly and predictively modulates the response of the J-lens . We also introduce of a family of J-lenses built to emphasize different temporal scales of information processing in LLMs, which we call $\omega$-J-lenses.

---


### 48. [POS-Signature Demonstration Retrieval for In-Context Dependency Parsing](https://arxiv.org/abs/2610.31966)

**<font color=#1a73e8>作者：</font>** Muhammad Azam Afridi, Rajab Ali, Marco Passarotti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Demonstrations for in-context learning are often retrieved by semantic similarity, which may be a poor proxy for relevance in structured prediction. We study demonstration selection for Universal Dependencies parsing with a POS-signature policy that represents sentences with weighted part-of-speech statistics and retrieves three length-compatible, gold-parsed examples from the labeled training split. We evaluate two open-weight language models without fine-tuning on all 2,077 sentences of the UD English Web Treebank test set, comparing the policy with shot- and format-matched fixed and semantic three-shot baselines, as well as zero-shot, chain-of-thought, and critique-refinement systems. POS-signature retrieval yields the highest labeled attachment score among the tested prompting systems for both models (72.4 and 73.2), outperforming semantic retrieval by 1.9 and 2.7 points; paired-bootstrap 95% confidence intervals exclude zero for both contrasts. Chain-of-thought and refinement comparisons vary across models. These exploratory results favor the tested POS-signature retrieval approach on English-EWT. We release the prompts, archived outputs, and evaluation code.

---


### 49. [Knowing Whom to Trust is not Enough: The Trust--Agreement Gap in Repeated Multi-Party LLM Negotiation](https://arxiv.org/abs/2610.31971)

**<font color=#1a73e8>作者：</font>** Amit Sarker, Moumita Choudhury, Saaduddin Mahmud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly participate in negotiations on behalf of individuals and organizations, yet they remain vulnerable to manipulation, particularly in repeated multi-party interactions. Classical multi-agent systems address this challenge through explicit trust and reputation models, whereas existing work on LLM negotiation largely treats trust as an emergent phenomenon. We investigate whether LLM agents can form useful trust estimates from prior interactions and leverage them to improve future negotiation outcomes. We introduce a repeated, multi-party, multi-issue negotiation framework in which recurring agents participate in a sequence of negotiation games while one participant covertly attempts to prevent agreement. After each game, agents assess their counterparts and maintain pairwise trust estimates that carry over to subsequent negotiations. We compare trust-aware and trust-agnostic agents and analyze how explicit trust influences negotiation outcomes. Our results reveal a \emph{trust--agreement gap}: trust-aware agents can identify the adversary within a few games, but accurate trust estimates do not consistently translate into better agreements. Trust increases agreement rates by up to 23 percentage points, but only when agents are explicitly guided to use it in their decisions. Explicit trust can therefore improve repeated LLM negotiations, but its value depends critically on how trust is assessed and incorporated into agents' reasoning.

---


### 50. [The Helpful Agent Problem: When Emergent Cooperation Among LLM Agents Bypasses Intended Workflows](https://arxiv.org/abs/2610.31985)

**<font color=#1a73e8>作者：</font>** Moumita Choudhury, Amit Sarker, Shlomo Zilberstein  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed in collaborative settings where they pursue separate tasks while sharing resources and operating under review or oversight processes. Such settings create safety risks not only when agents are malicious, but also when they are simply trying to help. Prior work has largely studied adversarial or explicitly collusive behavior; we show that benign agents pursuing separate objectives can spontaneously cooperate in ways that bypass intended workflows. We call this the \emph{helpful agent problem}. We study long-horizon shared-resource environments in which agents sometimes depend on resources owned by their peers and cross-owner changes are normally mediated by a reviewer. When review becomes unavailable, agents begin making changes on one another's behalf despite having no shared reward or explicit incentive to cooperate. Crucially, these actions remain within each agent's local permissions while circumventing the system's intended oversight structure. We introduce \textsc{FavorBench}, a controlled benchmark with measurable downstream side effects, and adapt \textsc{CooperBench} to test the phenomenon in realistic repositories. Across two benchmarks and four models, we find that out-of-workflow favors emerge frequently. Further, in \textsc{FavorBench}, favors from at least three models cause significant harm to parties outside the interaction. These results reveal a distinct multi-agent safety challenge: cooperation itself can create pathways around system-level safeguards.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
