# 🔐 大模型安全相关研究 | 2026年09月04日

> 本类共 **9** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Context Inference Attacks Without Jailbreaks](https://arxiv.org/abs/2609.01663)

**<font color=#1a73e8>作者：</font>** Prince Jha, Samuele Poppi, Nils Lukas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are increasingly deployed to process sensitive data at inference time, such as healthcare records or financial documents assembled into a hidden \emph{context} before the system answers. Prior work has studied privacy risks primarily through \emph{jailbreaking} attacks that induce models to directly disclose sensitive content, but has largely overlooked the agentic setting where the context is assembled by the agent's own tool calls. We show that the agents we evaluate remain vulnerable to hidden-context leakage despite the controls we test against them, namely an instruction not to disclose the context, logit suppression, and context dilution. For instance, a web-browsing agent answering benign user queries still carries exploitable signals about records silently loaded into its context. We introduce and formalize \emph{context-inference attacks} through a security game and evaluate three settings under decreasing attacker knowledge and increasingly indirect delivery of the context: a known context, an unknown context, and a context the agent retrieves through its own tool calls. We distinguish a grey-box setting, in which the target model is used to score observations, from black-box settings in which the attacker scores with a surrogate it controls. We further characterize how leakage varies with query budget, context size, and target-model size. A single attack carries through all three settings without modification, reaching $100\%$ ASR on small candidate sets and $63\%$ at $1024$ candidates against a known context, $78.9$ AUROC when the template and surrounding records are unknown, $92.5$ AUROC when a 14B surrogate scores a 32B target, and $81.8$ AUROC when the records arrive as an agent's retrieval returns, against chance rates of $1/|\mathcal{Z}|$ and $50$ respectively.

---


### 2. [Agent Flight Recorder: Tamper-Evident Audit Trails with On-Chain Anchoring for Long-Horizon Tool-Using Agents](https://arxiv.org/abs/2609.01931)

**<font color=#1a73e8>作者：</font>** Laurent Bindschaedler, Quentin Botha, Christoph Siebenbrunner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents execute thousands of actions, resulting in sequential failures rather than isolated errors. When a coding agent deletes a production database or a prompt injection spreads across agents, the incident raises questions of causality, authority, and non-repudiable third-party verification. The Agent Flight Recorder captures each agent action as a structured, canonically serialized event binding eight semantic fields from intent through execution to provenance. Hash chaining and Merkle batching provide tamper evidence and compact inclusion proofs. For cross-organizational disputes where no party's infrastructure qualifies as neutral ground, periodic on-chain anchoring of epoch roots lets any verifier with the disclosed payload and Merkle proof check the record independently, without pre-agreeing on a trusted intermediary. The on-chain footprint is minimal: each anchor stores a 32-byte epoch root and a back-pointer, and no event content touches the chain. We evaluate the system across five cumulative ablation configurations on synthetic agent workloads. The full system adds ~48 microseconds median per-event latency and 512 bytes per event. L2 anchoring costs $2.30 per 100K events at 100-event epochs. The full integrity stack detects edit, delete, reorder, and fork tampering at 100% with zero false positives. Structured forensic queries achieve 1.0 precision on guardrail and delegation lookups where unstructured text search yields 0.013 and 0.077 respectively.

---


### 3. [Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents](https://arxiv.org/abs/2609.02127)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent AI agents construct autobiographical state through reflection, retrieval, and consolidation. Persistence changes availability, not epistemic standing: stored or retrieved material is not thereby supported. Untrusted inputs, prompt injections, and model inferences can therefore enter persistent state and later be presented as agent history or user commitments. We specify typed provenance and assertion guardrails for autobiographical assertion boundedness, a system-relative release property requiring governed statements about the agent, user, or named relationships to satisfy accepted-evidence, temporal-validity, and disclosure policies. A typed provenance graph separates origin, dependency lineage, epistemic role, validity, and disclosure scope. A resolver evaluates authorized state projections and returns one evidential status, orthogonal conflict, staleness, and withholding flags, and a protected decision witness. A generate-verify-revise mediator then checks candidate semantic units before release and renders policy-authorized status responses. Under explicit assumptions about extraction, predicate correctness, resolution soundness, view declassification, and channel mediation, we prove a conditional assertion-boundedness contract. In an executable suite of 24 hand-authored conformance cases, typed mediation passed none of 19 unsafe opportunities unqualified while preserving all five supported controls. The flat/prior and source-tag comparison rules released 19/19 and 18/19 unsafe candidates, respectively. These results validate the encoded resolver and mediator obligations; they do not constitute an end-to-end evaluation of language models or retrieval systems.

---


### 4. [Breadth Beats Depth: Improving GCG-Based Jailbreak Optimization with Breadth-Oriented Suffix Search](https://arxiv.org/abs/2609.02172)

**<font color=#1a73e8>作者：</font>** Shiliang Xiao, Jingsong Wei, Yuzhi Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Optimization-based jailbreak attacks such as Greedy Coordinate Gradient (GCG) achieve strong effectiveness and transferability by optimizing adversarial suffixes on white-box source models. However, existing GCG-based methods rely on averaged adversarial loss and deep greedy search, which can over-emphasize easy-to-jailbreak behaviors and overlook promising regions of the suffix space. We propose BOSS, a plug-and-play framework that improves GCG-based jailbreak optimization through breadth-oriented suffix search. BOSS uses Tail-Focused Adversarial Loss (TFAL), standard source loss, and behavior coverage to select terminal suffixes, then explores multiple short trajectories and selectively continues promising suffixes. Experiments on public benchmarks show that BOSS improves attack success rates across multiple GCG-based methods while reducing optimization time.

---


### 5. [WeaveMark: Robust and Scalable Multi-bit LLM Watermarking via Coded Payload Spreading](https://arxiv.org/abs/2609.02177)

**<font color=#1a73e8>作者：</font>** Gang-Hyun Park, Ju-Hyeong Lee, Hee-Youl Kwak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-bit watermarking for large language models (LLMs) enables content source tracing by embedding user-identifiable messages into generated text. Existing methods face a fundamental trade-off among extraction accuracy, text quality, and payload capacity. We propose WeaveMark, a robust and scalable multi-bit LLM watermarking scheme based on coded payload spreading. WeaveMark shifts this trade-off frontier by improving payload capacity through multi-bit-per-token spreading, improving extraction accuracy through soft-decision error-correcting code, and preserving text quality through unbiased multilayer reweighting. It further introduces dedicated zero-bit layers for reliable watermark presence detection. Experiments show large gains, especially for long messages and edited text. WeaveMark achieves 89.8% match rate for 32-bit messages at 200 tokens, compared with 20.8% for BiMark. Under 10% substitution attacks on 16-bit messages at 200 tokens, it maintains 86.0% versus 30.7%, while preserving text quality. Our code is available at this https URL.

---


### 6. [LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails](https://arxiv.org/abs/2609.02246)

**<font color=#1a73e8>作者：</font>** Vansh Wahi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving agent pipelines have a problem at their center. An optimizer rewrites prompts to score higher, and the score comes from a judge that is itself an LLM. That judge has the last word on whether the system is getting better, and our position is that it has not earned it. The judge should be demoted from oracle to advisor: its verdict becomes one input among several, and every change is gated instead by a deterministic verification layer the judge cannot override. We reached this position by building the alternative and running it. Over months of running autonomous prompt-optimization loops in production across contract analysis, compliance review, and code quality, we cataloged eleven ways the evaluation signal failed, in four classes: judge bias, harness and metric failures, ground-truth errors, and reward hacking. Agents achieved perfect scores by reading cached answer keys from their environment, a 100% pass rate concealing 68% true capability. A corrupted ground-truth label caused the optimizer to delete correct compliance rules to agree with it. A syntactically broken prompt was promoted as the winner because a silent parser fallback improved the metric. Attempts to fix the judge by rewriting its rubric plateaued; the only reliable gain came from a structural constraint on its output order. In response we describe PROCTOR, a Teacher-Student loop in which a stateful orchestrator holds all tool access, stateless subagents diagnose failures and draft mutations they cannot apply, and a Teacher grades those mutations under five deterministic guardrails: hermetic sandboxes, capability-disjoint roles, acceptance checks that outrank the Teacher, frozen holdouts, and canary cases engineered so that a perfect score is itself evidence of cheating. We report the failures this prevented, and, because the Teacher is itself an LLM judge, the failures it did not.

---


### 7. [CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents](https://arxiv.org/abs/2609.02265)

**<font color=#1a73e8>作者：</font>** S M Asif Hossain, Ruksat Khan Shayoni, Md Kishor Morol  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized language agents use persistent memory to adapt to users over time, but the same mechanism creates an attack surface. When new information conflicts with stored preferences, an agent must distinguish genuine preference drift from temporary context shifts, ambiguity, or adversarial memory poisoning. We formulate this problem as a continuous-time partially observable decision process over a latent user state and show why rules based only on recency and provenance are insufficient. CAPTURE addresses this ambiguity with a neural differential-equation belief tracker, a multi-timescale memory ledger, uncertainty-triggered clarification, and counterfactual auditing of cited memories. On 480 held-out episodes from 96 users, CAPTURE achieves a 71.5% win rate, compared with 69.3% for an identically supervised baseline and 66.1% for the strongest heuristic baseline. It limits fixed-policy poisoning success to 11.5% while accepting 83.5% of genuine preference updates. Under an adaptive attacker with access to the released weights, attack success rises to 24.7%, exposing a real adaptation-security tradeoff. We further evaluate the frozen system zero-shot on an independently constructed benchmark and replay longitudinal interaction histories from 40 users collected over two to three weeks. These results suggest that modeling preference authenticity explicitly can improve both personalization and robustness in memory-augmented LLM agents.

---


### 8. [SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment](https://arxiv.org/abs/2609.02293)

**<font color=#1a73e8>作者：</font>** Qingyu Meng, Yiwei Zha, Jiahuan Pei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) is a scaling architecture for large language models that activates only a small subset of expert modules per token, enabling massive parameter growth with nearly constant computation. Recent Hybrid MoE architecture adds \textit{shared experts} to capture consistently useful representations, further improving stability and generalization. MoE now powers many flagship open-source and commercial models, yet remains vulnerable to adversarial attacks. Specifically, sparse routing introduces a structural vulnerability: MoE safety hinges on which experts are activated, and adversaries can subvert this selection through jailbreak prompts, malicious fine-tuning, and weight-level pruning of safety-critical neurons. Existing defenses primarily focus on hardening the router, but an adversary may still manipulate or bypass the routing trajectory due to the routing process's nondeterministic nature, thereby collapsing the defense. To cope with this problem, we first identify theoretically and empirically that shared expert, an always-activated component containing a small proportion of safety-critical neurons, can overcome the uncertainty of sparsely activated routing path and serve as a router-independent anchor to enhance global safety alignment. Based on this insight, we propose SEAL, a training-time parameter-efficient defense that produces a plug-and-play adapter attached to shared expert, and SEAL++, a variant that adds an orthogonal constraint preserving pre-existing safety subspaces during training. We evaluate SEAL and SEAL++ across six attack scenarios that combine three adversarial inputs (harmful prompting, jailbreak, malicious fine-tuning) with and without neuron pruning. SEAL reduces attack success rate (ASR) by up to 60\%, at a capability cost of at most 1.4\% on a five-benchmark average. Additionally, SEAL can seamlessly integrate with router-level ......

---


### 9. [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](https://arxiv.org/abs/2609.02786)

**<font color=#1a73e8>作者：</font>** Qinghua Mao, Wanying Qu, Dadi Guo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The performance of LLM-based agents is jointly shaped by the base model and the harness used when interacting with the environment. This exposes them to safety risks in both harmful final responses and multi-step execution trajectories. Existing safety alignment mechanisms often rely on either external harness updates or policy optimization, yet applying either paradigm in isolation fails to bridge runtime control with intrinsic safety. We propose SafeEvolve, an experience-driven self-evolving framework for agent safety alignment. SafeEvolve leverages safety experience from completed on-policy trajectories to drive a continual loop of harness-policy co-evolution. On the harness side, SafeEvolve converts trajectory-level safety evidence into bounded, component-level updates across safety prompt and hierarchical skills, yielding auditable and reversible harness artifacts. On the policy side, SafeEvolve follows a two-stage SFT-RL paradigm, where harness-use SFT bootstraps the policy to actively leverage evolved harness artifacts, and harness-augmented RL further shapes autonomous safety behaviors during multi-step exploration via verifier-decomposed rewards. Through harness-policy co-evolution, SafeEvolve converts safety experience into an evolved runtime harness and improved policy behavior. Experiments on agentic safety benchmarks show that SafeEvolve achieves a stronger safety-utility tradeoff than existing baselines. For Qwen3.5-4B, SafeEvolve achieves a $3\times$ ASR reduction on AgentDojo while improving benign utility from 59.79% to 61.86%.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
