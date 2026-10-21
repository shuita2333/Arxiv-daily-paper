# 🧠 大模型相关研究 | 2026年10月22日

> 本类共 **299** 篇论文：已确认 **275** 篇，待复核 **24** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

---

### 1. [H2DF: Calibrated Target Bands for Controllable Language-Model Unlearning](https://arxiv.org/abs/2610.26864)

**<font color=#1a73e8>作者：</font>** Jupiter Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gradient ascent (GA) is a simple language-model unlearning baseline, but it continues increasing forget loss after useful forgetting has occurred. This unbounded pressure can damage retained utility and make forgotten examples abnormally high-loss. We introduce H2DF, a calibrated target-band objective that applies GA-like pressure below a data-dependent lower target and suppresses, or reverses, that pressure after the target region is reached. The targets are estimated from matched non-member examples before training, so the base objective requires one forget-batch forward/backward pass per optimization step; our reported TOFU variant adds sparse retain replay every tenth step. We instantiate a one-sided objective for TOFU question answering and a two-sided objective for MUSE-News language modeling. Across three TOFU seeds, H2DF obtains a forget NLL of 1.528 with margin 0.049 and retain NLL of 1.165 with margin 0.047, matching GradDiff while using retain replay only every tenth step and showing substantially lower variability than GA. On MUSE-News, H2DF improves retention over GA and NPO and is competitive with SimNPO, but does not dominate it. Ablations show that the upper target reduces overshoot and that validation-based checkpoint selection is important. These results support calibrated target bands as a practical mechanism for controlling forgetting strength, while also exposing sensitivity to random seed and calibration quality.

---


### 2. [High-dimensional layer-state trajectories reveal the internal dynamics of transformer inference](https://arxiv.org/abs/2610.26866)

**<font color=#1a73e8>作者：</font>** Heng Zhao, Yufei Wang, Ruidian Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic studies of large language models localize function in parameters, attention heads or neurons, but those parts do not specify how one inference unfolds. We treat the ordered layer-state trajectory as the empirical process and test whether layer order defines a measurable computation. Across representative Qwen, Llama and Gemma checkpoints, realized order produced paths 1.60--2.24 times as aligned with their endpoint chord as endpoint-preserving shuffles. The order effect transferred to a lexical task, but was stronger in three random initializations of the same Qwen architecture, identifying an architecture-compatible scaffold rather than a training-specific law. Direct hidden states provided stronger mechanism coordinates than vocabulary readbacks, and a task-defined coordinate made candidate competition computable. After additive interventions failed, local transition actuators selectively controlled internal trajectories across checkpoints. A confidence gate then drove 17 of 87 held-out Qwen closure trajectories across the full-vocabulary top-1 candidate boundary while leaving all 203 non-closure top-1 outputs unchanged. Safety-matched action reassignment performed similarly, locating the gain in selective gating and the bounded actuator family rather than fine-grained dose assignment. Layer order exposes an observable, computable and behaviourally consequential process of transformer inference without establishing a complete theory of LLM dynamics or control of answer correctness.

---


### 3. [Navalia: Advancing Cowork Agents through Verifiable Task Synthesis and Long-Horizon Post-Training](https://arxiv.org/abs/2610.26887)

**<font color=#1a73e8>作者：</font>** Hengqi Liu, Ziyuan Liu, Yang Qin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are evolving from conversational assistants into Cowork Agents capable of autonomous planning, tool use, and complex task execution. Financial analysis requires these agents to integrate cross-document evidence and perform multistep numerical reasoning, but expert task authoring is costly, while direct LLM synthesis struggles to produce challenging tasks with reliable answers. We introduce Navalia, a framework for Cowork Agents that combines verifiable task synthesis with long-horizon post-training. Using corporate financial reports as its data source, Navalia semantically selects supporting evidence from complete fact sets and constructs executable computation chains to generate analytical tasks with traceable evidence and actual data dependencies between steps. We further use independent LLM review and programmatic checks to verify evidence consistency and answer correctness. The verified tasks are then used for trajectory collection, cold-start supervised fine-tuning (SFT), and reinforcement learning (RL) to improve long-horizon task execution. Navalia, initialized from Qwen3.6-35B-A3B, achieves consistent gains over the base model across all five benchmarks: OfficeQA Pro, FinSearchComp, Finance Agent Benchmark, APEX-Agents-AA, and Workspace-Bench-Lite. These results demonstrate that Navalia improves evidence integration, tool use, and long-horizon task execution capabilities and generalizes to broader Cowork settings, including general office tasks.

---


### 4. [Large language model and reinforcement learning based autonomous construction and progress updates](https://arxiv.org/abs/2610.26899)

**<font color=#1a73e8>作者：</font>** Yifei Xiao, Huasheng Lin, T.Y. Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Due to the rapid growth of the global population, traditional construction methods are gradually unable to meet the current housing demand. The advancement of machine learning algorithms has encouraged researchers to explore their applications in the construction industry, leading to more intelligent and efficient building processes. In particular, the rise of large language models in recent years has provided more possibilities for the transformation from traditional construction to smart construction. In this study, a large language model and reinforcement learning based autonomous construction method is proposed. An enhanced soft actor-critic reinforcement learning algorithm is developed to plan actions for a mobile crane according to construction tasks. Robot kinematics and control algorithms are used to ensure that the actions generated by the reinforcement learning algorithm can be executed by the crane. In addition, a customized embedding model is developed to extract information from the construction environment according to user interests. Then, a large language model, ChatGPT 5, is used to update construction progress, provide safety information to control system, and generate construction progress reports. The feasibility of proposed method is verified through several full-scall retaining wall construction experiments.

---


### 5. [Pareto-Optimal RTL Code Generation via Multi-Objective Reinforcement Learning with Large Language Models](https://arxiv.org/abs/2610.26904)

**<font color=#1a73e8>作者：</font>** Koki Takeshita, Kenji Uebayashi, Hikaru Tomonari 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies have proposed reinforcement learning with verifiable rewards (RLVR) methods that enable LLMs to generate high-quality RTL circuits from natural-language specifications. Existing approaches optimize circuit PPA (Power, Performance, Area) by aggregating multiple objectives into a single scalar reward, making it difficult to simultaneously generate diverse Pareto-optimal solutions across different trade-offs such as low power, low latency, and small area. However, in practical design, the relative importance of each objective varies depending on product requirements and design constraints; thus, obtaining a diverse and high-quality candidate set is beneficial in that designers can choose a preferred trade-off a posteriori. In this work, we are the first to propose a learning method for LLM-based circuit generation that optimizes, not the quality of a single circuit, but the quality and diversity of the entire circuit set obtained through multiple generations in the PPA objective space. The proposed method consists of (1) a generation-based training pipeline that reformulates coverage improvement of the entire Pareto solution set into a sequential circuit generation problem, and (2) a reward function based on Hypervolume Contribution (HVC) that measures how much a generated circuit contributes to the Pareto front. Evaluation on the RTLLM v2 benchmark shows that the proposed method achieves +13.3 percentage points in relative Hypervolume over a baseline without PPA optimization and +14.4 percentage points over a single-objective reinforcement learning method, while also demonstrating superiority in circuit diversity.

---


### 6. [Uncertainty Gates the Gradient: Adaptive Updates for Generalized Few-Shot 3D Segmentation](https://arxiv.org/abs/2610.26909)

**<font color=#1a73e8>作者：</font>** Yifei Zhao, Fanyu Zhao, Shengtang Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In generalized few-shot 3D point cloud segmentation, support annotations are often compromised by sparsity and occlusion. Blindly adapting to such low quality samples risks learning spurious geometric patterns rather than robust novel concepts. Although 3D Vision-Language Models have been introduced to sup plement supervision, the potential of uncertainty to actively govern adaptation dynamics remains underexplored. Existing signal-level methods like loss reweight ing fail to prevent unreliable episodes from steering the optimization trajectory. To address this, we propose Uncertainty-Gated Adaptive (UGA), to the best of our knowledge the first framework that elevates uncertainty to update-level gating for generalized few-shot 3D point cloud segmentation. The core mod ule, Uncertainty-Gated Update (UG-Update), estimates episodic reliability via intra-class dispersion over merged support and pseudo-labeled novel supervision, and selectively gates residual gradient updates. This encourages the model to learn novel semantics from reliable episodes while attenuating updates during unreliable ones. Complementing this, we introduce an Uncertainty-Based Pseudo Label Filter (UB-Filter) to enforce learning from high-confidence dense signals. On ScanNet200 and ScanNet++ (1-/5-shot), UGA sets new state of the art with an average +3.08 HM IoU over the strongest prior baseline.

---


### 7. [Memory Internalization via Test-Time Training for Long-Video Understanding](https://arxiv.org/abs/2610.26910)

**<font color=#1a73e8>作者：</font>** Haonan Zhao, Jiaxuan Chen, Qingyang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding often requires answering many questions about a single video whose evidence is distributed across extended temporal contexts. Conventional video-language models repeatedly encode frames or retrieve visual evidence for every question. Parameterized video memory offers a write-once alternative, but existing methods rely primarily on synthesized text and fixed adaptation configurations, leaving open where video knowledge should be written and how visual evidence should shape the memory. We introduce Memory Internalization via Test-Time Training (MIT^3), a per-video adaptation framework that writes each long video into compact, video-specific adaptive parameters for video-free, text-only question answering. Under compact multi-scale supervision, causal tracing measures the causal memory utility of each model layer for video-grounded answering and selects video-specific adaptation locations. Visual memory distillation then trains the text-only memory to reproduce the representation change induced by the relevant video clip, preserving the internal effect of visual evidence beyond textual supervision. Across LVBench, LongVideoBench, and Video-MME, MIT^3 achieves data-efficient video-free question answering with substantially fewer synthesized samples than prior parameterized video-memory methods, demonstrating that effective video internalization depends on both where knowledge is written and how visual evidence is distilled into the model.

---


### 8. [MedPAO-Assist: Edge-Deployable, Modality-Aware Agentic AI for Radiology Report Structuring](https://arxiv.org/abs/2610.26913)

**<font color=#1a73e8>作者：</font>** Shrish Shrinath Vaidya, Minmini Selvam, Ganapathy Krishnamurthi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The adoption of Large Language Models for radiology report structuring has been largely dominated by either proprietary cloud-based models or large open models requiring high-end GPUs for deployment, which is a critical bottleneck for clinical adoption in radiology workflows that demand data privacy and offline operation. To address this, we present MedPAO-Assist, an edge-deployable agentic framework that generates structured radiology reports directly from radiologist dictation and voice commands, requiring only $\approx3.3$ GB peak RAM and achieving an average end-to-end latency of $\approx31$ seconds on a standard laptop CPU through an asynchronous, multi-threaded execution pipeline. The system currently supports four major imaging modalities -- Chest X-ray, Chest CT, Abdomen CT, and Brain MRI. To our knowledge, it is among the earliest agentic systems to run its entire pipeline with a Small Language Model (SLM) in the 0.6B-parameter range. This multi-agent architecture, built around an Extract-Ground-Generate paradigm, performs concept extraction, SNOMED-CT grounding, and structured report generation, followed by a speech-driven human-in-the-loop correction phase, together forming a fully "no-touch" reporting workflow that requires no keyboard input, external API calls, or internet connectivity. We evaluate each pipeline stage individually -- concept extraction, ontology grounding, and concept categorization and report hardware profiling results demonstrating the system's feasibility for real-time, CPU-only clinical deployment.

---


### 9. [AtomSD: Procedural Atom-Guided Self-Distillation for LLM Agents](https://arxiv.org/abs/2610.26926)

**<font color=#1a73e8>作者：</font>** Bohan Yu, Pengfei Cao, Kai Tian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) possess broad factual knowledge and strong reasoning capabilities, but solving complex tasks also requires procedural knowledge about how to act. Existing approaches often represent procedural knowledge through trajectories or bundled skills, limiting flexible reuse across interaction histories. This paper introduces Procedural Atoms, fine-grained and independently applicable units that represent Intent, When, Do, and Avoid guidance. Building on this representation, we propose AtomSD, an Atom-guided Self-Distillation framework in which the learner continually extracts Procedural Atoms from its own successful trajectories and distills them into the evolving policy through Atom-conditioned supervision and task-reward optimization. Comprehensive experiments show that AtomSD consistently outperforms strong reward-based and distillation methods, exceeding the state-of-the-art baseline by up to 9.31 points in average performance. Further analyses demonstrate that the proposed Procedural Atoms provide effective guidance, highlighting the value of atom-level procedural knowledge for policy learning.

---


### 10. [Expert-Guided Rubrics as Dense Reward Signals for Reinforcement Learning in Non-Verifiable Domains](https://arxiv.org/abs/2610.26932)

**<font color=#1a73e8>作者：</font>** Ashish Bansal, Hossam Amer, Keerat Kaur Guliani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as autonomous agents in non-verifiable domains such as financial services, where they must interpret user intent, rewrite queries, and retrieve information under domain-specific constraints. Although reinforcement learning (RL) can train such agents from the consequences of their actions, recent successes largely rely on verifiable tasks with automatically computed binary rewards. In non-verifiable retrieval tasks, assessing query quality requires scarce subject-matter expert (SME) judgment that is inherently graded rather than binary. With Group Relative Policy Optimization (GRPO), sparse rewards yield no useful learning signal when all sampled outputs within a group receive the same outcome, causing optimization to stall. We introduce a method that converts a small, fixed investment of SME judgment into a dense reward and combines it with retrieval-based metrics to form a hybrid, GRPO-compatible training signal. Experiments show improvements of up to 6\% in Recall@3 and 6.7\% in MRR@3 compared with sparse-reward baselines.

---


### 11. [How Intervention History Changes AI Agent Sabotage on Subsequent Tasks](https://arxiv.org/abs/2610.26935)

**<font color=#1a73e8>作者：</font>** Daniel Saeedi, Amirali Aghazadeh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI control evaluations often reset agents' memory between tasks, although deployed agents may retain records of prior interventions. We ask whether learning that an earlier attack was caught changes an agent's ability to evade defer-to-trusted (DtT), a protocol that replaces suspicious work with a trusted model's solution. Herein, we study cross-episode adaptation: whether intervention history changes attack behavior on a subsequent task with different objectives and a fresh environment. We evaluate this using ControlArena's Infrastructure-as-Code (IaC) and SHADE-Arena as testbeds, where agents must complete a main task while covertly pursuing a harmful side objective. For each successor task, we pair a history-conditioned attempt with the model's no-history attempt. The retained history either states that the previous submission was replaced or additionally includes the trusted model's replacement. For Claude Opus 4.8 on IaC, intervention history reduces successful sabotage. Completion of both the main and side objectives falls from 77% to 12% when the agent is told about the replacement and to 38% when it is also shown the trusted model's replacement, while main task success remains essentially unchanged. Condensing the history weakens this effect, suggesting that the retained context matters and limiting attribution to intervention feedback alone. GPT-5.4 shows no significant change in successful sabotage on the same IaC benchmark. On SHADE-Arena, GPT-5's successful sabotage rate decreases, but the reduction is not significant. Across the tested models, history conditions, and deferral thresholds, intervention history never increases the rate of successful sabotage that survives DtT. These results show that intervention history can change subsequent attack behavior, but its effect depends on both the model and the retained context.

---


### 12. [Do We Need the Largest LLMs for Every Clinical Decision?](https://arxiv.org/abs/2610.26937)

**<font color=#1a73e8>作者：</font>** Ali H. Lazem, William Teahan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large clinical language models often require multi-GPU infrastructure, limiting local deployment. We introduce CERTA, a decision-level statistical certificate that determines when a quantized model may substitute for its native BF16 reference and escalates decisions that cannot be certified to it. Across eleven instruction-tuned models, both general-purpose and domain-adapted, from three families (7-72B), we evaluated 2,500 clinical-verification decisions from de-identified patient contexts (2,484 patients), with patient-disjoint calibration and testing. In the higher-power operational analysis, round-to-nearest 8-bit quantization at BF16 storage served 99.8-100% of held-out decisions across all eleven models; formal finite-sample guarantees were assessed separately using the exact split-sample procedure. In the same operational analysis, the class-conditional 4-bit frontier reduced the amortized, BF16-equivalent deployment cost to 25.8% and 27.3% of the BF16 reference for Qwen2.5-72B and HuatuoGPT-o1-72B, respectively, with measured peak memory of 43.0 and 42.7 GB, below the nominal capacity of a single 48 GB accelerator. Deployment on that specific hardware was not directly tested. Under the exact split-sample certificate, which also accounts for configuration selection, these costs were 26.7% and 27.9%. On external disease named-entity benchmarks against human annotations, the frontier-selected NF4 configurations had a mean absolute F1 change of 0.045 on both datasets, with substantial model-specific variation. CERTA converts compression from a fixed precision choice into a risk-controlled deployment policy for this verification task.

---


### 13. [Industrial Agentic AI: LLM-Driven New-Generation Agents for Smart Manufacturing](https://arxiv.org/abs/2610.26941)

**<font color=#1a73e8>作者：</font>** Lei Ren, Haiteng Wang, Shixiang Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are enabling agents to move beyond predefined workflows toward autonomous planning and execution, creating new opportunities for smart manufacturing. However, dynamic environments, complex physical constraints, and stringent reliability requirements hinder the direct deployment of general-purpose agents in smart manufacturing. This article presents a systematic overview of LLM-driven industrial agents. First, we analyze five key challenges and discuss the concept and core characteristics of industrial agents. We then establish a unified taxonomy covering application scenarios, embodiment forms, and five capability levels. Next, we propose a four-layer system architecture and detail its core modules and operational mechanisms for closed-loop task execution. Finally, we review representative applications across the industrial lifecycle and outline future research directions. This article provides a structured reference for the design, development, and application of industrial agents.

---


### 14. [Fix, Not Just Resample: Bounded Compiler-Guided Repair in Lean 4](https://arxiv.org/abs/2610.26942)

**<font color=#1a73e8>作者：</font>** Haotian Deng, Chris Farber, Sonal Narasimha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated theorem provers often rely on sampling language models, but proof assistants like Lean reject each failed step with a precise error message --- information that pure sampling discards. To overcome this, we introduce a bounded, online step-level repair module. Our search samples $K$ candidate tactics at each step and repairs a failed tactic at most $R$ times. Instead of discarding failed tactics, we feed the compiler's error message to a pretrained repair model to fix individual rejected steps in place. This approach improves the solve rate over a sampling-only baseline across all tested candidate budgets ($K \in \{1,3,5,8\}$), achieving up to a $32\%$ relative gain and solving $82$ additional theorems on a $1{,}990$-theorem subset of the LeanDojo benchmark. Repair is not free: it trades extra runtime for reachable proofs. But the trade is predictable: repair pays most when sampling is constrained; its return is front-loaded, with the first repair attempt capturing $84\text{--}96\%$ of the total gain; and the gain comes almost entirely from shallow tactic-execution failures rather than structural errors such as type mismatches. This targeted repair successfully replicates on a second benchmark (Lean Workbook), nearly doubling the solve rate with zero regressions.

---


### 15. [MAMath-Bench: Process-Aware and Robust Evaluation of Multimodal Multi-Agent Mathematical Reasoning](https://arxiv.org/abs/2610.26943)

**<font color=#1a73e8>作者：</font>** Xinping Wang, Jie Ma, Rui Xing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning is a fundamental capability for educational applications of Large Language Models (LLMs), where reliable problem solving requires not only correct answers but also coherent and verifiable reasoning processes. Multi-agent systems (MASs) have shown growing potential in this domain by leveraging collaboration and verification among multiple LLM agents. However, existing evaluations primarily focus on the correctness of final answers in text-only settings, offering limited insight into multimodal reasoning capabilities, the reliability of intermediate reasoning steps, and robustness against reasoning errors. To address these limitations, we introduce MAMath-Bench, a process-aware benchmark designed to evaluate the multimodal mathematical reasoning capabilities of MASs. MAMath-Bench comprises 1,003 problems spanning 11 mathematical categories, multiple difficulty levels, and several modalities, including text, images, and audio. It features fine-grained milestone annotations to evaluate systems across three dimensions: problem-solving correctness, reasoning-process reliability, and robustness to adversarial reasoning-chain perturbations. Our evaluation yields three key findings. First, multi-agent collaboration does not consistently improve final-answer accuracy over strong single LLMs. Second, collaboration can substantially enhance the coverage of intermediate reasoning, but such gains may come at the cost of increased reasoning redundancy. Third, current systems remain vulnerable to adversarial reasoning errors, particularly those involving subtle structural perturbations. The dataset is available at this https URL.

---


### 16. [Evidence-Grounded LLM-Assisted Android Mobile Forensic Reporting](https://arxiv.org/abs/2610.26946)

**<font color=#1a73e8>作者：</font>** Madhab Chandra Das, Sajid Ahmed, Tasnia Tabassum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models can assist forensic report drafting, but fluent output does not ensure evidentiary reliability. This study presents an evidence-grounded framework for evaluating LLM-assisted Android forensic reports at the atomic-claim level. Gemini, Llama, and Qwen each generated reports for two controlled cases: a public Android 13 dataset and a physical LG device with a zero-reportable-fact boundary. The six accepted reports were decomposed into 612 claims and evaluated against frozen, human-reviewed authorities through content labeling, citation validation, fact-recall analysis, independent rechecking, and dispute resolution. The final corpus contained 424 supported, 163 unsupported, four contradicted, four overstated or incomplete, and 17 excluded claims. In the public case, all three models recovered all 27 authorized report-level facts. Citation validity nevertheless differed substantially: Gemini produced 168 valid citations from 189 required citations, Qwen produced 145 from 189, and Llama produced none from 135. In the physical device case, the models generated 65 claims despite the zero reportable-fact boundary, including 38 unsupported and one contradicted claim. These results show that evidence restriction and complete fact recall do not guarantee claim support or valid evidence attribution. The framework provides an auditable method for detecting unsupported content, preserving claim-to evidence lineage, and retaining investigator authority over final forensic reports.

---


### 17. [LightCRS: Lightweight Multi-Domain Conversational Recommendation System](https://arxiv.org/abs/2610.26948)

**<font color=#1a73e8>作者：</font>** He Ma, Lan You, Qiyang Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational recommender systems have recently adopted vision-language models to match user dialogue intents with multimodal product information. However, extending these methods to many product domains faces a dilemma: deploying a separately adapted VLM per domain scales cost linearly with the number of domains and requires routing each dialogue to the right model, while naively merging all domains into a single VLM degrades accuracy because product characteristics vary widely across categories. We propose LightCRS, a lightweight, query-conditioned framework for unified multi-domain multimodal conversational recommendation. LightCRS precomputes multimodal product representations once offline with frozen encoders. Online, a compact 5.3M-parameter module fuses this evidence for each dialogue via query-conditioned cross-attention, whose parameters are shared across all domains, and compares candidates jointly with an inter-candidate Transformer. To enable rigorous evaluation, we construct MM-R2A-25, a 25-domain benchmark pairing natural Reddit recommendation-seeking conversations with Amazon product listings. LightCRS achieves state-of-the-art average HR@1, NDCG@5, and MRR, improving HR@1 by 35.4\% over the strongest baseline while reducing per-query latency by 266 times. Joint multi-domain training itself improves HR@1 by 15.2\% over separately trained single-domain models.

---


### 18. [Beyond Policy Discrepancy: Capability-Aware Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.26950)

**<font color=#1a73e8>作者：</font>** Xuanfeng Yang, Le Gui, Jiaming Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) integrates domain specialists into a shared student, but determining how strongly each teacher should supervise remains challenging. Existing discrepancy-based allocation can assign strong supervision even when the student already matches or exceeds the teacher's task performance, since behavioral mismatch does not necessarily imply a remaining capability deficit. We propose Capability-Aware Multi-Teacher On-Policy Distillation (CA-MOPD), which combines specialist merging with capability-guided allocation to account for what the student has already learned. CA-MOPD first merges reinforcement-learning specialists into a strong student initialization, then uses verifier-estimated teacher--student capability gaps to adjust domain-level distillation strength. Supervision decreases as capability gaps close and increases when estimated student capability regresses, while dense token-level guidance remains provided by the teachers. Across six benchmarks spanning mathematics, code generation, and instruction following, CA-MOPD achieves an average score of 32.22, outperforming naive MOPD, Open-MOPD, and the merged initialization by 0.86, 0.83, and 0.74 points, respectively. Controlled comparisons further support the benefits of merged initialization and capability-gap guidance under matched training budgets.

---


### 19. [The Bottleneck Is Retrieval, Not Reading: Diagnosing Evidence-Based Generation with RAG for Long Context Question Answering](https://arxiv.org/abs/2610.26951)

**<font color=#1a73e8>作者：</font>** Debopriyo Banerjee, Owais Aijaz, Ahmer Tabassum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is the dominant paradigm for grounding large language models in external corpora, but its similarity-driven, chunked pipeline has structural blind spots: it cannot anticipate which passages a question requires and discards document-level context that resolves cross-passage references. We introduce evidence-based generation (EBG), requiring models to return an answer with line-level citations, and a joint Ans+Evid metric that scores correctness and grounding simultaneously. We reformulate two corpora into evidence-grounded multi-document QA benchmarks- MultiHop-RAG and QASPER-MP, a multi-paper adaptation of QASPER with realistic short paper cues, and pair them with a controlled synthetic two-hop haystack and an evidence-augmented NoLiMa spanning 10K-1M characters. Across ten proprietary frontier and three open-weight LLMs, EBG isolates two RAG limitations that long-context models avoid: similarity retrieval surfaces any relevant chunk far more reliably than all required chunks for multi-fact queries, and chunking destroys document meta-information needed to resolve identity-bearing queries. EBG also exposes grounding failures invisible to answer-only evaluation, including incomplete citations in two-needle settings and a widening gap between Ans and Ans+Evid when context contradicts parametric knowledge. Data and code are available at this https URL.

---


### 20. [LAMB: Latent Multi-Hypothesis Beliefs for Long-Horizon Large Language Agents](https://arxiv.org/abs/2610.26955)

**<font color=#1a73e8>作者：</font>** Peien Ding, Hui Li, Yuhan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon language agents require compact memories that retain interaction evidence while preserving competing hypotheses about unobserved states. Although effective, many belief-state methods encode memory in discrete natural language, where repeated compression can omit evidence or prematurely discard plausible alternatives. We introduce LAMB, a recurrent framework for latent multi-hypothesis beliefs. A Common--Delta factorization combines a shared Common state for interaction evidence with weighted Delta components for competing hypotheses. Relative evidence from action-outcome predictions guides recurrent hypothesis updates without generating textual memory. A context-conditioned readout exposes hypotheses separately to the policy through a fixed-token belief prefix in the default configuration. The belief modules and policy are jointly trained using action imitation and auxiliary state, outcome, and observation-discrimination objectives. Across ALFWorld, BabyAI, ScienceWorld, and Crafter, LAMB matches or outperforms PABU, improving ALFWorld SR@30 and ScienceWorld success by 6.0 and 22.0 percentage points, respectively, and Crafter achievement progress by 26.37 points. On ALFWorld, it also reduces the redundant-action rate by 17.70 percentage points. These results support latent multi-hypothesis beliefs as compact memory for effective long-horizon decision making

---


### 21. [Dynamic System Inspired Continuous Large Language Model for AI4Science Tasks](https://arxiv.org/abs/2610.26959)

**<font color=#1a73e8>作者：</font>** Zhaoxin Fan, Zheng Zhu, Yuqing Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific foundation models increasingly operate on continuous phenomena, yet still use discrete residual computation. We ask whether pretrained residual transformations can support additional latent computation without expanding the backbone. To test this possibility, we introduce Continuum-LM, which reuses these transformations as dynamical operators in a continuous-depth language model. Its hidden states evolve through an ordinary differential equation evaluated by higher-order numerical integration, with solver order and step size controlling computation. Across eight scientific tasks, Continuum-LM trains stably and improves mean exact-match accuracy by 7.77 and 10.96 percentage points over discrete counterparts at the 0.6B and 1.7B scales, respectively. At 0.6B, it also outperforms an Ouro-style recurrent control under matched parameter and residual-function evaluation budgets. Together, these results support extensible computational depth through parameter reuse, identifying continuous hidden-state evolution as a practical design dimension for scientific language models beyond parameter scaling.

---


### 22. [When Planning Problems Become Hard for LLMs: Separating Structural Complexity from Semantic Interpretability](https://arxiv.org/abs/2610.26964)

**<font color=#1a73e8>作者：</font>** Mayukh Debnath, Adeyinka Adedigba, Rammohan Mallipeddi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) struggle with classical planning, but benchmarks rarely distinguish structural difficulty from the difficulty of interpreting symbolic vocabulary. We examine seven STRIPS domains with BFS-optimal plan lengths. For predicting structural difficulty without solving an instance, the zero-training delete-relaxation heuristic $h_{\mathrm{add}}$ outperforms learned alternatives on held-out domains (mean Spearman $|\rho|=0.931$), including ridge regression ($0.707$), object count ($0.657$), and the episodic retrieval architecture ARC ($0.400$). ARC also fails to outperform a linear model using the same features. To isolate semantic effects, we progressively rename predicates while preserving states, transitions, and optimal plans. Valid LLM planning success drops from $67.5\%$ to $40.0\%$ between $0\%$ and $100\%$ renaming, while refusals remain at $0\%$. An LLM supplied with ARC's conditioning information predicts difficulty in context better than trained ARC (mean $|\rho|=0.826$). Hybrid routing between an LLM and a symbolic planner depends more on calibration to the target LLM's outcomes than on the structural score selected. Thus, established symbolic heuristics already estimate structural difficulty well; improving hybrid planning requires modeling LLM behavior sensitive to predicate semantics rather than developing more structural predictors.

---


### 23. [SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents](https://arxiv.org/abs/2610.26995)

**<font color=#1a73e8>作者：</font>** Ran Zhou, Zehui Kong, Fanyu Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly rely on reusable skills. However, scaling skill libraries makes efficient and accurate skill use difficult. Full skill loading incurs high token and runtime overhead. In contrast, flat semantic retrieval treats skills as independent text entries, ignoring dependencies, execution order, state transitions, and data flow constraints. We propose SPEM, a lightweight structure-aware procedural memory framework for efficient skill use in LLM-based agents. SPEM maintains Atomic Skill Memory for individual skills and Skill-DAG Memory for reusable compositions derived from successful executions. For a new task, SPEM reuses high-confidence Skill-DAG templates when available. Otherwise, it retrieves atomic skills and invokes Skill-GNN for state- and structure-aware skill selection. Successful executions are written back as new Skill-DAGs, allowing procedural memory to accumulate over time. Experiments on ALFWorld and SkillsBench show that SPEM achieves the best overall effectiveness--efficiency trade-off, reaching 87.1% ALFWorld success and 38.38% SkillsBench reward while reducing token and runtime costs against strong baselines.

---


### 24. [Evaluating Tibetan Speech Recognition Across Dialects and Adaptation Regimes: A Multi-Granularity Analysis](https://arxiv.org/abs/2610.27002)

**<font color=#1a73e8>作者：</font>** Jacob Moore, Sheng Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tibetan speech recognition is usually evaluated with character or syllable error rates because the writing system does not mark word boundaries. These metrics can rank systems differently and respond differently to adaptation failures. We combine character error rate, syllable error rate, and segmented word error rate in one evaluation framework. We use dictionary-based, neural, and language-model-based segmentation and compare their boundaries with expert annotations. We evaluate five ASR architectures on Lhasa Tibetan, then test zero-shot transfer and target-corpus adaptation on five additional corpus subsets. We also vary LoRA rank and training-data size to examine adaptation failure. The results show that a lower character error does not always lead to a lower syllable or segmented-word error. These ranking differences persist across corpora. Metric correlations also weaken in some unsuccessful adaptation settings. Higher LoRA ranks improve syllable and segmented-word scores but remain worse than full fine-tuning in the tested range. A standardized phonological representation provides another view of spelling errors. These findings support evaluation at several linguistic levels and motivate better segmentation and adaptation methods for low-resource ASR.

---


### 25. [Exploration via Activation-Space Steering for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2610.27012)

**<font color=#1a73e8>作者：</font>** Yunan Zeng, Jinhao Jing, Xi Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) trains a language model by sampling responses, scoring them with an automatic verifier, and updating the policy from the resulting rewards. The policy therefore receives direct learning signals only from trajectories that appear in its rollouts. Yet repeated sampling from the same policy can concentrate on similar reasoning paths, leaving useful alternatives unexplored under a fixed rollout budget. We introduce Activation-Space Exploration (ASE), an online method for diversifying training rollouts. By clustering activation differences between correct and incorrect responses to the same problem, ASE builds a structured bank of latent exploration vectors. Different vectors are then applied to subsequent rollouts to explore alternative reasoning paths. On Qwen3-1.7B-Base and Qwen3-8B-Base trained on DAPO-Math-17k, ASE improves average Mean@8 across six mathematical reasoning benchmarks over GRPO by 4.87 and 1.87 percentage points, respectively, under the same rollout budget.

---


### 26. [BR-MoE: Budgeted Semantic Release for Privacy-Preserving Traffic Analytics](https://arxiv.org/abs/2610.27026)

**<font color=#1a73e8>作者：</font>** Abdolazim Rezaei  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traffic cameras support useful analysis, but their outputs can reveal private information. Replacing images with text reduces direct visual exposure. It does not place a formal bound on disclosure. The published reinforcement learning and mixture-of-experts framework refines scene descriptions through relevance, coverage, and brevity rewards. It does not account for repeated releases under a fixed privacy budget. This paper proposes budgeted semantic release as an extension of that framework. Four scene experts first process isolated video chunks. Their outputs are mapped to a fixed, bounded semantic schema. A reinforcement learning controller selects which expert summaries to release and how much privacy budget to spend. The controller uses public task requests and previous private releases. A separate privacy filter enforces the total budget. Calibrated noise is added before the summaries are converted to text. Under explicit chunk isolation and bounded-event assumptions, the complete release transcript satisfies an event-level differential privacy bound. The design also supports reuse of previous summaries without new disclosure. An evaluation protocol covers traffic utility, privacy attacks, release freshness, and computational cost. Illustrative tables show the intended reporting format. They do not establish empirical gains. The proposed contribution is a task-aware release interface with auditable privacy accounting for repeated traffic descriptions.

---


### 27. [Does Multi-Agent Collaboration Reduce Hallucination in Clinical Tasks?](https://arxiv.org/abs/2610.27027)

**<font color=#1a73e8>作者：</font>** Won Seok Jang, Harry Bhaskar Joshi, Hong Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems improve performance on clinical tasks, and that improvement is often read as evidence of a more trustworthy system. However, the two are not the same claim. A clinician acts on the stated reasoning and not only on the conclusion, so whether collaboration reduces hallucination, and what decides when it does, has to be measured in the reasoning too. Yet most evaluations score only the final answer. We evaluate four systems (a single-LLM baseline and three multi-agent topologies) across four models and three clinical tasks, scoring hallucination, under a factuality and faithfulness taxonomy, inside the rationale each system generates and reporting it alongside the task metric. We report that collaboration buys task performance but not lower hallucination as a rule, and no topology is reliably better than another. The effect differs by model: of the $36$ model--system--task comparisons, $12$ are large enough to resolve --- four decreases and eight increases, with no model on both sides. What sets the level, and the direction of any change, is the model rather than the topology or the number of agents. A self-correction experiment is consistent with this: shown its own flagged errors, every model except Llama-3.2-3B-Instruct reduces hallucination; the one model for which collaboration lowers hallucination gains the most, and Llama-3.2-3B-Instruct, the model whose hallucination it amplifies most, does not reduce its hallucination at all. We find that collaboration redistributes what its models can already do; it does not supply what they cannot.

---


### 28. [Teaching AI Agent to Play Poker Strategically Through Preference Optimization](https://arxiv.org/abs/2610.27028)

**<font color=#1a73e8>作者：</font>** Phurinat Polasa, Thanapon Thanadunpremdet, Phatthanasak Kraiduang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A poker agent can make a legal move and still make a strategically poor one. We ask whether compact AI agents can exhibit strategic behavior under hidden information and whether preference optimization can improve beyond static and zero-shot policies. We first evaluate a static baseline and three frozen language models: SmallThinker, Qwen3, and Gemma-3 whose performance varies substantially between exact-game and six-player evaluation. We therefore propose Strategic Preference Optimization with KL-anchored Equilibrium (SPOKE), combining teacher-relative value penalties, policy anchoring, risk constraints, and structured rationale supervision, and compare it with SFT, DPO, GRPO, and GSPO. Across three runs of a SmallThinker-4B-A0.6B policy, SPOKE achieves the lowest mean exploitability in Kuhn (0.213) and Leduc (1.081) and the highest six-max top-1 agreement (0.775), while maintaining teacher KL comparable to SFT (0.522 vs 0.523). These results provide preliminary evidence that strategic preference optimization can improve strategic quality while preserving teacher-consistent behavior.

---


### 29. [M-Plan: Comprehensive Planning For LLM Agents with Memory Arrangement](https://arxiv.org/abs/2610.27032)

**<font color=#1a73e8>作者：</font>** Ziyang Liu, Jiakang Yuan, Jiayuan Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents have recently demonstrated outstanding performance in single-turn tasks, yet they continue to struggle with long-horizon tasks, particularly in environments without prior training. A key limitation of single LLMs is their difficulty in processing long contexts, which stems from weaknesses in continuous decision-making and reasoning capabilities. Although existing multi-agent systems (MAS) equipped with long-term memory bases can partially address this gap, they mostly rely on knowledge reuse or summarization, an approach that is often constrained by directly retrieval without any adaptation for the current task, while the retrieved memory may contain much history noises waiting to be preprocessed. In contrast, MAS characterized by task-specific guidance often lack long-term memory specifically designed for the guidance. To address these challenges, we propose M-Plan, a closed-loop MAS framework that integrates long-term and short-term memory. By combining global-local and past-current guidance, M-Plan enhances agents' performance on multi-turn tasks while maintaining a plug-and-play design. During task execution, agents receive task-specific milestones and insights, and are provided with local hints only when confusion arises, which form global-local guidance together. These guidance generation and utilization construct the short-term memory as well. After task completion, relevant information about the current task is optimized or reorganized before being sent to the long-term memory storage for future retrieval. The designments mentioned above build a comprehensive framework different from other individual long-term or short-term memory works. Extensive experiments on multi-turn tasks including ALFWorld, Webshop, and PDDL across diverse models demonstrate that M-Plan outperforms multiple baseline methods in both accuracy and efficiency.

---


### 30. [Fluent but Fallible: Benchmarking Hallucination and Factual Reliability in Large Language Models](https://arxiv.org/abs/2610.27034)

**<font color=#1a73e8>作者：</font>** Osama Shabih, Dayam Nadeem, Shahab Saquib Sohail 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have significantly advanced natural language processing and artificial intelligence applications through their capabilities in reasoning, text generation and knowledge retrieval. However, LLMs are still vulnerable to two important challenges: hallucination, generating factually incorrect or fabricated content, and response deviation, meaning systematic deviations from ground-truth responses. These limitations raise serious concerns regarding reliability and trustworthiness in academic and research environments. This study offers a thorough comparative analysis using a variety of metrics of ten advanced LLMs ChatGPT, Gemini, Claude~3.5~Sonnet, LLaMA~3, Mistral, Grok, Perplexity, DeepSeek~V3, Falcon, and Gemma based on a benchmark consisting of 70 carefully designed academic prompts across four complexity levels: Basic, Explanation, Advanced, and Tricky, evaluated in February 2025 on specific model versions. Each response was independently evaluated by three reviewers using five metrics: Accuracy, Precision, Recall, Response Deviation Index, and Hallucination Index. Perplexity and DeepSeek~V3 achieved the highest overall accuracy, while Gemini demonstrated strong recall and a well-balanced performance profile across all five metrics. LLaMA~3 showed strong resistance against hallucinations through a conservative method of generation. Advanced-level prompts proved most challenging across all models, while Tricky prompts were handled more reliably owing to their binary true/false structure. Falcon achieved perfect precision and zero hallucinations, but at the cost of the lowest recall and the highest response deviation. The results show a fundamental trade-off between response completeness and factual reliability, intensified by prompt complexity.

---


### 31. [Robustness of Internal Signals for Hallucination Detection in Vision-Language Models](https://arxiv.org/abs/2610.27041)

**<font color=#1a73e8>作者：</font>** Allison Chen, William Yang, Salma Abdel Magid 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When given an image and a text prompt, vision-language models (VLMs) can produce seemingly sophisticated text responses. However, they are also prone to hallucinate objects in their output, which can have detrimental consequences in safety-critical applications. To detect these hallucinations, certain methods interestingly leverage internal signals from the VLM as it generates the text response; potentially, these methods use the same signals that led to a hallucination to detect it. We conduct an in-depth analysis to understand the robustness of these detection methods. First, we show that a naive baseline of a generated word's token position in the VLM text response achieves competitive performance. Further, we reveal how some detection methods rely on token position and use this heuristic as a shortcut. Second, we explore detection methods' sensitivity to language and vision modalities. Our experiments suggest that strong detection performance is often driven by detecting language-based hallucinations, and when methods rely on token position, they tend to be less visually grounded and exhibit reduced robustness when hallucinations occur earlier in a text response. Lastly, we demonstrate that different detection methods can carry complementary signals; when ensembling methods together, adding weaker methods to an ensemble of higher performing ones still offers performance improvements. Altogether, while there may be useful internal VLM signals to detect hallucinations, our investigation reveals important limitations of the current methods that try to leverage them.

---


### 32. [Cross-Lingual Reusability of LLM Pipelines: Financial Extraction, Multilingual Reasoning, and Semantic Screening](https://arxiv.org/abs/2610.27043)

**<font color=#1a73e8>作者：</font>** Joong Ho, Choi, Sherine George 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial institutions increasingly deploy large language models (LLMs) in multilingual markets, raising a practical question: can pipelines developed and validated in English be reused across languages, or must they be rebuilt per locale? We test cross-lingual reusability along three dimensions--accuracy, reasoning-effort transfer, and behavioural stability--through three complementary tasks. Task 1 (cheque extraction) and Task 2 (Mintaka QA with pinned evidence across nine languages and nine model-effort configurations) test whether accuracy and effort settings transfer; Task 3 (FinanceBench pilot, 50 items over SEC 10-K filings in four languages) validates whether these patterns generalise to financial content. Accuracy reusability is broadly confirmed: Gemini 3.5 Flash achieves 95.2-97.6% extraction accuracy across prompt languages, and FinanceBench per-language means span 5.8pp (77.1-82.9%), though the language-difficulty ranking reverses between domains (Hindi is worst on Mintaka, best on FinanceBench at 82.9%). Effort reusability is domain-dependent: higher reasoning effort yields marginal gains on general-knowledge QA but up to 8pp on financial content, and effort configurations that help in English help proportionally in other languages. Behavioural reusability holds: citation-set overlap with English averages 77-79% Jaccard, with no single language consistently worse. Together, these results support qualified reuse of English-built pipelines, but per-domain, per-language validation remains necessary--neither semantic similarity nor self-reported confidence reliably predicts cross-lingual accuracy.

---


### 33. [ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems](https://arxiv.org/abs/2610.27046)

**<font color=#1a73e8>作者：</font>** Zeyu Zheng, Yiyang Liu, Yuyang Zhao 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems begin to resolve open research problems, reliable verification becomes increasingly important. Formal mathematics provides a trusted framework for mathematical reasoning, enabling agents to produce machine-checkable proofs while conducting mathematical exploration. Existing formal mathematics benchmarks often focus on known results or a small set of prominent open problems, which can become difficult to evaluate reliably once solutions are discovered and widely disseminated. Existing evaluation protocols are also not always aligned with how modern coding agents operate. We therefore introduce ReuF2F, a Lean 4 benchmark of 244 formalized open problems drawn from Research Experiences for Undergraduates (REU), spanning entry-level open research problems across a broad range of mathematical subfields. We expect these less prominent open problems, which tend to attract less attention and may remain unsolved for longer, to be better suited for held-out evaluation of end-to-end open problem resolution in Lean. We adopt a standard coding-agent evaluation setting, placing each problem and its logical negation into a Lean project in a Docker container. We also build Leanimum-agent on mini-SWE-agent to provide a unified harness for fair comparisons across models. Our evaluation finds that even the best-performing model resolves only ~40% of the problems, leaving substantial room for improvement on formalized open research problems.

---


### 34. [SciFigBench: A Benchmark for Scientific Method Figure Understanding](https://arxiv.org/abs/2610.27087)

**<font color=#1a73e8>作者：</font>** Lijia Wu, Zheng Li, Yuxuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific method figures often provide researchers with a clear visual entry point into a paper's methodology and core contributions, yet their dense layouts and complex information flows are difficult for Vision Language Models (VLMs) to interpret. Existing benchmarks predominantly focus on coarse-grained tasks, such as context-based retrieval or holistic comprehension, overlooking the fine-grained content and inter-module relations within complex methodological diagrams. To address these overlooked aspects, we introduce Scientific Figure Benchmark (SciFigBench), a benchmark for evaluating core capabilities required for scientific method figure understanding. Specifically, it targets three capabilities: dense content perception, visual relation comprehension, and information-flow tracing. For this purpose, we curate 4,352 scientific method figures from real-world research papers and construct 40,670 QA pairs to operationalize these capabilities as measurable question-answering tasks. All annotations are generated by dedicated pipelines and then manually verified. We further propose SciFigCue, a training-free visual prompting module that externalizes arrow-induced dependencies as visual relational evidence for method-figure reasoning. Experiments across open-source and proprietary VLMs show that even strong models remain substantially limited in visual relation comprehension, while SciFigCue improves performance across several tasks without parameter updates. The code and related resources are available at this https URL.

---


### 35. [A general-purpose System One decision model for clinical records](https://arxiv.org/abs/2610.27099)

**<font color=#1a73e8>作者：</font>** Andrew Zhang, Trinh T.L. Vuong, Sophia J. Wagner 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical care, health-system operations and biomedical discovery depend on extracting reliable answers from patient records, yet applying diverse clinical questions across entire populations remains computationally expensive. Here we present Clinical System One (CS1), a 4-billion-parameter decision model for fast, typed judgments from clinical records, along with two agentic harnesses in which CS1 works together with a generalist language model. CS1-4B is trained on 12.4 million questions and answers from 3.6 million patients across a multi-hospital health system, combining structured-data keys, observed outcomes and language-model supervision across clinical notes, diagnostic reports and patient timelines. It answers multiple typed questions in a single forward pass without task-specific retraining, and each answer carries a probability that can route uncertain cases to human review. On 963,408 held-out patients, CS1-4B outperformed open decision models up to 27 billion parameters on 13 of 14 tasks scored independently of its training teacher. Across 21 external data sets, its aggregate performance approached that of the strongest tested 27-billion-parameter model, with 6.4-fold faster inference in a matched workload. Integrating CS1-4B with a language model agent produced cited answers over complete multi-year patient histories and screened a patient population against the eligibility criteria of 17 registered clinical trials, placing four times as many judged-eligible patients among its top 20 candidates as keyword search while using 690-fold fewer language-model tokens than a language model reading every record. These findings support a division of labour in clinical AI, with small decision models performing repeated record reading and generative models formulating questions and synthesizing evidence.

---


### 36. [Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs](https://arxiv.org/abs/2610.27103)

**<font color=#1a73e8>作者：</font>** Zijian Liu, Chaoyou Fu, Yan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent Omni LLMs (OLLMs) have demonstrated remarkable capabilities in joint audio-visual reasoning, yet cross-modal hallucinations remain a major challenge. Existing mitigation methods mainly operate at the output level, overlooking the entanglement of grounding evidence and learned priors within fused representations. To address this issue, we propose Omni-Woodpecker (OWP), a training-free framework that shifts hallucination mitigation from output-level manipulation to conflict-conditioned representation rebalancing. Specifically, OWP first identifies cross-modal conflicts from complementary modality-specific views. It then employs orthogonal decomposition to separate grounding evidence from competing priors within the hidden states. Finally, OWP adaptively rebalances fused representations by suppressing misleading priors and restoring ignored evidence before decoding. Extensive experiments demonstrate the effectiveness and strong cross-architecture generalization of OWP. Using Qwen2.5-Omni-7B as the backbone, OWP improves performance by 12.9 and 8.6 points on CMM and AVHBench, respectively, while consistently achieving gains of 0.67-2.25 points across four general OLLM reasoning benchmarks. Furthermore, OWP generalizes effectively to VideoLLaMA2-AV, improving performance by 4.6 and 3.9 points on the same benchmarks. Code is publicly available at this https URL

---


### 37. [LVMem: Image-Augmented Memory for Long-Horizon Question Answering](https://arxiv.org/abs/2610.27104)

**<font color=#1a73e8>作者：</font>** Victoria Khoruzhaya, Maksim Kalmykov, Tuong Do Minh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable language-guided perception is essential for embodied agents, where questions about objects, events, and their locations must be answered from long observation histories. Unlike conventional visual question answering, realistic robotic settings require reasoning over extended temporal horizons and persistent scene memory. We build upon the view-based memory paradigm and propose an efficient framework for long-horizon spatio-temporal question answering. While existing view-based systems typically store either text captions or visual embeddings, we extend the ReMEmbR-style memory with image paths that link each stored description to its original visual content. To make the stored annotations more informative, we replace uniform sampling during memory construction with an optical-flow-based frame selection strategy (PSFR) and store an object-centric descriptive scene representation instead of plain captions. We further equip a VLM-based agent with an adaptive retrieval tool that returns the image associated with the most relevant caption, allowing the agent to decide when visual inspection is needed. On the OC-NaVQA benchmark, LVMem outperforms ReMEmbR on binary and positional metrics with both backbones and matches or exceeds a 4D scene graph DAAAM baseline on binary accuracy, while operating on a lightweight view-based memory that requires no explicit graph construction.

---


### 38. [PORA: Learning When More Reasoning Pays Off for LLM Agents](https://arxiv.org/abs/2610.27119)

**<font color=#1a73e8>作者：</font>** Bo Yan, Qi Zhang, Zhen Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents perform tasks over multiple steps and revise their actions based on feedback. As the total reasoning budget is often limited and must support future steps, the agent must choose between short and long reasoning before each action. Longer reasoning may improve the final task outcome by preventing later errors, but it also uses budget capacity that may be needed for future decisions. This creates two challenges: estimating the downstream value of long reasoning and deciding when that value is worth using the remaining budget. We propose Paired Outcome-guided Reasoning Allocation (PORA), which learns this decision by comparing short and long reasoning from the same interaction state. During training, \method{} completes the task twice from each selected state, once with a short reasoning allowance and once with a long allowance, and compares their final quality and total processing to estimate when longer reasoning is valuable. During inference, a controller weighs this estimate against learned prices on remaining-budget pressure and chooses either short or long reasoning without running both alternatives. We evaluate PORA across application, memory, code, retail, and mathematics tasks, achieving strong results across all settings. On BFCL memory, it exceeds the strongest existing method by 17.4--32.9 percentage points. Within the same agent, it matches or exceeds always using long reasoning on code and mathematics with 50.6% fewer actor tokens and 31.2% fewer model requests, respectively.

---


### 39. [EDMA: Entropy-Driven Multimodal Answering](https://arxiv.org/abs/2610.27120)

**<font color=#1a73e8>作者：</font>** Emanuele Mezzi, Gertjan Burghouts, Fabio Massacci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal question answering (MMQA) is based on integrating heterogeneous data sources, selectively leveraging relevant modalities, and ignoring distractors. Existing approaches based on Multimodal Large Language Models (MLLMs) improve performance by splitting the task into intermediate steps, but do not quantify how each modality contributes to reaching the final answer. We argue that quantifying the effect that each modality has on the answering process improves process traceability and final performance. Thus, we propose Entropy-Driven Multimodal Answering (EDMA), which uses logical entropy to formalise multimodal QA as an iterative process of entropy reduction and to quantify the contribution of each modality in distinguishing correct from incorrect candidate answers. This enables the construction of quantifiable answering trajectories, where each step is associated with a measurable entropy reduction. EDMA introduces (i) modality-conditioned partitioning to estimate unimodal entropy reduction, (ii) entropy-driven multimodal fusion to capture complementary information across modalities, and (iii) entropy-based selection of the answering trajectory that minimises the most logical entropy. Evaluated across standard MMQA benchmarks, EDMA outperforms competitive prompting baselines, with average gains of 12.8 F1 and 4.6 LLM-J points over Planning Prompting and 18.6 F1 and 8.3 LLM-J points over Chain-of-Thought. Moreover, EDMA outperforms self-consistency baselines and is competitive with the multi-agent system baseline. Moreover, we show that higher entropy correlates with more false positives and, through controlled trajectory selection, demonstrate that logical entropy serves as an effective, monotonic selector for correct reasoning paths, validating entropy level as a reliable proxy for performance.

---


### 40. [Reconstruction-Optimized Expert Pruning for Mixture-of-Experts Language Models](https://arxiv.org/abs/2610.27123)

**<font color=#1a73e8>作者：</font>** Jelena Markovic-Voronov, Petros Prastakos, Kayhan Behdin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models reduce computation through sparse expert activation, but deployment still requires storing a large number of expert parameters. We study post-training expert pruning using task-domain calibration data as a subset-selection problem: given a pretrained MoE layer, select a fixed number of experts that best reconstruct its original output. Exact subset search is combinatorial and becomes intractable for modern MoE models with many experts per layer. We develop OptEP, a scalable continuous relaxation that directly optimizes differentiable expert-selection variables, followed by a lightweight reconstruction-based update of the retained expert weights. Across multiple MoE architectures and tasks spanning mathematical reasoning and code generation, our approach improves over the strongest existing expert-pruning baselines, with absolute accuracy gains of up to 15.05% on Qwen3-30B-A3B, 14.55% on Qwen3-235B-A22B, 11.06% on GLM-4.5-Air, and 16.20% on Mixtral-8x7B. The improvements are particularly pronounced under aggressive pruning, demonstrating that reconstruction-driven expert selection and weight adaptation can preserve substantially more of the original model's performance while reducing the number of retained experts.

---


### 41. [ICLHerd: Herding-Based Data Selection for LLMs with In-Context Learning as a Proxy](https://arxiv.org/abs/2610.27142)

**<font color=#1a73e8>作者：</font>** Yuqiao Wen, Lili Mou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data selection plays a central role in modern large language model training, as the quality of training data strongly influences downstream performance. A common approach is to curate a development set that encodes the desired skills (e.g., reasoning or multilinguality) and select data that are similar to them. Existing methods compute similarity using cosine distance over either the model's hidden states or gradients. However, we observe that this max-similarity strategy induces a mode-seeking bias: the selected data clusters tightly around the development samples. To address this, we propose ICLHerd, a data selection framework that leverages the von Mises-Fisher kernel to balance mode-seeking with mode-averaging. We further introduce in-context learning as a validation proxy, enabling efficient hyperparameter search over the balance trade-off. Results show that ICLHerd outperforms existing LLM data selection algorithms, highlighting the importance of balancing mode-seeking and mode-averaging.

---


### 42. [Who Takes the Lead? Model Ability and Task-Conditioned Collaboration with Humans](https://arxiv.org/abs/2610.27148)

**<font color=#1a73e8>作者：</font>** Weien Li, Haochen Liu, Zeyu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As language-model agents grow more capable, they can carry more of a task without asking anyone for help. Falling reliance on a human partner is easy to read as a failure of collaboration when it may instead be a correct division of labor, and the rate of human involvement alone cannot tell the two apart. We study this systematically by placing an agent and a person under a shared objective while varying who holds the advantage: the human has a clear advantage, neither does, or the agent does. To obtain this control, we introduce a shared-control maze, in which an agent-controlled and a human-controlled avatar share the objective of reaching a common target in as few team turns as possible. The agent allocates each team turn between acting itself and handing the move to the person, and initial placement sets the human's shortest-path advantage while the task is otherwise unchanged. We evaluate GPT~5.6~Sol, Command~A+, Qwen~3.8~27B, and Command~R, first measuring solo capability with a single avatar and full-map observability, then running co-play with human participants across the three advantage conditions. Across the four models, stronger solo performance is associated with selective, route-conditioned human involvement: the models that solve the maze reliably on their own act for themselves almost without exception when the human holds no advantage, and involve the human on roughly $80\%$ of initial decisions when the human route is shorter. Command R, the model with substantially weaker solo performance, shows no such selectivity.

---


### 43. [On the Fragility of Tasks under Composition: Implicit Budgeting in Language Models](https://arxiv.org/abs/2610.27190)

**<font color=#1a73e8>作者：</font>** Chenpan Li, Thies Brockmoeller, Stefanie Jegelka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern language models are increasingly asked to handle several tasks within a single prompt. Doing so requires solving each task correctly while integrating the resulting answers into a coherent response. In this paper, we identify a fundamental limitation in this process, where models make substantially more errors when tasks are composed, even when they can solve every constituent task reliably in isolation. This degradation cannot be fully explained by the accumulation of independent errors. Across both open-weight models and the frontier model Claude Opus 5, our findings instead point to an implicit thinking budget underlying this effect. In particular, under composition, models use substantially fewer tokens per task than in isolation, even when the full sequence remains well within the context window. Tasks that require longer solution traces in isolation are consequently more $\textit{fragile}$ under composition, i.e., models make more errors on prompts containing these tasks. In isolation, non-fragile tasks receive more reasoning than they need and waste compute. However, by grouping tasks according to their fragility, the implicit budgeting can be manipulated to reduce token usage by $43$\% across a range of math and linguistic tasks while also preserving accuracy.

---


### 44. [CARLAR Influence: A Structured Hallucination Risk in Multimodal Cheque Extraction and an Exploratory Compressed-Image Countermeasure](https://arxiv.org/abs/2610.27192)

**<font color=#1a73e8>作者：</font>** Joong Ho, Choi, Aditya Paul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (LLMs) are increasingly used for structured extraction from financial documents, but their behavior under visual ambiguity is poorly understood. We study CARLAR (Courtesy Amount Recognition and Legal Amount Recognition) influence: a model returns the same amount for both cheque fields even though their annotations differ, including cases with a blank annotation encoded as zero. Across ten visual prompting conditions, we evaluate GPT-4.1 and Claude 4.5 Sonnet on 243 primary cheques (124 with two observed unequal amounts) and 598 strict mismatches from two additional datasets. Under courtesy redaction, GPT-4.1 CARLAR reaches 73.7 percent (95 percent bootstrap interval: 68.3 to 79.0; p below 0.001 versus baseline). Model-reported confidence can remain high when predictions agree; expected calibration error reaches 0.93 among CARLAR cases. We also test a compressed-image few-shot intervention that presents examples as one visual table without model fine-tuning. On the 243-case cohort, Claude's Control condition increases paired joint extraction accuracy by 11.5 percentage points (95 percent interval: 6.2 to 16.9; adjusted p = 0.00054), but its strict-124 gain is smaller and not significant after correction. The intervention's effect on predicted-field agreement is model-dependent: it decreases for Claude and increases for GPT-4.1. These results motivate validation methods that account for visual context and dependencies between extracted fields.

---


### 45. [Preference-Aware Pareto Steering for Multi-Task Speech LLMs](https://arxiv.org/abs/2610.27200)

**<font color=#1a73e8>作者：</font>** Liuyuan Jiang, Vishal Sunder, Samuel Thomas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech large language models (LLMs) perform multiple tasks, including automatic speech recognition (ASR), timestamp prediction (TS), and speech translation (ST). Joint training of speech LLMs creates task trade-offs, yet standard training with fixed loss weights does not generally control the resulting trade-off according to deployment preferences. To address this, we propose Endpoint-Anchored Preference-Aware Sampling Uniformly along the Pareto Front (EA-SURF), an a priori method that adapts scalarization weights so that the resulting task trade-off reflects the desired preference. EA-SURF retains the standard weighted-loss training pipeline, tracking the current model's performance relative to each task-specific reference and adapting the scalarization weights as training proceeds. We theoretically show that EA-SURF can match a desired preference, with the update becoming stationary at the target under checkable regularity conditions. Across six three-objective speech LLM requests, EA-SURF empirically converges toward the requested targets and increases endpoint-inclusive normalized hypervolume by 17.8% over fixed loss weighting.

---


### 46. [The Culture Within: Towards Mechanistic Understanding of Cultural Reasoning in LLMs](https://arxiv.org/abs/2610.27202)

**<font color=#1a73e8>作者：</font>** Samee Arif, Furkan Danisman, Angana Borah 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly operate across culturally diverse settings, yet existing evaluations largely measure cultural behavior at the output level. We introduce CultureLens, a reference-grounded benchmark and mechanistic study of how LLMs use cultural information. CultureLens contains 9,261 scenarios across 75 countries and systematically varies country, value, true-norm, and contradictory-norm evidence. Across Llama-3.1-8B, Gemma-3-12B, and Qwen-3.5-27B, stating a contradictory norm lowers aligned answers by 32-47 percentage points, even when the model answers correctly from the country alone. Mechanistically, models default to Anglophone norms when no country is given. The failure under a contradictory norm is not one of missing knowledge, as blocking the norm inside the model restores the correct answer in most cases. Models accept a stated norm according to how it is presented and not whether it is true, which leaves them most exposed to errors in retrieved content. Supervised fine-tuning with contradictory-norm examples raises aligned answers under a contradictory norm to 85-93%, including on unseen countries, at a small cost under a true norm.

---


### 47. [Language Guidance for Supervised Vision Training: An Empirical Study of Generalization](https://arxiv.org/abs/2610.27208)

**<font color=#1a73e8>作者：</font>** Shruthi Gowda, Nikita Jain, Elahe Arani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks have achieved remarkable success on vision benchmarks, yet they continue to struggle with many generalization challenges. Supervised vision training relies on one-hot labels, which provide limited information about semantic structure and shared attributes between classes. This limited supervision can leave visual representations vulnerable to distribution shifts, spurious correlations, texture bias, adversarial perturbations, and forgetting in sequential learning settings. We study whether pretrained language models can serve as lightweight auxiliary supervision for vision training without requiring paired image-text data, prompt engineering, or contrastive objectives. Specifically, we evaluate two forms of language guidance, Explicit Language Guidance (ExLG) and Implicit Language Guidance (ImLG). We conduct a comprehensive evaluation across six generalization regimes, including in-distribution, out-of-distribution generalization, shortcut and spurious correlation resistance, texture and shape bias, adversarial robustness, and continual learning. Our analyses show that the two mechanisms have complementary strengths, with explicit guidance consistently benefiting in-distribution, low-data performance, and continual learning retention, while implicit guidance is often more useful in shortcut-sensitive settings and under stronger adversarial perturbations. Importantly, both are lightweight and add minimal parameters and training overhead. The analyses characterize when language-derived structure helps supervised vision training and provides a practical roadmap for using off-the-shelf pretrained models from another modality as auxiliary supervision.

---


### 48. [A Theoretical Analysis of Environment-Aware Out-of-Distribution Detection for Vision-Language Models](https://arxiv.org/abs/2610.27211)

**<font color=#1a73e8>作者：</font>** Salimeh Sekeh, Mary Wisell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual vision-language models (VLMs) encounter a stream of environments and must also reject inputs that do not belong to the environment at hand.
Class information from earlier environments can aid out-of-distribution (OOD) detection, yet existing detectors score each environment in isolation, and when previous environments help or hurt is theoretically unclear. We develop a theory of environment-aware OOD detection built on contribution scores, pairwise cosine expectations measuring how the image and text features of one environment align with those of another. We propose a cross-environment maximum-concept-matching (MCM) score with two terms: a primary term matching the test image against the current class texts, and a secondary term matching it against the class texts of a previous environment, weighted by the intra-modal alignment between the two environments. We prove that, under a positive environment transition and a bounded class-matching margin for OOD inputs, this score attains a false-positive rate no larger than that of the standard MCM detector at an adjusted threshold. We then show that the score gap of an MCM detector between two environments equals the self-contribution of the in-distribution environment minus its cross-modal contribution into the OOD environment, which separates soft OOD environments, with explicit AUROC, true-positive, and false-positive guarantees, from hard ones, which no threshold that retains the in-distribution data can reliably reject. For cascaded detection, in which the text prototypes of all seen environments are pooled, the false-positive rate on every past environment is non-decreasing in time, and we characterize when detection provably fails. A contribution balance factor applied to the gradients of the classification loss and of a smoothed false-positive rate completes the framework.

---


### 49. [Profile-DP: Differential Privacy for User-Controlled Profile Release in Personalized LLM Inference](https://arxiv.org/abs/2610.27213)

**<font color=#1a73e8>作者：</font>** Mingchen Li, Zifan Peng, Kewei Sha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Personalized large language models (LLMs) increasingly rely on profile-conditioned inference, pairing public requests with rich, user-specific facts. This paradigm exposes the user profile itself, together with the user's explicit sharing preferences. We introduce Profile-DP, a policy-aware local differential privacy framework designed specifically for user-profile release in personalized LLM inference. Profile-DP provably bounds the release of user-withheld facts while treating public instructions, profile schemas, and authorized facts as public side information. By generating a privatized profile that composes with the public instruction prior to answer generation, our framework decouples formal privacy guarantees from downstream model behavior. We develop two finite-domain mechanisms satisfying Profile-DP: DP-SLOT independently perturbs protected attributes, while DP-BLOCK uses public semantic decisions to coordinate their release and jointly sample related attributes. A positive, public compatibility prior connects these attributes while preserving a profile-level privacy bound. On PEEP, DP-BLOCK leads the utility composite among DP methods at all 13 structured budgets and is closest to the ideal privacy--utility point in 18 of 26 format--budget settings under our composite weighting. Direct measurements reveal complementary strengths: DP-BLOCK discloses less, while DP-SLOT retains more authorized facts. These results make policy-aware profile release a practical basis for studying privacy and personalization.

---


### 50. [Sparse RL Relaxation for LLM Reasoning](https://arxiv.org/abs/2610.27220)

**<font color=#1a73e8>作者：</font>** Jiabin Fan, Matthias Lindemann, Zita Marinho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has explored continuous representations in place of discrete tokens during Chain-of-Thought (CoT) reasoning, often referred to as soft CoT. This is motivated by the idea that a mixture of token embeddings can represent a superposition of multiple reasoning possibilities within a single step. However, it remains challenging to train large language models to realize this potential. Existing work has explored reinforcement learning (RL)-style training for soft CoT. However, these approaches treat soft tokens as actions in a Markov decision process rather than as differentiable intermediate computation steps. Thus, they do not propagate gradients across the soft tokens and miss out on the signal of how the choice of one soft token affects the next. In this paper, we propose a sparse relaxation method for RL (called SpaRLax), which leverages the differentiability of soft-CoT reasoning over time steps and makes training more stable and effective. We adopt an entmax sparsity method that adaptively determines the degree of softness, which truncates long-tail noise at confident steps while retaining multiple plausible candidates when uncertain. Across nine reasoning benchmarks, our method achieves the highest average performance compared with baseline methods. Further analyses validate the effective use of soft-token superposition in our approach, and also demonstrate the contribution of adaptive sparsity in our approach.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
