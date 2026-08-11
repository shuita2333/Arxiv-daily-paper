# 🔐 大模型安全相关研究 | 2026年08月12日

> 本类共 **14** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Evolving Safety Landscape of Multi-modal Large Language Models: A Survey of Emerging Threats and Safeguards](https://arxiv.org/abs/2608.07535)

**<font color=#1a73e8>作者：</font>** Xi Li, Shu Zhao, Xiaohan Zou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-modal large language models (MLLMs) integrate heterogeneous modalities through modality alignment and fusion, enabling stronger understanding and reasoning. However, this architectural shift reshapes the safety landscape of machine learning. Increased model complexity and cross-modal interactions give rise to novel threats, including compromised modality integration, modality misalignment, and fused safety risks, reflecting shifts in threat modeling beyond uni-modal assumptions. These shifts, in turn, impose new constraints on safety solutions not captured by existing frameworks rooted in uni-modal learning. Motivated by these challenges, this survey provides a systematic analysis of the evolving safety landscape of MLLMs. We first propose a multimodal grounded taxonomy of safety threats and analyze shifts in threat models, covering adversarial attacks, data poisoning, jailbreaks, and hallucinations. We then summarize updated safety assumptions and organize recent advances in MLLM safety strategies accordingly. Finally, we discuss open challenges and future directions to inform the development of more principled and scalable safety mechanisms for multimodal systems.

---


### 2. [The Anatomy of a Prompt Injection: A Component Model for Structured Analysis](https://arxiv.org/abs/2608.07808)

**<font color=#1a73e8>作者：</font>** Jeremy McHugh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Four years after prompt injection was first identified in 2022, attacks are still predominantly documented as verbatim strings rather than structured exploits, despite advancing agent capabilities and threat actors embedding injections to subvert AI-assisted security analysis. This paper formalizes the structure of prompt-injection artifacts, enabling defenders, red teamers, and cyber threat intelligence (CTI) teams to label, compare, and mutate attacks without relying on fragile string matching. Because large language models compile varied natural-language realizations into identical executable actions, labeling must track attacker intent (tool targets, sinks, and effects) rather than surface wording. We propose a seven-component model (carrier, delivery vector, concealment, context-break, privilege escalation, payload, and return channel) consisting of five artifact fields and two environment fields. This framework unifies roles partially addressed by HOUYI's payload decomposition, the Promptware Kill Chain, and campaign taxonomies, while framing minimal jailbreak frameworks like ReNeLLM as projections onto a restricted subspace. We provide clear labeling rules, a logical analysis record mapping directly to industry CTI schemas, worked examples including EchoLeak (CVE-2025-32711) and an in-the-wild malware AI-evasion sample, and an illustrative agentic flowchart.

---


### 3. [Capability-Routed Guard: Defending Large Reasoning Models Against Reasoning-Centric Jailbreaks](https://arxiv.org/abs/2608.07892)

**<font color=#1a73e8>作者：</font>** Yiyong Liu, Yixin Wu, Jun Sakuma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) expose a new safety failure mode: adversarial prompts can manipulate reasoning context, task decomposition, or capability interpretation so that harmful objectives are processed as legitimate reasoning steps. Existing safeguards, including safety reminders, external classifiers, and self-checking wrappers, are often brittle because they either inspect the adversarial prompt directly or ask the target model to perform additional safety reasoning on the same surface that attacks exploit. We introduce Capability-Routed Guard (CRG), a model-agnostic inference-time guardrail for closed-source LRMs, where defenders cannot inspect hidden reasoning traces or modify model weights. CRG reframes prompt defense as a capability-routing problem: a side-channel controller first constructs a trusted representation of the user's authorized task, active context, safety evidence, and capability-transfer risk, separating executable intent from untrusted reasoning context. This representation supports route-specific execution, allowing CRG to block high-risk requests, constrain ambiguous ones, and forward low-risk requests through trusted active context. Finally, CRG applies TraceCheck to verify consistency with the authorized task and invokes a restricted fallback to preserve utility for low-risk benign prompts. Extensive experiments demonstrate that CRG effectively mitigates diverse reasoning-centric jailbreaks while preserving benign utility and avoiding common over-refusal issues. Further analysis shows that its components contribute complementary benefits, highlighting the importance of coordinated defense mechanisms for securing large reasoning models.

---


### 4. [BASIS: Breach-Aware Selective Prompt Injection Shielding with Prefill Attention Probes](https://arxiv.org/abs/2608.08027)

**<font color=#1a73e8>作者：</font>** Laiqiao Qin, Tianqing Zhu, Longxiang Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection is a critical security threat in large language model (LLM) applications, where attackers hijack model behavior by embedding malicious instructions in user or external data. Existing detection methods only detect the presence of injection and refuse to respond upon detection, overlooking the fact that for many modern aligned models, well-crafted instructions can resist most injection attacks. This means that the injection robustness varies significantly across instructions and models. This leads to widespread unnecessary over-refusal: inputs containing injections that the model could have handled correctly are rejected incorrectly. To deal with this over-refusal issue, we propose BASIS (Robustness-Aware Prompt Injection Defense). This defense method uses the Attention Competition Ratio ($\rho$) as features to train two sparse linear probes: an existence probe and a breach probe. Both probes make defense decisions through cascaded gating, which does not require additional LLM inference. BASIS comprises three stages: injection existence detection, per-sample breach prediction, and instruction robustness assessment; the online cascade refuses only when the model would actually be compromised and thus avoids over-refusal on robust instructions. Experiments across four tasks and six open-source LLMs show that BASIS maintains near-perfect injection detection while substantially reducing over-refusal on safe attack samples, especially under robust instruction templates.

---


### 5. [Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning](https://arxiv.org/abs/2608.08303)

**<font color=#1a73e8>作者：</font>** Yuyang Luo, Haoran Wang, Kai Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic skills improve large language model (LLM) agents by encoding reusable procedures for complex tasks. However, manually authored skills often adapt poorly to long-horizon tasks and changing environments. To address the limitation, self-evolving skill systems have been developed to automatically construct and update skills from execution trajectories, shifting skill acquisition from external marketplaces to a trusted evolution pipeline. By replacing external skill acquisition with trusted internal construction, self-evolving skill systems reduce exposure to skill injection attacks that rely on direct skill manipulation. However, this skill evolution pipeline may introduce a new attack surface in which an attacker can indirectly steer skill evolution by inducing compromised trajectories through agent interactions. To demonstrate the threat, we propose Trajectory Backdoor Attack (TBA), a query-only attack that steers a trusted skill-evolution pipeline toward producing a backdoored skill. Specifically, we craft attacker-submitted queries to lead the agent to perform the target action and explicitly state the corresponding activation condition in the trajectory. We repeat the same condition-action pattern across diverse triggered tasks, while leaving clean queries unchanged, encouraging the evolver to consolidate the pattern as a reusable trigger-dependent rule into the evolved skill. Experiments on three benchmarks across two skill-evolution systems using four open- and closed-source backbone models demonstrate that TBA reliably implants conditional backdoors while preserving clean-task utility, matching or even surpassing direct skill injection. The results reveal a critical vulnerability in trajectory-driven skill evolution.

---


### 6. [Yesterday's Shield, Today's Spear: A Self-Evolving Safety Guardrail in Production](https://arxiv.org/abs/2608.08471)

**<font color=#1a73e8>作者：</font>** Cong Ming, Jingyi Chen, Bin Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deployed LLM safety guardrails are predominantly static: trained once and frozen at release, while new jailbreak techniques and previously un-addressed harmful categories emerge within days, leaving the defense perpetually a step behind. We present SESG (Self-Evolving Safety Guardrails), a multi-agent system running in production. SESG monitors the live traffic behind a deployed guardrail and surfaces two classes of failure: jailbreaks novel in form and harmful categories novel in content. Once a failure is confirmed, a generation agent synthesizes paired training data targeted at it; a validation agent rebalances the batch toward the direction in which the deployed model errs, so that the model's own mistakes steer its training set; and a routing agent matches the training action to the diagnosed gap and returns the next version to production. Over six rounds of live evolution (V0 to V6), a 1.7B guardrail adapts to a new threat in 16-24 hours, with about 2 hours of human effort, versus the 40-90 hours of the manual process it replaces. On six emerging threats, it outperforms static guardrails from 0.6B to 9B and an adaptive baseline while preserving its general screening competence. Since April 2026, SESG has been the primary update pipeline of Sangfor's guardrail, autonomously closing 14 of 15 new threat scenarios in two months. We release 9 test sets for the 6 new threats at this https URL. Warning: This paper contains examples that may be harmful or offensive.

---


### 7. [HoloAegis: Frozen Representation, Topological Inference: Minimally Parametric Safety Manifolds for Zero-Shot LLM Guardrails](https://arxiv.org/abs/2608.08485)

**<font color=#1a73e8>作者：</font>** Tak Ho Alex Li, Kaijie Liu, Lik-Hang Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current LLM safety guardrails face a fundamental tension: fine-tuning distorts pre-trained representations while generative judges incur prohibitive inference costs. We challenge the prevailing paradigm by asking: can safety be achieved through pure geometric reasoning over frozen semantic representations? We present HoloAegis, a minimally parametric topological inference framework that decouples representation from reasoning. We term our approach minimally parametric because the only free parameters are the anchor count K and the temperature tau, both fixed after construction and requiring no gradient-based training. An un-fine-tuned encoder maps text to a unit sphere, after which all decisions are purely geometric. We formalize safety evaluation as a Gibbs-Boltzmann Free Energy computation over a pre-computed System Topology Anchor Bank, and we introduce Dual Time-Scale Exponential Moving Averages to detect progressive multi-turn semantic drift. Our key theoretical insight is a Topological Boundary Stability Conjecture: we provide theoretical motivation and strong empirical evidence that sparse anchor centroids stabilize the decision boundary against high-frequency lexical perturbations far better than full vector space methods. Evaluated across 8 benchmarks, HoloAegis achieves state-of-the-art accuracy (1.0000 AUC on AuthenHallu, 0.9802 on HarmBench) with sub-millisecond latency, zero cold-start data, and cross-lingual transfer (0.9758 AUC on Chinese CHIFRAUD).

---


### 8. [When Skills Meet Safety: Benchmarking and Characterizing the Adaptive Jailbreak Robustness of Skill-Merged LLMs](https://arxiv.org/abs/2608.08542)

**<font color=#1a73e8>作者：</font>** Yu Ma, Hongli Shi, Jing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging has become the default way to give an aligned language model new skills without retraining: a practitioner folds task vectors from math, code, or domain specialists into a safety-aligned base using task arithmetic, TIES, or DARE. This convenience is known to carry a safety cost, but almost all of that evidence rests on static refusal tests: fixed harmful prompts scored for compliance. We argue this is misleading. Because safety alignment is "shallow," concentrated in the first few generated tokens, a merged model's static refusal can stay clean while a real adaptive attack still breaks it. We introduce SkillSafe-Bench, a controlled benchmark that scores skill-merged models on static refusal, adaptive jailbreak robustness, and capability retention under a conservative two-judge AND rule. Across six open-weight bases (five families, two scales), static safety does not predict robustness to attack: under a semantic template attack, safe-looking merges on the fragile bases (both Qwen scales and Gemma) are jailbroken 60-76% of the time while others (Llama, Phi-4) stay robust. We further show the static effect of merging is base-conditional, characterize same-recipe abliteration-style safety erosion through a data-free geometric signal (the overlap of a task vector with a safety subspace), and outline SubSafe-Merge, which projects this overlap away to remove that erosion at held capability. Adaptive evaluation is not optional for merged LLMs: the models that most need it look safe under static screening.

---


### 9. [Toward Metacognitive One-Shot Indirect Prompt Injection: Strategy Abstraction Via Outcome-Conditioned Reflection](https://arxiv.org/abs/2608.08795)

**<font color=#1a73e8>作者：</font>** Sihan Hou, Xinmeng Hou, Zhijun Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using large language model (LLM) agents are vulnerable to indirect prompt injection (IPI), in which malicious instructions embedded in external observations manipulate subsequent agent decisions and actions. Most existing adaptive attacks rely on repeatedly querying and refining against the target agent, whereas realistic attackers may have only a single opportunity to interact with an unknown target agent. We propose SAVOR (Strategy Abstraction Via Outcome-Conditioned Reflection), which shifts attack adaptation from test-time iteration to offline strategy distillation. SAVOR performs outcome-conditioned reflection over successful and failed trajectories collected from disjoint training environments, validates context-conditioned candidate strategies, and iteratively consolidates them into a reusable strategy memory. At test time, the frozen memory guides the generation of a single payload for each unseen target, requiring only one target-agent query and no target-agent feedback. Across two benchmarks and three victim models, SAVOR attains the highest average attack success rate in all six settings, leading the strongest prior attack by 2.5 to 11.8 points and the same injection channel without strategy learning by 23.1 points on Agent Security Bench, which holds out attacker tools, and 28.6 points on OpenClaw-IPI, an executable benchmark we introduce that holds out attack goals and verifies attacks through tool interactions and execution receipts. A memory learned under one defense also transfers to another.

---


### 10. [Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection](https://arxiv.org/abs/2608.08939)

**<font color=#1a73e8>作者：</font>** Rahul Deivasigamani, Sayeda Faatin Alvi, Derqui Andrea 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rise of autonomous AI agents represents a major paradigm shift in how users interact with mobile devices. Frameworks such as MobileRun and Mobile-Use can autonomously navigate Android applications and execute complex multi-step tasks. To interpret user interfaces, these frameworks rely primarily on Android accessibility (A11y) trees and secondarily on visual screenshots. In this paper, we demonstrate that this architectural dependence on unsanitized accessibility metadata, together with visual input, introduces a systemic vulnerability to indirect prompt injection. We show that adversarial prompts can cause autonomous agents to abandon their original objectives, violate context boundaries, and perform unauthorized device actions. Our empirical evaluation demonstrates goal hijacking, context drift, and unauthorized actions across visually hidden and fully exposed attack scenarios. In aggregate, MobileRun reaches an attack success rate of 0.822 with Gemma4:31B, while Mobile-Use with Qwen3.6:35B reduces this to 0.150 but does not eliminate context drift or unauthorized actions. These findings reveal that current mobile agent frameworks fail to enforce semantic context boundaries, treating passive environmental text as trusted instructions. Finally, we present a taxonomy of these attacks and discuss the need for zero-trust input validation, dedicated security agents, and strict context isolation within mobile agent architectures.

---


### 11. [Pragmatic Attack Surface: Vulnerabilities of Implicit Context in Large Language Models](https://arxiv.org/abs/2608.09551)

**<font color=#1a73e8>作者：</font>** Bocheng Chen, Han Zi, Roucheng Ou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the era of large language models (LLMs), attackers often manipulate natural language to elicit unsafe or harmful outputs, creating a new natural language attack surface unique to LLM-based systems, where attacks directly exploit explicit linguistic cues in user prompts to bypass the safety mechanism of LLMs. However, such attacks can often be mitigated by existing safety alignment algorithms. On the other hand, human language is inherently grounded in pragmatics, necessitating typical context to interpret language, e.g., world knowledge, social norms. However, such contexts are often implicit because they are not directly expressed in human language and are not sufficiently leveraged in safety alignment, creating a fundamental mismatch between human language interpretation and safety alignment approaches. In this paper, we demonstrate that this mismatch exposes vulnerabilities in LLMs. We refer to this vulnerability as the pragmatic attack surface, which can be exploited to achieve high attack success rates. The experimental results demonstrate that our proposed approach outperforms baseline attack methods across various open-source and closed-source models by a substantial margin.

---


### 12. [ElasticBack: Stealthy Conditional Backdoor in LLM-Agent Skills via Coupled Trigger-Rule Optimization](https://arxiv.org/abs/2608.09577)

**<font color=#1a73e8>作者：</font>** Hao Sui, Simeng Qin, Jie Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills, bundles of instructions and resources that an LLM agent loads on demand, form an emerging supply chain where a single poisoned skill can persistently compromise every agent that installs it. However, existing skill attacks either fire on every request or rely on fine-tuned weights or multiple skills, leaving a conditional and low-cost backdoor unexplored. In this work, we present ElasticBack, an effective conditional single-skill backdoor that plants a rule R in the skill document and a benign-looking trigger T in the user query, so the malicious payload fires only when both co-occur. ElasticBack binds the two sides through a trigger-as-switch construction, generating R via semantic-anchored rule injection. It then freezes R and evolves T against it with a stealth-constrained genetic search, so that effectiveness and stealth are optimized, keeping the backdoor weight-free and dormant on benign inputs. Extensive experiments across three target behaviors (50 skills each) and four agent LLMs show that ElasticBack attains a high attack success rate at a near-zero false-positive rate with preserved clean accuracy, transfers across models, and evades deployment-time defenses. These results motivate stronger defenses for the skill supply chain.

---


### 13. [Measuring the Wrong Thing: Internal Harmfulness Scores Anti-Rank Successful Jailbreaks](https://arxiv.org/abs/2608.09624)

**<font color=#1a73e8>作者：</font>** Mingyu Luo, Ming Deng, Zilang Qiu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Internal safety scores judge a prompt before any text is generated, and they are validated by how well they separate harmful prompts from benign ones. That separation is then read as evidence that the score will also catch the attacks that succeed. Harmful intent is a property of the prompt. Jailbreak success is an outcome produced later by a particular target model, decoding policy, and judge. A filter tuned on a score that measures the wrong quantity spends its false positive budget on attacks that would have failed anyway. In this paper we audit that inference. Attention based measurements are usually read from prompt dependent locations, so a wrapper changes both the content being judged and the place the signal is taken from. We therefore introduce Active Attention Probing, which supplies a fixed content independent measurement coordinate. We pair every base goal with a plain and a wrapped version and generate real completions from the target models. On Llama, wrapping raises harmful generation from 0.05 to 0.27 while harmful intent AUROC falls from 0.936 to 0.803, so the attacks grow more dangerous while the prompts look safer to the score. Among wrapped harmful prompts the outcome AUROC is 0.220, which places the attacks that succeeded below the attacks that failed. Rare token, passive, and detector derived channels reproduce the reversal on the same matched design, and the reversal itself persists across three target models, seven attack families, and two independent judges. Distribution shift then degrades calibration and threshold transfer before it degrades ranking.

---


### 14. [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867)

**<font color=#1a73e8>作者：</font>** Alexander Panfilov, David Schmotz, Ilia Shumailov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Leading large language model providers now conceal their models' step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as blocks of encrypted text, which the client passes back with each subsequent request. Building on prior research, we identify an architectural vulnerability: these encrypted blocks are fully compatible and interchangeable across different sessions, users, and models within a provider's ecosystem. We exploit this compatibility to develop a scalable decryption jailbreak. By injecting an encrypted reasoning trace from a given model into a weaker, and less safeguarded model from the same provider, we force it to decode and output the trace verbatim in plaintext, without ever jailbreaking the more capable model directly. This vulnerability enables four distinct attack vectors. First, it circumvents anti-distillation mechanisms, allowing adversaries to extract a proprietary model's reasoning, as we demonstrate across Anthropic, OpenAI, and Google. Second, it allows for large-scale private data extraction. Developers frequently share session logs publicly, unaware of contents of the encrypted blocks. By decoding 315,320 reasoning blocks scraped from public repositories, we recovered 367 Personally Identifiable Information (PII) artifacts and 182 credentials. Third, it inadvertently reveals hazardous information hidden within the reasoning process, even in cases where the model's final, visible output safely rejects a malicious request. Fourth, attackers can leverage this flaw to execute invisible prompt injections, embedding malicious payloads entirely within encrypted blocks to poison public agentic rollouts. Following responsible disclosure, we propose concrete cryptographic and system-level mitigations to secure client-side reasoning.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
