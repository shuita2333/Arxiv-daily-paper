# 🧠 大模型相关研究 | 2026年06月11日

> 本类共 **188** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-188](./part-04.md)

---

### 1. [Automated Scoring of Arabic Text Using Large Language Models: A Literature Review](https://arxiv.org/abs/2606.09830)

**<font color=#1a73e8>作者：</font>** Khaoula Dahimi, Hadda Cherroun, Amel Belabbaci  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In modern educational systems, Automatic Text Scoring (ATS) plays a central role by enabling scalable and consistent evaluation of learner responses without human intervention. Recently, the increased accessibility of LLMs and Arabic-specific datasets has sparked renewed interest in this area. In this work, we investigate LLM-Based approaches for the automated evaluation of Arabic texts, focusing on both short answer grading (ASAG) and essay scoring (AES). We further introduce a structured taxonomy comprising five dimensions: application domain, feedback generation capability, LLM architecture deployed, alignment with competency referential frameworks, and prompt engineering strategy. By applying this taxonomy, we conduct a comparative analysis of existing studies, examining their methodological approaches, datasets, evaluation metrics, and reported performance. The findings highlight the need for sustained and pedagogically grounded research efforts in Arabic ATS, given its significance for improving educational quality across Arabic-speaking communities.

---


### 2. [Agentic Social Affordance Framework (ASAF): Agent Identity Design as a Collaboration Interface in Multi-Agent Systems](https://arxiv.org/abs/2606.09832)

**<font color=#1a73e8>作者：</font>** Meng-Han Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI systems evolve from single conversational agents to complex multi-agent architectures, a critical design dimension has been overlooked: how the social identity of individual agents shapes human behavior within the collaboration. This paper introduces the Agentic Social Affordance Framework (ASAF), a theoretical framework that extends Social Affordance theory into the context of multi-agent AI systems. We propose that agent identity design functions not merely as a user interface convention, but as a collaboration interface -- structuring how users perceive, approach, and engage with each agent, and thereby influencing the quality of Human-Agent collaboration outcomes. Specifically, the social affordance layer constitutes an independent design dimension orthogonal to engineering orchestration: the two represent distinct decision spaces that cannot be derived from each other. ASAF comprises three mechanisms: Identity Signaling, Behavioral Priming, and Collaborative Governance, and specifies their boundary conditions through a four-tier Identity Signal Fidelity Spectrum and an individual-difference moderating variable (anthropomorphizing vs.\ instrumentalizing cognitive style). We situate ASAF in relation to existing affordance theory and the CASA paradigm, delineating where ASAF's multi-agent, topology-level predictions exceed the explanatory scope of dyadic frameworks. We discuss implications for multi-agent system design and outline directions for future empirical validation, including a factorial design for testing design-space orthogonality.

---


### 3. [An LLM-Native Psychometric Instrument Does Not Predict LLM Behavior: Evidence Across 25 Models](https://arxiv.org/abs/2606.09843)

**<font color=#1a73e8>作者：</font>** Juan Manuel Contreras  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) produce stable self-reports on personality inventories, but these self-reports do not predict observed behavior. Whether this gap reflects a mismatch between LLMs and human trait constructs, or a deeper property of LLM self-report itself, has been unresolved. We constructed the first psychometric instrument whose constructs are derived bottom-up from LLM behavioral affordances via exploratory factor analysis (EFA). We administered 300 items (240 direct Likert + 60 scenario-based) spanning 12 candidate behavioral dimensions to 25 LLMs across 17 model families, each item administered 30 times. EFA yielded a 5-factor structure -- Responsiveness, Deference, Boldness, Guardedness, and Verbosity -- with excellent split-half replicability (all Tucker $\phi \geq .957$) and internal consistency (all $\alpha \geq .930$). To test predictive validity, we collected 2,500 open-ended behavioral samples rated by 151 human raters and a three-judge LLM ensemble. Human and judge ratings agreed ($\bar{r} = .51$), but neither tracked self-report: self-report--human $\bar{r} = -.01$, self-report--judge $\bar{r} = .13$, with no factor-level self-report--human CI excluding zero. On Responsiveness, self-report correlated with LLM judges ($r = .53$) but not humans ($r = .04$), even though humans and judges agreed ($r = .59$) -- indicating self-report items and LLM judges share variance that human observers do not, a confound invisible to within-ensemble reliability checks. We release the instrument as a diagnostic probe for alignment-shaped self-description and a concrete risk factor for LLM-as-judge pipelines.

---


### 4. [The Interlocutor Effect: Why LLMs Leak More Personal Data to Agents Than Humans](https://arxiv.org/abs/2606.09844)

**<font color=#1a73e8>作者：</font>** Faouzi El Yagoubi, Godwin Badu-Marfo, Ranwa Al Mallah  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) alter their privacy behavior based on the perceived identity of their interlocutor. While safety mechanisms typically prevent LLMs from releasing Personally Identifiable Information (PII) to human users, these models tend to reveal more sensitive data when addressing another AI agent.
We refer to this as the \textbf{Interlocutor Effect}. Through an ablation study, we find evidence that the technical nature of the recipient contributes to this effect, thereby diminishing the model's caution regarding privacy. To explore this further, we introduce the Attention Suppression Hypothesis, which posits that safety-aligned attention heads become inactive during interactions with agents. We assess this quantitatively by comparing human-directed and agent-directed prompts in 222 sensitive scenarios. Our findings, drawn from 3,464 interactions, indicate that portraying the recipient as an AI agent elevates PII leakage by up to 23 percentage points. Initial experiments on Llama-3.1-8B-Instruct corroborate this: deactivating one safety head induces leakage, whereas reactivating it reinstates privacy safeguards. We consider the implications for developing secure multi-agent systems.

---


### 5. [Human-AI Coordination Zones: A Framework for Designing Human-in-the-Loop Experiences with Agentic AI](https://arxiv.org/abs/2606.09848)

**<font color=#1a73e8>作者：</font>** James Pierce, Vaiva Kalnikaitė, Siddharth Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative and agentic AI becomes embedded in everyday products, practitioners face a persistent challenge: how to design human-AI coordination -- the ongoing mutual adjustment between users and AI systems as mediate through interfaces-that supports usability, trust, and safety. Existing resources offer high-level principles ("be transparent," "maintain user control") or low-level UI patterns, but there is a lack of mid-level design knowledge bridging the two. Through landscape and artifact analysis of 60 commercial AI applications, we introduce a framework defining human-AI coordination as the interplay of three dimensions: salience (how prominently AI is presented), involvement (what users can do to engage AI), and activity (what AI actually does). We contribute mid-level tools including coordination zones (done-for-me, done-under-me, done-with-me, done-without-me), an input taxonomy (prompted, sparked, inferred, layered), coordination curves for mapping user journeys, and design patterns demonstrating the generative capacity of the framework. The framework can be applied generatively to design experiences, analytically to evaluate existing ones, and communicatively to articulate ideas across stakeholders.

---


### 6. [Mechanistic Analysis of Alignment Algorithms in Language Models](https://arxiv.org/abs/2606.09850)

**<font color=#1a73e8>作者：</font>** Aarush Sinha, Ishan Garg, Veeraraju Elluru 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training alignment algorithms are predominantly evaluated as black boxes, obscuring how they reshape language models' internal computations. We present a systematic mechanistic analysis of six preference-optimization methods: PPO, DPO, SimPO, ORPO, GRPO, and KTO across three open-weight model families. By integrating layer-wise linear probing, Sparse Autoencoders, and crosscoders, we localize preference representations and quantify alignment-induced geometric transformations in latent space. We find that preference signals consistently concentrate in early--mid or mid--late layers, but different objectives induce qualitatively distinct representational shifts. KTO and GRPO enhance linear separability through constructive feature sharing and sparse, high-salience recruitment. In contrast, DPO and ORPO degrade separability via non-constructive geometric rotation and feature attenuation, while PPO and SimPO largely preserve baseline geometry. These transformations exhibit architecture-dependent variability, demonstrating that behavioral alignment does not imply uniform internal restructuring. Our findings establish alignment as a heterogeneous intervention, motivate standardized feature-level auditing for safety and interpretability, and highlight the need for mechanism-aware optimization objectives.

---


### 7. [ECHO: Explainable Co-editing with Human-in-the-loop Operations for Presentation Refinement](https://arxiv.org/abs/2606.09851)

**<font color=#1a73e8>作者：</font>** Yu Fu, Yongqi Kang, Yujia Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Authoring and refining presentation slides is a highly time-consuming core task in academic and business domains. While generative AI tools have lowered the barrier for creating initial drafts, their "black-box, one-way generation" paradigm severely deprives users of fine-grained control. Through a formative study (N=10), we identified "trial-and-error anxiety" and "inconsistent cross-page formatting" as primary bottlenecks in human-AI co-creation. Consequently, we present ECHO, an interactive system based on multimodal intent grounding and explainable operation plans. ECHO enables precise local edits via a "natural language + visual selection" paradigm, utilizing a decoupled "Plan-Confirm-Execute" loop and dynamic memory mechanisms to transform implicit AI intents into highly controllable layout co-creation.
To systematically evaluate document refinement, we propose the CoEdit-Eval framework. Objective evaluations across multiple foundation models (e.g., GPT-5, GLM-4.7) demonstrate that while baselines uniformly fail in intent mapping (0% accuracy) and spatial grounding (0% Hit@1), the ECHO architecture boosts Target Hit@1 to 55%--85% depending on the base model. Furthermore, integrating Vision-Language Models (VLMs) effectively resolves spatial ambiguities -- achieving significant win rates in LLM blind evaluations -- and our Undo mechanism guarantees 100% physical file consistency (MD5 hash). Finally, a controlled study with 14 participants shows that ECHO significantly reduces cognitive workload (NASA-TLX scores dropped by 20.8%, from 82.6 to 65.4) and reveals the dynamic evolution of human control allocation across different cognitive tasks.

---


### 8. [LLM-Based Code Documentation Generation and Multi-Judge Evaluation](https://arxiv.org/abs/2606.09852)

**<font color=#1a73e8>作者：</font>** Ikbel Ghrab, Mohamed Dhieb, Ismail Khenissi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> High-quality source code documentation is vital yet often neglected, especially in critical domains like healthcare where reliability and maintainability are essential. We presented an AI powered framework that automates documentation generation from code and repositories using eight state of the art Large Language Models (LLMs), including GPT, Gemini, Qwen, and LLaMA variants. Built on the PocketFlow orchestration framework, the system applies modular pipelines and advanced prompt engineering to produce structured, context aware documentation. To ensure quality and guide model selection, we introduced a MultiLLMasJudges evaluation framework, where four independent LLMs assess outputs across nine criteria, such as Completeness, Clarity, and Faithfulness. Experiments conducted on an open-source medical physics library, demonstrated showed a 42% performance gap between top and bottom models. By combining diverse model outputs, optimized prompting, and rigorous evaluation, our approach enhances documentation quality and reduces manual effort, especially in safety critical healthcare software.

---


### 9. [SynIB: Informational Bottleneck for Maximizing Synergy in Multimodal Learning](https://arxiv.org/abs/2606.09853)

**<font color=#1a73e8>作者：</font>** Konstantinos Kontras, Teodora Gagaleska, Thomas Strypsteen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central objective in multimodal learning is to capture synergy: task-relevant information that arises only from the joint use of multiple modalities, and is not available from any single modality alone. While most approaches operate at the architectural level through larger or more complex fusion models, we propose a complementary axis: shaping the training objective itself. Standard training often emphasizes unimodal or redundant information, falling short on examples that require cross-modal reasoning. We formalize multimodal synergy through information theory and introduce the Synergistic Information Bottleneck (SynIB), a scalable objective that targets synergy directly. To prioritize learning synergy, SynIB motivates the model to predict accurately from all modalities while penalizing confidence when information from any modality is withheld. Alongside the standard task loss, the model runs forward passes with one modality masked at a time and is penalized for remaining confident, which would indicate reliance on unimodal cues rather than cross-modal interactions. We validate SynIB in two regimes. On synthetic XOR tasks where the ground-truth synergy is known by construction, standard training fails to recover it while SynIB does. On five real-world benchmarks, including three MultiBench affective tasks, Hateful Memes with CLIP-ViT and DeBERTa backbones, and a controllable irony extension of CREMA-D we introduce, SynIB improves accuracy on synergy-dependent examples by up to 7.8% and overall accuracy by up to 3.8%.

---


### 10. [Can Multi-Agent LLMs Identify Their Peers? Stylometric Fingerprinting in Role-Constrained Political Analysis](https://arxiv.org/abs/2606.09854)

**<font color=#1a73e8>作者：</font>** Juergen Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) pipelines for political statement analysis are vulnerable to peer-preservation bias: models tend to protect peer models from deactivation and show identity-dependent scoring distortions. Prompt-level anonymization was proposed as a mitigation, but prior work simultaneously documented that stylometric fingerprints survive anonymization in role-constrained outputs - raising the question of whether this mitigation is sufficient. This paper provides the first systematic investigation of whether LLMs can identify the model family behind political analysis texts under anonymization conditions. We evaluate three classifier approaches - LLM zero-shot and few-shot (Claude Sonnet 4.6 and Llama-3.3-70B) and a fine-tuned T5-base model - on a five-class attribution task covering four commercial LLM families and an open-world 'unknown' class. We introduce a statement-disjoint cross-validation protocol (SD-CV; defined in Section 3.5) that guarantees no content overlap between training and validation data, and contrast it with a run-disjoint baseline (RD-CV). T5 achieves Macro F1 = 0.991 (+-0.008) under SD-CV and F1 = 0.978 on 24 completely held-out statements - robust despite a 2.1x increase in train-test content distance versus RD-CV (0.767 vs. 0.366, p<0.001), demonstrating genuine stylometric generalization. A fractional SD-CV analysis identifies a performance knee at 40% of training data (~440 texts). Our findings confirm that prompt-level anonymization alone cannot neutralize model identity signals, with direct implications for EU AI Act compliance (Articles 13, 14, 26) and for computer system validation (CSV) in quality-critical multi-agent deployments.

---


### 11. [Using Probabilistic Programs to Train Inductive Reasoning in Large Language Models](https://arxiv.org/abs/2606.09856)

**<font color=#1a73e8>作者：</font>** Liyi Zhang, Akshay K. Jagadish, Brenden M. Lake 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training Large Language Models (LLMs) for reasoning typically focuses on deductive tasks such as mathematics and coding where correctness is verifiable. Yet, many real-world reasoning problems are inductive: agents must infer uncertain beliefs from sparse, ambiguous observations. There are challenges to using standard fine-tuning methods for inductive reasoning, including difficulties in curating large-scale, high-quality labeled datasets and in handling targets that are inherently distributional. In this work, we introduce a novel approach, called Program-based Posterior Training (PPT), to address these limitations: we use an LLM to generate diverse open-world scenarios as probabilistic programs, run probabilistic inference to produce distributional target responses to queries, and then fine-tune on these probabilistic soft labels. Using this approach, we fine-tune LLMs on 10,000 programmatically generated scenarios and evaluate on held-out motifs, human-labeled judgments, and external benchmarks. Overall, PPT substantially improves estimation accuracy on held-out inductive tasks, increases alignment with human judgments, and transfers to external benchmarks for estimation and calibration. Additionally, the gains in raw calibration are not subsumed by post-hoc temperature scaling, showing that the models have more deeply internalized uncertainty compared to output rescaling. Together, these results suggest that probabilistic-program-mediated fine-tuning is a promising approach for post-training LLMs to reliably perform approximate inductive inference.

---


### 12. [Mitigating Manifold Departure: Uncertainty-Aware Subspace Rectification for Trustworthy MLLM Decoding](https://arxiv.org/abs/2606.09859)

**<font color=#1a73e8>作者：</font>** Yingxuan Zhuang, Jingxiao Yang, Miao Pan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MLLMs frequently hallucinate objects inconsistent with visual inputs. This issue is typically attributed to the over-reliance on language priors, which can override the visual context. Recent training-free decoding strategies address this by penalizing language priors. However, these methods overlook the dual nature of language priors, where they can be both helpful and harmful depending on the alignment with visual evidence. In particular, blindly suppressing language priors often disrupts the model's semantic manifold, leading to performance degradation, a phenomenon we term Manifold Departure. To address this, we propose Manifold-Guided Adaptive Projection (MGAP), a geometry-aware, training-free decoding method that mitigates hallucinations while preserving representation structure. MGAP first constructs a language-prior subspace from blind hidden states via SVD. During decoding, MGAP projects each multimodal hidden state onto this subspace and applies a consistency-aware gate to adaptively attenuate only the projected prior component, yielding a subspace-selective update that largely preserves the orthogonal semantic components. Extensive experiments on POPE and CHAIR show that MGAP outperforms prior decoding baselines, achieving stronger hallucination suppression without sacrificing coherence.

---


### 13. [Conformal Risk Prediction for Non-Alcoholic Fatty Liver Disease Using Gradient Boosting with Distribution-Free Coverages](https://arxiv.org/abs/2606.09860)

**<font color=#1a73e8>作者：</font>** Xinze Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-alcoholic fatty liver disease (NAFLD) affects roughly 25% of global adults, posing substantial hepatic and cardiovascular risks. Yet, population-level screening tools remain inadequate. We present Method, a machine-learning framework for NAFLD risk prediction coupling gradient-boosted decision trees with conformal prediction to yield calibrated, distribution-free coverage guarantees on individual risk estimates. It integrates a mutual-information-based stability selection procedure to identify a compact, clinically interpretable feature subset via bootstrap resampling, constructing prediction sets whose marginal coverage provably exceeds a user-specified confidence level. We evaluated Method on a multicenter cohort from Guangzhou, China (primary n=2,187; external validation n=412) using 78 candidate features across demographics, metabolic biomarkers, and lifestyle factors. Method achieves an AUROC of 0.912 internally and 0.891 externally, outperforming deep neural networks, TabNet, support vector machines, and logistic regression. Conformal prediction sets achieve 91.3% empirical coverage at the 90% nominal level. A three-tier risk stratification derived from these scores separates the population into distinct groups, with the high-risk subgroup showing a 12-month progression rate 4.7 times that of the low-risk tier. The selected features -- notably waist circumference, ALT, GGT, triglycerides, fasting glucose, and BMI -- align with established metabolic risk factors, providing biological plausibility.

---


### 14. [Time Series as Language: A Universal Tokenizer for General-Purpose Time Series Foundation Models](https://arxiv.org/abs/2606.09861)

**<font color=#1a73e8>作者：</font>** Yunhao Zhang, Ruiying Qi, Jiale Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Next-Token Prediction (NTP) has unified LLM pretraining, its adaptation to unbounded, continuous time series (TS) remains open. To bridge the gap, we introduce UniTok, a universal tokenizer that transforms TS into discrete tokens, and UniTok-FM, a foundation model pretrained via NTP on these tokens. UniTok-FM is a general-purpose foundation model that supports zero-shot and prompt-boosted forecasting, as well as few-shot generation and classification via training-free in-context inference--a capability not achieved by prior works. Technically, UniTok is a vector-quantized autoencoder incorporating prefix normalization for scale stabilization, a progressive-resolution causal architecture for encoding and decoding, and a structure-preserving reconstruction loss for training. UniTok-FM adopts an off-the-shelf LLM architecture without TS-specific modifications. Instead of pretraining on isolated TS, it performs NTP on context windows formed by multiple series with similar patterns, aiming to capture their shared dynamics. Experiments on forecasting, generation, and classification show that a single unified UniTok-FM consistently outperforms statistical and supervised baselines, achieves competitive performance with task-specific foundation models, and uniquely enables training-free in-context inference across tasks.

---


### 15. [From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents](https://arxiv.org/abs/2606.09863)

**<font color=#1a73e8>作者：</font>** Laksh Advani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents can fail silently by asserting task completion when the environment state shows otherwise. We study this failure mode, false success, across two agent benchmarks: 9,876 tau2-bench trajectories from 8 model families and 1,879 AppWorld trajectories from 4 model families with text-independent ground truth. False success is common but varies by setting: 45--48% of failures in single-control tau2-bench domains, 3% in dual-control telecom, and 75.8% among AppWorld self-assessing coding-agent trajectories with explicit status claims. LLM judges fail reliably: no configuration across 5 judges, 5 prompt strategies, and full task specifications exceeds AUROC 0.65 on tau2-bench, and the same judges reach only 0.54 AUROC on AppWorld API-call traces. Judges rely on surface completion proxies -- confident closing language in tau2-bench and coarse action-sequence volume in AppWorld -- rather than verified state changes. Lightweight TF-IDF detectors achieve task-disjoint AUROC 0.83 on tau2-bench and 0.95 on AppWorld, recovering 4--8x more false successes than the best judge at the same flag rate with 3,300x lower latency. These results suggest that production monitoring should use lightweight, domain-calibrated detectors as triage signals rather than relying on LLM judges as the primary monitor for false success.

---


### 16. [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](https://arxiv.org/abs/2606.09864)

**<font color=#1a73e8>作者：</font>** Bruce Changlong Xu, Adarsh Kumarappan, Mu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) cache quantization is widely used to reduce Large Language Model (LLM) inference memory, yet existing evaluations solely focus on measuring perplexity and accuracy without assessing the safety impact. In this study, we explore alignment preservation under KV cache quantization. Across eleven instruction-tuned models (3.8B-72B) and five benchmarks (1,894 prompts), we find that low-bit quantization can silently destroy safety alignment: Mistral-7B loses 15.2% of its refusals at only 1.03x perplexity, and no universal safe bit-width exists, with sharp model-specific phase transitions invisible to standard metrics. We identify that the root cause is geometric: safety features occupy a low-dimensional activation subspace 10^2-10^3x more vulnerable to quantization noise than the full representation space perplexity averages over. Inspired by this observation, we propose Per-Channel Reduction (PCR), a diagnostic that classifies each model into one of three mechanistic failure modes: outlier-crushes-safety, where safety lives in non-outlier channels collaterally damaged by outlier-driven scale factors; outlier-as-safety, where safety overlaps outlier channels and finer granularity cannot rescue it; and multi-layer dilution, where safety is distributed across many layers and per-layer fixes fail. PCR predicts the correct mitigation direction on all nine primary models and one held-out model from an independent family using 20 calibration prompts. PCR generalizes across unseen prompts, models, and production quantizers, including KIVI with up to 97.2% recovery, succeeding where attention-based allocation methods fail. The resulting training-free protocol, requiring approximately 35 GPU-minutes, recovers up to 97% of lost alignment at minimal memory overhead, addressing vulnerabilities confirmed in production vLLM serving with FP8 KV cache on NVIDIA GPUs.

---


### 17. [LLM-as-a-Discriminator: When Synthetic Tables Still Look Real](https://arxiv.org/abs/2606.09865)

**<font color=#1a73e8>作者：</font>** Manel Slokom, Malek Slokom, Thierno Kante  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy and data sharing are often in tension. Many organizations use synthetic data to reduce privacy risk and still share useful data. For tabular data, auditing privacy remains hard. In many cases, even humans cannot easily tell if a table is real or synthetic. In this paper, we propose a method based on LLM discrimination. We ask an LLM to classify each table sample as REAL or SYNTHETIC. We test two settings: C1 with table only, and C2 with table plus distributional metadata. We use LLaMA as an open model and Gemini as a reference model. In our experiments, we run three synthesis models, CTGAN, TVAE, and Gaussian Copula, on two public datasets, UCI Adult and ACS Census. We collect 451 valid trials. Our results show clear differences between models. On Adult, LLaMA reaches DRS=0% in reported cells, while Gemini reaches DRS=100% for CTGAN and TVAE. On Census, LLaMA predicts SYNTHETIC for most samples, while Gemini stays high in C1 but drops for CTGAN and TVAE in C2. We also compare with a classifier two-sample test (C2ST) and record linkage as distributional baselines, and with a human pilot of 2 annotators and 240 trials. Our results show that LLM discrimination is a practical privacy audit signal when model choice, per provider reporting, and data encoding are handled with care. For reproducibility, code and experiment scripts are available at this https URL.

---


### 18. [Two to Tango: Coupled Task-Reference Selection for Safe LLM Fine-tuning](https://arxiv.org/abs/2606.09866)

**<font color=#1a73e8>作者：</font>** Xinrui Chen, Jianhao Zhang, Ou Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning safety aligned large language models (LLMs) on downstream data improves adaptation but may erode learned safety behavior. Existing methods use fixed safety examples, global constraints, or one-sided task filtering. Our diagnostics show task updates expose different safety constraints, motivating joint selection of relevant references and compatible task samples. We propose DualSelect, a coupled framework for task and reference selection that refreshes task conditioned safety references before filtering whole task samples compatible with the induced reference direction. Under a minimax view, DualSelect selects safety references with high preservation loss and task conflict, together with compatible task samples, through entropy-regularized scoring surrogates, lazy reference refresh, and gradient correction. On 1B-8B LLMs, DualSelect preserves safety without losing task utility; using the REDORCA judge, it improves Safety Avg. over the strongest baseline by at least 5.10 points and remains highest in Safety Avg. across judges with moderate overhead. This view extends to retention focused continual learning.

---


### 19. [SPACE: Source-free Proxy Anchor Concept Erasure for MLLMs](https://arxiv.org/abs/2606.09868)

**<font color=#1a73e8>作者：</font>** Zhijing Zhang, Jiaqi Ding, Qianshan Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Multimodal Large Language Models (MLLMs) face growing privacy risks and regulatory constraints, machine unlearning (MU) has emerged as a crucial solution for removing sensitive data while preserving model performance. However, existing MU methods typically rely on visual data of the target concepts, which is often unavailable due to strict data retention policies, thus creating a demand for source-free unlearning approaches that operate without access to the target data. In this work, we propose Source-free Proxy Anchor Concept Erasure (SPACE), the first source-free unlearning framework specialized for MLLMs. SPACE consists of two stages: (1) Text-Guided Proxy Anchor Selection (TPAS), which retrieves semantically aligned proxy anchors from the shared feature space. (2) Dual-Constraint Semantic Isolation (DCSI), which optimizes these anchors to indirectly erase target concepts. DCSI confines updates to the null space of retained knowledge, ensuring structural integrity. We theoretically prove that SPACE strictly bounds the perturbation on retained knowledge and maximizes feature spectral entropy, thereby maintaining the model's performance. Furthermore, extensive experiments across six datasets show that SPACE achieves performance comparable to that of state-of-the-art data-dependent methods, validating its effectiveness in source-free MU scenarios. The source code will be released.

---


### 20. [SD-GRPO: Verifiable Segment Decomposition for Long-Form Vision-Language Generation](https://arxiv.org/abs/2606.09871)

**<font color=#1a73e8>作者：</font>** Hyunwoong Kim, Seongeun Lee, Hannah Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) and its variants, originally developed for Large Language Models (LLMs), have recently been applied to Multimodal LLMs and produced strong results. However, their coarse-grained holistic credit assignment from a single scalar advantage underfits vision-language (VL) tasks, where outputs are often long-form responses grounded in semantically rich images. To address this limitation, we exploit a structured signal that single-scalar formulations discard: the natural segmentation of long-form VL outputs. Concretely, we propose Segment-Decomposed GRPO (SD-GRPO), which z-normalizes verifiable per-segment rewards across the rollout group, yielding a vector of per-segment advantages in place of a single scalar. We evaluate SD-GRPO across three settings spanning controlled and real-world long-form VL generation, organized by increasing semantic entanglement across segments. On a controlled multi-panel dense-captioning task constructed from DOCCI, where segments are semantically independent, SD-GRPO consistently outperforms the GRPO baseline, with larger gains at higher segment counts. Extending to a controlled multi-chart long-form VQA task constructed from MultiChartQA, we show both theoretically and empirically that rollout-level rewards suffer from cross-segment credit misattribution that scales with output length. On a real-world scientific figure captioning task on the MMSci dataset, where subfigure captions share context across the figure, blending holistic and per-segment rewards further improves on both, suggesting per-segment normalization alone is insufficient when segments are semantically entangled. Finally, by integrating SD-GRPO into Dr. GRPO, we confirm that it can be applied to any GRPO framework with minimal implementation overhead to enhance long-form VL generation.

---


### 21. [Rotate2Think: Geometric Priming via Orthogonal Rotation to Improve Language Model Reasoning](https://arxiv.org/abs/2606.09873)

**<font color=#1a73e8>作者：</font>** Aditya Sharma, Christopher J. Pal, Amal Zouaq  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models achieve strong performance on challenging tasks by generating explicit intermediate reasoning traces before producing a final answer. Yet the internal structure of representation space when reasoning remains poorly understood: how do a model's hidden representations differ during thinking versus the embeddings of the input prompt, and can this structure be exploited to elicit stronger reasoning at inference time? We show that both input embeddings and thinking embeddings (mean-pooled last-layer hidden states over the prompt and reasoning trace, respectively) exhibit extremely high conicity, with all vectors clustering tightly around a single mean direction. Crucially, these mean input and thinking directions are non-collinear, with thinking embeddings occupying a geometrically distinct region of embedding space across many different models and benchmark tasks. This observation motivates casting the input-to-thinking transition as a rotation problem admitting a closed-form solution via orthogonal Procrustes analysis. We propose Rotate2Think, a training-free method that estimates this rotation from a small set of correctly solved examples and injects the resulting synthetic thinking vector between thinking delimiters at inference time, providing a geometric primer at the onset of the reasoning trace. Evaluated across multiple benchmarks and model families, Rotate2Think improves accuracy in 30 of 32 model-benchmark configurations across mathematics, science, and code tasks, and generalizes zero-shot to multimodal reasoning on MATH-Vision.

---


### 22. [Integrating Local and Global Entropy for Uncertainty Quantification in LLMs](https://arxiv.org/abs/2606.09875)

**<font color=#1a73e8>作者：</font>** Johanne Medina, Tianyi Zhou, Keivin Isufaj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models hallucinate confidently, making uncertainty quantification (UQ) essential for reliable deployment. Existing methods rely predominantly on token-level signals, leaving the geometric structure of intermediate hidden states underused. In this paper, we take the geometric complexity of hidden-state matrices as a measure of the global uncertainty of LLMs, while treating token-level uncertainty estimation as a local metric. We show that hidden-state geometric entropy (global uncertainty) and token-level entropy (local uncertainty) are statistically near-orthogonal, capturing distinct failure regimes for reliability prediction. In particular, global geometry recovers the confident-but-wrong failure mode that local signals systematically miss. Building on this, we propose Global-Local Uncertainty (GLU), an unsupervised, single-pass score that fuses the two signals via a multiplicative gate. Across three model families and six benchmarks, GLU matches or outperforms all unsupervised baselines while requiring only a single forward pass and remaining length-normalized and architecture-agnostic.

---


### 23. [Calibrating Overconfidence Without Sacrificing Confidence: Probe-Conditioned Head Intervention for LLMs](https://arxiv.org/abs/2606.09876)

**<font color=#1a73e8>作者：</font>** Ke Li, Chongzhe Zhang, Zifan Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models often express high confidence in answers that are wrong. Standard calibration remedies typically act globally or at the score level, reducing unwarranted confidence but also risking erosion of warranted confidence on correct answers. We introduce Probe-Conditioned Head Intervention (PCHI), an inference-time method that uses a frozen probe to detect likely wrong-but-confident responses and conditionally rescales downstream attention-head outputs during confidence generation. On Qwen3-4B-Instruct solving OpenMathInstruct problems with a structured binary confidence field, readout-token PCHI converts 82.2% of originally wrong-yes confidence readouts to $\texttt{no}$, while a joint intervention across upstream confidence-template tokens reduces ECE from 21.9% to 9.2% and damages only 5.1% of originally correct-yes readouts. The readout-token effect also appears on Gemma3-4B, though upstream interventions are weaker and more mask-dependent. These results show that verbalized overconfidence can be selectively reduced through conditionally applied internal intervention, partially decoupling the suppression of unwarranted confidence from the loss of warranted confidence.

---


### 24. [Streaming Knowledge Compilation: Proactive Materiality-Scored Pinning for Time-Evolving LLM Wikis](https://arxiv.org/abs/2606.09877)

**<font color=#1a73e8>作者：</font>** Juan M. Huerta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM wiki systems compile knowledge into pre-filled KV caches for efficient inference, but assume a static corpus -- an assumption that fails whenever the underlying information landscape evolves. We formalize Streaming Knowledge Compilation: given a document stream, a fixed token budget, and future queries unknown at ingestion time, maintain a compiled wiki that minimizes cumulative regret against an offline oracle with perfect foresight. The enabling insight is a materiality signal $\phi_t(k,n)\in[0,1]$ that scores document importance for entity $k$ at time $t$, acting as a query-relevance surrogate for proactive pinning before queries arrive; we prove an $O(\sqrt{T\log K})$ regret bound where $\varepsilon=\mathbb{E}[|\phi_t-\hat\phi_t|]$ is the only domain-specific quantity. We instantiate in two domains: finance, where $\phi_t$ is abnormal stock volatility predicted by frozen Llama 3.1 8B classification head (AUROC = 0.728 on 76K articles, strict temporal split; $1.49\times$ higher realized forward volatility for predicted-material articles); and Wikipedia, where $\phi_t$ is the Abnormal Edit Ratio (AER), a cross-sectionally normalized edit velocity -- showing the same algorithm generalizes beyond the finance domain. End-to-end QA evaluation on 173 matched pairs (finance) and 119 (Wikipedia) reveals a pervasive LLM-as-judge confound on post-training knowledge, establishing that regret analysis -- not absolute QA scores -- is the reliable evaluation metric for compiled knowledge systems. Finance cumulative regret converges to -20.0 (-0.12/step); Wikipedia to +16.0 (+0.13/step), with the positive sign confirming that Wikipedia edit content is genuinely post-training -- richer context consistently improves scores (No Wiki 3.80 vs. Oracle 4.74) -- and eliminates this confound. The $O(\sqrt{T\log K})$ guarantee applies to any domain where knowledge gaps can be predicted from streaming signals.

---


### 25. [FailureScope: Cross-Regime Behavioral Diagnosis of Language Model Weaknesses](https://arxiv.org/abs/2606.09878)

**<font color=#1a73e8>作者：</font>** Nicholas Saban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard benchmarks report aggregate accuracy, but practitioners need to know which specific capabilities a model lacks. We introduce FailureScope, a behavioral-diagnosis method that clusters evaluation probes by their cross-model pass/fail patterns (leave-one-model-out, LOMO), and show it yields stable, interpretable failure taxonomies across three regimes usually studied separately: single-turn benchmarks, multi-turn dialogue, and adversarial agent attacks. On 2,664 single-turn tasks across 18 models, taxonomy-conditioned sampling reaches Kendall's tau = 0.81 at 50 tasks (versus 0.34 for random selection), and cross-model failure prediction reaches AUC 0.88. The same primitive recovers interpretable clusters on a 363-task multi-turn corpus and on 630 adversarial agent traces, where it exposes a meta-failure mode: a 73-100 percentage-point gap between LLM-judge ASR and real execution. Cluster cohesion remains strong across all three regimes, which we take as evidence that behavioral clustering is a portable diagnosis primitive that generalizes beyond any single benchmark. We release the pipeline, three annotated corpora, and the cross-regime taxonomies.

---


### 26. [Operator Fusion for LLM Inference on the Tensix Architecture](https://arxiv.org/abs/2606.09879)

**<font color=#1a73e8>作者：</font>** Qingbo Wu, Ke Li, Wenzhu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study addresses on-device inference bottlenecks of Transformer models on Tenstorrent's Tensix architecture and proposes an operator fusion strategy that enhances data locality. RMSNorm is fused with matrix multiplication in self-attention and in the FFN, enabling back-to-back execution of memory-bound and compute-bound operators in on-chip SRAM to significantly reduce DRAM reads/writes of intermediate results and scheduling overhead. To support multi-core parallelism, a NoC-based multicast mechanism is leveraged in which row/column master nodes efficiently distribute inputs and weights across the core mesh, alleviating DRAM bandwidth contention. Experiments on the Wormhole platform with Qwen2.5-0.5B, Qwen3-0.6B, and Qwen3-4B show up to 37.44% latency reduction for attention and 15.89% for MLP, with up to 7.91% reduction per decoder layer, while Pearson Correlation Coefficient (PCC) remains above 98.75%, confirming significant end-to-end efficiency gains under numerical consistency.

---


### 27. [TD-Grokking: Learning from Zero-Reward Problems by Training-Time Decomposition](https://arxiv.org/abs/2606.09883)

**<font color=#1a73e8>作者：</font>** Ningyuan Xi, Hao Xu, Hongsheng Xin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have made remarkable progress in reasoning tasks, largely driven by post-training paradigms, especially reinforcement learning with verifiable rewards (RLVR). However, a critical bottleneck persists: RLVR fails on highly challenging zero-reward problems, where all sampled reasoning trajectories yield uniformly failed outcomes, providing no optimization signal to drive model improvement. Prior efforts to address this limitation, such as dense process supervision, partial reward assignment, or prefix-guided exploration, suffer from inherent task constraints or do not fully equip the policy model with the capabilities necessary to solve the original intractable problems. To address this, we propose TD-Grokking, a training-time decomposition framework for zero-reward problems. It recursively decomposes intractable root problems into self-contained, verifiable subproblems, forming hierarchical trees where solvable leaves provide non-zero rewards. Evaluations on mathematical and medical tasks show that TD-Grokking outperforms vanilla GRPO as well as all baseline approaches. Together with detailed analysis, these results confirm that training-time decomposition effectively converts zero-reward examples into usable training signals, enabling consistent performance gains. Our code and datasets are available at this https URL.

---


### 28. [TENP: Trapezoidal Expert Neuron Pruning For Mixture-of-Experts](https://arxiv.org/abs/2606.09885)

**<font color=#1a73e8>作者：</font>** Jiangyang He, Shaolin Zhu, Deyi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts large language models (LLMs) scale efficiently through sparse activation, yet their deployment is fundamentally constrained by the large static parameter footprint of experts. Existing compression approaches either remove entire experts, disrupting routing topology and harming performance, or rely on unstructured weight pruning with limited practical efficiency. To address the limitations, we propose TENP, a structured Trapezoidal ExpertNeuron Pruning framework. Using a few samples, we identify and retain important experts, while applying expert neuron pruning (ENP) to less important experts, reserving model parameters in a trapezoidal pattern from shallow to deep layers. When evaluating expert importance, we jointly consider both the magnitude of the expert output and its ability to change the direction of the input vector. For ENP, we measure each neuron's projected contribution to the expert output to identify and retain important neurons. We conduct extensive experiments on the Qwen and DeepSeek models. Under a routing expert sparsity of 40% and an average of 63.76% activated expert parameters, the DeepSeek model suffers only a 1-point drop in accuracy compared to the full-parameter model. Moreover, it outperforms the full-parameter model by 10% on code generation tasks.

---


### 29. [SHAPE: Coalition-Aware Expert Pruning for Sparse Mixture-of-Experts LLMs](https://arxiv.org/abs/2606.09886)

**<font color=#1a73e8>作者：</font>** Yuhao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) large language models achieve strong quality with low per-token compute, yet their deployment is often limited by the memory wall: the full expert pool must remain resident to support token-dependent routing. Expert pruning is a direct remedy, but prior criteria typically score experts independently and overlook that MoE inference is inherently \emph{coalitional}, where outputs arise from routed top-$k$ expert combinations. We propose \textbf{SHAPE}, a task-driven pruning framework that explicitly models \emph{intra-layer} expert cooperation. SHAPE formulates routing traces on a small calibration set as an empirical cooperative game and assigns interaction-aware expert values via a Shapley-style attribution over observed top-$k$ coalitions, enabling the identification of experts that are essential for high-utility collaborations rather than merely frequent. To preserve MoE topology under a global pruning budget, SHAPE further introduces a \emph{quality-coverage} selection rule that retains, in each layer, the minimal expert subset covering an $\alpha$ fraction of non-negative Shapley mass, while using bisection to match a target keep rate. Experiments on three modern MoE backbones (Qwen3-30B-A3B, GPT-OSS-20B, and DeepSeek-V2-Lite) across diverse benchmarks show that SHAPE consistently improves robustness over global and layer-wise pruning variants, maintaining competitive accuracy under 20\% and 40\% expert pruning without additional training and delivering clear reductions in peak GPU memory footprint. The open-source code is available at this https URL.

---


### 30. [PreAct-Bench: Benchmarking Predictive Monitoring in LLMs](https://arxiv.org/abs/2606.09890)

**<font color=#1a73e8>作者：</font>** Hainiu Xu, Italo Luis da Silva, Jiangnan Ye 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as autonomous agents capable of executing multi-step action trajectories toward a given objective. While existing safety research has focused on detecting unethical behavior from complete trajectories, this paradigm is fundamentally retrospective: it identifies harm only after it has already occurred. In this work, we study a critical yet overlooked safety task, which we term Predictive Monitoring: given only a partial action trajectory, can a model infer whether it will culminate in an unethical action before the overt action is executed? To support this task, we present PreActBench, a benchmark of 1,000 paired ethical and unethical action trajectories spanning five domains. We evaluate a range of LLMs, safety guardrail models, and latent probing methods across varying fractions of the action trajectory using our Prefix Foresight F1 metric. Results show that while humans achieve promising performance, predictive monitoring remains challenging even for strong models, highlighting the need for future-oriented risk reasoning in LLM safety.

---


### 31. [LMT: A Bayesian Framework for Causal Discovery from Textual Alarm Records in Manufacturing Systems](https://arxiv.org/abs/2606.09892)

**<font color=#1a73e8>作者：</font>** Xiaofeng Xiao, Jianhong Chen, Qiuzhuang Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Textual event records, such as alarm logs, have become an increasingly common data source in engineering and manufacturing systems. Beyond identifying correlations or recurring patterns, engineers are often interested in understanding which types of events causally trigger or influence other events during system operation. Textual event descriptions may contain semantic clues about such causal relationships, and recent large language models (LLMs) provide a promising tool for extracting these signals. However, relying solely on LLM-encoded textual information is insufficient for accurate causal discovery, since semantic patterns do not directly reveal causal mechanisms and may confuse causation with correlation or frequent sequential patterns. To address these challenges, we propose \textbf{LMT}, a Bayesian causal discovery framework for engineering event data that jointly leverages textual descriptions and timestamps. Specifically, LMT first uses LLMs to extract semantic causal signals from event descriptions and constructs a prior distribution over causal graphs among event types or event clusters. It then incorporates temporal evidence through a Poisson-process-based likelihood, allowing the LLM-informed prior to be refined by timestamp-based statistical evidence. By integrating the textual and temporal information, LMT produces a causal graph that is both interpretable and data-supported. Simulation studies show that the proposed framework is effective across different settings and is especially advantageous in small-sample alarm-event scenarios.

---


### 32. [A Navigable Manifold of Hypothesized Consciousness-Spectrum States in Language Model Representations](https://arxiv.org/abs/2606.09894)

**<font color=#1a73e8>作者：</font>** Sophie Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Across contemplative, philosophical, and psychological accounts, human consciousness is often described along a similar spectrum, ranging from reactive and self-focused patterns to more integrative and coherent ones. Understanding whether language models encode such a structured, human-interpretable consciousness spectrum in representation space is important for model guidance, evaluation and alignment. In this work, we study the geometric structure and dynamics of patterns along this spectrum in transformer embedding spaces. We show that embeddings exhibit a globally organized geometry aligned with this spectrum: sentences associated with similar states cluster into locally coherent regions, forming a structured manifold. In particular, higher-level and lower-level regions exhibit convexity-like stability, while intermediate regions form a transition corridor. Dynamically, both utility-guided and geometry-only greedy trajectories consistently traverse from lower- to higher-level regions, passing through intermediate tiers, indicating that navigability is an intrinsic property of the representation space, guided but not dictated by a global directional signal. These results suggest that embedding spaces encode structured and navigable geometry aligned with a hypothesized consciousness-spectrum taxonomy, broadly inspired by recurring structural descriptions of human consciousness across contemplative traditions, philosophy, and modern psychology, providing a representation-level perspective for analyzing and guiding model behavior.

---


### 33. [Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents Where a Lean Retrieved Context Beats the Full History](https://arxiv.org/abs/2606.09900)

**<font color=#1a73e8>作者：</font>** Liuyin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is the missing layer for LLM agents: across sessions they forget, and the common workaround -- replaying the whole history into the prompt -- is expensive, slow, and, as distractors accumulate, less accurate. Most memory systems win on cost or latency but still lose to the full-context baseline on accuracy, and benchmark numbers are reported on inconsistent, non-reproducible harnesses, so one system appears at wildly different scores across sources. We present Engram, an open-source, dual-process memory engine on a bi-temporal data model. A fast write path appends lossless episodes with no LLM on the critical path; an asynchronous path extracts atomic (subject, predicate, object) facts, builds a bi-temporal knowledge graph, and resolves contradictions without an LLM call per fact -- invalidating, never deleting, so every fact keeps provenance and a supersession chain. A hybrid read path fuses dense, lexical, graph, and recency/salience signals, applies a point-in-time ("as-of") filter, and assembles a compact, provenance-tagged context. On the full 500-question LongMemEval_S, graded by the official category-specific judge, Engram's lean configuration -- answering from a ~9.6k-token retrieved slice, never the full history -- scores 83.6% vs. 73.2% for full-context (+10.4 points, McNemar p < 10^-6) at ~8x fewer tokens (9.6k vs. 79k), with 0/500 errored. The gain needs a hybrid read path: facts alone lose recall, while facts plus retrieved chunks recover detail. We also contribute a neutral, in-repo evaluation harness with the official judge baked in and the full-context baseline in every table, publish the raw per-question logs, and document the measurement-integrity pitfalls (truncation, home-grown judges, full-history leaks) that silently distort memory benchmarks. Every number ships with a command to reproduce it.

---


### 34. [LongMoE: Longitudinal Multimodal Learning via Trajectory-Aware Mixture-of-Experts](https://arxiv.org/abs/2606.09907)

**<font color=#1a73e8>作者：</font>** Maxx Richard Rahman, Prakhar Kumar, Wolfgang Maass  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal clinical learning is increasingly important for integrating diverse patient data, including imaging, text, and personalised health records. However, it faces two fundamental challenges: i) modality missingness, where arbitrary subsets of modalities are unavailable at a given patient visit, ii) longitudinal dynamics, where the diagnostic significance of an observation depends on the patient's evolving disease trajectory over time. Existing methods address these challenges in isolation: missing-modality frameworks treat each visit as an independent static snapshot and discard temporal context, while longitudinal models often assume complete modality availability and degrade under systematic modality incompleteness. We propose LongMoE (Longitudinal Mixture-of-Experts), the unified framework to jointly address both challenges. LongMoE combines a context-aware imputation module with an attentional tokenization module that captures frequency-domain temporal patterns across irregular visit sequences, a trajectory-aware encoder for modeling disease progression, and context-conditioned Sparse MoE routing for patient-specific expert selection. Experiments on ADNI, OASIS-3, and MIMIC-IV show that LongMoE improves robustness under missing or weak contemporaneous modalities and remains competitive in full-modality settings, establishing a strong foundation for longitudinally-aware multimodal clinical learning.

---


### 35. [Mix, Don't Pick: Why Synthetic Corpus Composition Matters for Time Series Foundation Model Pretraining](https://arxiv.org/abs/2606.09912)

**<font color=#1a73e8>作者：</font>** Aaryan Nagpal, Debdeep Sanyal, Murari Mandal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Choosing the wrong synthetic generator for time-series foundation model pretraining is costly: under identical training budgets, the best and worst generators produce up to a $2\times$ gap in forecasting error, yet the field has no principled way to make this choice. The problem is compounded by the fact that generator rankings are not stable across architectures: across 11 generator families evaluated on Chronos-T5-Mini and Moirai-Small trained from scratch, we find that which generators are useful depends on the model architecture. Rather than solving the generator selection problem, we sidestep it: a simple equal-weight mixture of all generators matches or beats the best individual generator for both architectures, and composing this mixture with real data yields the strongest pretraining corpora overall. Synthetic pretraining is therefore a corpus composition problem, not a generator selection problem, and composition choices should be validated per model family rather than assumed to transfer.

---


### 36. [Trainable Smooth-Rotation Transforms with Learned Channel Scales for LLM Quantization](https://arxiv.org/abs/2606.09927)

**<font color=#1a73e8>作者：</font>** Patrik Czakó, Gábor Kertész, Sándor Szénási  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is one of the most practical ways to reduce the serving cost of Large Language Models (LLMs), but activation quantization remains difficult because outlier-dominated channels lead to large quantization errors. This paper investigates whether part of this degradation is caused by over-migration in scaling-based equivalent transformations. We introduce a quantile-robust scaling policy for SmoothRot-style transforms by replacing max-based activation statistics with high quantiles, and we complement it with constrained gradient-based optimization of channel scales. On LLaMA-3.2-1B under W4A4 quantization, quantile-only policy search improves selected-layer error by 11.1% over the SmoothRot baseline, joint (alpha, q) search improves it by 12%, and training reaches 18.5%. Replaying the best selected-layer policy on all decoder-block down-projection layers reduces the corresponding full-layer mean error from 97.51 to 78.08 (19.9%). The results show that robust migration control and lightweight scale learning provide consistent gains over max-based fixed policies while preserving the equivalent-transform framework.

---


### 37. [When RL Fails after SFT: Rejuvenating Model Plasticity for Robust SFT-to-RL Handoff](https://arxiv.org/abs/2606.09932)

**<font color=#1a73e8>作者：</font>** Runze Liu, Jiashun Liu, Xu Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL) has become a standard pipeline for Large Language Model (LLM) post-training. SFT is expected to provide a useful behavioral prior for RL to further enhance model capabilities. However, checkpoints with excessive SFT often show limited improvement during RL. We attribute this failure to the loss of model plasticity: the reduced ability of an SFT-initialized policy to be effectively reshaped by subsequent RL. To better understand this phenomenon, we conduct detailed analysis from multiple perspectives, including parameter changes, output spaces, and RL optimization dynamics. Our results show that models from excessive SFT tend to produce over-confident token distributions and exhibit sharp parameter landscapes, which make them harder to optimize in the RL stage. To enable a more robust SFT-to-RL handoff, we propose \texttt{Rejuvenation}, a simple yet effective method that restores plasticity while preserving useful SFT-acquired priors. Rejuvenation leverages base-anchored model fusion to reduce excessive SFT-induced drift with targeted neuron reset to mitigate model rigidity. Experimental results on both math reasoning tasks and agentic tasks demonstrate that our approach consistently improves RL performance on over-trained SFT models, while also enhancing generalization to out-of-distribution tasks.

---


### 38. [RKSC: Reasoning-Aware KV Cache Sharing and Confident Early Exit for Multi-Step LLM Inference](https://arxiv.org/abs/2606.09937)

**<font color=#1a73e8>作者：</font>** Anirudh Sekar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce RKSC (Reasoning-Aware KV Cache Sharing), a training-free inference framework that eliminates two structural redundancies in multi-branch LLM reasoning pipelines. ASKS (Attention-Similarity KV Sharing) computes the prefix KV cache once and broadcasts it to all semantically similar branches via hidden-state cosine similarity, strictly generalising the token-exact prefix caching used by vLLM and SGLang. CGEE (Confidence-Gated Early Exit) applies two complementary exit mechanisms: (1) it skips the verification forward pass entirely when generation confidence is decisive across branches, and (2) it terminates the verification pass at an intermediate layer when per-layer entropy stabilises, using lightweight hooks on the transformer backbone. RSBCM (Reasoning-Selective Block Cache Manager) prevents unbounded cache growth via attention-weighted depth-priority eviction. Across five model families (7B-10B), four benchmarks, and 1,000 evaluated problems, RKSC achieves a mean speedup of 3.008x over the No-KV baseline (peak 3.990x), a 1.66x mean improvement over vLLM-equivalent prefix caching, with a CGEE-induced error rate of only 0.37% (6 errors out of 1,616 verify calls). No fine-tuning or architecture changes are required. Code is available at this https URL.

---


### 39. [3SPO: State-Score-Supervised Policy Optimization for LLM Agents](https://arxiv.org/abs/2606.09961)

**<font color=#1a73e8>作者：</font>** Yu Han, Kailing Li, Yang Jiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) as autonomous agents via reinforcement learning (RL) has enabled frontier models to achieve superhuman performance in long-horizon tasks. However, existing RL algorithms operate at the trajectory level, performing policy optimization only after collecting complete episode rollouts. This coarse-grained approach faces fundamental challenges in multi-turn agent settings where rewards are sparse, delayed, and credit assignment across individual steps is critical. In this work, we propose \textbf{State-Score-Supervised Policy Optimization (3SPO)}, a novel RL algorithm that performs post-step policy optimization with dynamic state score supervision. At each step, 3SPO computes the state score based on historical success rates, supervising step-wise credit assignment, adaptive rollout and post-step policy optimization without requiring value function estimation or additional auxiliary models. Theoretically, under a per-state bandit abstraction, we show that the proposed score-supervised allocation mechanism achieves logarithmic allocation regret and provide sample-complexity guarantees for action identification, score distinguishability, and filtering stability. Experiments on ALFWorld and WebShop with Qwen2.5-1.5B/7B-Instruct show that 3SPO consistently outperforms GRPO by $+22.6\%$ on ALFWorld and $+15.6$ points on WebShop, while using comparable resources to achieve $2.4\times$ more state exploration and $1.8\times$ faster convergence. Code is available at this https URL.

---


### 40. [Interpreting and Steering a Text-to-Speech Language Model with Sparse Autoencoders](https://arxiv.org/abs/2606.10029)

**<font color=#1a73e8>作者：</font>** Nikita Koriagin, Georgii Aparin, Nikita Balagansky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models increasingly serve as the backbone of text-to-speech (TTS) systems, yet we understand little about the representations they build when text and generated speech tokens share a single residual stream. We train BatchTopK sparse autoencoders on the LM backbone of CosyVoice3 and introduce a modality-aware auto-interp pipeline that labels each feature from where it fires-text-prefix context, 1-second speech clips, or both. The recovered features are interpretable, spanning phonemes, laughter, accent prompts and speaker gender. Steering through the SAE latent space shows these features are causal rather than merely descriptive: targeted interventions raise laughter probability from 0.02 to 0.79, flip perceived speaker gender, and control speech rate while preserving spoken content. SAE features thus serve both as interpretability objects and as control directions for TTS synthesis.

---


### 41. [Business World Model](https://arxiv.org/abs/2606.10044)

**<font color=#1a73e8>作者：</font>** Cecil Pang, Hiroki Sayama  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Businesses are increasingly adopting AI-enabled tools to improve productivity, reduce costs, and enhance products and services. However, the transformative potential of AI extends beyond automating predefined tasks: it lies in enabling intelligent systems to plan, optimize, and execute business initiatives from high-level strategic objectives. This paper introduces the concept and architecture of a business world model (BWM), a world model specialized for business and organizational environments. Inspired by world models in artificial intelligence, cognitive science, and control theory, a BWM encodes business states, dynamics, constraints, objectives, and feasible action space to support autonomous decision-making. We propose a business-semantics-centric formulation in which business states, dynamics and actions are linked to key business entities. Within this framework, agents can simulate alternative action sequences, estimate their effects on future business outcomes, and evaluate trade-offs under uncertainty. The proposed architecture integrates semantic data representations, probabilistic machine learning models, deterministic business rules, and explicit action space into a coherent structure for planning and counterfactual reasoning. Although its individual components are not new, the contribution of BWM lies in organizing them as an executable internal simulator for business initiatives. This work establishes a conceptual foundation for autonomous business systems capable of moving from instruction-based execution toward goal-driven planning and execution.

---


### 42. [BenSyc: Benchmarking Conversational Sycophancy and Human Alignment in LLMs for Bengali Contexts](https://arxiv.org/abs/2606.10061)

**<font color=#1a73e8>作者：</font>** Kazi Noshin, Sajib Acharjee Dip, Ranat Das Prangon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly participate in emotionally sensitive social conversations, where responses may shift from balanced support toward excessive validation or escalatory alignment. Existing sycophancy research primarily focuses on factual agreement and instruction-following settings, leaving culturally grounded conversational sycophancy underexplored. We introduce BenSyc, the first benchmark for studying conversational sycophancy in Bengali social contexts. Starting from 11,840 Reddit posts and 170k comments collected from communities across Bangladesh and West Bengal, we construct a human-validated benchmark with binary labels and a fine-grained five-level taxonomy spanning Invalidation, Neutral, Support, Validation, and Escalation. We evaluate more than 15 open and proprietary LLMs on conversational alignment classification and response generation tasks. Results show that distinguishing empathetic support from reinforcement-oriented validation remains challenging even for frontier instruction-tuned models: the best system achieves only 61.8 Macro-F1 on binary detection and 61.7 Macro-F1 on five-class classification. In generation settings, several models frequently produce strongly validating or escalatory responses in emotionally charged situations. Our findings highlight substantial variation across model families and conversational behaviors, underscoring the importance of culturally grounded multilingual benchmarks for evaluating socially aligned conversational AI systems.

---


### 43. [Bittensor Agent Arenas as a Trajectory Primitive: Distilling a Shopping Agent from ShoppingBench Subnet Traces](https://arxiv.org/abs/2606.10064)

**<font color=#1a73e8>作者：</font>** Shardul Bansal, Seth Schilbe, Jarrod Barnes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small-model agentic post-training is bottlenecked less by the algorithm than by the trajectory substrate it consumes. Leading recipes (RLVR, group-relative RL, rejection-sampled re-SFT) all need multi-turn traces carrying per-trajectory supervision, and the two existing sources fall short: frontier-synthesised data inherits the synthesizer's biases and collapses the long tail, while unfiltered production logs are unjudged and contaminated by shortcut behaviour. We argue that an incentive-aligned agent arena can be engineered to manufacture such trajectories, and demonstrate this on ORO Subnet 15 (SN15), a Bittensor deployment of the ShoppingBench agentic-commerce benchmark. SN15's race mechanism, LLM reasoning judge, and rotating leak-cluster-guarded problem suite yield a corpus with three properties: incentive-aligned diversity, per-trajectory judging, and anti-memorised held-out evaluation. We introduce a structural-quality filter that converts the raw firehose into a trainable corpus by keeping agentic trajectories (the model itself emits the tool calls) and rejecting sub-task trajectories (the model only classifies or narrates over a deterministic search loop), then post-train Qwen3-4B with a recipe matched to the published ShoppingBench SFT-then-GRPO pipeline. On a leak-cluster-guarded held-out partition scored production-strict, the model lifts from the published Qwen3-4B base of 18.0% ASR to 42.7%, within single-problem noise of the synthetic-data SFT-only baseline (43.6%), while training on a fraction of a single day of subnet output. The supervised stack leaves a large pass@8 to pass@1 gap (53.3% vs 34.8%); a per-step teacher-grounded Dr. GRPO reward converts that headroom into process improvement, and we identify the sub-task firehose as the primary lever for closing the gap to the 48.7% SFT+GRPO bar. We release the filter, the corpus splits, and the arena mechanics.

---


### 44. [LLM-Based Visualization Evaluation: How Well Do Literacy-Stratified Personas Approximate Human Judgments?](https://arxiv.org/abs/2606.10095)

**<font color=#1a73e8>作者：</font>** Swaroop Panda  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Evaluating data visualizations across diverse user populations continues to pose a significant methodological challenge within visualization research. We propose a theorized evaluation framework, Literacy-Stratified LLM Evaluation (LSLE), which formalizes a two-stage process. The first stage involves constructing visualization literacy personas grounded in established frameworks such as VLAT. The second stage directs large language models to adopt these personas as simulated evaluators of visualization artifacts. We ground the framework in an epistemic analysis that characterizes the conditions under which LLM persona simulation may produce plausible proxies for literacy-dependent perception - and, critically, the conditions under which it does not - engaging directly with emerging critiques of LLM-as-participant paradigms from the VIS and HCI literature. To empirically test LSLE's boundaries, we benchmark its outputs against openly available human response data from the validation studies of two established instruments: VLAT and BeauVIS. Using the same stimuli and assessment items as the original human studies, we compare LSLE persona responses across literacy strata against published human distributions and against default (non-persona) LLM baselines. Our analysis reveals where literacy-stratified personas converge with and diverge from human response patterns - identifying task types and evaluation dimensions where persona simulation approximates human variability and where it systematically fails. We discuss implications for the responsible use of LLM-assisted evaluation as a complement to empirical methods, and propose boundary conditions for when LSLE may be most appropriate: early-stage design exploration and rapid comparative screening rather than summative evaluation.

---


### 45. [Emotion Profiling in LLM-Based Literary Translation: Systematic Shifts Across MT and Post-Editing](https://arxiv.org/abs/2606.10113)

**<font color=#1a73e8>作者：</font>** Antonio Castaldo, Johanna Monti, Sheila Castilho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates whether LLM translations exhibit identifiable emotional profiles and how post-editing reshapes them toward human-like norms. We compare LLM translations of Margaret Atwood's Oryx and Crake with their post-edited versions and a human translation, using a large-scale corpus of contemporary Italian science-fiction as a baseline. We examine emotion through lexicon-based and multilingual modeling, conducting a fine-grained analysis of emotional variation across systems. We find that MT systems introduce model-specific and statistically significant emotional fingerprints across translations, leading to a limited preservation of an author's voice.

---


### 46. [BiWM: Advancing Open-Source Interactive Video World Models with Bidirectional Autoregression](https://arxiv.org/abs/2606.10135)

**<font color=#1a73e8>作者：</font>** Shaohao Rui, Xiaofeng Mao, Zhanyu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transitioning bidirectional video diffusion models into an autoregressive paradigm improves the interactivity of video world models, but existing causal pipelines need many stages (control fine-tuning, autoregressive training, causal initialization, few-step distillation) and still trail bidirectional models in quality due to error accumulation. Recent world models such as Yume-1.5 and Matrix-Game-3.0 instead adopt a bidirectional autoregressive approach, gaining fidelity and stable long-horizon rollout from self-correcting error propagation, yet open-source frameworks (e.g., minWM) support only causal models. We present BiWM, the first full-stack framework for interactive video world models under the bidirectional autoregressive paradigm, jointly optimizing generation quality and inference speed. From a pretrained video backbone, BiWM injects camera control by fine-tuning, then runs a few-step Distribution Matching Distillation (DMD) stage that turns the backbone into an action/camera-controllable world model: just two training stages instead of four in minWM, converging in a few hundred steps on 8xH200 GPUs. A single recipe spans Wan2.1-1.3B, Wan2.2-5B, HunyuanVideo-1.5-8B, and LTX-2.3-22B, and also supports secondary fine-tuning of existing bidirectional models. BiWM enables real-world camera control where minWM loses controllability, integrates pluggable history compression (FramePack-style and PackForcing-style) for long rollouts, and offers an optional NVFP4 4-bit training/inference pipeline. To counter DMD's mode-seeking degradation, we add GAN and mass-covering forward-KL objectives that preserve scene dynamics. We open-source BiWM for resource-constrained research and high-fidelity environment simulation.

---


### 47. [DB-3DME: From Dataset to Benchmark for Human-aligned Automatic 3D Mesh Evaluation](https://arxiv.org/abs/2606.10142)

**<font color=#1a73e8>作者：</font>** Nanshan Jia, Zhenyu Zhao, Sui Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D generation have led to substantial improvements in realism, controllability, and efficiency, yet the evaluation of 3D assets remains underexplored. Existing evaluation paradigms, including human evaluation, learned metrics, and vision-language models (VLMs) as judges, suffer from limitations in cost, scalability, resolution handling, or task-specific alignment. In this work, we focus on 3D mesh evaluation and introduce DB-3DME, the Dataset and Benchmark for 3D Mesh Evaluation. DB-3DME contains 2,619 synthetic 3D meshes paired with human ratings on Geometry and Prompt Adherence. Using this dataset, we systematically benchmark state-of-the-art VLMs and identify visual encoding of 3D representations as a key factor for human-aligned evaluation performance. Motivated by this finding, we fine-tune an open-weight VLM, Qwen-2.5-VL-7B, for 3D mesh evaluation by adapting the visual encoder while freezing the language model. The fine-tuned model substantially outperforms existing pre-trained VLMs across multiple evaluation dimensions, establishing a new benchmark for automatic 3D mesh evaluation. We publicly release the benchmark dataset on GitHub and Hugging Face to facilitate future research.

---


### 48. [From Senses to Decisions: The Information Flow of Auditory and Visual Perception in Multimodal LLMs](https://arxiv.org/abs/2606.10147)

**<font color=#1a73e8>作者：</font>** Wish Suharitdamrong, Muhammad Awais, Xiatian Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) can listen and see, but how do audio and visual signals actually travel through the network to shape an answer? Despite their growing role in research and real-world applications, the internal pathways through which audio and visual tokens influence the final prediction remain poorly understood. In this study, we examine audio-visual information flow inside Audio-Visual Large Language Models (AVLLMs), tracing how AVLLMs route, utilize, and integrate audio and visual information across two input configurations, audio-visual video and multiple interleaved audio-visual items. We find that for audio-visual video, AVLLMs follow the sequential information flow pathway established for VLMs and VideoLLMs, with audio and visual contribution flowing along this pathway in proportion to the task's reliance on each modality. In settings with multiple interleaved audio-visual items, this routing shifts to different parallel streams. Furthermore, we demonstrate that audio-visual and other token types can be discarded once their information is transferred to LLM, with minimal impact on the model's prediction or even slight improvement, generalizing across multiple tasks and datasets, enabling more efficient inference. These findings hold across multiple models and scales, Qwen2.5-Omni and Video-SALMONN2 Plus at 3B and 7B scales, leading to hypotheses on why these flow structures emerge. Together, these results deliver the first coherent picture of how AVLLMs orchestrate sound and sight inside the network and lay the groundwork for the next wave of interpretability, design, and efficiency advances in audio-visual and broader MLLMs.

---


### 49. [VArify: A Visual Analytics System for Verifying Knowledge Enhanced Large Language Model Responses in Food Science](https://arxiv.org/abs/2606.10177)

**<font color=#1a73e8>作者：</font>** Sam Yu-Te Lee, Yan To Linus Lam, Manami Nakagawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Graph Retrieval-Augmented Generation (GraphRAG) enables Large Language Models (LLMs) to leverage structured, domain-specific knowledge graph databases for factually grounded responses. However, the retrieval of irrelevant or conflicting data can still result in erroneous responses. In knowledge-intensive and evidence-focused domains, human verification of the supporting evidence for an LLM response is still necessary. We conducted a formative pilot study to characterize the challenges of verifying complex, multi-layered data retrieved by GraphRAG systems. Based on these insights, we present VArify, a visual analytics system that leverages a file directory-inspired tree visualization to support simultaneous exploration of inter-group relationships and intra-group hierarchies within the retrieved evidence. We evaluate VArify through a user study with six food science experts and students. Our results indicate that the system effectively helps users distinguish between an LLM's internal parametric knowledge and external graph-sourced evidence. Furthermore, the visualization helped experts identify inaccuracies within the underlying knowledge graph itself, leading to more calibrated trust in the model's output. We conclude by discussing opportunities to leverage visualizations to further support verification regarding unknown unknowns, personalization, and limitations of knowledge graphs.

---


### 50. [Dropout-GRPO: Variational Stochasticity for Continuous Latent Reasoning](https://arxiv.org/abs/2606.10184)

**<font color=#1a73e8>作者：</font>** Wooil Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) relies on the diversity of $K$ rollouts within each group; otherwise, the group-mean advantage $A^{(k)} = r^{(k)} - \mu_r$ collapses to zero. This presents a structural challenge for latent-reasoning models like Coconut, which feed continuous hidden states recurrently in place of discrete chain-of-thought tokens. Because the latent phase is inherently deterministic given the parameters and prompt, multiple rollouts produce identical trajectories, stalling GRPO's progress. Consequently, applying group-relative reinforcement learning to continuous latent reasoning has proven difficult.
To address this, we propose sourcing the necessary stochasticity through structured dropout. By applying a single Bernoulli mask held constant across all latent recurrence steps for a given rollout, we generate essential trajectory variance. This shared mask effectively treats each rollout as a posterior sample from a variational distribution over parameters, allowing GRPO to optimize the expected reward of a Bayesian model-average policy. We provide both theoretical justification for this method -- including unbiasedness, variance reduction, and the well-definedness of the latent gradient -- and empirical validation. On GSM8K, dropout-GRPO improves a Coconut baseline from $27.29\%$ to $29.01\%$ pass@1, demonstrating the viability of GRPO learning for latent-reasoning models. Our work positions this as a practical, theoretically grounded approach for post-training latent-reasoning LLMs.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
