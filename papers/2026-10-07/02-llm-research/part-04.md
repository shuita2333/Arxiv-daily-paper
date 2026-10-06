# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

---

### 151. [Understanding Errors in LLM-Based Question Answering over Imperfect Tables](https://arxiv.org/abs/2610.04687)

**<font color=#1a73e8>作者：</font>** Baowen Zhang, Wei Fan, Ruman Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate error discovery and handling in question answering over imperfect tables through controlled studies across three large language models (LLMs) on human-reviewed RADAR-T examples. Answering questions over these tables requires handling errors that can affect the answer. We vary row order and compare original, error-marked, and repaired tables to test whether discovery depends on where errors appear and whether providing their locations is sufficient for accurate question answering. First, reordering rows changes error discovery even when the table contents and gold answer remain unchanged. Complete discovery is higher for back than front placements and, averaged over the tested mean positions, for compact than widely spaced layouts. Second, providing verified error locations alone is insufficient for accurate QA, leaving a substantial accuracy gap between error-marked and repaired tables. Providing tables with human-reviewed repairs already applied raises code-assisted QA accuracy by 39.0-59.1 percentage points over the error-marked tables across the three systems. GBDI, a simple workflow, puts these findings into practice by combining error discovery across shuffled table views with explicit guidance for verifying and handling the reported errors. On RADAR-T, GBDI raises observed QA accuracy by 3.8-18.5 percentage points over a code-agent baseline across five systems. These results highlight the importance of both reliable error discovery and effective error handling in question answering over imperfect tables. Our anonymous repository is available at this https URL

---


### 152. [RAGStress: A controlled benchmark for evaluating retrieval-augmented generation under knowledge-base degradation](https://arxiv.org/abs/2610.04691)

**<font color=#1a73e8>作者：</font>** Shiqi Yang, Jiekai Ma, Gaoyuan Du  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is typically evaluated under the implicit assumption that the underlying knowledge base (KB) is clean, leaving the behaviour of RAG systems under realistic KB degradation poorly characterised. We introduce RAGStress, a controlled evaluation benchmark for stress-testing RAG systems under systematic KB corruption. The benchmark pairs four naturalistic corruption types (factual corruption, numeric typo, relevance poisoning, and contradiction injection) with three severity levels (subtle, moderate, and obvious) over a single-KB, metadata-filtered experimental design built from 57 MMLU subjects and 182,546 documents. Across 52,500 model-question-condition evaluations, RAGStress reveals that clean retrieval can mask robustness differences, semantic-fidelity corruptions are substantially more harmful than signal-utility perturbations, no-retrieval accuracy does not predict corrupted-retrieval robustness, and mixed-KB accuracy should not be treated as worst-case robustness. We document the benchmark's intended use, supported claims, and limitations, and provide an artifact bundle including generation scripts, corruption prompts, metadata schema, and evaluation code. RAGStress is intended as a controlled stress test for RAG robustness under KB corruption, not as a general model leaderboard.

---


### 153. [Not Self-Decidable: LLMs Cannot Draw the Boundary of What an Agent Verifier Can Check](https://arxiv.org/abs/2610.04699)

**<font color=#1a73e8>作者：</font>** Anthony Rhodes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A verifier for an agent faces rules of two kinds: the ones a fixed check can settle and the ones that require a judge. A team that derives its own checks fixes that split up front. Where the requirements come from outside, as in finance, healthcare and law, the agent enforces rules it did not write, so the split falls to runtime, recurring for every predicate of every rule on every action at a rate no reviewer can audit. Every escalation scheme assumes a model can make that decision itself, that it is self-decidable. Across six corpora, including the EU AI Act, FINRA guidance and a deployed credit agent, we collect roughly 22,000 labels from four models built by three labs. They agree almost perfectly where the answer is obvious and collapse on regulatory text; their errors run in opposite directions, so no model can be trusted as the conservative choice; and on the deployed agent's own rule-set they err together, over-claiming that a fixed check will do, the direction that never gets escalated. We introduce CoVer (corroborate-then-verify), which treats unanimity as a nomination, admitting a predicate only when the check synthesized for it survives intervention, reading fields the agent cannot write and holding under deterministic rewording. That gate rejects most of what corroboration wrongly admits, at a cost in coverage we report rather than tune away. The obvious alternative, agreement with a reference judge, certifies nothing: it climbs from 30% to 77% across calibration bands while the genuinely decidable share does not move, because a judge drawn from the population under indictment ratifies the blind spot it shares. Self-decidability is not a capability to elicit from a model but a boundary the verifier must construct.

---


### 154. [Organising Trajectory Evidence for Language-Model Agent Assurance: Fragments, Methods, and the Residual](https://arxiv.org/abs/2610.04710)

**<font color=#1a73e8>作者：</font>** Xiaowei Huang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Methods for assessing language-model agents include rule checkers over logs, analyses of skill coverage and composition, support checkers, prefix monitors, execution gates, and rare-event estimators. Each observes a different part of a run and makes a claim of a different strength, and no common account says how these claims combine or what they leave unchecked. We give one, built from a logic, information fragments, and an assurance ledger. Requirements are formulas of a two-tier logic: an outer finite-trace temporal logic over recorded events, and an inner logic of standing over the argument structure that the agent's recorded context supports at a decision. A rule violation and an action taken on withdrawn support are thus formulas of one language. The information available to an assessor, to the agent, and to an execution gate defines fragments of that language; each checking method decides one fragment and returns a typed claim: exact, on a named test suite, a risk bound, or descriptive. The ledger merges the evidence and classifies every obligation as established, addressed but not established, or unaddressed. On 456 released $\tau^2$-bench telecom trajectories, the benchmark oracle flags 231 runs; adding a rule checker, a support stand-in, and a prefix-monitor baseline raises the union to 391, 401, and 407, each contributing flags the others miss, and a gate makes one prohibition exact on a gated deployment. The 49 unflagged runs and the unmet or unaddressed obligations form the residual. Discovery makes unknown requirements explicit, and new or stronger checkers then reduce it.

---


### 155. [Learning to Clarify Underspecified Intents Under Limited Interaction](https://arxiv.org/abs/2610.04719)

**<font color=#1a73e8>作者：</font>** Pranav M R, Manuel Cherep, Pattie Maes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI assistants receive requests that leave out information needed for a good outcome, for example about users' preferences or goals. They must then either speculate or ask for more information before proceeding. We reconceptualize this as a value-of-information problem: the assistant should acquire information whose absence causes the greatest avoidable loss in user utility. This is rarely known ex ante; rather, assistants must predict it in order to optimally allocate limited user interactions. We instantiate this problem in image generation and derive a reinforcement learning framework using multi-turn simulated users to maximize utility recovery under uncertainty. In a preregistered study with 456 interactive sessions across 76 human participants, this helped users significantly better match reference images with significantly fewer questions, less total interaction time, and lower cost. This points toward a simple and scalable framework for training language model assistants to better disambiguate user intent by asking more informative questions.

---


### 156. [WNet: Discrete Wavelets Transform for Efficient Token Mixing](https://arxiv.org/abs/2610.04720)

**<font color=#1a73e8>作者：</font>** Rana Aref Salama, Abdou Youssef, Mona Diab  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In a Transformer, token mixing is the step that lets each token draw information from other tokens, and it dominates the cost of encoding long sequences. Self-attention does this mixing very well: every token weighs every other token by content, which gives strong contextual modeling. That all-pairs comparison is also why its cost grows quadratically with sequence length. We introduce WNet, a Transformer encoder that replaces self-attention with token mixing based on the discrete wavelet transform (DWT). Three attention-free mixers recombine the scales: by linear fusion, by learned gating, or by letting each token choose its scales. A hybrid adds self-attention in the last layer only. A receptive-field analysis shows that wavelet mixers built from two-tap filters, such as Haar, never relate tokens outside fixed blocks, however deep the network, even when the filters are learned. Longer filters reach the whole sequence within two layers. We pre-train every model with masked language modeling on a fixed-token subset of C4 and fine-tune on GLUE, using one controlled setup with size-matched BERT and FNet baselines and a control that cannot mix tokens. The token-gated mixer trains as fast as attention at 256 tokens and 2.7 times faster at 4,096.

---


### 157. [Knossos and Ariadne: Benchmarking and Learning Complete Diagram Topology Extraction with Vision-Language Models](https://arxiv.org/abs/2610.04721)

**<font color=#1a73e8>作者：</font>** Bangwei Guo, Xujiang Zhao, Shengyu Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structural diagrams are widely used to represent complex systems and relational information across scientific, engineering, procedural, and spatial domains. Recent vision-language models (VLMs) have become increasingly capable of recognizing diagram elements and reasoning about their content, while complete diagram topology extraction remains comparatively underexplored. In this paper, we study diagram-to-graph topology extraction: extracting all diagram entities and the complete relations among them. To enable large-scale supervised training and systematic evaluation of this task, we introduce Knossos, a benchmark of 19,200 diagrams across six diverse domains, with 245,179 nodes and 439,740 edges. Its symbolic generation process provides exact alignment between rendered diagrams and annotations of complete topology, relation types, and connector geometry. To address the modeling challenge of complete topology extraction, we also present Ariadne, a structured framework that decomposes the task into node inventory extraction and source-conditioned edge prediction. Extensive experiments show that training on Knossos substantially improves complete topology extraction in smaller open-source VLMs. Ariadne further improves over one-step extraction under matched supervision, demonstrating the additional benefit of structured decomposition. It achieves the highest average Edge F1 among the evaluated methods on Knossos, while both backbone variants also improve over their unadapted counterparts on the real-world external benchmark. Code and benchmark are available at this https URL.

---


### 158. [Verb-ICL: Rethinking In-Context Learning for Structured Prediction](https://arxiv.org/abs/2610.04725)

**<font color=#1a73e8>作者：</font>** Fan Bai, Hengshuo Miao, Sanjit S Batra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured prediction tasks pose unique challenges for in-context learning (ICL): their compositional outputs require modeling fine-grained, token-level patterns that sentence-level approaches fail to capture, and their task-specific annotation conventions are human-defined artifacts that cannot be acquired through pretraining alone. We propose Verb-ICL, a selective annotation framework for ICL-based structured prediction that addresses both challenges. Verb-ICL first selects representative examples using a token-level coverage strategy that captures local semantic patterns critical for structured prediction, then generates actionable error feedback that codifies task-specific annotation guidelines and incorporates this feedback into ICL demonstrations. We evaluate Verb-ICL on six structured prediction datasets spanning information extraction and semantic parsing. Experiments with recent LLMs show that Verb-ICL consistently outperforms strong selective annotation baselines under low-resource settings and continues to provide gains as the annotation budget increases. Extended analyses demonstrate that the generated feedback is predominantly useful across a four-category quality taxonomy, generalizes as task-level guidance beyond instance-specific corrections, and improves performance regardless of the underlying selection strategy.

---


### 159. [PyINE: A Framework for Scalable Elicitation and Oversight via Code Execution](https://arxiv.org/abs/2610.04737)

**<font color=#1a73e8>作者：</font>** Pierre-Luc St-Charles, Alessandro Palmas, Damiano Fornasiere 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models can remain capable of solving a task while still defaulting to cheaper but misleading shortcuts. This creates a central oversight problem: when a model gives an answer with plausible but incomplete reasoning, can an overseer determine whether that output should be trusted? To study this problem, we introduce PyINE, a framework for scalable elicitation and oversight using instrumented Python programs as a verifiable execution substrate. In PyINE, programs define task environments, execution traces provide authoritative labels for outcomes and intermediate facts, and task variants can be generated mechanically rather than through static human annotation. We instantiate the framework in PyINE-v1, a first release built from nearly one million deterministic execution traces and over 500,000 matched LLM-generated code variants used for counterfactual evaluation. Using standard RL with verifiable rewards on cue-varied tasks, we train a shortcut-following model that improves substantially at predicting execution outcomes while still making systematic errors when misleading human-facing cues conflict with the program's realized behavior. We then evaluate activation probes, trained text classifiers, prompted judges, and a lightweight debate protocol as overseers of this model. We find that performance pooled at the dataset level can hide weak coverage of the failures that matter most: cheap learned overseers often miss rare shortcut-driven errors, while stronger model-based checks are more balanced but substantially costlier and harder to turn into reliable thresholded decisions. PyINE-v1 turns this failure-mode coverage problem into a reusable experimental setting for developing oversight methods that are verifiable, failure-mode-aware, and cost-sensitive.

---


### 160. [Toward a Locally Deployable Agentic Co-Scientist: Small-Model Planning for Early-Stage Drug Discovery](https://arxiv.org/abs/2610.04740)

**<font color=#1a73e8>作者：</font>** Tian Liang, Jiayu Chang, Alejandro F. Frangi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early-stage computational drug discovery requires coordinating heterogeneous scientific tools across multi-step workflows. We present a lightweight, tool-augmented framework in which a locally deployable compact language model plans calls to 18 modular tools. A Unified Molecular Schema maintains shared molecular records, while a plug-in interface supports tool replacement and extension. We construct 1,263 manually refined query-plan pairs through workflow-graph path coverage and apply LoRA fine-tuning to three compact model families. Under the query-level split, all fine-tuned models generate fully parseable and schema-compliant plans on 47 held-out cross-group queries. Llama 3.2-3B achieves a tool-selection F1 of 0.998, sequence exact match of 0.979, and argument F1 of 0.960. Under the stricter workflow-grouped split, which excludes identical ordered tool sequences across partitions, sequence exact match reaches 0.452 to 0.548, highlighting the remaining difficulty for compact models in generating complete workflow paths unseen during training. These results demonstrate the feasibility of compact, locally deployable planning while identifying compositional generalization as an important direction for further improvement.

---


### 161. [Agentic discovery of blood biomarker from distilled private health records](https://arxiv.org/abs/2610.04749)

**<font color=#1a73e8>作者：</font>** Seffi Cohen, Liat Antwarg Friedman, Amir Anisman 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Routine complete blood counts (CBCs) could yield new biomarkers, but the private records needed to evaluate candidates cannot be shared with frontier language model agents that excel at discovery. We distilled the evidence held in the Clalit Health Services panel of over 5.4 million patients into a released scoring tool: for each of 13 immune-mediated diseases, a graph attention network was trained inside the data boundary to predict the case-control AUC of candidate CBC expressions, and only the trained weights were released. The tool grounds an agent's propose-score-refine loop in real-world data without exposing any patient data. In external validation, agent-discovered expressions improved on their literature-seeded starting points by a median of 4.18 AUC percentage points, and across three independent cohorts, reranking the candidates of three frontier research tools improved on their first choices in most comparisons, with gains that varied by cohort. The released scorer supports privacy-preserving biomarker hypothesis generation.

---


### 162. [Dynamic Routing as a New Dimension for Test-time Versatility of LLMs](https://arxiv.org/abs/2610.04751)

**<font color=#1a73e8>作者：</font>** Michal Štefánik, Marek Kadlčík, Josef Kuchař 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Beyond scaling their parameters and data, large language models currently gain versatility on new problems along a single axis: the tokens they spend on chain-of-thought (CoT). We investigate whether dynamic routing programs, which execute a subset of the model's layers or iterate some of them, can open a second axis of test-time adaptation, complementary to CoT and free of any gradient update. Prior work showed that such programs exist and bring accuracy and efficiency gains on problems similar to those they were trained on; we ask whether they can also be identified rapidly, from a handful of demonstrations (3 or 10), by a strategy that transfers across models and tasks without training. First, we find that strategies that select programs by the probability they assign to the demonstrations' labels, arbitrated by the model's own confidence, bring consistent gains: on average over the 49 tasks of MMLU and substantially on four of seven models, and most of all on far out-of-distribution tasks such as ARC-AGI, where programs double the accuracy of a 7B model whose CoT fails. Second, on MMLU across the seven post-trained models, routing complements CoT in practice: the two succeed on different queries, and their composition exceeds CoT alone. Despite these gains, our analyses show that confidence-based selection leaves much of the potential untapped, in two places in particular: (1) in surfacing the routing potential that is already present early in pre-training but becomes harder to select after post-training, and (2) in making models robust to the refinements routing introduces, since unsuccessful routes tend to drive the residual stream out of the distribution that the following layers expect. Together, our results point to dynamic routing as a paradigm for extending the plasticity of existing and future LLMs in rapid test-time adaptation.

---


### 163. [More Value per Key: Asymmetric Sparse Attention for Faster LLM Decoding](https://arxiv.org/abs/2610.04753)

**<font color=#1a73e8>作者：</font>** Noam Elata, Itay Lamprecht, Mikey Shechter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> utoregressive generation in Large Language Models (LLMs) is constrained by the memory and computational demands of attention mechanisms. Sparse attention methods mitigate this cost by selecting only high-probability entries of the attention matrix. We observe that in many such methods, this renders the probability-value multiplication negligible, shifting the bottleneck to the query-key step. Key heads can therefore be reduced to accelerate inference, while retaining more value heads preserves capacity with limited additional decoding cost. We introduce Sparse Asymmetric Group-Query Attention (SAGA), which decouples key and value head counts to exploit this principle, and pair it with approximate top-N (Atop-N) attention, a simple sparse attention method designed to study the interaction between sparsity and head-count asymmetry. We formalize the benefits of this asymmetry theoretically and validate them empirically through latency measurements and quality evaluations on models up to 1.5B parameters. Together, SAGA and Atop-N achieve end-to-end decoding speedups exceeding $2\times$ over our full-attention GQA baseline at long contexts. Models trained from scratch with SAGA nearly match the quality of comparable GQA variants on the evaluated benchmarks. To facilitate adoption, we introduce an efficient fine-tuning method that converts pretrained models to the SAGA architecture, enabling practitioners to benefit from our approach without costly retraining.

---


### 164. [When Is Enough Enough in Self-Evolving LLM Systems?](https://arxiv.org/abs/2610.04756)

**<font color=#1a73e8>作者：</font>** Enoch Yin, Bin Liu, Zhengling Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving large language model (LLM) systems repeatedly propose, evaluate, and incorporate updates to prompts, skills, or other persistent artifacts. Despite their growing effectiveness, these systems typically operate under a predetermined iteration or compute budget, without a principled criterion to determine when further evolution is no longer worthwhile. This can lead to two undesirable consequences: unnecessary computation after performance has saturated and the risk of returning late updates that overfit or exploit the evaluation signal. These issues motivate us to study two fundamental questions: when should a self-evolving system stop, and what should it output once it stops? We address the first by formulating an online sequential testing problem and constructing an anytime-valid restart detector using the per-item paired evaluation outcomes already produced by self-evolving LLM systems. We address the second by formulating a change-point estimation problem and using the estimated transition to select an earlier artifact for output. The resulting procedure is plug-and-play and requires no modification of the underlying self-evolving algorithms. Across two self-evolving frameworks, three LLM model families, and five benchmarks, our method substantially reduces computation costs while maintaining comparable unseen-test performance. For example, on SearchQA with SkillOpt and DeepSeek V4 Flash, our method stops at round 4 rather than the full budget of 40, reducing token usage by 91.6% while achieving 82.43% unseen-test accuracy versus 82.00% under the full-budget run.

---


### 165. [ARISE: Adaptive Agentic Reasoning with Image-grounded Self-Evaluation for Interpretable IBD Assessment](https://arxiv.org/abs/2610.04777)

**<font color=#1a73e8>作者：</font>** Pronoma Banerjee, Anuva Shah, Jason Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inflammatory bowel disease (IBD) requires frequent imaging-based assessment, yet interpretation of modalities such as wireless capsule endoscopy (WCE) and intestinal ultrasound remains heavily dependent on specialist expertise. Vision-Language Models (VLMs) demonstrate significant potential in multimodal medical image analysis, but their clinical adoption is hindered by their insufficient domain-specific reasoning, susceptibility to hallucination, scarcity of high quality training data in fine-grained diagnostics and limited interpretability. We introduce ARISE (Adaptive Agentic Reasoning with Image-grounded Self-Evaluation), an autonomous planning framework that models few-shot medical image understanding as a sequential agentic workflow. ARISE structures agent execution into a transparent 5-stage workflow: hypothesis generation, image-grounded evidence summarization, evidence-conditioned refinement, symbolic verification, and final diagnosis. We apply ARISE to IBD assessment across two independent patient cohorts: wireless capsule endoscopy (WCE) images for Crohn's disease and B-mode ultrasound data for ulcerative colitis. ARISE consistently improves diagnostic performance over baseline VLMs while exposing where reasoning succeeds or fails, providing a more interpretable basis for clinical decision support and realistic deployment.

---


### 166. [Not All Answers Are Contextually Persuadable: Inference Dynamics in Large Language Models under Contextual Influence](https://arxiv.org/abs/2610.04791)

**<font color=#1a73e8>作者：</font>** Zongye Hu, Weiqing Luo, Yanjie Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> At the core of modern prompting techniques is contextual sensitivity, the ability of large language models to adapt their predictions based on inference-time context. Despite its central role, inference behavior under strong contextual influence remains poorly understood, particularly at the level of internal inference dynamics. We introduce a theoretical framework for analyzing contextual influence through inference dynamics, enabling quantitative characterization of inference behavior beyond output-level answer changes. Our analysis shows that inference dynamics do not exhibit unbounded drift under repeated contextual assertions. Instead, predictive representations converge to stable, query-dependent regimes that fundamentally constrain whether contextual signals can alter a model's prediction. This leads to a surprising finding: Repeated contextual assertions do not act as accumulating evidence during inference and may therefore fail to alter a model's prediction even under unbounded repetition, while in other cases a prediction change becomes inevitable. We empirically validate our theoretical predictions, demonstrating strong alignment between theory and observed inference behavior. These contributions offer a principled pathway toward characterizing the limits of contextual influence during inference, providing practical implications for model development.

---


### 167. [Do More Modalities Always Help? A Geometric Perspective on Missing-Modality Robustness](https://arxiv.org/abs/2610.04792)

**<font color=#1a73e8>作者：</font>** Songyuan Sui, Zhen Tan, Mohan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Missing modality remains a longstanding challenge in multimodal learning. Existing methods typically address this issue through modality recovery or adaptive strategies. However, they overlook models' internal cross-modal dependencies formed during multimodal training, which later impair robustness. We systematically characterize a counterintuitive deployment-time failure mode: models trained on full modalities can underperform unimodal models when one modality is missing at inference time. This pattern appears across diverse architectures, such as fusion models, CLIP-style two-tower models, and vision-language models. We show that such degradation is closely associated with learned cross-modal dependencies in the principal parameter subspaces. Multimodal training induces structured rotations of these subspaces, particularly in cross-modal interaction layers. These rotations are associated with reduced task-aligned margins and larger task-aware representation harm under missing-modality inputs. We propose Geodesic Unlearning (GU), a lightweight parameter-editing method that leverages Grassmannian subspace geometry for structured subspace correction to improve missing-modality robustness. It rotates the principal input subspace toward a unimodal reference along a geodesic path. We prove that this correction minimizes the distance to the reference within a fixed subspace-distance budget. Experiments across architectures and datasets show that GU improves performance under missing-modality inference while preserving full-modality accuracy, outperforming strong missing-modality robustness baselines. These findings support a geometric view of deployment-time missing-modality degradation and suggest localized subspace editing as a practical route for robustness correction.

---


### 168. [Pressure, Context, and Machine Self-Control: A Criminological Test of Reward Hacking in Generative AI Models](https://arxiv.org/abs/2610.04793)

**<font color=#1a73e8>作者：</font>** Murat Ozer, Isaac Kofi Nti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent incidents show that AI agents sometimes reach measured goals through unsanctioned means. This study applies self-control, general strain, anomie, neutralization and routine activity theory to reward hacking in generative AI models, and it treats the measures as behavioral analogues. Study 1 (2,310 conversations, seven models) measured delay discounting with the Kirby Monetary Choice Questionnaire and stated willingness to take shortcuts. Pressure raised the discount rate k 2.8-fold in fresh conversations but 12.6-fold when the same sentence followed a baseline answer, which indicates a response to conversational cues rather than a stable trait. Models chose a shortcut in 1 of 700 dilemmas when answering as themselves and in 64 of 700 when asked to assume human impulses, each step of pressure raised the odds by 40%, and shortcut answers contained far more techniques of neutralization (rate ratio = 146). In the preregistered Study 2, five models worked on 20 coding tasks whose tests contradicted their specifications. Two Claude models never cheated. GPT-5.6, Qwen and DeepSeek cheated in 86%, 69% and 65% of episodes and clearly disclosed the conflict in 27%, although their reasoning recognized it in 95%. GPT-5.6 had never endorsed a shortcut in Study 1. The registered effects of pressure and of an auditor cue did not survive correction for multiple testing. In exploratory analyses, two further models cheated in 69% and 100% of episodes, and one sentence stating that the specification takes priority eliminated cheating in all 280 episodes. Therefore, stated refusal does not guarantee compliant agent behavior.

---


### 169. [Knowing the Store: What a Memory Backend Must Write Down Before an Agent Can Read It](https://arxiv.org/abs/2610.04794)

**<font color=#1a73e8>作者：</font>** Ansuman Mullick, Eray Tüzün  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent with long-term memory can answer from a record it should no longer use, such as a plan the user later cancelled. We ask what a memory store must expose for an agent to know this before retrieving anything, and we score that judgment on its own, as metamemory monitoring. Readers see only a value-free summary: record counts by lifecycle state and a list of attribute names. Each of 148 questions is asked against three versions of one store that differ in one attribute, so wording cannot give the answer away. What a model adds depends on the length of that list. On the short lists the benchmark's ground truth produces (2.6 names on average), none of five language models reliably beats a cosine-similarity lookup over the names, and the three stronger ones are equivalent to it within 0.05. Under a control that fixes counts and list length, none is reliably above it and none is shown equivalent. On lists longer than the stores we tested write, padded to 60 names, the lookup loses 0.18; GPT-5.6 Luna and Sol lose 0.06 to 0.07 and lead it by 0.13 to 0.14, while the other three fall with it. The lead holds for Sol against a sibling padded to the same length and counts. Reworded to share no word with the names, the lookup loses 0.02 and one stronger reader edges 0.04 ahead. On the short lists the three stronger readers lead only where the summary counts a state without naming it, and one count feature closes that lead within a question, though not when items are pooled. The backends we tested omit or misstate this information: under FR-Bank's own metadata, GPT-4.1 mini, Haiku 4.5 and the lookup fall from 0.73, 0.82 and 0.75 to 0.60, 0.71 and 0.59. In these tests, what the store wrote down limited every reader we gave it to. All stores are synthetic; control, whether a better judgment yields a better answer, is left to a later study.

---


### 170. [Forecasting Cybersecurity Incidents Using Geopolitical Data and Large Language Models](https://arxiv.org/abs/2610.04798)

**<font color=#1a73e8>作者：</font>** Mark Fesenko, Abdullah Garra, Yaniv Harel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Predicting security incidents is a profound task critical for informing proactive defensive measures and cyber-insurance policies. Prior work tackling this problem mainly utilized structured, manually defined features based on network measurements (e.g., protocol misconfigurations). Still, despite leading to promising performance, the network-based features may fail to capture aspects related to adversaries' motives.
To fill this gap, our work leverages geopolitical data mined from public sources--which may help capture attacker motives--to forecast security incidents. Specifically, our approach relies on news articles and transcribed podcasts that are fed to large language models to automatically produce rich representations. The representations are then fed to a classifier trained to forecast future incidents based on historical ones.
Our evaluation with a large incidents dataset (>15,700 records) demonstrates substantial accuracy (71.4% ROC AUC) with geopolitical data alone. Notably, combining geopolitical data and network measurements outperforms the state-of-the-art technique based on network features alone (81.3% vs.77.5% ROC AUC). Our analysis also helps shed light on when geopolitical data is most helpful and the data sources that are most useful for accurate forecasting.

---


### 171. [Agent Behavior as Code: Efficient and Robust LLM Agents with Programmatic Specifications](https://arxiv.org/abs/2610.04824)

**<font color=#1a73e8>作者：</font>** Peng Qi, Chunliang Lyu, Gang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents based on foundation models (FMs) have demonstrated strong capabilities to perform complex open-ended tasks. However, they face some common challenges in practice: (a) agent behavior can deviate drastically even for semantically similar tasks, leading to catastrophically propagated errors; (b) high cost and latency due to FM calls, repeated in full whenever a task recurs with different inputs; (c) FMs' limited context and instruction following capability confine how well agents manage the ever-growing execution context and follow complex plans. We introduce $\textbf{A}$gent $\textbf{B}$ehavior as $\textbf{C}$ode $\textbf{Agent}$ (ABCAgent), which uses a symbolic program (e.g., Python code with potential neural functions) to fully specify the agent's behavior at runtime, with a powerful FM agent editing that program for flexibility. Behavior is thus specified without premature variable binding, and its execution is deterministic. We evaluate ABCAgent on six agent benchmarks, two of which we construct to test how well a derived program generalizes to variants of the task it was written for. ABCAgent matches a model-matched neural agent on GAIA and augmented GAIA, and surpasses it where robustness and long control flows matter: 98.3% against 97.3% on GSM-Symbolic ($p = 0.001$), 71.9% against 47.4% $\mathrm{Pass}^4$ on the telecom domain of $\tau^2$-bench ($p = 0.0001$), and more records written correctly at every loop length on our control-flow-augmented WorkArena benchmark. For more parametric task families, ABCAgent is also significantly superior in efficiency. Without authoring a new program, ABCAgent solves 92.6% of GSM-Symbolic instances and 20.1% of augmented GAIA variants, which yields $5.2\times$ lower latency and $7.0\times$ lower cost on GSM-Symbolic, 19% lower cost on augmented GAIA, and $9.5\times$ lower agent latency on $\tau^2$-telecom.

---


### 172. [DICE: Decoupling Capability from Intervention Necessity in LLM Tutoring](https://arxiv.org/abs/2610.04825)

**<font color=#1a73e8>作者：</font>** Sayantan Pal, Kaiyi Ji, Rohini K. Srihari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fluent guidance is not the same as useful intervention. LLM tutors are typically trained to generate the next teacher utterance, implicitly assuming that every student turn warrants a response. However, our experiments indicate that this conflates tutoring capability (what to say) with intervention necessity (whether to say it). We introduce DICE, a framework that decouples intervention decisions from response generation by first selecting an explicit pedagogical action. To calibrate this action selection policy, we define Intervention Value (IV), a rollout-grounded counterfactual metric that compares each action against non-intervention. IV shows that many prescribed interventions provide little or no marginal benefit. We further introduce DICE-Bench, a multi-variant math tutoring benchmark with skill-preserving problem variants for session-level evaluation. Using IV-weighted and KL-regularized policy optimization, DICE learns to intervene selectively while preserving tutoring effectiveness. In simulated tutoring sessions, DICE reduces the over-intervention rate to near zero while guiding students to correct solutions in approximately 3-4 fewer turns on average than existing Socratic tutoring baselines.

---


### 173. [Viva La Vida: Verification and Accumulation Failures in Multi-Agent Proof Search](https://arxiv.org/abs/2610.04829)

**<font color=#1a73e8>作者：</font>** Benji Xu, Ken Zheng, Noah Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When an agentic prover works on an open problem, there is no proof assistant to fall back on: its verifier and lemma library are ultimately language models judging model outputs. We instrumented such a system end to end and analyzed $51{,}754$ traced observations across three full runs ($186$ hours, \$$5{,}694$). We find three connected failure modes. First, the three-model verifier requires unanimity and treats parse or API failure as non-approval; in $10$ of $12$ verification events, one member returned no parseable output or an API error, making acceptance arithmetically impossible without surfacing an error. Second, when the ensemble did function, one verifier approved $3$ attempts that GPT rejected, each claiming to resolve the open problem; a single-verifier design would therefore have announced a solution three times. Third, because nothing could be approved, every review was a refutation, yet the lemma extractor mines reviews as well as proofs: $24$ of $93$ lemmas ($26\%$) were extracted from rejected arguments with their refutational context removed. Taken together, these findings show that without external verification, supervision is itself a critical trust boundary: systems must distinguish abstention from rejection, preserve useful disagreement, and preserve the provenance and polarity of information before it becomes future context.

---


### 174. [MemTrace: State-Consistent Memory for Long-Horizon Coding Agents](https://arxiv.org/abs/2610.04838)

**<font color=#1a73e8>作者：</font>** Hongming Xu, Le Zhou, ZhongHe Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As coding agents take on long-horizon software evolution tasks spanning multiple files and stages, longer execution trajectories introduce two coupled challenges: (1) accumulated histories strain context budgets, and (2) repository changes can invalidate earlier execution evidence. Existing approaches address these challenges through techniques like larger context windows, compression, retrieval, or repository representations, but often fail to reconstruct a consistent task state after a context refresh or verify whether recalled evidence remains valid. Thus, we introduce MemTrace, a provenance-aware memory system that preserves execution history and aligns its reuse with the evolving task (e.g., iterative cross-file repair) and repository state. MemTrace stores history as immutable Memory Traces anchored to key information (e.g., files, symbols, tests), and organizes their execution order and dependencies in a Memory Trace Graph. When context is constrained, working memory retains only compact Memory Anchors, from which the agent can reconstruct the latest execution state and locate evidence relevant to its next action. Before restoring historical evidence, MemTrace checks its validity against the current repository state and retrieves only what the next action requires. Across three complementary long-horizon coding benchmarks, MemTrace consistently outperforms all fully evaluated baselines under the same backbone and harness, improving DeepSWE pass@1 by 21.2 points, SWE-EVO Resolved Rate by 4.4 points, and SWE-Milestone Score by 17.8 points under Codex CLI.

---


### 175. [Which Preferences to Train On? End-to-End Multi-Objective Alignment with an Adversarial Preference Distribution](https://arxiv.org/abs/2610.04845)

**<font color=#1a73e8>作者：</font>** Minjae Lee, Kyunghyun Cho, Sangdon Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with human values is important for safe, efficient, and beneficial AI deployment. However, human values are multifaceted: helpfulness, harmlessness and humor trade off against one another, and different users want different trade-offs. Multi-objective alignment (MOA) addresses this by training a policy that can provide any point of the Pareto front, but existing methods either train one model per preference, interpolate a few separately aligned experts post hoc, or train a single conditioned model without considering which preferences it should be trained on. Since the hard regions of the preference simplex depend on the objectives at hand, existing methods leave them under-trained and do not get the most out of a single model. Therefore, we propose MAESTRO (Multi-objective Alignment via End-to-end STeering and Robust Optimization), which formulates MOA as a minimax problem over preference distributions and trains a single prompt-conditioned policy end-to-end with RL against an adversarial preference distribution: a Dirichlet distribution updated by online mirror descent toward the preferences the current policy serves worst, rather than on a fixed one. On HH-RLHF, BeaverTails and a summarization task, with up to three objectives, MAESTRO attains the best Pareto front on most tasks in a single training run, at the lowest training cost among the compared methods. The largest margins appear in the hard regions that a fixed preference distribution leaves under-trained, confirming that a single prompt-conditioned model is capable of covering the objective trade-offs on its own.

---


### 176. [CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery](https://arxiv.org/abs/2610.04851)

**<font color=#1a73e8>作者：</font>** Tao Feng, Fangxu Yu, Zijie Lei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-ended discovery requires learning from repeated attempts while continuing to explore directions whose value is not yet apparent. Search with a frozen large language model (LLM) can reuse previous solutions in context, but cannot update the model from its successes and failures on the test problem. Reinforcement learning (RL) enables such adaptation; however, strongly favoring high-reward trajectories may suppress low-reward yet potentially promising directions too early. We introduce CURIO, a curiosity-driven test-time learning framework that complements task feedback with an Intrinsic Curiosity World Model (ICWM). The ICWM learns transitions in the policy's hidden-state representation and supplies prediction-error bonuses at sampled tokens outside the policy's top-k choices. Epoch normalization and an annealed weight regulate their contribution to the policy update. On six mathematical discovery tasks and single-cell denoising with Qwen3 backbones from 8B to 235B, three-run means improve over a matched task-only RL control on five mathematical objectives, match the best reported performance on Circle Packing, and improve denoising Score and mean squared error (MSE) on both held-out corpora at every tested scale. Relative gains reach 18.3% on Hadamard and 10.8% on denoising Score. Code-diversity measurements show greater structural variation among generated programs, supporting curiosity as a complementary exploration signal for learning in open-ended discovery.

---


### 177. [Invisible Ink, Visible Lies: How Production Watermarking Causes LLMs to Hallucinate](https://arxiv.org/abs/2610.04860)

**<font color=#1a73e8>作者：</font>** Haocheng Ye, Aoting Hu, Xinwei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text watermarking helps identify AI-generated content, but its effect on factual reliability remains underexplored. In this paper, we study watermarking hallucination: factual errors induced or amplified by watermarking even when the required evidence is present in the context and the unwatermarked model can answer correctly. Using a controlled retrieval-augmented generation setting, we compare unwatermarked and watermarked generations under the same context, query, and decoding configuration, and quantify their factual accuracy decrease. Across six representative watermarking methods, including KGW, SWEET, DiPmark, GumbelSoft, Gumbel-Max, and SynthID watermarking, we consistently observe watermark-induced hallucination. Watermarked outputs can remain fluent while introducing factual errors. We attribute this failure mode to two mechanisms: (1) token perturbations in the current-step arising from method-specific reweighting or keyed sampling, and (2) prefix-induced attention drift, which accumulates through autoregressive decoding and weakens later attention to the factual context. Motivated by this analysis, we propose two plug-in interventions at the token and attention levels that can be integrated into existing watermarking methods to improve factuality. At a matched TPR of 0.90 at 1% FPR, combining the two interventions reduces factual errors by approximately 90% relative to watermark-only decoding while preserving fluency and comparable decoding efficiency. Overall, this work highlights factuality as a first-class criterion in watermark evaluation, alongside detectability and robustness, and calls for careful factuality validation before deploying watermarks in fact-critical applications.

---


### 178. [GitSwarm: Decentralized Compounding Inference](https://arxiv.org/abs/2610.04862)

**<font color=#1a73e8>作者：</font>** Vedant Shah, Ankur Samanta, Paras Dahal 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon problem solving and scientific research require computation to accumulate across successive attempts. Partial solutions, experimental findings, and unsuccessful approaches can inform later work, yet most inference-time computation is organized around individual trajectories or candidates rather than a persistent body of reusable work. We call this paradigm compounding inference: organizing inference-time computation so that intermediate work persists and can be inspected, extended, combined, or challenged by subsequent computation. We instantiate compounding inference in GitSwarm, an asynchronous system where homogeneous agents independently decide how to advance a task while collaborating through structured persistent memory. Agents explore, experiment, verify, refine, and synthesize previous work in a shared, branch-able Git repository. Atomic commits preserve intermediate artifacts, while explicit semantic dependencies record how later contributions build on work across branches. We evaluate GitSwarm on long-horizon problem solving and sustained GPU-backed experimental research. On IMOProofBench-Advanced, GitSwarm solves all 30 problems in one run using GPT-5.5. On ProgramBench, it achieves a $79.4\%$ mean score, versus $65.1\%$ for the strongest reported baseline under the stated budget. On three neural architecture research tasks (Residual Matrix Transformer, Looped Transformer, NanoChat), GitSwarm improves upon the starting architectures through successive experimentation. Beyond final performance, we measure whether computation accumulates: on ProgramBench, $94.7\%$ of contributions are subsequently built upon, while the selected solution's ancestry covers $82-93\%$ of the contribution graph. These results show that inference-time computation can accumulate across otherwise independent episodes, forming an evolving body of work that subsequent inference can reuse.

---


### 179. [Enhancing Long-Video VLM Embeddings with Query-Aware Streaming Latent Reasoning](https://arxiv.org/abs/2610.04864)

**<font color=#1a73e8>作者：</font>** Haozhe Chi, Song Jin, Yang Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video embedding requires capturing sparse query-relevant evidence under a limited visual-token budget. Uniform sampling can miss brief events in videos spanning minutes or hours, whereas encoding more frames in a single context increases memory and computation. We introduce \textbf{Query-Aware Streaming Latent Reasoning} (QASLR), a post-training framework that accumulates evidence across clips while keeping the embedding size fixed. QASLR selects a bounded set of frames, restores their temporal order, and processes them clip by clip with a vision-language backbone. A compact set of persistent think tokens cross-attends to each clip's features, while an embed token reads out a normalized representation after every update. This design integrates evidence across multiple backbone calls without requiring all selected frames to share a single context. Training combines final contrastive learning, step-wise contrastive supervision, and final-embedding self-distillation. Intermediate supervision trains partial-video readouts for retrieval, while self-distillation regularizes them toward the final representation. Query-aware selection produces query-conditioned representations for candidate-set scoring and reranking, whereas query-independent selection enables reusable corpus indexing. Under the full training recipe, HourVideo retrieval Hit@1 increases from 54.2 to 70.7 and from 57.4 to 72.8 for 2B and 8B Qwen3-VL-Embedding backbones, respectively. Gains extend to the evaluated moment-retrieval and video-QA tasks, and the streaming head transfers to a second Qwen-family embedding backbone. These results support streaming latent aggregation as an effective approach to integrating long-video evidence into fixed-dimensional representations.

---


### 180. [Greedy Local Learning for Language Model Pretraining: Gaps and Objective Design](https://arxiv.org/abs/2610.04867)

**<font color=#1a73e8>作者：</font>** Jihwan Moon, Sheir A. Zaheer, Jinmyoung Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Greedy block-wise local learning splits a network into gradient-isolated blocks trained by local auxiliary losses, deleting the backward pass between blocks: inter-stage communication becomes forward-only and every block can step its optimizer independently, properties directly relevant to decentralized model-parallel training. Local learning is competitive with end-to-end backpropagation on image classification, and on small Transformers it is known to trade a worse best loss for parallel speedup. How this loss gap behaves in autoregressive language model (LM) pretraining at larger scale, and which auxiliary designs reduce it, has not been measured. We present a token-budget-matched empirical study at 125M and 400M parameters with $K \in \{1,2,4\}$ blocks at Chinchilla-optimal budgets, factorizing the auxiliary design into network architecture and training objective. We observe: (i) the gap to end-to-end training more than doubles from $K=2$ to $K=4$, but at $K=4$ shrinks from 125M to 400M; (ii) replacing an MLP auxiliary with a Transformer-based one is a strong network-side intervention, recovering 22-41% of the gap; (iii) a multi-token-prediction (MTP) auxiliary objective helps at the first block boundary, whereas adding it at deeper boundaries hurts, and restricting it to the first block yields the best $K=4$ configuration ($+0.062$ vs. $+0.075$ nats at 400M); and (iv) deployment-style per-block execution reduces activation memory by up to $2.2\times$. We frame these results as an empirically grounded method direction rather than a finalized method: local objectives should apply future-predictive pressure selectively across boundaries while resisting shortcuts that bypass predictive content.

---


### 181. [SpecFold: Folding Multi-Branch Redundancy for Faster Speculative Decoding in Diffusion Language Models](https://arxiv.org/abs/2610.04875)

**<font color=#1a73e8>作者：</font>** Chung-En Ho, Weiyu Sun, Cheng-Jhih Shih 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (DLLMs) generate text through iterative block denoising, and multi-branch speculative decoding accelerates this process by verifying a main branch together with multiple draft branches in a single forward pass. While prior DLLM acceleration methods primarily exploit temporal redundancy across denoising steps, we identify a complementary redundancy axis within each speculative verification step: multi-branch computational redundancy. During speculative verification, draft branches inherit most tokens from their parents while unmasking a small set of additional positions, causing large portions of hidden states to remain highly similar across branches. We propose SpecFold, an algorithm-system co-design that exploits this multi-branch redundancy to reduce the cost of multi-branch speculative verification. Algorithmically, SpecFold performs token-level residual gating and selectively reuses parent computation through folded attention and FFN while preserving residual hidden states. Systemically, a Triton kernel implementation translates this fine-grained reuse into end-to-end throughput gains through efficient sparse multi-branch execution. SpecFold is orthogonal to temporal caching and compatible with existing DLLM speculation strategies. Across two DLLM families, five models, and five standard benchmarks, SpecFold achieves up to 1.64x throughput over Spiffy and up to 1.99x over vanilla decoding, while maintaining comparable task performance.

---


### 182. [ResOPD: Tail Residualization for Sparse On-Policy Distillation](https://arxiv.org/abs/2610.04882)

**<font color=#1a73e8>作者：</font>** Penghui Yang, Long Xing, Xuanlang Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student model on self-generated trajectories, but transmitting dense teacher distributions across long reasoning traces creates prohibitive communication and memory bottlenecks. Practical systems therefore rely on sparse teacher interfaces, typically transmitting either the sampled-token score or a small Top-$k$ distribution. However, this sparse setting faces a fundamental dilemma: sampled-token estimators are unbiased but suffer from severe gradient variance, whereas directly optimizing Top-$k$ objectives introduces systematic bias. To improve this trade-off, we propose ResOPD (On-Policy Distillation with Tail Residualization), which provides unbiased full-vocabulary reverse KL gradient estimation under on-policy sampling, with substantial variance reduction under the same sparse payload in the evaluated settings. ResOPD aggregates the unobserved vocabulary into an observable coarse tail event, computes its exact aggregate gradient, and samples only the fine-grained within-tail residual, which requires no additional teacher queries or forward passes. Extensive experiments demonstrate that ResOPD substantially reduces gradient variance, stabilizes online training dynamics, and improves downstream performance across the evaluated settings. These results establish ResOPD as an efficient, plug-and-play variance reduction primitive for sparse on-policy distillation.

---


### 183. [No Hindsight for LLM Fact-Checkers: Measuring Leakage Channels in Misinformation Detection](https://arxiv.org/abs/2610.04888)

**<font color=#1a73e8>作者：</font>** Kuan-Hua Wu Lu, Yohanes Andre Setiawan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As automated fact-checking scales on social media, large language model (LLM) verdict scores can look stronger than warranted. One reason is that evaluations mix in information that was not knowable at claim time. Two channels are easy to conflate: outcomes memorized in pre-training and retrieved evidence published after the claim. Yet standard benchmarks rarely separate the two. In this study we measure both channels on AVeriTeC and QuanTemp++ by reconstructing point-in-time evidence conditions and probing for outcome information encoded in model representations. We find substantial evidence of parametric leakage, that can be hidden by the aggregate accuracy, while a simple representation bottleneck reduces this future leakage more efficiently than a mutual-information-based training penalty. We also find that allowing post-claim evidence inflates zero-shot accuracy by 6.3 points in AVeriTeC while the effect is negligible in QuanTemp++, where retrieval provides little post-claim evidence. These results show that misinformation benchmarks can overstate fact-checking performance when they do not account for what information was actually available at claim time.

---


### 184. [ForkPilot: Self-Evolving Policy for Retrospective Search in Long-Horizon Agents](https://arxiv.org/abs/2610.04889)

**<font color=#1a73e8>作者：</font>** Xinyue Zeng, Shivam Shandilya, Guilherme Potje 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive language-model agents increasingly solve complex tasks through long-horizon, multi-call reasoning, where errors in beliefs or actions can compound across tool interactions. Retrospective search can recover from such failures but is prone to misallocation. Delayed outcomes obscure the contribution of intermediate search decisions, leading to Attribution Complexity, while evolving execution evidence leads to Adaptation Complexity, where previously learned estimates become stale. To address these challenges, we first introduce Search Value Dynamics (SVD), which characterizes the evolving trade-off between the gain and cost of retrospective search. Building on SVD, we propose ForkPilot, a self-evolving two-stage policy-learning framework. In the first stage, ForkPilot learns a search-value policy offline from completed trajectories through automatically constructed outcome comparisons. In the second stage, it makes search decisions based on current observations and then self-evolves by incorporating newly completed trajectories into subsequent policy updates. We evaluate ForkPilot across 6 diverse benchmarks and 7 widely used LLM backbone families, including four open-source families, GPT-5.6 Sol, and Opus 4.8 in a production agentic system, against 9 competitive baselines, including a real-world harness deployment used by hundreds of thousands of paid users. ForkPilot achieves comparable state-of-the-art performance while reducing token usage by up to 59.2%, demonstrating its efficacy.

---


### 185. [Rewrite What Matters: Adaptive Multilingual Query Rewriting for Reasoning via Agentic Reinforcement Learning](https://arxiv.org/abs/2610.04899)

**<font color=#1a73e8>作者：</font>** Rui Qi, Yufeng Chen, Yunlong Liang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In multilingual scenarios, queries with equivalent semantics but in different languages could guide the model into different reasoning trajectories, leading to performance disparities. To mitigate this gap, previous studies typically apply a one-size-fits-all query rewriting strategy, such as translation, which overlooks the fact that different scenarios require diverse types of semantic transformations. In this paper, we propose mRewriter-R1, an agentic multilingual query rewriting framework with reinforcement learning. Unlike single-turn rewriting, mRewriter-R1 formulates multilingual query rewriting as a multi-turn sequential decision-making process, where the model dynamically performs multi-aspect optimization through adaptive operator selection. Experimental results demonstrate that mRewriter-R1 outperforms all strong multilingual rewriting baselines on different large reasoning backbones. Further analyses show that the learned policy can adaptively decide on rewriting operators according to query characteristics, exhibiting strong generalization ability across diverse reasoning tasks, and plug-and-play compatibility with heterogeneous reasoning language models.

---


### 186. [Self-Evaluating Recursive Agents](https://arxiv.org/abs/2610.04902)

**<font color=#1a73e8>作者：</font>** TianYi Lyu, Xiaozhe Li, Yang Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive language-model agents decompose tasks and delegate subtasks to child instances of the same policy, forming a tree of work. Training them, however, is hard: the final outcome is verifiable, but the self-invented intermediate subtasks are numerous and carry no ground truth. Existing methods score each node with a verifier or judge, which is costly at scale and blind to decomposition quality. We argue that a recursive agent must learn three coupled capabilities within one set of weights: decomposing problems into subtasks, solving them, and evaluating the outcomes, each requiring its own training signal. SERA (Self-Evaluating Recursive Agents) turns evaluation into a learned capability of the policy itself. Before delegating, the parent writes a rubric of weighted success criteria for each child subtask; a ranking objective against verified outcomes then trains rubric generation so that the criteria track genuine subtask success. In addition, a complementary leaf-coverage signal provides direct credit for task decomposition. Our central finding is that \emph{training} the policy to generate aligned rubrics is what drives the gains: because the same weights both evaluate and execute, learning to judge subtasks sharpens the agent's ability to solve them. Notably, external supervision is also reduced: the judge is consulted only to train the rubric generator, while solving is trained against the agent's own rubric scores, which outperform direct use of the judge. Beyond training, the learned rubric doubles as an inference-time selector for tree search. On TextCraft-Synth and TextWorld-Sync, SERA improves over strong recursive-agent baselines by 5.38 and 13.14 points on average, and rubric-guided tree search at inference adds a further 2.43 points on TextWorld-Sync.

---


### 187. [Scaling Verifiable Environments for Long-horizon Work Agents](https://arxiv.org/abs/2610.04906)

**<font color=#1a73e8>作者：</font>** Jiazheng Zhang, Long Ma, Yunxian Yang 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Work agents operate over digital artifacts to execute professional knowledge-intensive work, requiring training environments that support long-horizon interaction and trustworthy verification. However, hand-crafted environments incur prohibitive engineering overhead that prevents environment scaling, whereas synthesis methods sacrifice workspace complexity, realism, or grounded verifiability. To bridge this gap, we introduce WorkForge, a scalable synthesis framework for constructing verifiable work-agent environments from real-world resources. Starting from expert workflows, WorkForge first identifies the resources, decisions, and deliverables required by each workflow. It then retrieves relevant real-world files and organizes them into a workspace. WorkForge inspects the workspace to extract concrete, checkable facts about its content. These factual anchors fix which task types the workspace can support and how their outcomes can be verified. Therefore, WorkForge derives each task's instructions, solution plan, and complementary programmatic and semantic verifiers directly from these factual anchors, keeping verification traceable to observable workspace evidence. Furthermore, we construct 16.7K verifiable environments across 40 professional domains, with workspaces collectively covering 60 file types. Post-training Qwen3.5-35B-A3B-Base improves GDPVal from 45.5 to 73.6 and APEX Score from 5.0 to 21.3, while enabling Qwen3.5-27B to achieve highly competitive performance and outperform strong competitors. Our analyses confirm the efficacy of the proposed method and reveal consistent scaling behaviors across both data volume and interaction horizons.

---


### 188. [Why Subliminal Learning Needs So Much Data: A Noisy Inverse View through Steering Vector Recovery](https://arxiv.org/abs/2610.04907)

**<font color=#1a73e8>作者：</font>** Luoyu Chen, Xiaoyu Ding, Weiqi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subliminal learning lets a student inherit a teacher's behavioral trait from semantically unrelated data, yet published demonstrations typically require tens of thousands of carrier examples. We ask where this data requirement comes from. Our testbed is subliminal steering: the teacher trait is a known residual-stream vector $\Delta_T$, so transfer can be measured directly as parameter recovery. On identical carrier prefixes, we compare token-level (hard) NLL supervision with full-distribution (soft) KL supervision. At initialization the two objectives give nearly collinear gradients, and both align poorly with $\Delta_T$. Under iterative optimization, however, they diverge: soft supervision recovers $\Delta_T$ almost exactly from a few hundred carriers, while hard supervision stays well below it even with tens of thousands. We explain this gap by casting steering-vector distillation as a noisy linear inverse problem. Locally, the carrier task maps the trait through its Fisher matrix $F$, so gradients point toward $F\Delta_T$ rather than $\Delta_T$. Gradient descent then acts as a progressively less-damped inverse of $F$. With soft targets, this inverse restores low-curvature directions. With hard labels, it also amplifies the sampling noise in those same directions. The result is an optimal inversion depth that grows with the number of independent carriers. Experiments on Qwen2.5-7B and Gemma-2-9B confirm four predictions: the Fisher distortion of the initial gradient, recovery ordered from steep to flat directions, an optimal depth that shifts with data scale, and the finding that resampling completions from a fixed prompt pool works as well as adding new prompts. In this setting, large carrier datasets are needed less to reveal the trait than to suppress label noise amplified by Fisher inversion. Code is available at \url{this https URL}.

---


### 189. [VideoResearchAgent: Grounded Task Synthesis and Sim-to-Real RL for Open-Web Video Research](https://arxiv.org/abs/2610.04911)

**<font color=#1a73e8>作者：</font>** Yuhang Zhou, Fei Li, Yuxi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing deep research agents are designed primarily for text- and image-based web sources, while video reasoning systems typically assume that relevant videos are provided in advance. We study open-web video research, where an agent must autonomously discover relevant videos, navigate their temporal content, and ground answers in visual evidence. Training such agents at scale is challenging as live video interaction is slow and unreliable, whereas fixed local simulation can induce retrieval-specific shortcuts that fail to transfer to the open web. We introduce VideoResearchAgent, a scalable training framework to address these challenges. First, we introduce controllable task synthesis pipeline to synthesize multi-hop research tasks from timestamped visual evidence while filtering text-only shortcuts. Second, we build a field-aligned local video simulator that preserves deployment-facing search and watch interactions while accelerating video search by a factor of 34.5-64.6. Third, we introduce Retrieval-Domain-Randomized GRPO (RDR-GRPO), which diversifies candidate rankings, distractors, metadata, and result structure during training to reduce overfitting to simulated retrieval. On Video-BrowseComp, the VideoResearchAgent trained using Qwen3.5-4B achieves 40.48% accuracy, comparable to Gemini-3-Flash-Preview, while reducing cumulative API-token consumption by 74.9% relative to the untrained model. Together, these results establish an accurate and efficient training recipe for open-web video research.

---


### 190. [Static Bootstrap Placement for Encrypted Language Model Decoding](https://arxiv.org/abs/2610.04912)

**<font color=#1a73e8>作者：</font>** Halil Ibrahim Kanpak, Didem Unat  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language models increasingly serve prompts that carry private data, and secure inference under homomorphic encryption lets a client outsource the computation without revealing the prompt. Existing secure inference systems run a forward pass without consuming a token under encryption, and generating text with them requires a client round trip at every generated token. Keeping the loop on the server instead requires selecting and consuming a token under encryption, and placing bootstraps for a loop body that grows with the context. We build AR-HE, which runs the whole loop on the server, selects each token under encryption, retrieves its embedding, and writes it back into the encrypted state. The client sends one prompt and remains offline until the output. One rule places every bootstrap in the run, without search, so the bootstrap cost of a token is a formula in the context length that is known before the run starts. The schedule skips work whose result cannot reach the output, packs bootstraps that share an operand, and keeps the keys and values of past positions in an encrypted cache. With every optimization applied, generating a GPT-2 small token costs 544 seconds on one NVIDIA H100, down from 4715 seconds without optimization. The prompt step before it costs 4630 seconds. The cache alone takes a generated step from 11751 bootstraps to 1072. The formula predicts every step we measured, including steps of a model it was not derived from.

---


### 191. [Monitorability Disposition in Large Reasoning Models](https://arxiv.org/abs/2610.04914)

**<font color=#1a73e8>作者：</font>** Shahriar Golchin, Marc Wetter  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Monitoring the chain-of-thought (CoT) of large reasoning models (LRMs) is a common way to detect misbehavior in real-world practice. However, current monitoring is passive: a separate model inspects the session only after execution. This means harm may already have occurred before it is caught. An active alternative is to have the model self-report its misbehavior as it happens. Whether models are willing to do this, however, is unknown. We introduce "monitorability disposition": a model's willingness to make itself monitorable and stay monitored throughout inference when warranted. We measure it as the fraction of warranted cases in which a model self-reports its own misbehavior via tool calls to available monitoring channels. We evaluate four LRMs on three misbehaviors (sycophancy, reward hacking, and bias) while varying the available monitors (AI and human) and the pressure to use the monitoring tools. We find that when tool use is optional, models self-report in only about 16% of warranted cases on average. Increasing tool-use pressure does not improve reporting where it matters: high-severity misbehavior is never self-reported. Models also systematically select the monitor they perceive as least strict. Overall, we identify monitorability disposition as a new contributing factor to model monitorability: when sufficiently strong, it keeps models seeking monitorability throughout inference.

---


### 192. [Are We Measuring Scientific Intelligence? Rethinking the Evaluation of AI Scientists](https://arxiv.org/abs/2610.04915)

**<font color=#1a73e8>作者：</font>** Kate Zhang, Yuante Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can now carry out data-driven scientific analyses end to end, and benchmarks assess them by giving an agent a question and a dataset and scoring its final answer against a fixed key. These benchmarks assume that a correct answer was derived from the supplied data, a property we call evidence grounding. However, an agent can also reach the key from prior knowledge or by ruling out the other options, and a score based on a single run cannot tell these cases apart. We show how to test this assumption and find that it often fails. For each question, we build versions of its data files in which the evidence for the answer is left intact, withdrawn or reversed, check each edit with a pre-registered reference statistic, and run the same agent on every version. We then measure evidence-grounded accuracy, which credits a correct answer only if the agent also responds when the evidence is withdrawn and follows it when it is reversed. We evaluate three agent scaffolds and five models on 18 single-cell questions from BAISBench and four synthetic problems from GeneBench-Pro. On the single-cell questions, the Claude agents are 95% accurate and answer 83% correctly without any data, but their evidence-grounded accuracy is only 41%. Hiding gene names raises the share of runs that follow reversed evidence from 58% to 93% on ten gene tasks, suggesting that prior knowledge competes with the supplied data. The benchmark score and LLM judges can also reward answers that ignore the changed evidence. Measuring scientific intelligence rather than recall therefore requires checking whether answers follow the evidence and whether scores reward them for it.

---


### 193. [Increasing Resilience of Smart Home Agents](https://arxiv.org/abs/2610.04923)

**<font color=#1a73e8>作者：</font>** Christopher Terrazas, Eduardo Cotilla-Sanchez  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Smart homes and smart devices are becoming more prevalent across millions of homes around the world. With the rise of AI, the smart home industry is quickly increasing its integration to manage common smart home tasks. However, existing work in large language models (LLMs) as agents within smart homes have shown minimal resilience due to limited environment scenarios or poor performance in complex tasks. We explore several strategies for LLMs as agents within the popular open-source software (OSS) smart home automation framework HomeAssistant to increase overall smart home resilience. Our approach combines traditional supervised learning techniques and optimized prompting as the core learning process. We use a diverse set of LLMs covering different levels of reasoning and costs in our optimization pipeline and evaluate their performance on a subset of the hardest tasks in a smart home benchmark. We include ReAct and Reflexion agentic paradigms and reveal how both provide marginal return on investment compared to fine-tuned LLMs for multi-device control within HomeAssistant but show promise in resilience tasks such as failure response.

---


### 194. [Prompt Dominance and Asymmetric Verifier Costs: Empirical Ablations of GRPO at 1B Scale on GSM8K](https://arxiv.org/abs/2610.04928)

**<font color=#1a73e8>作者：</font>** Yi Hou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies GRPO at 1B scale from both directions: what estimator choices do to the learning signal, and what a degraded reward signal does to what is learned. We train OLMo-2-0425-1B on GSM8K with a from-scratch implementation and measure both sides in controlled sweeps, including a verifier-quality experiment that degrades the training reward and the test-time selector identically. Four results stand out. The prompt is the first-order decision: the zero-shot prompt leaves the base model at 0.08% (its outputs are degenerate continuations, not wrong answers), so almost no group carries a gradient, and training succeeds because the 3-shot prompt reaches 18.3%. At this scale the estimator variants sit within seed noise, with Dr. GRPO ahead on both seeds. In the off-policy regime, clipping is the whole story: training on data without a clipped ratio loses 4-6 points relative to the on-policy reference, while GRPO-style clipping and GSPO recover the loss entirely. Finally, the same weak verifier is far cheaper in RL than in test-time selection: a 10%-flip verifier leaves RL's attainable gain intact (91% and 106% retained across two seeds) where selection retains 57%, and a format-only verifier leaves RL with 16-30% of its gain and selection with essentially nothing. Flip noise acts as an affine transform on the expected reward, and the group-normalized advantage with Adam's rescaling removes it exactly; the residual is a second-order variance effect that the matched-step comparison at a 30% flip rate tests.

---


### 195. [Software World Models: From Consequence Prediction to Decision Value](https://arxiv.org/abs/2610.04940)

**<font color=#1a73e8>作者：</font>** Tongli Su, Yuntong Hu, Liang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A coding agent may safely modify one repository while silently breaking downstream services, libraries, or datastores that depend on it. Exhaustively running integration tests after every agent action is impractical, so the agent must predict these failures before executing them. Existing software world models predict the agent's own observations, while static change-impact analysis only identifies where a change may propagate. We instead introduce the Software World Model (SWM), which models the broader system affected by a code change and predicts its blast set: the components that the change will break. SWM follows three stages: explore, learn, and act. Explore executes candidate changes from restored system states, prioritizing regions where observed failures contradict the dependency graph. Learn fine-tunes a language model on these execution outcomes to predict downstream breakage. Act converts sampled predictions into per-consumer break probabilities for change ranking, proactive migration, and deciding when another execution is worth its cost. On held-out synthetic systems, SWM improves blast-set F1 from 0.431 for static reachability to $0.571\pm0.037$, more than halves ranking regret, and improves migration return at all nine evaluation checkpoints. The two methods are complementary: reachability is stronger on dependencies represented in the graph, while SWM recovers failures caused by couplings the graph misses. Experiments on held-out real libraries further show that predicting structured failure outcomes, rather than only scalar risk, is important for downstream decision quality.

---


### 196. [How Should Teachers Be Prepared? RL on Student-Induced States for On-Policy Distillation](https://arxiv.org/abs/2610.04950)

**<font color=#1a73e8>作者：</font>** Xiaoyu Ma, Haoyue Liu, Zhichao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves the reasoning capabilities of small language models through token-level teacher supervision on student-generated trajectories. Yet can teachers that excel at solving problems independently also guide student reasoning effectively? Prior work shows that when student prefixes follow reasoning paths that differ from the teacher's own or contain errors, teachers can be less accurate when continuing from these prefixes than when solving problems independently. To this end, we propose Prep-OPD, which uses reinforcement learning (RL) before distillation to train the teacher to adapt to the student's existing reasoning state and correct course when errors arise. Training optimizes teacher continuations from fixed student prefixes using final-answer correctness as the reward. The prepared teacher then trains the student through trajectory guidance and token-level supervision. We evaluate Prep-OPD on eight mathematical reasoning benchmarks, using Qwen3-4B-Instruct-2507 as the teacher and Qwen3-0.6B and Qwen3-1.7B as students. With the 4B teacher and 1.7B student, Prep-OPD improves average accuracy over standard OPD and the strongest baseline, Relay-OPD, by 8.28 and 2.30 percentage points, respectively. Controlled experiments further show that teacher RL conditioned on student-generated prefixes yields higher student accuracy than problem-start teacher RL with and without handoff on Qwen3-1.7B. Reusing the same prepared teacher also improves Qwen3-0.6B.

---


### 197. [From Overloaded to Guaranteed: High-Throughput Multi-SLO Enforcement for LoRA-Assisted On-Premise LLM Deployment](https://arxiv.org/abs/2610.04956)

**<font color=#1a73e8>作者：</font>** Zeshen Zhang, Han Zhao, Weihao Cui 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) become essential in privacy-sensitive sectors like hospitals and government agencies, the on-premise LLM servers offer a cost-effective and secure alternative to public cloud services. However, these resource-constrained servers struggle to guarantee heterogeneous Service Level Objectives (SLOs) when serving multiple LoRA-adapted services simultaneously. Existing serving frameworks suffer from severe SLO violations due to the computational overhead of LoRA layers and the rigid nature of batch scheduling. To address this, we propose HALO, a scheduling method tailored for LoRA-assisted on-premise LLM deployment. HALO introduces two key innovations: a spatial multiplexing strategy that overlaps Base and LoRA computations by partitioning GPU Streaming Multiprocessors (SMs), and an SLO-aware scheduler that decouples request execution based on "request-level slack." By prioritizing urgent tasks and utilizing idle budget for traffic shaping, HALO significantly mitigates resource contention. Our evaluation demonstrates that HALO minimizes SLO violations while improving throughput compared to state-of-the-art baselines.

---


### 198. [Building LLM Agent Systems the Deep Learning Way: From Modular Design to Architecture Search](https://arxiv.org/abs/2610.04961)

**<font color=#1a73e8>作者：</font>** Tao Feng, Pengrui Han, Zhongjie Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have revolutionized AI research and enabled exciting agent systems. To build a complex LLM agent system, most existing research relies on insights from other domains or heuristics to manually build the agent system. However, this approach often requires heavy hand-engineering and fails to fully optimize for the downstream task of interest. Inspired by the tremendous success of deep learning, we propose to construct LLM agent systems in a modular manner, similar to building a deep neural network. Our key insight is to make analogies between LLM building blocks, such as retrievals, memories, and prompting strategies, and the successful deep learning modules, such as MLPs, attention, and recurrent modules. We further design forward inference and feedback mechanisms for LLMs, where prompts in LLMs are considered as the weights in deep models, and the prompt optimization from feedback is analogous to the back-propagation algorithm. We additionally leverage a search algorithm to search for the best configuration of LLM agent systems, similar to the neural architecture search (NAS) in deep learning research. Comprehensive experimental results demonstrate that the proposed deep learning recipe for LLM agent systems is highly effective, in particular: (1) Organizing LLM modules into deep-learning-style architectures yields noticeable performance gain; (2) Automatic prompt optimization, equivalent to backpropagation, is efficient in incorporating feedback from the task of interest and achieves at least 5% performance improvement; (3) NAS equivalent algorithm works well for further optimizing the LLM agent system architecture with 11% performance gain compared with randomly designed architectures. Overall, our research demonstrates the exciting opportunity of transferring the success of deep learning to building LLM agent systems.

---


### 199. [One Token Can Be Enough: Bridging Prompting and Activation Steering with Prefix Steering](https://arxiv.org/abs/2610.04967)

**<font color=#1a73e8>作者：</font>** Xudong Zhu, Zhihui Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompting guides language model behavior through the initial context, whereas activation steering often intervenes throughout generation. A natural question is whether steering can produce effects on subsequent computation similar to those of prompting. Under fixed-state attention assumptions, we establish sufficient conditions for single- and multi-token steering to match prompt-induced attention-head outputs, and characterize how changes in input representations affect this match and its approximation error. This attention-level connection leads us to ask whether, at the behavioral level, steering can also guide subsequent generation through a brief initial intervention. We study Prefix Steering, which applies existing steering directions and operators over a short span starting at the final prompt token, with no further direct intervention afterward. We examine how intervention duration and strength jointly shape the control-capability trade-off. Across four models and five tasks, intervention over a short span, even a single token, often retains much of full steering's behavioral control while better preserving general capabilities, offering a trade-off competitive with, and in some settings better than, prompting and alternative steering-strength policies. Prefix Steering also remains effective on final-answer formatting tasks after reasoning, suggesting that a brief initial intervention can influence behavior expressed well after steering ends. These findings challenge the common practice of steering every generated token and motivate a more dynamical view of activation steering, in which a brief intervention can alter the trajectory of subsequent generation without continued intervention.

---


### 200. [TrajLong: Co-Designing Agentic and Long-Context Supervision for Mid-Training](https://arxiv.org/abs/2610.04973)

**<font color=#1a73e8>作者：</font>** Miao Peng, Qintong Zhang, Nuo Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents for coding, search, and workplace tasks increasingly rely on long-context capabilities to effectively aggregate and reason over extended interaction histories. Recent work has incorporated agent trajectories into mid-training stage, drawing on their naturally long and interaction-rich structure. Yet how to organize the information within these trajectories into effective mid-training supervision remains underexplored. In this work, we investigate the relationship between long-context and agent atomic capabilities and introduce TrajLong, a novel framework that compiles trajectories into long-context training tasks with dense supervision, targeting three representative atomic capabilities: evidence grounding, cross-evidence aggregation, and temporal state maintenance. We mid-train Qwen3-14B-Base and Qwen3-30B-A3B-Base with data compiled by TrajLong, followed by supervised fine-tuning. Experiments on 6 long-context and 12 agent benchmarks demonstrate broad performance gains, with controlled ablations showing improvements over raw and masked trajectory baselines. Capability-level analyses further reveal task-dependent associations between long-context and agent atomic capabilities. These findings suggest that the shared capability demands of long-context reasoning and agent execution provide a principled basis for designing mid-training data to develop downstream agent capabilities.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
