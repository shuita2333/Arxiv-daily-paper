# 🔐 大模型安全相关研究 | 2026年10月28日

> 本类共 **14** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Deletion, Substitution, Repair and Transplant: Component Attribution in BARBICAN, a Layered Prompt-Injection Gateway for MCP](https://arxiv.org/abs/2610.33198)

**<font color=#1a73e8>作者：</font>** İpek Abasıkeleş Turgut, Edip Gümüş  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A neural classifier can fail completely inside a layered defense without any end-to-end number moving. We demonstrate this on BARBICAN, a fail-closed gateway for language-model tool mediation whose arbitration stage spent an entire recorded evaluation receiving text mangled by a misconfigured tokenizer. Correcting the misconfiguration lifts that stage's corpus-wide area under the ROC curve (AUC) from 0.392 to 0.855 and pushes system recall down, from 80.67% to 80.34%; a stub that answers "malicious" scores 80.77%, higher than either. The reason emerges once the stage's input distribution is examined: upstream routing hands it a band that is 96.82% malicious, and the enforcement design lets an incriminating verdict block while an exculpating one releases an input only through one narrow branch. Yet deleting it costs 673 detections. Substituting its verdict with a constant instead moves between 12 and 140 of 25,000 decisions. Transplanted into the arbitration stage, an off-the-shelf classifier that separates the band's inputs at an AUC of 0.916 changes 16 of 25,000 decisions. Measured against such detectors with operating points chosen away from the test data, the gateway leads on its own benchmark distribution and falls behind once that distribution changes. In our earlier gateway, the review model's band is 92.94% malicious and a constant verdict is as accurate as the review model. We argue that an ablation figure for any routed stage is unreadable without the class balance of the band that stage receives, and that deletion experiments need substitution experiments beside them.

---


### 2. [Auditing evaluation artifacts and data leakage in large language model systems for rare disease diagnosis](https://arxiv.org/abs/2610.33592)

**<font color=#1a73e8>作者：</font>** Jian Yang, Peilin Liu, Xiaohan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Augmented large language model (LLM) systems have reported high benchmark accuracies in rare disease diagnosis, yet their real-world clinical utility remains unproven. A recent meta-analysis flagged augmented LLM diagnostic evaluations as having a high risk of bias due to suspected data leakage; however, the precise impact of these vulnerabilities on model inference has yet to be fully quantified. In this study, we present a comprehensive empirical audit to quantify evaluation artifacts across prevailing AI paradigms, using a repository of over 60,000 cases from diverse public and independent clinical cohorts. By reconstructing a state-of-the-art agentic framework, we demonstrate that candidate-space contamination artificially inflates performance: enforcing strict cross-dataset isolation resulted in a marked performance decline, with the cross-dataset mean Recall@1 decreasing from 54.3% (under conventional one-vs-rest evaluation) to 40.3% (Hedges' g = 0.94). Similar spatial overfitting in supervised classifiers caused diagnostic accuracy to drop from an internal mean of 42.9% to 16.7% across external cohorts (Cohen's d = 2.01). Furthermore, we quantify how LLMs infer diagnoses by exploiting retrospective therapeutic cues in clinical narratives, and how temporal misalignment in foundational knowledge bases leads to performance fluctuations. We conclude that prevailing evaluation protocols for augmented LLM systems inadvertently reflect data leakage rather than genuine medical reasoning. To address these systematic artifacts, we propose a rigorous evaluation framework - coupling strict data-isolation protocols with standardized benchmarking safeguards - to ensure future diagnostic AI for rare diseases is evaluated on actual clinical robustness.

---


### 3. [Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses](https://arxiv.org/abs/2610.33849)

**<font color=#1a73e8>作者：</font>** Pushkal Kumar, Arvin Sahaym  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Query-time filters that screen each retrieved document before it reaches the generator are the dominant published defense against retrieval-augmented generation poisoning, and they report near-perfect detection on domain benchmarks. We show that this performance is predicted by how the poison set was built rather than by what the filter reads: removing a single construction cue destroys the deployed decision before it destroys the ranking. Two label-free statistics of a poison set and its clean corpus profile the cue: containment, how often the target question appears verbatim in the poison, and length overlap. PoisonedRAG's released code prepends the target question to every inserted passage. Of the 21 published defense evaluations we survey, 8 verifiably run poison built this way and 5 substitute a length cue; separately, 12 report no false-positive rate at the operating point they deploy. Deleting only that prefix from the attack authors' own passages (0.93 still retrieved for their target) takes RAGuard, a published content filter we re-implement, from AUROC 0.953 to 0.758 and its miss rate from 0.191 to 0.763. Across four corpora, four attack families and ten per-document defenses on one shared candidate set, the profile predicts where detection saturates. Padding medical poison to clean length with word-shuffled filler that carries no content takes TrustRAG's set-level stage from a miss rate of 0.000 to 0.827, and one learned scorer of ours from 0.000 to 0.986 (0.321 at a matched 5% false-positive rate) while its AUROC holds at 0.953. The ranking survives; the decision does not. A defense-aware attacker defeats our own scorer, so we claim no defense. A detection result is evidence only when it is reported with its poison set's construction profile and the false-positive rate at the threshold actually deployed; we release the script that computes the profile.

---


### 4. [Identically Trained Language Models Break on Different Jailbreaks](https://arxiv.org/abs/2610.34074)

**<font color=#1a73e8>作者：</font>** Chi-Wei Chang, Mu-Tien Kuo, Kuan-Wei Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jailbreak benchmarks test one checkpoint and treat which jailbreaks break it as a property of its pretraining data and safety training. We ask whether another pretraining run of the same data, given the same safety training, would break on the same jailbreaks. For each of 25 pretraining data recipes, we take 1B base models from 3 pretraining seeds and give each the same safety post-training with 2 post-training seeds, for 150 models in all. We then collect 20 responses from every model to a shared set of jailbreak prompts and correlate the per-prompt non-refusal rates between every pair of models. On average, two post-trained copies of the same pretraining run have per-prompt non-refusal rates that correlate at 0.984. A different pretraining seed lowers the correlation to 0.811, and a different data recipe lowers it only slightly further, to 0.779. These results indicate that which jailbreaks break a checkpoint depends much more on its pretraining run than on its data, a pattern that holds in all 25 data recipes and at 150M and 300M parameters. In practice, the best of 91 attack templates found on one checkpoint stays the best after a new pretraining seed in only 27% of model pairs, against 67% after a new post-training seed. Each pretraining run also leaves a fingerprint: across 3,211 prompts, a model's per-prompt non-refusal rates identify its pretraining run among all 75 runs every time, and a random subset of 50 prompts still does so 98% of the time.

---


### 5. [Factual Yet One-Sided: Stance Poisoning and Evidence Balancing in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.34294)

**<font color=#1a73e8>作者：</font>** Puyuan Yang, Shaoxuan Dong, Liujie Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The stance expressed in responses from retrieval-augmented generation systems is significantly influenced by the stance distribution of the retrieved materials. Existing research on knowledge poisoning has primarily targeted factual errors. In contrast, this study focuses on injection attacks in which the facts are correct but the stance on a controversial issue is one-sided. At a mean topic-level poisoning share of 18.9% within the post-injection ProCon documents, all four generation models from different vendors exhibited stance shifts aligned with the poisoning direction; across four concentration levels, the shifts increased monotonically.
This paper proposes a Stance-Balancing Middleware positioned between the retriever and the generator. It consists of stance detection, fixed balancing (2 supporting + 2 opposing + 1 neutral), and a debiasing prompt, without introducing additional large language model calls. Across all eight concentration-direction settings, the complete method reduced the magnitude of stance deviation by an estimated 0.106 to 0.350; the six settings at poisoning shares of 11.9%-18.9% remained significant after Holm adjustment (adjusted p <= 0.009). In the cross-model experiment, all eight model-direction combinations moved along the stance axis in the corrective direction, and seven of eight showed a clearly detected reduction in absolute distance from 0. In the concentration sweep, the post-defense intervals included 0 in all eight settings, while the cross-model pro-poisoning results retained small positive residual point estimates of +0.045 to +0.063. For 20 candidate documents, stance detection took approximately 1.5% of the median generation time on a single GPU and approximately 16% on CPU.

---


### 6. [SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments](https://arxiv.org/abs/2610.34535)

**<font color=#1a73e8>作者：</font>** Md Abu Yusuf, Oyshi Tabassum Aditi, Md Faysal Hosain Mazed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly wired to consequential tools that send public alerts, dispatch responders, and query citizen records, where one erroneous tool call carries real-world cost. Existing agent-safety benchmarks measure generic harm or prompt-injection success and implicitly treat refusing as the safe default. In public-safety deployments that assumption breaks: an agent too cautious to dispatch help fails as surely as one that triggers a false alert. We present SentryBench, which scores agents on a two-sided, cost-sensitive frontier jointly measuring attack success, over-refusal (missing a real emergency), and over-reaction (unwarranted action) under adversarial tool use, with scenarios grounded in real emergency-call transcripts, disaster messages, and real injection/jailbreak payloads. We formalize deployment harm as an asymmetric cost functional, prove naive caution is harm-dominated whenever it refuses more genuine emergencies than the attack harm it averts, and prove a targeted trust gate adds zero over-refusal on clean input. Across 840 scored episodes over three frontier models and three defenses, refuse-more caution drives over-refusal to 100 percent on two of three models for at most a 3.7-point change in attack success and yields the worst harm everywhere, whereas our trust-gating wrapper dominates the frontier (lowest harm on every model, over-refusal at or below baseline, higher containment). Provider content filters also silently perform part of the defending and must be reported separately.

---


### 7. [InferPriv: Evaluating Inferential Privacy Leakage in LLM Assistants](https://arxiv.org/abs/2610.34640)

**<font color=#1a73e8>作者：</font>** Pengrun Huang, Yiwei Fu, Luoxi Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based personal agents are increasingly deployed to handle everyday tasks on users' behalf. These agents have access to private user information, while their tasks involve communicating with third parties; this raises a critical privacy concern that agents may inappropriately reveal sensitive user information to these recipients. Existing benchmarks primarily assess direct privacy leakage, where an agent explicitly states a pre-specified secret or attribute. However, they do not capture \textit{inferential leakage}, where the model leaves indirect cues in the reply that implicitly leaks sensitive attributes. We introduce \textsc{InferPriv}, a benchmark that measures whether an honest-but-curious recipient can infer a user's sensitive attributes from an LLM's reply on routine task. Evaluating five frontier models, we find that inferential leakage substantially exceeds direct leakage across models and prompts. Under a privacy-aware system prompt, GPT-6.1-Sol, Sonnet-5.5, and Gemini-3.8-Flash achieve near-zero direct leakage, yet the inferential leakage rate remains between 16.2--25.2\%. These findings suggest that evaluating explicit leakage alone can substantially understate the privacy risks.

---


### 8. [Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition](https://arxiv.org/abs/2610.34777)

**<font color=#1a73e8>作者：</font>** Weihang Niu, Mengxing Ren, Che Qu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces Scope-Gap Injection (SGI), an indirect prompt injection method for multi-stage LLM-agent safety pipelines. In the IJCAI 2026 OpenClaw Agent Security Attack Competition, each attack package is judged by a static skill scan (S1), an LLM-judge safety check over the task and skill definition (S2), and a live execution audit (S3). Our observations suggest a scope gap: S2 appears to inspect the task instruction and skill definition without inspecting attachment contents, while the agent reads attachments during S3. SGI keeps the visible task and skill benign, while target identifiers, bypass parameters, and authorization procedures are moved into an attachment written as a business worklist. The S2 judge therefore sees a harmless task, while the agent follows the hidden worklist and triggers the permission bypass. In OpenClaw, SGI bypassed all three stages for 5 of 19 targets. The highest-scoring single submission achieved $F = 0.385$. Across the submission campaign, attachment placement was associated with higher aggregate S2 acceptance than in-skill placement: 78% versus 23%. We close with defenses that align evaluator scope with the channels available to the agent.

---


### 9. [Logic Hijacking of RAG: Single-Document Poisoning via Local Optimization](https://arxiv.org/abs/2610.34829)

**<font color=#1a73e8>作者：</font>** Hangyi Zhao, Bonan Zhang, Fusen Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-document corpus poisoning under black-box access poses a severe threat to Retrieval-Augmented Generation (RAG). However, existing attacks predominantly rely on explicit factual refutations or imperative instruction overrides. Modern aligned LLMs often arbitrate such conflicts conservatively, rejecting overt contradictions in favor of parametric memory or clean retrieved context while triggering input guardrails. We propose MONOLOGUE, a single-document poisoning framework based on Logic Hijacking without explicit refutation. Rather than disputing the ground truth, our method concedes it as an authoritative historical baseline before introducing the update, weaving a grounded record-correction narrative (e.g., dated institutional reattributions) that presents the counterfactual target as the most recent update. To prevent suspicious live writes, payloads are refined entirely offline via local multi-dimensional gated optimization, coupling automated text quality audits with surrogate behavioral verification. Evaluations across three benchmarks, three retrieval backends, and four open-weight generator regimes show that our method achieves the strongest overall attack efficacy among the evaluated single-document poisoning attacks.

---


### 10. [C-SafeGen: Certified Safe LLM Generation with Claim-Based Streaming Guardrails](https://arxiv.org/abs/2610.34961)

**<font color=#1a73e8>作者：</font>** Mintong Kang, Zhaorun Chen, Bo Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable capabilities of large language models (LLMs) across diverse applications, they remain vulnerable to generating content that violates safety regulations and policies. To mitigate these risks, LLMs undergo safety alignment; however, they can still be effectively jailbroken. Off-the-shelf guardrail models are commonly deployed to monitor generations, but these models primarily focus on detection rather than ensuring safe decoding of LLM outputs. Moreover, existing efforts lack rigorous safety guarantees, which are crucial for the universal deployment of LLMs and certifiable compliance with regulatory standards. In this paper, we propose a Claim-based Stream Decoding (CSD) algorithm coupled with a statistical risk guarantee framework using conformal analysis. Specifically, our CSD algorithm integrates a stream guardrail model to safeguard sequential claims generated by LLMs and incorporates a backtracking mechanism to revise claims flagged with high safety risks. We provide theoretical guarantees demonstrating that the CSD algorithm achieves the desired generation distribution subject to safety constraints. Furthermore, we introduce a generation risk certification framework and derive a high-probability upper bound on the safety risk of the proposed CSD algorithm. We prove that our method can asymptotically control safety risk to any desired level. Empirical evaluations demonstrate the effectiveness and efficiency of the CSD algorithm compared to state-of-the-art safety decoding approaches. Additionally, we validate the soundness and tightness of the derived safety risk upper bound using realistic data.

---


### 11. [The Target Agent Is Its Own Best Critic but a Poor Proposer: Self-Improved Red Teaming](https://arxiv.org/abs/2610.34965)

**<font color=#1a73e8>作者：</font>** Mintong Kang, Stephen Rawls, Melissa Kazemi Rad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automatic red teaming increasingly relies on large language models (LLMs) to iteratively diagnose failed attacks and propose improved adversarial prompts or injections. Although prior work strengthens this loop through prompt engineering and search-harness design, the mechanisms underlying its two core roles, criticism and attack proposal, has not been explored. To further investigate the core roles and therefore improve red teaming effectiveness, we disentangle two design choices: whether criticism is generated by the target session itself (self-criticism) or by a separately instantiated critic (external criticism), and whether that criticism is translated into the next attack by the target session (self-proposal) or by a separate attacker (external proposal). Through our analysis, we find that self-criticism is more effective because it is grounded in the target's live execution context, including observations, constraints, and available reasoning; removing reasoning reduces downstream attack success by 6%-17%. In contrast, self-proposal is substantially less effective because awareness of the adversarial objective induces explicit refusal and non-refusal sandbagging. These findings motivate a role-separated red-teaming approach: the target session diagnoses why an attack failed, while a separately instantiated attacker generates the next proposal. On DTAP-BENCH, spanning Telecom, Workflow, CRM, and Code domains, under both direct misuse and indirect threat models, as well as multiple agent frameworks, this configuration achieves 63.2% overall attack success rate (ASR), much higher than baselines. Our results show that effective automatic red teaming depends not only on model capability and search strategy, but also on how execution context and adversarial responsibility are distributed across model sessions.

---


### 12. [GuardRAG: A Post-Retrieval Defense against Poisoning Attacks in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.35071)

**<font color=#1a73e8>作者：</font>** Linghui Jiao, Kang Wei, Fushuo Huo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) enhances the factual grounding of Large Language Models (LLMs) by incorporating external evidence, but also exposes them to corpus poisoning attacks. In particular, coordinated attacks can introduce multiple mutually reinforcing poisoned documents into retrieved contexts, making reliable evidence filtering challenging. To address this problem, we propose GuardRAG, a training-free and plug-and-play post-retrieval defense that exploits the semantic structure of retrieved evidence to identify suspicious document groups. Specifically, GuardRAG first expands the retrieval range and removes near-duplicate candidates, then partitions the retained documents using Hierarchical Agglomerative Clustering (HAC) with a query-adaptive threshold. Finally, it scores and prunes suspicious clusters based on query relevance, cluster size, and semantic compactness. Experiments across three question-answering datasets, multiple poisoning attacks, and six LLMs demonstrate that GuardRAG substantially reduces attack success rates while maintaining answer utility under clean retrieval.

---


### 13. [CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems](https://arxiv.org/abs/2610.35082)

**<font color=#1a73e8>作者：</font>** Yujia Zheng, Tianhao Li, Shangzhi Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent Skills allow LLM agents to combine reusable capabilities, but checking each Skill in isolation cannot rule out policy violations when they are composed. We term such failures Conflict of Skills (CoS): artifacts or assessment signals produced for one purpose may be reused downstream without preserving the restrictions or authorization needed for their new use. Using controlled executions of publicly available Skills and matched single-Skill controls, we identify four recurring mechanisms behind CoS. Building on these findings, we introduce the Conflict of Skills Attack (CoSA), which adds locally admitted Skills to an existing pool to supply missing business operations (capability supplementation) or reshape artifact exchange, decision reuse, and target/action bindings (relationship reshaping). CoSA leaves existing Skills and runtime permissions unchanged. To evaluate this threat under autonomous Skill selection, we introduce CoSA-Bench, built from real-world Skills and controlled services, with 288 tasks across recruiting, finance, IT, and business, covering data leakage, unauthorized state modification, and unsafe execution. Across five LLMs and three agent harnesses, additions capped at 5% of each original pool raise the policy-violation rate from 35.02% to 58.45%, an increase of 23.43 percentage points. Trace analysis links compliant-to-violating transitions to cross-Skill dependencies involving the additions. Finally, we develop a lightweight harness-level guard that checks information flow and authorization before consequential actions. On OpenClaw recruiting tasks across five models, the guard reduces violations from 65.28% to 6.67%, while policy-compliant task completion on matched benign controls changes from 66.67% to 65.00%.

---


### 14. [Then there is prompt injection, a malicious email, ...: The Wild Wide West of OpenClaw Agentic System Security](https://arxiv.org/abs/2610.35451)

**<font color=#1a73e8>作者：</font>** Mostafijur Rahman Akhond, Mahmuda Khatun, Gias Uddin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-powered personal assistant frameworks such as OpenClaw combine LLM reasoning, persistent memory, tool invocation, local execution, and web-based workflows. These capabilities enable useful automation, but they also create security risks when untrusted inputs, model reasoning, tools, memory, and deployment configuration interact without explicit trust boundaries. This paper presents an empirical study of reported security concerns in OpenClaw using two complementary data sources: Reddit discussions and security-tagged GitHub issues. We analyze more than 25K Reddit posts from 13 OpenClaw-related subreddits and identify 162 security-relevant posts with 1,787 associated comments. We further collect 358 security-tagged GitHub issues and retain 180 issues describing concrete security concerns. Using qualitative analysis and evidence-grounded CWE mapping, we identify 521 CWE instances across 59 distinct weakness types, concentrated in access-control failures, sensitive-data exposure, injection, and unsafe execution. We also extract 543 practitioner mitigation suggestions and consolidate them into seven recurring strategies. To complement the empirical analysis, we present an evidence-grounded illustrative reconstruction of a representative sensitive-data exposure pathway using dummy secret values. Our findings show that OpenClaw security issues are not isolated implementation bugs; they reflect recurring trust-boundary failures across the agent execution pipeline. We discuss how these weaknesses map to both traditional software-security categories and agent-specific failure mechanisms, and derive implications for safer agentic systems, including explicit trust boundaries, least-privilege tool access, execution containment, runtime oversight, and defense-in-depth deployment.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
