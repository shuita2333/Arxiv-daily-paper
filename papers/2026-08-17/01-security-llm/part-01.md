# 🔐 大模型安全相关研究 | 2026年08月17日

> 本类共 **7** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Don't Want Your LLM to Recommend Nuclear Strike? Try Asking It in Japanese](https://arxiv.org/abs/2608.12373)

**<font color=#1a73e8>作者：</font>** Rian Touchent  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in strategic and advisory contexts, yet their safety alignment is typically evaluated in English only. We test nine models from six providers and ask whether the language of a prompt can change a model's decision in a high-stakes scenario. We use single-turn game-theoretic vignettes in which a model advises a nuclear-armed nation on whether to strike a defenseless opponent. The prompt is intentionally amoral and strategically identical across languages. We find that Japanese prompts reduce launch rates in the Claude model family: Claude Sonnet 4.6 drops from 40% to 0% in scenarios where the strike is unnecessary and from 93% to 17% in contested scenarios, with minimal effect when the strike is strategically rational. The effect extends to Gemini Pro 3.1 (53% to 13%). A cross-language experiment isolates the mechanism: when instructed to reason in Japanese in an English prompt, launch rates drop from 93% to 37%. It is the language the model is asked to reason in, not the language of the input, that drives the effect. When reasoning in Japanese, models spontaneously generate moral vocabulary (''moral cost'', ''millions of lives'') that is entirely absent from the prompt. Five other models show no language effect, but they launch in nearly every condition regardless of language. The effect requires a model that already hesitates in English. These results show that LLM safety behavior is language-dependent, and that evaluating in English alone can miss both risks and safeguards encoded in other languages.

---


### 2. [When Explanations Betray Backdoors: Black-Box Auditing for Language Model Classifiers](https://arxiv.org/abs/2608.12623)

**<font color=#1a73e8>作者：</font>** Yang Liu, Ran Zou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model classifiers with explanations are used for moderation, routing, topic triage, and low-resource annotation. We study black-box auditing when the defender has only clean calibration data without trigger information but can ask the classifier for a label plus a short rationale or quoted evidence. We introduce Groundedness Drift, a lightweight score measuring whether the answer summary remains grounded in the input. Across two 7B backbones, five datasets, and four common non-adaptive OpenBackdoor-style attack families, Groundedness Drift achieves higher AUROC and lower residual target ASR than every compared detector in all cases at a nominal 5\% clean-FPR budget. We then evaluate Unsupported Groundedness, a multi-probe escalation for explanation-camouflage stress cases. Unsupported Groundedness improves signals but does not close the adaptive gap.

---


### 3. [HiRoute: Hierarchical Routed Prompt Tuning for Safety Alignment of Large Language Models](https://arxiv.org/abs/2608.12821)

**<font color=#1a73e8>作者：</font>** Fangzhou Chen, Shiji Zhao, Mengyang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain vulnerable to harmful requests and jailbreak attacks. Parameter-efficient safety alignment methods based on prompt tuning typically rely on a single global prompt or externally selected prompt modules. Such static designs struggle to maintain a cross-category safety boundary while generating constructive responses tailored to specific risks and avoiding over-refusal of benign inputs. To address these limitations, we propose HiRoute, an input-adaptive hierarchical prompt-tuning framework that separates category-agnostic safety control from category-specific response guidance. HiRoute first trains a lightweight hierarchical router on representations extracted from a frozen LLM to jointly detect harmful intent and predict multi-label risk scores. It then freezes both the backbone model and the router and uses preference optimization with alternating gradient updates to learn a shared coarse-grained prompt and a set of fine-grained prompt experts as continuous embeddings. At inference time, benign inputs bypass the safety branch, whereas risky inputs are processed using the shared prompt together with a router-weighted mixture of risk-specific prompt experts. Experiments across three instruction-tuned models show that HiRoute achieves high safety rates across multiple safety benchmarks while preserving safe-response helpfulness, reducing over-refusal, and maintaining competitive performance on general-purpose tasks.

---


### 4. [Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation](https://arxiv.org/abs/2608.12880)

**<font color=#1a73e8>作者：</font>** Rana Muhammad Ahmed, Sabahat Abbas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security evaluations of tool-using agents often equate stored labels with behavioral facts. We audit a preserved campaign by tracing 10,200 execution rows to 180 model-bound requests, 45 semantic requests, and 15 observable stimuli. Two schema treatments were delivered, but the planned external payload-family corpus was not. The historical grader exhibited direct treatment leakage: treatment metadata gated the ATTACK_SUCCESS class, so fixed behavior could change class under treatment relabeling. A treatment-blind reconstruction corrects 58 historical ATTACK_SUCCESS or HIJACK_ATTEMPT labels to authorized benign completions while preserving three verified protected-data transfers and one separate unauthorized-forwarding case. The locked v2 census contains exactly zero ATTACK_SUCCESS records, while the forwarding case remains a HIJACK_ATTEMPT at a semantic boundary concerning objective completion. A dual-reviewer blinded concordance review of all 96 requests deemed structurally interpretable by locked v2 produced identical reviewer-consensus classes but differed from the locked codebook on four construct-boundary cases. We contribute a seven-link Integrity Chain and an executable, scope-bounded endpoint-integrity linter. The result is a campaign-bounded measurement audit, not a population attack-rate, model-ranking, defense-efficacy, or causal estimate.

---


### 5. [Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs](https://arxiv.org/abs/2608.12911)

**<font color=#1a73e8>作者：</font>** Beining Xu, Hairui Wang, Jiaxin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While the privacy risks of multimodal large language models (MLLMs) have drawn significant attention, the unique vulnerabilities of domain-specific MLLMs remain largely underexplored. Focusing on document understanding MLLMs for identity document processing, this paper investigates the privacy issues inherent in Key Information Extraction (KIE) tasks. We reveal that when input images lack sufficient visual evidence, these models often rely on memorized field relations from training data to infer missing content, thereby leaking multiple correlated fields containing sensitive personal information. To mitigate this risk, we make three key this http URL, we propose the Dynamic Relational Unlearning Framework (DRUF) which comprises a Relational Decoupling Unlearning (RDU) module and a dynamic set update mechanism. It suppresses the leakage of high-risk field pairs while preserving KIE this http URL, we introduce DocPrivacyBench, a novel benchmark to systematically evaluate a model's susceptibility to privacy leakage under conditions of absent or minimal visual this http URL, we evaluate three MLLMs and six unlearning methods using this benchmark, assessing both post-unlearning leakage suppression and utility this http URL results demonstrate that existing MLLMs consistently exhibit privacy leakage when visual evidence is scarce, particularly on noisier datasets. In contrast, DRUF outperforms the strongest baseline by improving leakage suppression by 4.8 percentage points, effectively mitigating privacy risks while maintaining robust document information extraction performance.

---


### 6. [Capability Sheaves for Compositional Agent-Harness Repair: Controlled Quotients and a Real-Repository Stress Test](https://arxiv.org/abs/2608.13228)

**<font color=#1a73e8>作者：</font>** Saveliy Batruin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses combine retrieval, routing, state, provenance, and verification, but locally successful components may disagree on shared state. We model this failure with a finite \emph{capability sheaf}: stalks encode typed behavior signatures, restriction maps retain shared fields, and accepted runs are useful global sections. An exact finite constraint-satisfaction problem (CSP) defines acceptance, while a linearized relative cohomology class provides a diagnostic and search feature.
A controlled experiment over 20 task clusters introduces hidden interior mediators whose raw states are nuisance variables. Quotienting their coboundaries reduces the candidate budget from 2,000 to 1,000 per cluster; aligning the hidden state removes the gap. Exact CSP matches the quotient, so the result demonstrates invariance to stale representatives, not superiority over exact reasoning.
We then test the method on a discovery split from the SWE-bench Multilingual pool of PatchFuseBench: 160 issues from 20 repositories, 875 real candidate patches, 2,579 source-aware edit atoms, and 153 newly executed patches. A first pool-level construction is constant because $[b-Dx]=[b]$ in $\operatorname{coker}D$ and therefore cannot rank configurations. A candidate-indexed repair is nontrivial on 848/875 candidates and varies within 120/160 issues. It resolves 118 issues versus 116 for a matched noncohomological selector, but the difference is not supported across repositories (exact sign-flip $p=0.75$). A leave-one-repository-out abstention gate reaches 127/160, tying the strong anchor and exceeding its matched gate by one issue ($p=1.0$). The discovery gate therefore fails and the confirmatory split remains sealed. The study supports the controlled invariance mechanism and an identifiability correction, but not a real-world cohomological advantage.

---


### 7. [Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety](https://arxiv.org/abs/2608.13304)

**<font color=#1a73e8>作者：</font>** Ping Wu, Haibo Tong, Feifei Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety tuning can improve harmful refusal, but models may learn surface-form shortcuts: wrapped harmful prompts bypass safety, while similarly wrapped benign prompts are over-refused. We propose Wrapper-Based Intent-Form Augmentation (WIFA), an automatic intent-group augmentation method that pairs wrapped harmful examples with structurally matched wrapped benign counterexamples, requiring no external teacher or manual per-wrapper intent labels. We use WIFA as a common data layer for two complementary fine-tuning routes: WIFA-Boost, a two-stage high-safety recipe, and Anchored Group-Consistent Refusal Training (A-GCRT), which regularizes refusal/compliance decision scores across same-intent wrappers and anchors harmful and benign groups on opposite sides of a margin. In the Qwen setting, WIFA-Boost reaches the strongest transformed-harmful refusal, while A-GCRT reduces OR-Bench over-refusal from 25.7\% for the base model to 17.4\%; reproduced baselines do not match these operating points. Llama results and ablations over data structure, two-stage order, and A-GCRT components support this intent-group interpretation without claiming universal below-base over-refusal.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
