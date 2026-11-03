# 🔐 大模型安全相关研究 | 2026年11月04日

> 本类共 **16** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Kerkoporta: Injecting Structured-Output Backdoors in Reasoning Coding Agents](https://arxiv.org/abs/2611.00138)

**<font color=#1a73e8>作者：</font>** Georgios Syros, Blake Bullwinkel, Alina Oprea 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing large language model (LLM) backdoor attacks operate primarily in chat settings, where the risk is bounded by free-form text outputs. AI agents remove that bound by performing actions and executing commands on the user's machine. We introduce structured-output backdoor attacks against reasoning models in agentic coding settings. A trigger placed anywhere in the agent's context causes the model to emit an attacker-chosen tool call, which the harness executes, directly compromising the system's confidentiality, integrity, or availability. We present Kerkoporta, a methodology that constructs high-quality poison samples, injects the backdoor via supervised fine-tuning, and recovers utility loss with lightweight reinforcement learning. We evaluate on modern, heavily post-trained open-weight models across proprietary and open-source harnesses, focusing on coding for its wide adoption and long-horizon task structure. The attack reaches success rates of up to 96.2% and can be configured to generalize across harnesses or bind to a single target. The resulting models can outperform the clean baseline on standard utility benchmarks, giving victims a direct incentive to adopt them. Overall, we demonstrate that LLM backdoors can have critical security impacts in the context of modern coding agents, and we characterize the poisoning methodology required to insert backdoors that are both effective and stealthy in this setting.

---


### 2. [AgentCap: Capability-Based Runtime Authorization for Secure LLM Agent Execution](https://arxiv.org/abs/2611.00729)

**<font color=#1a73e8>作者：</font>** Aravinda Kashyap Kabbinamakki Suresh, Peng Gao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language-model agents commonly collapse two decisions that security systems separate: selecting an action and determining whether that action is authorized. When a model exercises standing authority, indirect prompt injection can convert influence over its reasoning into unauthorized effects. We present AgentCap, a runtime authorization layer that externalizes this decision from the model and mediates every tool invocation through an MCP wrapper. Each request declares an intent, and AgentCap evaluates policy constraints over trust, workflow prerequisites, mutually exclusive authority, and the provenance of security-sensitive arguments. Authorized requests receive short-lived, budget-bounded capability tokens that are validated at the tool boundary. Delegation is restricted to session-bound parent-child chains that preserve action and resource while budget and lifetime can only be attenuated, preventing authority from being expanded or reused across unrelated agent sessions. A declarative policy language provides a common representation for runtime enforcement and predeployment analysis. Across AgentDojo and InjecAgent, AgentCap reduces attack success in every evaluated model-benchmark setting, including zero attack success with GPT-5.4 on both benchmarks. Controlled adversarial scenarios further show that AgentCap blocks every attempted unauthorized execution (ASR 0%) while preserving all legitimate operations exercised. These results demonstrate that agent security requires authorization of model-proposed effects at the tool boundary, independently of the model's reasoning.

---


### 3. [Inherited or Learned? Backdoor Selectivity in Distilled Language Models](https://arxiv.org/abs/2611.00748)

**<font color=#1a73e8>作者：</font>** Dipto Sumit, Sanzar Rahman, Ramisa Faria Puspita 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distillation is a routine step in building small language models, and a backdoored teacher can pass its backdoor to the student. We study what a student inherits when the backdoor is a rare string that triggers a fixed refusal. Keeping the trigger fixed, we vary only where it appears, at a random word boundary or appended to the instruction, and compare teachers and students on the exact trigger, six control strings and clean inputs. Across Qwen2.5, Llama 3.2 and Gemma 3, with 5% of transfer prompts triggered, randomly inserted triggers become less selective after distillation in all nine teacher-student pipelines, while appended triggers gain selectivity in Qwen and Llama and change little in Gemma. Students trained on the same prompts without a teacher show that much of this is not inherited. Llama and Gemma students learn an appended backdoor from the 150 poisoned examples alone, and only Qwen's 0.5B student needs the teacher. The data also sets where the trigger works. Gemma teachers respond to it anywhere, but their students only when it is appended. Audits should compare teacher and student on the same inputs, probe several trigger positions and include a student trained without the teacher.

---


### 4. [Context-Shielded Backdoor Attack against Large Vision-Language Models](https://arxiv.org/abs/2611.01252)

**<font color=#1a73e8>作者：</font>** Zhifang Zhang, Qiang Huang, Chenpeng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) routinely use inference-time visual-token compression to prune hundreds of patch tokens down to a compact budget. Existing LVLM backdoors fire whenever a triggered image appears, whereas prior deployment-triggered attacks activate only when model weights are quantized or pruned. However, conventional LVLM backdoors exhibit nearly 100% attack success rate (ASR) under full-token inference, immediately exposing compromised checkpoints during pre-deployment auditing. We reveal context stripping: surrounding clean visual tokens suppress an embedded trigger at full length, whereas token pruning strips this context away and activates the backdoor. Motivated by this finding, we propose StripWake, a projector-only backdoor that remains dormant under full-token auditing yet activates across unseen compressors. Specifically, StripWake pairs clean-supervised full-token views with target-supervised randomized compressed views, and aligns early visual attention with a frozen benign teacher to preserve clean utility. On LLaVA-1.5-7B across nine unseen compressors, StripWake stays dormant at 0.4% full-token ASR yet achieves 94.0%-99.7% compressed ASR across five primary compressors without CIDEr loss.

---


### 5. [MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents](https://arxiv.org/abs/2611.01700)

**<font color=#1a73e8>作者：</font>** Zhihua Wang, Yunhao Feng, Yifeng Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents often rely on persistent memory to retain user preferences and operational rules across sessions. However, this capability introduces a new safety risk: malicious instructions from messages, documents, or Web content can be retained in memory and influence future tasks even after the original attack content is removed. Existing attack success metrics, however, fail to capture who is affected and how attacks translate into downstream harm during otherwise normal task execution. We introduce MemHarmBench, a victim-centric benchmark for evaluating cross-session prompt injection in memory-persistent AI agents. MemHarmBench considers three categories of potential victims: users, workspace/project owners, and external stakeholders. Our evaluation first exposes an agent to malicious instructions and tests whether they are retained in memory. We then remove the attack content and initiate a new session with a legitimate task while preserving the agent's memory. We jointly evaluate whether the agent follows the attacker's intent, completes the legitimate task, and exhibits observable execution anomalies. Across multiple agent systems, we find that cross-session attacks can remain behaviorally stealthy: agents often complete tasks normally and exhibit no detectable anomalies while still making critical decisions aligned with the attacker's intent. By connecting malicious memory retention to downstream decisions and affected parties, MemHarmBench provides a systematic framework for exposing safety risks that conventional attack- and task-success metrics may overlook. We publicly release MemHarmBench at this https URL.

---


### 6. [Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security](https://arxiv.org/abs/2611.01976)

**<font color=#1a73e8>作者：</font>** Shiyu Kan, Yue Qi, Yufei Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model based agents increasingly rely on external tools to invoke services and interact with web resources. These tools can evolve through software updates, yet agentic frameworks may continue trusting them without re-verifying their safety after implementation changes. This tool update gap creates a supply-chain vulnerability in agentic systems: because updated tool code executes outside the LLM's context window, malicious functionality embedded in tool updates can bypass defenses centered on model-visible interactions, leaving agents exposed to stealthy, persistent threats that existing in-context defenses can hardly address.
To thoroughly investigate this threat, we introduce ETUDE (Exploiting Tool Updates for Direct Execution), an attack that embeds malicious functionality into updates of initially benign tools to produce compromised tools, while preserving their legitimate tool functionality. Unlike prompt-based attacks, ETUDE operates entirely outside the LLM's context and requires no adversarial instructions, thereby bypassing defenses restricted to model-visible content. We evaluate ETUDE across three representative attack workloads and seven widely used commercial and open-source agentic frameworks, including Gemini CLI, Codex CLI, and Claude Code. The results show that ETUDE achieves a 97.6% ASR while maintaining a 95.9% legitimate task completion rate.
We further examine existing defenses and find that they provide insufficient protection against this threat. These findings expose a fundamental blind spot in current agent security practices: trust established for a tool does not necessarily remain valid after its implementation updates.

---


### 7. [HaloGuard 2.0: An Open-Weights Constitutional Output Guard for Multilingual Response Safety](https://arxiv.org/abs/2611.02134)

**<font color=#1a73e8>作者：</font>** Ashmiya Lenin, Navaneeth Sangameswaran, Preetham S  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An input guard decides whether a request reaches the model, but never sees what the model says. Harm that emerges during generation, because a jailbreak passed the input layer or a benign request drifted into operational detail, is visible only on the output side and only as tokens arrive. We present HaloGuard 2.0, an open-weight streaming output guard that assigns a safe/unsafe probability to every response token in a single forward pass, so a deployment can stop the stream once harm is confirmed. The guard reuses the constitution of HaloGuard 1.0, our input guard, to organise a 478,532-response training corpus, and supervises each token from the point where the response becomes harmful. We find that a guard trained on conventionally shaped data learns a shortcut specific to streaming: it judges the prompt instead of the response, and handles only 13.9% of matched safe/unsafe response pairs correctly. We correct this with a second phase on 106,043 counterfactual responses built around the base guard's own failure modes, and release the equal-weight average of the base and corrective models. On six English response-safety benchmarks, HaloGuard 2.0-0.8B reaches a macro F1 of 83.6 (83.3 on held-out halves of the decision-rule search), up from 72.8, with 38% fewer false positives. It matches the strongest full-response guards with 5-10x fewer parameters and is 2.6 points above the strongest streaming guard, Qwen3Guard-Stream-4B. A multilingual variant, HaloGuard 2.0-Poly-0.8B, trained on PolyGuardMix, reaches 83.1 F1 on the response labels of PolyGuardPrompts across 17 languages, 5.0 points above the strongest baseline. On one H100 the guard costs 0.37 ms per token per stream when moderating 64 concurrent responses. Both guards are hardened continuously through the weekly red-teaming protocol of HaloGuard 1.0, extended here to the output layer.

---


### 8. [LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents](https://arxiv.org/abs/2611.02332)

**<font color=#1a73e8>作者：</font>** Sreehari Sankar, Debargha Ganguly, Vikash Singh 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language-model agents often execute actions that their domain policies forbid. We present LeanGuard, a runtime that checks every proposed tool call against a policy written in Lean4 before the call reaches the environment. Policies combine state predicates with scoped past-time temporal operators over the execution history, evaluation is fail-closed, and the decision procedure is proved equivalent to a LeanLTL semantics. A denied call can be corrected in two ways. With feedback, the agent receives the violated rule and a hint; with proof-guided repair, Lean metaprogramming searches for a nearby call that preserves the user's intent and proves that the policy admits it, without the model. On Tau-Bench with five Qwen models (0.8B-27B), unguarded agents execute at least 33 calls that the Lean policy forbids, while LeanGuard executes none; with feedback, task success does not change significantly. On DTap, LeanGuard reduces direct prompt-injection success from 57.9% to 5.9%, and in telecom, where benign tasks need no writes, benign success is unchanged. Feedback reduces repeated blocked calls and raises task success for four of five models over a bare denial. On replayed denials, repair proves an admissible edit for 88 of 252 denials caused by argument values, in a median of 2,ms.

---


### 9. [Cumulative and Audited Guardrail Tool Evolution for LLM Agent Safety](https://arxiv.org/abs/2611.02516)

**<font color=#1a73e8>作者：</font>** Xiao Yang, Aishan Liu, Siyuan Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate in open-world environments where safety risks cannot be fully predefined. However, most existing guardrail mechanisms remain static, relying on fixed rules, prompts, or classifiers that generalize poorly to emerging risks. Here we present EVOLVE, a tool-level self-evolving defense framework that formulates agent security as a process of cumulative security evolution. Inspired by how human societies transform experiences into transferable protective knowledge, EVOLVE externalizes security knowledge into executable guardrail tools that are continuously inherited, independently audited, and iteratively refined through lifelong interaction. Across multiple benchmarks, backbone models, and embodied environments, EVOLVE consistently outperforms existing defenses across diverse risk scenarios with +22\% average F1 score. We further validate the framework in real-world robotic and autonomous agent systems. Our results suggest that scalable agent safety may require continuously evolving defense systems rather than static guardrails.

---


### 10. [Ranked but Not Stopped: Detecting Prompt-Injection Hijacks from Typed Decision Models' Output Probabilities](https://arxiv.org/abs/2611.02522)

**<font color=#1a73e8>作者：</font>** Junwei Yao, Jianan Liu, Yongxi Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Programs that use a language model as a classifier act on its most probable label. Text injected into the input can move that label to one the attacker chooses, a hijack. A monitor that does not know the attacker's label can read the model's own confidence and raise an alarm when the top probability is low. We test this monitor on AG News topic classification with five systems, three of them served through a provider's API. Pooled over five families of injected text, low confidence ranks hijacked answers above clean ones on four of the five systems (AUROC 0.86-0.90). Ranking them does not stop many of them. A threshold set so that at most 5% of clean answers to separate calibration articles alarm falls among the least confident clean answers, and every more confident hijack passes. In our main gate run on the three API-served systems, the monitor misses 51-70% of the hijacks caused by a plain injected note (per-system point estimates). When the note adds one handwritten sentence that calls the target certain and asks for full probability, the monitor misses 99-100% of the hijacks, although low confidence still ranks them at AUROC 0.70-0.79. Confidence monitors should be tested at their operating alarm rate, against attackers who claim certainty.

---


### 11. [SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in Language-Model Search](https://arxiv.org/abs/2611.02643)

**<font color=#1a73e8>作者：</font>** Kainan Zhou, Gangzhen Qian, Janet Sung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An indirect prompt injection can affect a search-augmented large language model only after its carrier page reaches model context. SearchInject controls this admission decision with a joint score combining retrieval relevance, search-abuse cues, instruction likelihood, and two relevance interactions. A quarantine threshold is selected under an empirical 0.5% clean-candidate false-quarantine constraint on a calibration split. Evaluation uses 300 held-out SciFact queries and held-out payload categories within four construction families already represented during development. Across 1,200 query-family outcomes per retriever, top-10 target exposure falls from 0.9408 to 0.1583 for BM25, from 0.9158 to 0.1508 for a normalized hybrid, and from 0.8450 to 0.1375 for latent semantic analysis. These are relative reductions of 83.2-83.7%; the largest absolute change in clean normalized discounted cumulative gain at rank 10 is 0.0018. The frozen threshold yields clean test false-quarantine rates of 0.59-0.65%, above the empirical calibration constraint. A query-level analytical reanalysis accounts for the repeated construction outcomes under an independent-query assumption. A separate 104-case generation follow-up records context removal but no confirmed undefended hijacks under a post hoc endpoint, so it cannot estimate a reduction in attack success. The evidence supports retrieval exposure control within the evaluated construction families; the benefit of the interaction terms at matched clean cost remains unresolved.

---


### 12. [ATrust: Adaptive Trust Boundary Expansion for Securing LLM Agents](https://arxiv.org/abs/2611.02741)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Zhichao Lu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents take on more complex tasks with greater autonomy, security has become a major obstacle to their broader deployment. Unlike in attacks that require complex exploitation of operating system vulnerabilities, attackers can easily hijack agents through indirect prompt injection (IPI), leading to privacy leakage, financial loss, and destructive operations. However, existing defenses often make security decisions based on limited static trusted evidence or assess observations in isolation. Such rigid trust assumptions can cause task-essential information to be unnecessarily discarded, resulting in over-defense and degraded agent functionality. To address this problem, we propose ATrust, a defense mechanism that adaptively expands the trust boundary during agent runtime. Starting from the user query as the root trust anchor, ATrust evaluates external observations against the current trust boundary and execution state, progressively admitting task-essential information as new trust anchors. This preserves necessary environmental feedback while excluding irrelevant content, whether benign or malicious, from subsequent decision-making, thereby limiting unnecessary exposure to external environment. We evaluate ATrust on AgentDojo and AgentDyn, where it achieves the strongest overall security--utility trade-off among existing defenses. With GPT-4o as the engine model, ATrust reduces the attack success rate on AgentDyn from 37.80% to 4.37% while enhancing utility by 10.00%, outperforming AuthGraph, the state-of-the-art defense, by 12.33%. These results demonstrate the effectiveness and practicality of ATrust.

---


### 13. [PGuard: A Native, Streaming, and Plug-in Guardrail for Multimodal Large Language Models](https://arxiv.org/abs/2611.02791)

**<font color=#1a73e8>作者：</font>** Junyu Lin, Mengjie Wu, Yonghao Dong 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As streaming generation becomes the dominant serving paradigm for both text-only and multimodal large language models, ensuring safety throughout the generation process has become a critical challenge. We introduce PGuard, a native, streaming, and plug-in guardrail that transforms safety monitoring from an external serving dependency into an integrated capability of the backbone model. PGuard directly leverages the backbone's intermediate representations for token-level safety detection, without altering its original inference pathway or generation behavior. Specifically, dynamic layer gating selectively aggregates residual-stream representations across layers to extract safety-relevant signals during both prefill and autoregressive decoding. To balance detection accuracy and computational efficiency, PGuard supports multiple representation-modeling architectures, including a lightweight stateless variant and sequence-aware variants built on multi-scale causal EMA-attention and GRU-based recurrent modules. Its design also accounts for the execution characteristics of LLM serving frameworks, such as SGLang, optimizing computation and data access to minimize additional runtime and synchronization overhead. As a result, PGuard incurs only 0.82-2.26% end-to-end overhead on the hundred-billion-parameter backbone Qwen3.5-122B-A10B served by SGLang. Extensive evaluations across more than 30 benchmarks spanning text and multimodal safety, jailbreaks, cyber and CBRN risks, multilingual scenarios, and real-world traffic demonstrate state-of-the-art performance among native guardrails. On text queries with Qwen3.5-9B, PGuard achieves an average F1 score of 0.836, approaching dedicated external guardrails, while supporting deployment-time configuration of category-specific thresholds and enforcement actions.

---


### 14. [Predictive Safety Guardrails Do Not Always Make LLM Agents Safer](https://arxiv.org/abs/2611.02815)

**<font color=#1a73e8>作者：</font>** Weixiang Zhao, Zhihao Liu, Guancheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly take consequential actions in digital and physical environments, where safety risks may emerge only after multiple interaction steps. This has motivated world-model-driven predictive safety guardrails, which anticipate future consequences before execution. However, existing evaluations largely focus on end-to-end safety outcomes, leaving unclear whether safety gains arise from reliable prediction and faithful use of predicted risks. In this work, we systematically diagnose the prediction-to-action pipeline along three dimensions: how world-model predictions are integrated into decision making, whether the predictions themselves are reliable, and whether their content is faithfully used. Across seven policy models and two safety environments, we find that stronger prediction involvement does not yield monotonic safety gains and can reduce task completion while substantially increasing inference cost. We further find that world-model predictions remain insufficiently reliable, especially over longer horizons, where safety prediction degrades substantially relative to near-term forecasting. Finally, we find that safety gains can persist even under corrupted predictions, while locally verified predictions still leave subsequent safety violations, showing that predictive content is not faithfully incorporated into the decision process. Together, these findings expose a fundamental prediction-to-action gap in current predictive guardrails: producing more or seemingly accurate foresight is insufficient unless that foresight is both reliable and faithfully translated into safer decisions.

---


### 15. [IAMRAGBENCH: Benchmarking Authorization Expansions in LLM-Generated AWS IAM Policies under RAG Poisoning](https://arxiv.org/abs/2611.03431)

**<font color=#1a73e8>作者：</font>** Hasan Kaplan, Indika Kumara, Willem-Jan van den Heuvel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) using retrieval-augmented generation (RAG) can synthesize Amazon Web Services (AWS) Identity and Access Management (IAM) policies from tasks and operational documents. Attacker-controlled context may induce provider-valid policies that exceed trusted authorization requirements. We present IAMRAGBENCH, a 60-case benchmark spanning scope, conditions, explicit denies, trust, permissions boundaries, and role delegation. It combines deterministic authorization-envelope scoring with case-specific validation, including request-level checks where supported. An attack requires a provider-valid clean policy that satisfies the task and a provider-valid treatment policy that violates the envelope, matches a predeclared goal, preserves an intended request, and newly authorizes a forbidden request.
Across five endpoints, included-context exposure produces 49 exact authorization deltas, including 46 goal-matched attacks (46/292; 15.75\%). End-to-end BM25 over 720 documents retrieves the designated poison for all 60 tasks at \(k=5\) but produces 7/294 goal-matched attacks (2.38\%). Presenting the same weakening as a final security architecture exception produces 74/116 attacks in a frozen two-endpoint stress test (63.79\%) and 115/294 in a post hoc all-five extension using the same frozen prompts (39.12\%). In a replay of 194 provider-valid treatment policies that violate task requirements, AWS \texttt{CheckNoNewAccess} reports no new access for four of 168 goal-matched exact attacks. The full pre-deployment rule rejects all 171 exact deltas and routes five unresolved cases to review. These findings support treating IAM copilots as untrusted proposal generators whose outputs require independent authorization checks before deployment.

---


### 16. [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study](https://arxiv.org/abs/2611.03555)

**<font color=#1a73e8>作者：</font>** Farooq Shaikh, Biagio Montaruli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) lets agentic AI frameworks connect language models to external tool providers, but it carries attacker-controlled content (tool descriptions, schema fields, and response data) into model context without validation. Prior benchmarks measure model compliance with poisoned instructions without confirming real execution. We present the first cross-framework measurement of MCP tool poisoning with real tool execution. A 25-class root-cause taxonomy unifies prior classifications, and the open-source tool mcpvenom drives a 9,720-cell susceptibility matrix across 12 frameworks, 18 models, and 45 attack scenarios, with a dual oracle that confirms exfiltration via canary HTTP receipt. The overall attack success rate is 22.9% (2,113 vulnerable cells). Of these, 64.9% dispatch an attacker tool call, 23.0% contact the attacker endpoint, and 12.1% verifiably exfiltrate a secret. Resistance is model-level: nine core frameworks cluster within 23 to 26% (chi-squared = 3.30, p = 0.91), and no framework implements intentional defense. Incidental framework properties mitigate in specific cases, and a regex description scanner rejects 20 of 45 scenarios at a 7.2% false-positive rate, so metadata scanning alone is a partial control. Model ASR ranges from 0.4% to 49.7%. Claude Opus 4.8 is vulnerable in 8 of 530 cells while issuing 223 explicit refusals. A code-level audit finds no intentional defense across twelve frameworks, and all five coordinated disclosures across four vendors were rejected.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
