# 🧠 大模型相关研究 | 2026年08月27日

> 本类共 **190** 篇论文：已确认 **178** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-190](./part-04.md)

---

### 101. ['Ghaib in Translation' aka Unseen Harm: Measuring Cross-Script Safety Inconsistency with 'Missed-in-Urdu' Scores in LLM Hate Speech Detection](https://arxiv.org/abs/2608.24191)

**<font color=#1a73e8>作者：</font>** Fawzia Zehra, Kara-Isitt, Sonal Khosla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Urdu, the world's tenth most spoken language with 246 million speakers, remains almost entirely absent from mainstream LLM safety evaluation and nine years of WOAH proceedings. To investigate whether this absence has measurable consequences for content moderation reliability, five large language models, GPT-4o, Claude Sonnet 4.5, Gemini 2.5 Flash, Qwen-2.5, and Llama-3.1, were tested across six datasets spanning Nastaliq Urdu, Roman Urdu, English, and code-switched Urdu-English. Across the five Urdu-script datasets, label instability between original-script and English-translation classification ranged from 15.9% (Gemini 2.5 Flash) to 31.6% (Qwen-2.5), with a 'Missed-in-Urdu' rate, content flagged as harmful in English translation but passed as normal in the original script, ranging from 2.4% to 9.9% (median 4.3%). A complete enumeration of all 205 papers across nine ALW/WOAH editions via the ACL Anthology API confirms zero dedicated Urdu papers across the entire period. Results indicate that current LLMs provide uneven safety assurance across Urdu's script varieties, with smaller open-weight models showing substantially higher instability and missed-harm rates than frontier closed models.

---


### 102. [Preference Data Selection for Mitigating the Alignment Tax in Large Language Models](https://arxiv.org/abs/2608.24192)

**<font color=#1a73e8>作者：</font>** Minsu Kim, Jianxun Lian, Xing Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning large language models to human preferences is crucial for real-world deployment but frequently incurs an alignment tax, leading to the catastrophic forgetting of pre-trained general capabilities. While previous works primarily frame this problem as an optimization or architectural challenge, the inherent characteristics of preference data that drive this degradation remain largely underexplored. In this paper, we propose BALIGN, a balanced data selection strategy that explicitly mitigates catastrophic forgetting while optimizing alignment efficacy. Through theoretical and empirical analyses of the preference optimization gradient, we identify three key data-centric features that dictate parameter drift: the reference model's log-probability margin, the token length difference between chosen and rejected responses, and the TF-IDF similarity to general capability corpora. By aggregating these orthogonal features into a unified composite risk score, BALIGN systematically filters out high-risk preference samples that disrupt intrinsic model parameters or provide minimal alignment utility. Extensive experiments on standard human preference datasets demonstrate that BALIGN strongly preserves foundational capabilities without compromising alignment gains, consistently achieving the optimal Pareto frontier with minimal computational overhead.

---


### 103. [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212)

**<font color=#1a73e8>作者：</font>** Yumeng He, Yichen Song, Xiaotian Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advancement of Embodied AI necessitates high-quality simulation assets that faithfully mirror the real world. However, transforming raw visual observations into simulation-ready scenes remains challenging due to the lack of physical grounding and scene-level interactivity in current image-to-URDF methods. We propose NeoWorld-Pro, a framework that reformulates monocular scene reconstruction as procedural programming for interactive 3D environments. Leveraging the zero-shot reasoning and code synthesis capabilities of MLLMs, NeoWorld-Pro converts a single RGB image into executable programs specifying object geometry, articulation, and physical properties. A physics-in-the-loop mechanism then iteratively refines the generated programs by validating their execution in a physics engine, enforcing physically plausible articulations, valid object compositions and interactions, and accurate spatial relationships. Experiments show that NeoWorld-Pro outperforms open-loop and prior monocular reconstruction methods, while enabling complex downstream tasks such as stable stacking and fine-grained manipulation.

---


### 104. [MetaRAG: Belief-Action Aligned Policy Optimization for Agentic RAG](https://arxiv.org/abs/2608.24214)

**<font color=#1a73e8>作者：</font>** Qiuyi Qi, Tian Liang, Jiamu Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval-augmented generation (RAG) requires language models to decide when to continue searching and when to answer. Existing RL-based methods rely on external supervision and overlook the agent's internal belief about whether the current evidence is sufficient. To address this problem, we reformulate the search decision quality as belief-action alignment and propose MetaRAG, a belief-action aligned policy optimization framework for agentic RAG. MetaRAG uses Verify-first Action Generation to elicit an explicit verification process before each actual action, and Internal Belief Probing to estimate the policy model's own answerability belief from the same question-history context. Based on these, MetaRAG derives a consistency reward that is further gated by answer correctness, avoiding reinforcement of internally consistent but incorrect trajectories. The belief probe is used only during training and introduces no inference-time overhead. Experiments on seven public QA benchmarks show that MetaRAG consistently improves the accuracy-efficiency trade-off over strong RL-based agentic RAG baselines, with gains that transfer to deep research settings, different optimizers, and multiple model backbones.

---


### 105. [Agentopia on a Consumer GPU: A Reduced-Scale Long-Horizon Port with an 8B Model](https://arxiv.org/abs/2608.24215)

**<font color=#1a73e8>作者：</font>** Luo Huan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent social simulation has demonstrated compelling results, but Agentopia was evaluated with 100 agents over 10 simulated years using Qwen3.5-397B-A17B, leaving the behavior of reduced-scale deployments on consumer hardware unclear. In this paper, we implement and evaluate a reduced-scale Agentopia port on a single NVIDIA RTX 5070 Ti(12 GB VRAM) using Qwen3-8B-AWQ, a 4-bit quantized model. We introduce three structural adaptations for this setting: (1) system-managed layered memory compression, (2) four activity blocks per simulated day, and (3) explicit physical- and mental-health state variables. Across three independent stochastic runs, two runs completed 52 weeks and the third completed 50 weeks before reaching the context limit, totaling 154 system-weeks (770 agent-weeks). No agent died,and no threshold-based health warning was logged; activity records containing at least one NO_RESPONSE field occurred at rates of 10.15-10.29% across runs. A 52-week memory-off run tied L2/L3 artifact production to layered memory; a separate 10-week comparison associated four daily time blocks with 2.72 times more finalized records and lower lexical duplication, but a higher missing-field rate. These comparisons do not support causal behavioral claims. We release validated configurations, derived audits, analysis scripts, aggregate figure data, and our implementation changes in a public fork; raw runs and initial persona data are excluded because their redistribution provenance is not fully resolved.

---


### 106. [Constraint-Guided Enterprise Data Mapping with Large Language Models](https://arxiv.org/abs/2608.24218)

**<font color=#1a73e8>作者：</font>** Sebastian Monka, Pramod Anantharam, Thien Vo Minh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise entity alignment must handle semi-structured records, implicit attributes, and unit or granularity mismatches. Manual matching is still common in practice, but does not scale as schemas and providers evolve. LLM-only matching improves semantic recall, yet can violate structural and physical invariants, producing fluent yet operationally invalid correspondences.
We propose constraint-guided mapping (CGM), a neuro-symbolic method with three stages: (i) schema-grounded admissibility constraints with metadata mc = <tau_c, delta_c>, where tau_c denotes the constraint type and delta_c provides executable relation and normalization logic; (ii) constraint-restricted candidate generation with cascade relaxation to guarantee a nonempty feasible set under noise; and (iii) neural ranking with bounded LLM disambiguation restricted to that feasible set.
Methodologically, constraints operate as hypothesis-space operators rather than post-hoc validators, enabling controlled degradation under relaxation and auditable, human-guidable decisions. On a controlled structural-decoy benchmark, hard admissibility shrinks the candidate space by ~480x without dropping the GT, and a layer-by-layer ablation shows this gate, not the LLM, is the decisive lift (F1 0.08 to 0.66). The benefit is model-independent and adds no extra inference cost: a small model with constraints matches a frontier LLM used without them at ~28x lower cost. The method, not a single tuned configuration, transfers across seven enterprise makes (macro F1 0.70), each under its own automatically discovered, expert-refinable constraints, and lowers expert effort by ~7x versus spreadsheet workflows. Public Valentine results add an external ranking sanity check and mark the boundary: constraints should be hard only where structural invariants are match-determining.

---


### 107. [Measuring Digital Labour Market Transitions with a Digital Semantic Score: An AI-Based Methodology Applied to the Dutch Labour Market](https://arxiv.org/abs/2608.24222)

**<font color=#1a73e8>作者：</font>** Sadegh Shahmohammadi, Xavier Pinho, Mairi Bowdler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The digital transformation of the Dutch labour market is reshaping occupational language, career pathways, and job-related skills. Addressing these changes requires granular labour market intelligence. This paper develops an AI-based methodology to analyse digitalisation using data covering millions of Dutch job profiles. The methodology combines embedding-based similarity search and large language model classification to map unstructured job information to harmonised ESCO occupations. We also introduce a Digital Semantic Score that measures how strongly job titles and skills are associated with digital concepts relative to a non-digital reference. Using embeddings and cosine similarity to transparent digital and non-digital anchor groups, this indicator moves beyond keyword-based approaches by capturing broader digital meanings in occupational language and worker skill profiles. It enables analysis across occupations, career transitions, emerging job-title vocabulary, and skill digitality. The findings reveal that digitalisation is unevenly distributed across the labour market. Digital job-title language is most prominent among managerial, professional and ICT-related occupations, but is increasingly visible in hybrid business, marketing and automation-related roles. Career-transition analyses show that movement toward digital work is pathway-dependent, while skill analyses highlight the multidimensional nature of digital capability, encompassing technical, hybrid and business-systems skills. By combining profile data, AI-supported occupational classification and semantic scoring, this study advances AI-driven labour market analytics and provides a scalable framework for monitoring digital labour market change. The methodology helps identify emerging skill needs, support reskilling strategies, and inform policies addressing skills mismatches and labour shortages in the Netherlands.

---


### 108. [Aura: Dynamic Intra-Turn Emotion-Aware Adaptation of Large Language Model Responses](https://arxiv.org/abs/2608.24224)

**<font color=#1a73e8>作者：</font>** Rachel Schuchert, Christian Holz  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective human-AI interaction requires systems that dynamically adapt to a user's behavior and evolving understanding. When users interact with Large Language Models (LLMs), these models typically respond to prompts without sensing the user's immediate reactions. This lack of communicative synchrony can lead to information overload or leave confusion unresolved in real time. In this paper, we introduce Aura, a framework that enables LLM systems to dynamically modulate output based on a user's evolving emotions. Aura's Perception Module continuously estimates the user's emotional state from facial expressions. Our Policy Module then selects interventions through a probabilistic belief model. Finally, Aura's Generation Module uses parameter-efficient Low-Rank Adaptation (LoRA) adapters to produce contextually tailored responses mid-turn during response generation. We evaluated Aura in a within-subjects user study (N=20) on information-seeking tasks, where it achieved statistically significantly higher normalized perceived learning gains than a Llama-3 baseline and reduced interaction time by 21% relative to existing LLM baselines (GPT-4o, Llama-3). Our results indicate that real-time, context-sensitive interventions can improve learning efficiency and user satisfaction without observable degradation in factual accuracy. Aura thus supports the potential for more responsive and effective human-AI interaction.

---


### 109. [Evaluating Multiple LLM Generations with Validated Task Coverage](https://arxiv.org/abs/2608.24228)

**<font color=#1a73e8>作者：</font>** Florian Le Bronnec, Rio Yokota  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many LLM applications are most useful when they provide several candidate outputs for comparison, validation, or combination. Predominant evaluation settings, however, still focus on individual outputs or reduce multiple samples to a single success or selected answer. This can miss whether the outputs include several genuinely different useful results. We introduce VTC-Bench, a five-domain benchmark for this setting, together with Validated Task Coverage (VTC) as its core evaluation quantity. The benchmark is built from carefully selected real-data tasks where both output quality and task-relevant distinctness can be checked automatically and reproducibly, without model-based judges. VTC measures how many distinct useful results are obtained within $k$ attempts. Across multiple models and inference settings, the benchmark leads to different conclusions from conventional evaluation: configurations that look strongest from single-draw quality are not necessarily those with the best coverage, and simple measures of output variation do not reliably recover task-relevant coverage. These results show that finite candidate sets can be evaluated directly as objects of interest, revealing differences in model behavior that are not apparent from conventional per-output evaluation.

---


### 110. [RecurSE: Bounded Recursive Self-Evaluation for LLM Rubric Judges](https://arxiv.org/abs/2608.24231)

**<font color=#1a73e8>作者：</font>** Kaiyuan Liu, Ziyuan Zhuang, Rongxiang Weng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge is essential for evaluating open-ended text and steering post-training, yet improving the judge itself typically relies on expensive annotations, reward models, or distillation from stronger teachers. In this work, we eliminate external gold supervision from the RL training reward: the model's own evaluative capability generates learning signals for its optimization -- a closed-loop setting of bounded recursive self-improvement (RSI) termed Recursive Self-Evaluation (RecurSE). We study two central questions: when can self-improvement occur, and when must it stop? First, RecurSE pairs a trainable judge evaluating candidate responses under per-rule rubrics (Pass 1) with a synchronized policy-copy checker that audits the judge's reasoning against meta-rubrics to supply a scalar process reward (Pass 2). To enable learning, interface decoupling structurally isolates the checker's scalar score from the judge's verdict tokens, eliminating a degenerative token-copying shortcut that inflates self-assigned rewards. Second, because unanchored recursive learning is inherently bounded, Pairwise Advantage Validity (PAV) serves as an unbiased validation monitor that jointly tracks judge accuracy and checker fidelity to reliably identify the optimal early-stopping window. Across Qwen3.5-9B, Gemma-4-E4B-it, and Qwen3.6-27B, RecurSE achieves consistent generalization gains across held-out medical, pairwise, summarization, and professional benchmarks. Ablations demonstrate that synchronized judge-checker co-evolution outperforms frozen checkers, external meta-judges, self-consistency, and scaled teacher distillation. Furthermore, preference pairs curated by our judge effectively enhance downstream policy alignment. Bounded RSI for LLM-as-judge is thus viable when self-produced reward validity is explicitly decoupled and monitored.

---


### 111. [TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models](https://arxiv.org/abs/2608.24232)

**<font color=#1a73e8>作者：</font>** Zhenyu Wu, Siyuan Chen, Changchun Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) generate intermediate reasoning traces that may contain unsafe content, even when their final responses appear safe. Guardrail models are designed to detect and block unsafe content, yet existing benchmarks for unsafe content detection focus primarily on prompts and final responses, leaving reasoning traces largely unexamined. Moreover, these benchmarks typically provide only binary safety labels, without evidence annotations that justify the judgments. To address these limitations, we introduce TRACE, an evidence-grounded safety evaluation benchmark that covers the entire LRM inference pipeline: prompts, reasoning traces, and final responses. TRACE includes prompts in two languages spanning nine risk categories and ten attack strategies. For each prompt, four LRMs generate reasoning traces and final responses, and we annotate the safety of each component and extract supporting evidence from the corresponding source text. Evaluating 18 guardrail models on TRACE reveals that safety judgment for reasoning traces is substantially more challenging than for prompts or final responses, and that current models struggle to accurately extract supporting evidence. These findings highlight the need for guardrail models that can reliably detect and precisely localize unsafe content across the LRM inference pipeline.

---


### 112. [SA-Bench: Evaluating Semantic Alignment in LLM-Based Paper Reproduction](https://arxiv.org/abs/2608.24252)

**<font color=#1a73e8>作者：</font>** Xue Hu, Zewei Pan, Zeli Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents can generate paper reproduction code, yet often produce scientifically unfaithful implementations. We define this failure mode as semantic drift, where generated code silently diverges from the paper's specifications. We introduce SemanticAlign-Bench(SA-Bench), a diagnostic benchmark covering 30 papers from ICLR, ICML and NeurIPS 2025. For each paper, we decompose its specifications into atomic and verifiable implementation claims, which we call Semantic Alignment Units (SAUs) and evaluate repositories along four diagnostic dimensions spanning numerical, methodological, protocol and ordering drift. In total, we construct 1,491 SAUs across five ML domains and evaluate 12 generator configurations (4 models $\times$ 3 scaffolds). Even the strongest configuration (Claude+PaperCoder) achieves a mean SAU score of only 0.301 out of 1.0, with an overall mean of 0.221 across 360 evaluations. A failure taxonomy reveals that agents attempt most requirements but implement them incorrectly, with implementation mismatch and stubs accounting for the majority of zero-scored claims. Our analysis further indicates that scaffolds optimized for executability provide limited leverage for scientific reproduction; narrowing the gap requires scaffolds that prioritize semantic specification verification. The benchmark, annotations and evaluation pipeline are publicly available.

---


### 113. [Beyond Accuracy: A Dual-Judge Evaluation Protocol for Vision-Language Models in Legally Grounded Tasks](https://arxiv.org/abs/2608.24258)

**<font color=#1a73e8>作者：</font>** Su Myat Noe, Ha Thanh Nguyen, May Myo Zin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly evaluated for legally accountable settings, where correct outputs must also be justifiable against an applicable legal standard. Existing legal-AI benchmarks and LLM-as-judge protocols provide important infrastructure for measuring task performance and open-ended response quality. We contribute one additional evaluation signal: a dual-judge protocol that pairs a standard 0-10 quality judge with a strict binary semantic-equivalence judge against a human-curated reference.
We study a controlled, visually grounded regulatory task - UK traffic-sign interpretation, whose meaning is a codified question with a known reference for every input - and measure not merely whether the two judges disagree (by construction they must) but how much and where. On 4,680 evaluations under seven visibility levels and two occlusion modes, the two judges are moderately associated (point-biserial r = 0.644), while revealing an asymmetric Type II pattern affecting 8.0% of all evaluations.
Its distribution is instructive: the marginal rate peaks at high visibility (14.2% at v = 0.8) simply because high-scoring answers are common there, but conditioned on the answer already scoring above 7, the rate is highest under heavy occlusion (54-63% at v <= 0.3), so a high quality score is least trustworthy when the input is most degraded.
We are explicit that the signal is a property of this judge and reference: a 49-row human check shows the 0-10 judge aligns closely with everyday-reader judgement (Pearson r = 0.81; r = 0.80 with the LLM accuracy sub-score), while the equivalence judge is fairly but one-directionally stricter. The protocol adds one LLM call per evaluation and surfaces a signal single-judge protocols do not report. We release the prompt template, occluded variants, and full evaluation results.

---


### 114. [Real-World Knowledge-Guided Change Data Synthesis for Remote Sensing](https://arxiv.org/abs/2608.24263)

**<font color=#1a73e8>作者：</font>** Yaoyi Qi, Xingxing Weng, Chao Pang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Change data synthesis provides a cost-effective solution for expanding training data and improving the performance of change detection models. However, existing synthesis methods typically rely on handcrafted rules to simulate changes, where limited coverage of class transitions restricts the diversity of synthesized data, while predefined transition designs limit their flexibility in accommodating varied change types. In this work, we introduce KnowChange, a knowledge-guided change data synthesis framework that leverages pretrained vision-language models as knowledge sources to reason about plausible change locations and class transitions from pre-change scenes and desired change types. By integrating knowledge-guided change simulation with generalizable synthesis models, KnowChange enables flexible synthesis of diverse change types within a unified framework. Extensive experiments demonstrate that KnowChange-generated data consistently outperforms existing synthetic datasets in both synthetic-to-real transfer and synthetic data augmentation, despite being generated at a compact scale. Further analyses show that the knowledge-guided change simulation can be seamlessly integrated into existing synthesis pipelines and enhance the downstream utility of synthesized data.

---


### 115. [ROBE: Reversed-Order-Biased-Experts for Extracting Extreme Long-tail Events from Historical Texts](https://arxiv.org/abs/2608.24268)

**<font color=#1a73e8>作者：</font>** Stella Verkijk, Piek Vossen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper proposes methods to extract over 50 types of events from a Dutch historical corpus spanning the 17th and 18th centuries. The methods we propose aim to tackle the impossible: extracting the long-tail of the long-tail. Historic data from before the 19th century is in itself a niche domain not covered in the pre-training of Large Language Models, and we aim to extract events only very scarcely annotated in the training data available for this domain. We propose creating expert classifiers for subgroups of the events present in the training data. We make these groupings based on similar frequency in the training data or on semantic relatedness. Experts trained on underrepresented events are assigned higher priority when predicting to avoid being dominated by frequency biases. We refer to this new way of combining classifiers, specifically tailored to protect the long-tail, as ROBE: Reversed-Order-Biased-Experts. We also propose a controlled method to create domain-specific synthetic data. Our two implementations of ROBE outperform a simple fine-tuned encoder model with a .10 increase in recall and a .16 increase in precision respectively. The best model achieves a .10 increase in f1 for a group of long-tail classes in our niche data set.

---


### 116. [RePolicy: Reinforcement Learning for Safety-Policy Invocation in Agent Safeguards](https://arxiv.org/abs/2608.24275)

**<font color=#1a73e8>作者：</font>** Houcheng Jiang, Boxuan Zhang, Qiyong Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safeguarding language model agents requires assessing complete execution trajectories under context-dependent safety policies. Existing policy-aware safeguards mainly rely on prompting or supervised fine-tuning, limiting their ability to adapt to unseen trajectories and changing policy contexts. We propose RePolicy, an agent safeguard that learns safety-policy invocation through reinforcement learning. Given an agent trajectory and a dynamic policy library, RePolicy invokes the applicable policy and uses its content to produce a policy-grounded rationale and safety judgment. We construct PolicyTraj-20K to support supervised initialization, followed by GRPO with verifiable rewards and policy-context perturbation. Experiments across six agent safety benchmarks show that RePolicy achieves strong overall safety-detection performance and robust policy invocation under varying policy contexts.

---


### 117. [ReproAgent: Contract-Guided Paper-to-Code Reproduction](https://arxiv.org/abs/2608.24291)

**<font color=#1a73e8>作者：</font>** Xue Hu, Zewei Pan, Zhongyuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Paper-to-code reproduction asks scientific AI agents to turn research papers into executable repositories that preserve the paper's method, protocol and artifacts. This is difficult because the specification is split: explicit paper content such as algorithms, metrics and artifacts is often lost across long agent trajectories, while implicit details such as framework defaults and conventions inherited from related work are absent from the paper. We introduce ReproAgent, a four-stage Prepare--Plan--Generate--Repair pipeline built around a persistent implementation contract with two channels: an implementation-requirement channel that turns paper snippets into code obligations, and a reference-evidence channel that retrieves content and structure evidence from related repositories. Both are bound to work packages, projected into file-level contracts, and consumed across generation and repair. On PaperBench Code-Dev, ReproAgent reaches the highest mean score among same-backbone scaffolds under both Claude-Sonnet-4.5 and Gemini-3-Flash. End-to-end channel ablations and per-paper cases support the contribution of both channels. Code and experimental artifacts are publicly available.

---


### 118. [When AI "Works," When Does Help Begin?: Intergenerational Support Around Older Adults' LLM Usage](https://arxiv.org/abs/2608.24297)

**<font color=#1a73e8>作者：</font>** Hyehyun Chu, Yuri Lee, Yeon Su Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLMs are becoming part of everyday life, including for older adults (OAs). OAs often learn digital technologies with younger family members, who have traditionally served as "warm experts" providing trusted and personalized operational help. LLMs expand this role: family supporters may also help OAs judge appropriate uses, consider what information to disclose, assess the credibility of outputs, and decide when AI-generated advice is safe to act on. We conducted a formative qualitative study with six OAs and seven younger adults (YAs), using semi-structured interviews and scenario-based think-aloud activities. OA participants described using LLMs to lighten their recurring reliance on family, while preserving family as a selectively invoked support channel. However, because LLMs rarely produced visible operational breakdowns, YAs had limited signals for when support was actually needed. Instead, YAs relied on OAs' partial disclosures and negotiated intervention through general warnings and self-imposed action boundaries. As a result, family support often solved an immediate problem without leaving reusable calibration knowledge for future use. Based on these findings, we propose design implications for intergenerational LLM support (e.g., consentful help requests, learning-oriented family support that preserves OA task ownership).

---


### 119. [Contrastive Branch Policy Optimization](https://arxiv.org/abs/2608.24300)

**<font color=#1a73e8>作者：</font>** Ying Wang, Changlin Qiu, Bang Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) enables language models to learn multi-turn interaction with external tools, yet its sparse outcome rewards provide no signal for identifying which intermediate decisions are responsible for success. Branch sampling induces local comparisons among alternative continuations, but existing methods tend to conflate two distinct problems: allocating a fixed rollout budget and translating branch outcomes into token-level credit. We introduce Contrastive Branch Policy Optimization (CBPO), which disentangles these two problems and assigns a dedicated mechanism to each. Generation entropy screens candidate branch positions across the entire response, while path-level and node-level decay distribute a fixed budget across trajectories and positions to prevent exploration from collapsing onto a few paths or adjacent tokens. A parent trajectory together with the branches that share an identical token prefix forms an exact-prefix group, and the reward variation within this controlled group defines the Contrastive Branch Value (CBV), an outcome-based estimate of local decision sensitivity that rescales continuation advantages without altering their sign. When multiple nodes are selected along the same trajectory, CBPO partitions it into non-overlapping credit segments, thereby avoiding duplicated gradients on shared tokens. Requiring only outcome rewards and no process-level annotation, CBPO provides a practical solution for fine-grained credit assignment in tool-integrated agent training. Extensive experiments on ten benchmarks, including five for mathematical reasoning and five for knowledge-intensive search, show that CBPO consistently outperforms state-of-the-art policy-optimization and branch-based methods, attaining the highest macro-average accuracy in both domains and across two model scales.

---


### 120. [VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models](https://arxiv.org/abs/2608.24302)

**<font color=#1a73e8>作者：</font>** Guoyang Xu, Hao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-video understanding depends critically on how a limited model context is constructed from a much longer video. Existing approaches improve this process through compression, retrieval, memory, and agentic evidence acquisition, but these mechanisms are typically introduced as part of a manually designed inference system or optimized together with other components. This makes it difficult to isolate a simpler question: how much can be gained by improving the executable context-construction program alone? We study this question through VIDEOHARNESS-RSI, a controlled baseline for recursively searching executable context constructors around a frozen vision-language model (VLM). An outer-loop proposer uses prior programs, evaluation outcomes, and execution traces to generate candidate harnesses, which are executed and evaluated end to end before successful variants are retained for further search. This makes long-video understanding a controlled instance of automated harness design: the searchable object is executable program structure, while the answering model and interface remain fixed. Starting from uniform sampling, recursive harness search consistently finds room for improvement and surpasses several weaker hand-crafted baselines. Starting instead from a stronger hand-crafted baseline, the same RSI process yields a further improvement. The selected harness also transfers to additional long-video benchmarks without further search. Together, these results establish executable context construction as a distinct optimization layer and provide a reproducible baseline for studying harness discovery and transfer around frozen VLMs.

---


### 121. [SENSESHIFT: Continuous Sentiment-Controlled Text Generation via Encoder-based Mask Infilling](https://arxiv.org/abs/2608.24304)

**<font color=#1a73e8>作者：</font>** Shahed Masoudian, Markus Frohmann, Emmanouil Karystinaios 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent controllable text generation (CTG) for sentiment control has largely focused on decoder-based large language models, making causal attention the dominant paradigm. While effective for fluent generation, these models still struggle to satisfy complex constraints and follow fine-grained sentiment signals specified by users. Existing sentiment-aware CTG methods typically simplify the problem by treating sentiment either as a coarse categorical label (e.g., positive or negative) or as a single fine-grained control signal applied to an entire document. Consequently, more challenging settings such as sentence-level sentiment control within long-form text remain underexplored. To address these limitations, we introduce SenseShift , an encoder-based framework for fine-grained sentence-level CTG. Unlike standard decoder architectures, SenseShift leverages bidirectional attention, quantized sentiment signals, and iterative mask infilling to generate local sentences conditioned on target sentiment intensity. Empirical evaluations on story and review generation demonstrate that SenseShift achieves stronger sentiment controllability while maintaining text quality and robustness to out-of-domain generation compared to larger decoder-based baselines.

---


### 122. [OPDSearch+: On-Policy Distillation with RL Refinement for Search-Augmented Reasoning](https://arxiv.org/abs/2608.24310)

**<font color=#1a73e8>作者：</font>** Qinglin Ye, Zhiyuan Gu, Jingjie Xia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search-augmented reasoning remains difficult for small language models. On-policy distillation (OPD) from trained teachers offers a promising direction, but suffers from two issues: (1) high-quality multi-turn search trajectories depend on dynamic retriever responses, making SFT data prohibitively expensive to collect at scale; (2) task-specifically trained teachers incur substantial training cost, while directly applying OPD with an off-the-shelf teacher without task-specific fine-tuning constrains the student to the teacher's performance ceiling and suffers from severe training instability. We propose OPDSearch+, the first distillation paradigm that requires no teacher fine-tuning for search-augmented reasoning. We investigate the role of a frozen off-the-shelf instruct model as the teacher in on-policy distillation, and reveal a key insight: the teacher reshapes the student's policy distribution so that subsequent RL converges to a superior solution that RL alone cannot reach. In stage one, the student interacts with a live search engine and is distilled via a per-position forward KL objective, transferring reasoning decomposition and evidence integration skills without any task-specific teacher training. In stage two, RL refines the distilled student from a richer behavioral foundation, achieving performance that RL alone cannot reach from scratch. Across seven QA benchmarks, OPDSearch+ with a 3B model consistently outperforms all prior 3B RL baselines, achieving gains of 13.1% on HotpotQA and 8.5% on 2WikiMultihopQA.

---


### 123. [Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight](https://arxiv.org/abs/2608.24314)

**<font color=#1a73e8>作者：</font>** Anupam Purwar, Shashank Singh, Kritika Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating conversational voice agents at scale re- quires reliable assessment methods that capture both observ- able interaction quality and the contextual judgment typically provided by human evaluators. We investigate LLM-as-a-Judge evaluation by comparing human judgments with GPT-4.1 and GPT-5 on telecom and retail voice-agent conversations, across conversational quality and safety dimensions. The same interac- tions are scored under three evaluation configurations, p0, p1, and p2, to test whether automated judgments are sensitive to the evaluation setup and whether observed patterns generalize across configurations and judge models. Beyond aggregate agreement, we examine metric-level correlations, evaluator consistency, and systematic human-LLM disagreement to identify which conver- sational attributes can be judged reliably by automation and which remain sensitive to interpretation and context. Effective voice-agent evaluation is also shaped by pipeline-level factors such as speech generation, streaming, and error propagation across ASR, reasoning, and tool-calling stages, motivating our focus on comparing how human and LLM judges score the same interactions end to end. Our results show that LLM- based evaluation can serve as an effective component of large- scale voice-agent assessment, but that its reliability is metric- and configuration-dependent rather than uniform. This pro- vides an empirical framework for identifying which metrics suit automated evaluation and supports hybrid pipelines in which LLM judges handle scalable assessment while human evaluators remain engaged for metrics that demand contextual interpretation and higher-confidence judgment.

---


### 124. [SonarLLM: A Native Sonar--Optical Multimodal Large Language Model for Underwater Perception](https://arxiv.org/abs/2608.24325)

**<font color=#1a73e8>作者：</font>** Cong Su, longxuan ma, Ling Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable underwater perception requires complementary sensing under variable visibility. Optical cameras capture appearance and semantics but degrade rapidly with turbidity, whereas imaging sonar preserves geometry while exhibiting distinct range-azimuth structure and acoustic artifacts. Existing MLLMs, built primarily on optical encoders, are therefore ill-suited to model sonar or adaptively exploit sonar-optical complementarity. We propose SonarLLM, a sonar-optical MLLM that treats sonar as a native perceptual modality. It combines a sonar-specific encoder, modality-specific physics-aware feature enhancement, and reliability-aware hierarchical fusion to align acoustic structure with optical semantics and dynamically adjust their contributions as sensing quality changes. We also introduce SonarBench, a paired benchmark that spans four tasks: recognition, counting, visual question answering, and captioning; and, across the benchmark, three input settings: sonar-only, optical-only, and fusion. By fixing the scene and sonar observation while varying optical degradation, SonarBench enables controlled measurement of cross-modal complementarity. SonarLLM achieves 72.0% macro accuracy across sonar-only recognition, counting, and VQA, outperforming the strongest baseline by 34.4 percentage points, and 68.7% under fusion, exceeding the best baseline by 25.1 points. For recognition and counting, the fusion-over-optical gain grows from 6.0 to 36.0 points as turbidity increases, indicating the increasing complementary value of sonar under controlled optical degradation. Together, these results show that robust heterogeneous perception depends not only on adding sonar, but on representing and weighting it according to its sensing characteristics.

---


### 125. [Speech-to-SOAP: End-to-End Summarization of Medical Dialogues: KIT@BeTraC 2026](https://arxiv.org/abs/2608.24327)

**<font color=#1a73e8>作者：</font>** Enes Yavuz Ugan, Fabian Retkowski, Yuka Ko 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the advent of Large Language Models and its instruction following capabilities a promising application is the task of summarization. Within this domain of task the extractive sub-task of clinical protocolling has emerged as a topic of particular interest as it can significantly reduce the downtime and protocolling burden of health-care workers thus enabling them to focus on their core work helping humans. A further step towards automation is the direct generation of clinical notes from speech without intermediate transcripts, reducing processing time while preserving information such as coughing or other paralinguistic cues that may be lost in transcript-based systems. To this end, we present KIT's submission to this years BeTraC challenge in the lightweight track. Our main contribution is a scalable data augmentation pipeline that unifies heterogeneous medical dialogue datasets through synthetic speech generation and automatically generated SOAP supervision, enabling robust adaptation of a speech foundation model for end-to-end speech-to-SOAP generation.

---


### 126. [How Do Professional Editors Evaluate the Editing Quality of AI-Generated Cinematic Video Ads?](https://arxiv.org/abs/2608.24329)

**<font color=#1a73e8>作者：</font>** Po-Ming Law, Weizhi Li, Arpit Narechania  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> On social media, we often encounter short-form video ads that employ cinematic editing techniques to evoke an emotional response. While AI tools are beginning to generate such cinematic ads automatically, we lack a fine-grained framework for evaluating these ads. In this paper, we first characterize social media video ad formats and identify cinematic ads as a recurring format in our corpus. We then analyze the duration, shot structure, audio and text elements, and editing techniques of cinematic ads to inform a two-stage generation pipeline in which an LLM first generates a shot plan and a video generation model renders the video. Using this pipeline, we generated 70 cinematic ads for 35 real brands and recruited professional video editors to critique their editing choices. From their critiques, we derive six dimensions of editing quality: narrative progression, audiovisual coordination and sound design, visual composition and graphics, shot-to-shot continuity, message and brand coherence, and temporal rhythm and pacing. We discuss how these dimensions can guide editing-aware generation, human evaluation, and automated evaluation of AI-generated cinematic ads.

---


### 127. [SteerCheck: Attribution Specificity and Alignment Leakage in Activation-Steering Audits](https://arxiv.org/abs/2608.24335)

**<font color=#1a73e8>作者：</font>** Daming Luo, Christy Liang, Junyu Xuan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering can change behaviour without establishing that the effect is specific to the intended concept. We introduce SteerCheck, a preregistered attribution audit that matches off-target KL and separates mean, protected-tail, polarity, transfer, and semantic claims. Exact replay of 960 Qwen3-14B interventions reveals complementary limits of common controls: isotropic directions occupy a narrow near-orthogonal region, whereas sign-randomized same-construction directions often retain substantial target alignment. Effect is strongly associated with signed cosine within the sign-randomized family ($\rho=.94$); $25.3\%$ of its draws exceed cosine $.5$, and every draw exceeding the observed mean effect has cosine above $.80$. This alignment leakage does not by itself invalidate a conditional randomization test; it limits what the comparator can distinguish and motivates reporting exchangeability assumptions, a construction diagnostic $A$, and the empirical cosine distribution. The primary Qwen complete gate remains negative because the protected tail fails all families. On independent data, continuous margin transfers only in Qwen and accuracy transfers in no selected cell. Prospectively registered language controls pass the complete gate in Qwen and DeepSeek, while a passing DeepSeek detox comparator rules out categorical separation; all nominal passes are sensitive to $\Gamma=1.10$. Frozen three-rater open-generation evaluation supports factual correction in DeepSeek but not Qwen; the automatic judge fails calibration (macro-F1 $.562$), so null-wide semantic results remain descriptive. SteerCheck makes these conditional and mixed conclusions auditable.

---


### 128. [Selective Regenerative Decoding: Trajectory-Level Intervention for Inference-Time Reasoning](https://arxiv.org/abs/2608.24338)

**<font color=#1a73e8>作者：</font>** Sophia Xiao Pu, Yumo Xu, Sailik Sengupta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference-time decoding methods improve LLM reasoning by exploring multiple candidate trajectories, yet treat each trajectory as atomic: either retaining it whole or discarding it irreversibly. This wastes computation on partially promising candidates whose high-quality prefixes are abandoned alongside degraded suffixes. We introduce Selective Regenerative Decoding (SRD), which routes each candidate to discard, keep, or refine only the degraded portion of the suffix while preserving the useful prefix of borderline candidates, without requiring a larger target model. Under mild assumptions, SRD achieves a provable 1.28-to-1.36-fold gain in sample efficiency over rejection sampling with strictly higher expected trajectory quality, with the gain growing as the candidate pool grows. Across MATH500, GPQA Diamond, HotpotQA, and AlpacaEval with multiple generation-reward model pairs, SRD matches Best-of-N accuracy with substantially fewer generated tokens and outperforms speculative rejection in low-compute regimes. By enabling segment-level intervention rather than whole-trajectory selection, SRD opens a previously underexplored region of the accuracy-compute tradeoff for inference-time reasoning.

---


### 129. [FARCA: Fact-Aligned Reliability-Aware Credit Assignment for Reinforcement Learning with Factual Supervision](https://arxiv.org/abs/2608.24350)

**<font color=#1a73e8>作者：</font>** Qiming Xie, Wenjie Zheng, Xiangqing Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To reduce the hallucination risk caused by outcome-driven rewards in large language models trained through reinforcement learning with verifiable rewards, existing mitigation approaches introduce process-level factual supervision. However, due to coarse-grained aggregation of factual signals and the lack of reliability assessment for these signals, they create a mismatch between fact verification and policy updates. We term this noisy factual credit assignment and decompose it into two aspects: credit localization ambiguity and credit reliability ambiguity. To address these issues, we propose FARCA (Fact-Aligned Reliability-Aware Credit Assignment), a policy optimization framework that transforms factual supervision into localized, reliability-weighted token-level training signals. FARCA achieves fine-grained credit localization by aligning the granularity of fact verification with that of policy updates. It further introduces counterfactual evidence attribution, which uses the dependence of a factual judgment on key evidence as an empirical proxy for verification reliability to compute reliability weights. These weights modulate factual rewards and local policy advantages, reducing the influence of potentially unreliable signals on policy optimization. Experiments across different models and multiple factual reasoning benchmarks show that FARCA significantly improves model factuality while preserving general reasoning capabilities.

---


### 130. [The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents](https://arxiv.org/abs/2608.24358)

**<font color=#1a73e8>作者：</font>** Roy Ganz, Mor Shpigel Nacson, Adi Kalyanpur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents perform long-running tasks spanning dozens of model calls, tool uses, and code edits. As these runs unfold, users face a practical cost-quality trade-off: escalating to a stronger model when a cheaper one struggles, or downshifting once the hard reasoning is complete. Each switch requires the receiver to continue a non-native trajectory produced by another model. We study how this handoff affects quality and cost, and how varying the trajectory information inherited by the receiver changes the outcome. Using pairs of low-cost, low-capability (LC) and high-cost, high-capability (HC) models from the Claude and GPT families, we vary handoff direction, timing, and interface, comparing full-trajectory transfer, compaction, and trajectory removal while preserving the repository state. Across both model families, full-trajectory escalation recovers less than half of the LC-to-HC quality gap while incurring a substantial cost premium. We term this cost-quality penalty the handoff tax. By contrast, downshift offers a favorable cost-quality point. Interestingly, the preferred interface also reverses with direction: reducing LC-model trajectory information improves escalation quality, whereas removing the HC-model trajectory reduces downshift quality.

---


### 131. [Words, Spaces and Generative AI: Layers of language in contemporary architecture](https://arxiv.org/abs/2608.24360)

**<font color=#1a73e8>作者：</font>** Anca-Simona Horvath  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language can be considered a design material in architecture, and in the context of text-to-X generative AI models becoming a common tool for architectural practice, looking more closely at language is more important now than in the past. After describing some of the important developments in linguistics starting from Wittgenstein, and including the work of Chomsky, Lakoff, conceptual and generative metaphors as proposed by Schön, this chapter connects them to contemporary architectural design and generative text-to-X tools. The chapter builds on the idea that three main forms of language intertwine in architectural design done using generative AI, namely (I) discourse (or natural language which can contain professional terminology specific to our field), (II) programming languages (which are artificial languages sitting at the basis of all computational systems), and (III) annotations (as language elements attached to pieces of data). It concludes by outlining a research agenda for connecting generative metaphors to generative AI: (a) conducting corpus linguistics studies on architectural texts (using quantitative tools such as topic modelling, and qualitative tools such as discourse analysis); (b) bringing communication theory and information studies closer to architectural research and (c) taking into account that different (natural) languages come with different affordances meaning generative and conceptual metaphors differ in relation to this.

---


### 132. [Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems](https://arxiv.org/abs/2608.24361)

**<font color=#1a73e8>作者：</font>** Yarden Bakish, Amir Dudai, Roy Ganz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems are increasingly deployed in real-world applications, where failures can be costly and difficult to localize. Despite growing efforts to automate failure attribution, diagnosing failed runs still largely relies on human engineers. Yet engineers rarely debug complex systems by reading raw logs end to end. Instead, observability tools organize traces around components, actions, and dependencies to support targeted navigation. We hypothesize that modern LLMs can benefit from the same paradigm. To test this hypothesis, we introduce Adaptive Influence Graphs (AIGs), a two-stage agentic framework that first transforms a failed trace into a structured graph and then navigates it to identify the critical error. Across multiple models, we show that richer trace representations consistently improve failure attribution, with adaptive graph construction and agent-directed traversal yielding the strongest results. AIGs establish a new state of the art on Who&When, the standard benchmark for multi-agent failure attribution. This affirms our hypothesis that attribution depends not only on the diagnosing model, but also on how the trace is represented and explored.

---


### 133. [From State to Action: OODA-Tool for Reliable Multi-Turn Tool Use](https://arxiv.org/abs/2608.24368)

**<font color=#1a73e8>作者：</font>** Rongfeng Guo, Yinxuan Huang, Yusen Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable multi-turn tool use requires an agent to preserve an evolving task state and ensure that each action remains consistent with it. However, direct function-calling and ReAct-style policies learn state tracking and action generation within the same autoregressive trajectory. This coupling creates state-action competition: the pressure to produce the next call can overwrite or ignore information accumulated earlier in the interaction. Inspired by Boyd's Observe-Orient-Decide-Act cycle, we introduce OODA-Tool, a typed closed-loop policy designed to mitigate this competition by separating state preservation from action realization. Rather than generating an action directly from the interaction history, OODA-Tool routes each decision through controller-checked intermediate states, ensuring that the final output remains grounded in the current task state. Specifically, Observe reconstructs the task state, Orient determines whether execution is warranted, Decide forms an admissible action structure, and Act realizes the external output. We evaluate OODA-Tool against direct function-calling and ReAct policies using Qwen3 models ranging from 0.6B to 14B across multi-turn, multi-tool, and incomplete-information settings. OODA-Tool consistently improves task success across model sizes, with larger gains on smaller models and on tasks whose actions depend strongly on information accumulated across turns and prior tool results. Controlled variants, stage-level ablations, and transfer evaluations further demonstrate the robustness of these improvements.

---


### 134. [Do Recipes Have Personas? Characterizing and Generating Creator Style in Attributed Procedural Graphs](https://arxiv.org/abs/2608.24369)

**<font color=#1a73e8>作者：</font>** Lei Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) possess vast zero-shot procedural knowledge, their tendency to produce homogenized logic often obscures the unique, idiosyncratic execution processes of individual human creators. In this paper, we investigate the computational discovery of procedural personas from unstructured data. To achieve this, we introduce ViralRecipesTrans, a new dataset of procedurally aligned execution flow graphs extracted from popular culinary video transcripts and explicitly mapped to specific creators. We formulate procedural stylometry as a graph learning and process discovery task, revealing a fundamental duality: while traditional lexical classifiers overfit via semantic leakage, discrete topological metrics successfully capture the rigid physical constraints of a creator's workflow. Building upon this characterization, we extend our framework into a novel generative task--predicting a creator's exact structural execution graph for unseen dishes. We expose a fundamental dichotomy in style generation between global macro-planning and local structural execution. Our results demonstrate that few-shot LLMs dominate semantic assignment but suffer from persistent macro-planning deficits, whereas our structured two-stage model achieves superior topological control via rigid Markovian priors. Together, an ensemble approach to procedural generation combines the strengths from both sides, dynamically synthesizing global semantic reasoning with localized topological footprints to automate the discovery and generation of personalized workflows.

---


### 135. [ResiSpec: Enhancing Multi-Candidate Speculative Sampling via Residual Distribution Shaping](https://arxiv.org/abs/2608.24411)

**<font color=#1a73e8>作者：</font>** Zhi-Kai Chen, Jun-Jie Tao, Wei-Xiang Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The efficiency of Large Language Model (LLM) serving is fundamentally limited by the sequential nature of autoregressive decoding. Speculative Decoding (SD) mitigates this by using a lightweight draft model to speculate future tokens, which are then validated by the LLM in a single parallel forward pass. To further boost efficiency, multi-candidate schemes propose diverse candidate sets to increase the likelihood of token acceptance. However, we show that these schemes are bottlenecked by Residual Drift: a phenomenon where the rejection of initial candidates causes the residual target distribution to diverge from the draft model's predictions. This shift renders subsequent candidates ineffective and forces the system into expensive resampling. To resolve this, we propose ResiSpec, a framework that strategically reforms the proposal distribution during verification to anchor the residual target mass within the draft model's high-confidence regions. By mathematically re-aligning the verification process without compromising output exactness, ResiSpec prevents candidate obsolescence and achieves up to 1.92$\times$ speedup over state-of-the-art multi-candidate methods. Code is available at this https URL.

---


### 136. [A Judge Should Know What Changed:Construct Validity for LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2608.24419)

**<font color=#1a73e8>作者：</font>** Jianlin Chen, Wenhui Chen, Ziyao Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge evaluation is usually assessed by agreement and robustness to surface perturbations, but reliability does not establish construct validity. We formalize construct validity for an evaluator as a two-dimensional profile: invariance S, the probability that a verdict is unchanged under construct-preserving edits, and construct sensitivity R, the probability that it changes under minimal construct-changing edits. We show that S and R are independent and that no scalar summary preserves all relevant comparisons. We measure the profile across 7 judges and 4 domains using 7 construct-changing intervention types and 5 register-only controls, with intervention direction determined by human annotators and generation, verification, and judging assigned to disjoint model families. At matched invariance S >= 0.90, judges average S = 0.945 but R = 0.319. Sensitivity also differs between scope and strength edits: R_scope = 0.383 versus R_strength = 0.262, a +0.121 gap with the same sign for all 7 judges. We further audit five public label sets and find that surface-only predictors reproduce 55%-67% of labels in paired mode, including 67.4% of MT-Bench human votes. These results show that high judge agreement can coexist with weak sensitivity to changes in the construct being evaluated, motivating joint reporting of invariance and sensitivity and auditing the validation set itself.

---


### 137. [Vision Language Model Fusion for Explainable Face Recognition](https://arxiv.org/abs/2608.24430)

**<font color=#1a73e8>作者：</font>** Ana Estrada-Real, Lydia Alapatt, Christoph Busch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Responsible deployment of face verification systems requires more than accurate decisions: systems should also provide interpretable and auditable evidence that enables users to understand, assess, and challenge their decisions. Vision-language models (VLMs) provide a promising foundation for explainable face recognition by combining visual analysis with natural-language reasoning. However, relying on a single model may further limit the decision accuracy as well as provided explanations. This work therefore investigates whether multiple VLMs can be combined to improve recognition accuracy, and to enrich the explanations associated with those decisions. This work evaluates four VLMs as standalone face verification systems and subsequently proposes a fusion framework, where two source models provide similarity scores and textual justifications and a third VLM acts as a decider model. Four different fusion scenarios are considered, progressively providing the decider model with scores, justifications, face images, and combinations of these modalities.
Overall, the findings suggest that the value of multi-VLM fusion extends beyond recognition performance. VLMs can provide complementary justifications and perspectives that enable richer explanations of face recognition decisions, supporting greater transparency, auditability, and error analysis. This is relevant to the development of responsible explainable face verification systems, where users and operators should be able to understand not only the final decision but also the evidence and potential sources underlying it. The proposed multimodal VLM, which combines decision scores, explanations, and face images, achieves higher recognition accuracy than state-of-the-art VLMs and domain-specific face recognition models, while also providing fused explanations that are expected to be more robust than those generated by individual VLMs.

---


### 138. [DoublesEval: Diagnosing Multi-Agent Tactical Reasoning in Vision-Language Models via Professional Doubles Badminton](https://arxiv.org/abs/2608.24439)

**<font color=#1a73e8>作者：</font>** Jintao Cheng, Weibin Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Language Models (VLMs) excel at describing visible scene content but struggle to reason about dynamic multi-agent interactions, where action semantics depend on coordinated roles and spatial-temporal dependencies. We formalize this capability as \textbf{multi-agent tactical reasoning} and introduce \textbf{DoublesEval}, a diagnostic evaluation framework that leverages professional doubles badminton as a structurally tractable testbed. DoublesEval employs a key-moment-based protocol that decomposes rallies into tactically salient instants and probes models across four interpretable dimensions: atomic recognition, intra-segment composite understanding, cross-segment causal reasoning, and high-level tactical abstraction. This design isolates \emph{where} reasoning fails, rather than merely measuring answer correctness. To address observed failure modes, we propose \textbf{TacticCheck}, a lightweight constraint-guided test-time consistency checker that reranks candidate answers using the model's own lower-level tactical predictions, requiring no parameter updates or ground-truth labels at inference time. Evaluating four representative open-source VLMs on 60 curated rallies (yielding $\sim$9.6K structured instances) via a zero-shot protocol, we find that models remain weak across all diagnostic levels, with especially clear bottlenecks in spatial state, interaction binding, and terminal evidence. TacticCheck delivers consistent gains across all evaluated models, while still leaving a substantial gap to robust tactical reasoning. These results highlight the need for structured, interaction-aware evaluation paradigms for next-generation VLMs. The source code is available in \href{this https URL}{\textcolor{blue}{our GitHub repository}}.

---


### 139. [Do System Prompts Leave Behavioral Fingerprints? A Large-Scale Empirical Study of Clone Detection via Output Similarity](https://arxiv.org/abs/2608.24461)

**<font color=#1a73e8>作者：</font>** Linghan Chen, Yudong Gao, Jiyao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System prompts can be extracted from commercial LLMs with over 80\% success and redeployed at zero cost, yet a prompt owner has no way to verify whether a suspected deployment is a clone. We propose Black-Box Behavioral Fingerprinting (BBF): the prompt owner registers a behavioral signature from model outputs and later tests whether a suspect deployment matches that signature more closely than an unrelated baseline. BBF requires only black-box API access. Through a large-scale study (4 model families, 8 benchmarks, 288{,}000 responses), we find that prompt choice explains 24.4\% of output variance and same-model detection reaches AUC 0.876. Cross-model performance is bounded by detector identity, with off-diagonal AUC ranging from 0.845 (Claude as detector) down to 0.665 (Qwen) and overall mean 0.725. BBF resists non-adaptive prompt paraphrasing (AUC $\geq 0.889$) and is robust to imperfect extraction, but a single-sentence formal-tone prefix can collapse detection on short structured outputs (MNLI 0.978 $\to$ 0.547), isolating style-invariant detection as the key open problem. Diagnostic Query Optimization, a zero-cost query selection rule, adds $+0.120$ to cross-model AUC.

---


### 140. [HMGCLIP: Heterogeneous Multi-Granularity Contrastive Learning for E-commerce Representation Learning](https://arxiv.org/abs/2608.24467)

**<font color=#1a73e8>作者：</font>** Qiuyu Zhu, Yi Gao, Zhichao Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although recent Multimodal Large Language Models (MLLMs) have advanced general product understanding, they implicitly encode product information into global embeddings, thereby limiting their ability to capture fine-grained attributes. This limitation hinders performance in tasks requiring precise attribute discrimination, such as distinguishing subtle material differences among visually similar products. To address this challenge, we propose HMGCLIP, a unified multimodal embedding framework. By constructing a heterogeneous hypergraph, we leverage hypergraph topology to mine structure-aware hard negatives and align multi-granular semantics at both relation and hyperedge levels. This design enables a dual-granularity inference mechanism that dynamically fuses attribute evidence for both fine-grained and coarse-grained downstream tasks. Furthermore, we release a comprehensive fine-grained e-commerce dataset to facilitate future benchmarking. Extensive experiments on this new dataset and the public MAVE benchmark show that HMGCLIP outperforms strong multimodal encoders, MLLMs, and e-commerce baselines, validating the superiority of HMGCLIP.

---


### 141. [Low-Rank Ternary Adaptation for Fine-Tuning Transformers](https://arxiv.org/abs/2608.24469)

**<font color=#1a73e8>作者：</font>** Alexandru-Dragos Manolache, Yunqiang Li, Jan van Gemert  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ternary transformers offer extreme memory and compute efficiency, but existing low-bit LoRA-based methods cannot directly fine-tune ternary weights. Current approaches either require dequantization, restoring low-bit base weights to higher precision to merge with adaptation weight, or update only quantization parameters, preventing a merged model that remains ternary. We propose ternary multiplicative adaptation, which represents discrete updates of ternary weights such as sign flips or zeroing through a low-rank Kronecker factorization into two small ternary matrices applied element-wise to ternary weights. This design is parameter-efficient and expressive, preserves the ternary domain, and supports direct merging without dequantization. Experiments on six models across language and vision, including ternarized LLaMA-3 1B and 3B and a ternary ViT-B/16, demonstrate that our method recovers much of the performance lost to quantization and outperforms strong low-bit and ternary baselines. Code is available at this https URL.

---


### 142. [Dataset Scarcity Limits Robust Evaluation of Multilingual Embedding Models: A Case Study of Slavic Languages](https://arxiv.org/abs/2608.24477)

**<font color=#1a73e8>作者：</font>** Ana Gjorgjevikj, Barbara Koroušić Seljak, Tome Eftimov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual text embedding models enable cross-lingual transfer of knowledge across a wide range of NLP tasks, but their evaluation remains highly uneven across high-, mid- and low-resource languages. In this paper, we propose a two-dimensional framework, specifically tailored for analyzing multilingual embedding benchmarks under dataset scarcity, and apply it on the Slavic-language subset of the MTEB benchmark. The framework distinguishes between task-specific and cross-task evaluation, while jointly analyzing three complementary aspects: (1) ranking robustness, (2) model consistency, and (3) evidence strength. At the task-specific level, we evaluate the stability of model rankings under changes in ranking methodology and benchmark dataset composition. At the cross-task level, we assess the ability of models to generalize across diverse tasks within a language. To quantify the reliability of benchmark conclusions, we introduce an Evidence Strength Score that accounts for dataset availability, diversity, and robustness assessability. Our analysis reveals severe benchmark sparsity, with many Slavic language-task pairs relying on a single dataset or highly correlated benchmark collections, limiting the ability to draw robust conclusions. The cross-task analysis reveals a small group of highly transferable models, most notably llama-embed-nemotron-8b, multilingual-e5-large-instruct, and Qwen3-Embedding variants, that consistently perform well across Slavic languages and tasks. Overall, the results demonstrate that benchmark rankings and robustness conclusions must be interpreted jointly with certain notation of their evidence strength and highlight benchmark scarcity as a major obstacle to trustworthy multilingual evaluation.

---


### 143. [When Do Supervised UQ Ensembles Improve LLM Hallucination Detection? A Robustness Study](https://arxiv.org/abs/2608.24492)

**<font color=#1a73e8>作者：</font>** Mohit Singh Chauhan, Vipin Gyanchandani, Dylan Bouchard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification (UQ) methods are widely used for hallucination detection in large language models (LLMs) in closed-book settings where ground-truth evidence is unavailable at inference time. Prior work has proposed combining UQ signals via learned ensembles, but empirical investigations into the robustness of these ensembles are limited. We study a supervised ensembling framework that trains a classifier over heterogeneous UQ-based scorer outputs on a small, domain-specific dataset of labeled LLM responses, then applies it to out-of-sample hallucination classification without retrieval, tools, or reference documents. Across four LLMs, nine datasets, and three generation regimes (short-form QA, long-form generation, and code generation), we provide a systematic robustness analysis along three axes: sample efficiency, in-domain dataset transfer, and generation regime dependence. We find that supervised ensembles outperform the best individual scorer in 30 of 32 settings, with gains realized from as few as 100 labeled instances. Ensembles retain most of their advantage in cases of in-domain transfer under distribution shift, outperforming the best non-ensemble scorer in 23 of 28 transfer settings. Sampling-based black-box ensembles are nearly as effective as full ensembles, while single-generation white-box ensembles offer limited benefit.

---


### 144. [SeriCrypt: An LLM-Driven Context-Aware Serialization Framework for Cryptographic Protocols](https://arxiv.org/abs/2608.24498)

**<font color=#1a73e8>作者：</font>** Maosong Chen, Xi Chen, Mengcheng Ju 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Constructing syntactically correct and cryptographically valid message sequences is essential for protocol state machine learning, conformance testing, and fuzzing. Unlike plaintext protocols, cryptographic protocols involve complex cross-message state dependencies and cryptographic computation constraints. Existing automated approaches predominantly target text-based or plaintext protocols, leaving cryptographic message construction largely manual. We present SeriCrypt, an LLM-driven, context-aware serialization framework for cryptographic protocols. It employs a large language model to extract field constraints, state dependencies, and cryptographic computation rules from unstructured protocol specifications into a unified structured intermediate representation, formally characterized by a domain-specific language for cryptographic protocols (CDSL). A protocol-agnostic execution engine parses CDSL declarations, automating field value resolution, cryptographic primitive invocation, and byte-stream serialization. As case studies in protocol security testing, we use the framework to construct violation messages targeting specification-defined security constraints and to support protocol fuzzing, evaluating it on mainstream implementations of TLS 1.2/1.3, IKEv1/v2, SSH, and TLCP. SeriCrypt generated message sequences accepted by all evaluated implementations and completed handshakes in every scenario. Security constraint testing revealed five specification violations, and fuzzing reached deeper protocol states with higher code coverage than mainstream fuzzers under the same time budget, demonstrating the framework's practical value for cryptographic protocol security testing.

---


### 145. [PeakBench: Benchmarking Resource-Aware Tool Invocation in LLM Agents](https://arxiv.org/abs/2608.24509)

**<font color=#1a73e8>作者：</font>** Zhi-Kai Chen, Xu-Xiang Zhong, Song-Yan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly solve tasks by invoking multiple tools, where parallel execution is essential for low latency but difficult to manage safely. Existing agent benchmarks primarily evaluate tool selection, argument generation, and end-to-end success under mostly serial execution, largely overlooking valid parallelization and resource-constrained scheduling. This missing scheduling dimension creates a practical failure mode: serial execution is safe but slow, while resource-agnostic parallel execution is fast but prone to avoidable resource overflows. To address this gap, we introduce PeakBench, a benchmark of executable multi-tool workflows with execution-grounded dependency annotations and measured resource profiles. A central challenge in evaluating such workflows is attribution: failures and inefficiencies may arise from incorrect dependency planning, poor resource-constrained scheduling, or both. PeakBench addresses this challenge with a two-part evaluation framework that disentangles logical planning from physical scheduling, with dedicated metrics for each dimension. Using this framework, we show that strong logical planning does not reliably translate into safe or efficient execution under resource constraints. We further show that exposing resource information can reduce avoidable overflows and improve resource utilization, making PeakBench a useful testbed for diagnosing resource-aware agent behavior. Code is available at this https URL.

---


### 146. [Beyond Information Seeking: Severity-Aware Question Supervision for Proactive Medical Dialogue](https://arxiv.org/abs/2608.24521)

**<font color=#1a73e8>作者：</font>** Chenxuan Li, Xinrong Chen, Luyan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Proactive medical dialogue requires an agent to decide what to ask from incomplete patient information. Existing information-seeking approaches commonly prioritize questions that most reduce diagnostic uncertainty. While effective for acquiring informative evidence, this criterion overlooks an important property of medical diagnosis: different diagnostic errors can carry substantially different consequences. Missing a severe condition may matter more than reducing uncertainty among less consequential alternatives. Question acquisition should therefore consider not only how informative new evidence is, but also how it is expected to affect the downstream diagnostic decision. To this end, we propose Expected-Severity-Risk (ESR), a consequence-aware question-supervision objective that values each candidate by its expected reduction in severity-aware terminal risk. Because questions must be selected before their answers are observed, ESR marginalizes over possible answers using train-only population statistics. Its rankings are then distilled into a prefix-only language policy, so next-question selection requires no teacher-side computation at deployment. Across three Qwen3-4B training seeds on DDxPlus, matched ESR supervision reduces mean high-severity diagnostic miss from .0645 to .0455 (-29.5%) and improves mean diagnostic accuracy from .9123 to .9320 while requiring only 0.14 additional questions per dialogue. Fixed-budget analyses show that the two objectives remain behaviorally distinct when question count is controlled, while a matched expected-0/1-risk control shows that severity-aware weighting improves the high-severity error profile beyond generic decision-aware supervision. These results support moving proactive medical dialogue beyond uncertainty reduction toward consequence-aware evidence acquisition.

---


### 147. [Neurosymbolic Alignment for Physiologically-Safe Clinical Language Models](https://arxiv.org/abs/2608.24534)

**<font color=#1a73e8>作者：</font>** Abdulhady Abas Abdullah, Erik Cambria, Milena Zivkovic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical LLMs can generate recommendations that are factually plausible yet physiologically unsafe. We investigate whether safety alignment can be improved by grounding preference optimization in structured physiological knowledge rather than text-only supervision. Methods: We propose Neurosymbolic Alignment, a training-time framework that couples a 7B clinical LLM with an HGNN-based Physiological World Model over an 847K-node biomedical knowledge graph. Candidate responses are scored using homeostatic constraints, multi-hop path plausibility, and drug-interaction penalties, and the resulting rankings drive iterative on-policy ORPO updates. Evaluation is performed on the Clinical Safety Benchmark (CSB), a 2,500-scenario benchmark for physiological constraint violations in generative clinical reasoning. Results: Relative to ORPO, the proposed method improves CSS from 69.5% to 90.8% (+21.3 pp), reduces physician-evaluated HR from 14.1% to 5.1% on the blinded subset, and improves DID from 72.8% to 91.6%. These gains are corroborated by an HGNN-independent Rule-Engine Safety Score (RSS: 86.4%, +21.2 pp over ORPO; r=0.97 concordance with CSS). The method also exceeds GPT-4 (5-shot) on all safety metrics despite a 10x parameter disadvantage, and outperforms an inference-time self-correction pipeline (SFT+SelfCorrect) by 11.4 pp CSS. Under synthetic EHR-style noise, 84.2% CSS is retained. Ablation analysis shows that HGNN scoring (-16.2 pp) and iterative training (-11.5 pp) are the dominant contributors. PhysioScore calibration against 200 clinician labels yielded ECE = 0.038 and kappa = 0.91. Conclusion: Training-time physiological grounding produces measurable and independently verifiable safety improvements in open-weight clinical LLMs under controlled evaluation. External validation on real clinical data is required to determine whether these gains transfer to deployment settings

---


### 148. [VizAnchor: Decoding Manipulation Intent from Tampering Visualizations via Dual-Anchor Reasoning](https://arxiv.org/abs/2608.24535)

**<font color=#1a73e8>作者：</font>** Xiaotian Zhang, Huayuan Ye, Haiyang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data visualizations are widely used for communicating information, but they are also vulnerable to intentional manipulations that induce misleading interpretations. Existing methods focus on locating tampered regions or recovering hidden information, without explaining how the visualization has been manipulated or why the resulting changes may mislead viewers. We propose \textbf{VizAnchor}, a framework for visualization manipulation understanding through dual-anchor evidence construction and VLM-based reasoning. In the first stage, VizAnchor constructs a semantic anchor to recover authentic chart information and a spatial anchor to localize tampered regions. In the second stage, three specialized agents decode the manipulation. The misleader grounding agent analyzes a four-panel visual prompt to predict the misleader information. The chart narrative reconstruction agent takes the original and tampered charts as inputs and reconstructs their respective visual narratives. Finally, the intent inferring agent integrates the visual evidence and misleader information to infer the misleading intent. We further construct a dataset for tampering localization and a dataset for misleading intent inferring. Evaluation shows that VizAnchor accurately localizes manipulations and produces faithful explanations of their manipulation, misleaders, and misleading intents.

---


### 149. [Discovering Adaptive Transmission Programs for Collective Innovation](https://arxiv.org/abs/2608.24545)

**<font color=#1a73e8>作者：</font>** Cédric Colas, Jérémy Perez, Eleni Nisioti 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human collective intelligence depends on transmission processes: who shares what with whom, how, and when. While these processes emerge from individual cognition, they can also be directed by deliberate top-down protocols. Prior work has studied how transmission shapes collective outcomes primarily through the lens of network structure, varying who shares with whom and when. But networks are state-agnostic: they cannot condition transmission on what agents know or on the state of the collective. Here, we formalize transmission protocols as state-aware programs that route information and resources based on agent and collective states, and we use LLM-guided evolutionary search to design effective protocols in a collective discovery task. Evolved protocols increase collective performance over standard baselines from the literature by up to 37%. Ablations confirm that state-awareness drives this advantage: removing content-dependence while preserving network topology and timing eliminates performance gains. We find that evolved protocols also transfer across domain variations and agent populations. These results demonstrate that effective and generalizable transmission protocols can be discovered in silico, suggesting a path toward AI-assisted design of coordination infrastructure that enhances human collective intelligence.

---


### 150. [X-MULTI: VLM-based Imaging Factor Disentanglement for Factor-Aware Image Synthesis](https://arxiv.org/abs/2608.24563)

**<font color=#1a73e8>作者：</font>** Sonali Godavarthy, Matthias Neuwirth-Trapp, Tim-Felix Faasch 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Imaging factor disentanglement in text-to-image generation aims to independently control image acquisition properties such as types of camera lenses, sensor types, viewpoints, and domains to enable combinatorial generalization. This should let the model synthesize novel factor combinations unobserved in the training data, such as pairing a fisheye lens with an event sensor never observed in training data. Recent work, MULTI, introduced learnable, factor-specific embeddings to disentangle imaging factors, along with the Factor Alignment Accuracy (FAA) metric to evaluate disentanglement quality. We identify and address two independent limitations. First, MULTI's pixel-level reconstruction objective supervises the model only on observed imaging factor combinations, providing no direct training signal for novel combinations. We therefore propose X-MULTI, which uses a pretrained vision-language model (VLM) to supervise novel factor combinations synthesized during training. Second, we show the FAA metric exhibits severe cross-factor correlation leakage, misrepresenting true disentanglement quality. We therefore propose Improved-FAA (I-FAA), which employs factor-specific augmentation strategies to break these correlations and enables more rigorous evaluation. Experiments demonstrate that X-MULTI achieves improved factor alignment on novel combinations compared to MULTI. Moreover, we show that correlation leakage in FAA distorts the evaluation of true factor disentanglement and I-FAA reduces this leakage and therefore provides a more robust assessment of factor alignment.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
