# 🔐 大模型安全相关研究 | 2026年09月09日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety Refusal](https://arxiv.org/abs/2609.04482)

**<font color=#1a73e8>作者：</font>** Alejo López-Ávila, Iker García-Ferrero, Jezabel Garcia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment is usually posed as a topic-level question: is this subject harmful? Deployments ask a narrower one. A civics tutor and a public-sector assistant may share a base model yet need different boundaries inside the same topic, refusing targeted political manipulation while still answering factual questions about the same election. We formulate this as narrow-boundary safety and introduce an offline self-generated framework combining controlled topic generation, coverage repair, in-distribution compensation data, and harmful-benign pairs for training and evaluation. Single-shot generation leaves 19.88% of prompts without accepted refusal traces, whereas escalating retries leave 0.20%. On political persuasion with Qwen3-8B, training on refusal data completed through Escalate increases target-domain refusal from 9.47% to 84.75% and reduces the mean unsafe-response rate across three broader harmfulness benchmarks from 26.26% to 0.14%, but increases XSTest over-refusal from 2.00% to 74.00%. In a separate matched comparison, replacing external responses with verified target-model responses reduces over-refusal from 15.20% to 5.20%. Boundary-pair data reduces comply-side over-refusal on held-out pairs from 32.94% to 4.16%, while harmful-side refusal decreases only from 91.88% to 87.72%. These results show that data composition controls the safety and usability trade-off, and that safety alignment should be evaluated on both sides of the intended refusal boundary.

---


### 2. [Rethinking Indirect Prompt Injection as a Test-Time Search Problem](https://arxiv.org/abs/2609.04495)

**<font color=#1a73e8>作者：</font>** Duong M. Nguyen, Joon Sik Kim, Blazej Manczak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We formulate indirect prompt injection as a test-time search over a task-dependent attack surface induced by the environment, user task, and injection task. To operationalize this formulation, we introduce an agentic attacker with a dedicated search harness that performs environment reconnaissance, structured reasoning over attack strategies, and adaptive evaluation using victim-agent feedback. Across heterogeneous tasks, we find that increasing attacker test-time compute improves vulnerability discovery and exploitation, while ablations show that explicit strategy management is important for avoiding redundant search and sustaining gains at larger budgets. These results suggest that agentic security evaluations should characterize both the attacker's search procedure and compute budget, rather than treating attack success as a budget-independent property of the victim. More broadly, our findings identify the attacker's adaptive search over the system attack surfaces as an important and underexplored security risk for tool-using agents.

---


### 3. [Repeat-After-Me: Black-Box Adaptive Visual Prompt Injection](https://arxiv.org/abs/2609.04533)

**<font color=#1a73e8>作者：</font>** Sizhe Chen, Yu-Lin Tsai, Ivan Evtimov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection is widely recognized as a major security threat to AI agents that interact with untrusted external data, such as websites, documents, and emails. Prior work has shown that, in the text domain, black-box prompt injection can achieve near-perfect attack success rates (ASRs). In the image domain, however, existing visual prompt injection methods are substantially less effective in attacking frontier commercial VLMs for materially harmful behavior. Achieving such outputs is hard because it requires a long and/or format-compliant target string, such as a precise, parseable native tool call with exact function names and arguments. We present Repeat-After-Me, a black-box adaptive visual prompt injection attack that can reveal personally identifiable information or make malicious tool calls. Across both open-weight and commercial frontier VLMs, including Qwen3.6-27B and GPT-5.5, our method achieves ASRs exceeding 80% and 47%, respectively, under a realistic setting in which the benign user prompt is semantically unrelated to the injected task and does not verbally authorize it. In our evaluation, injections optimized on one surrogate retain 43-46% of the original ASR on two commercial victims, and cross-sample transferability retains 64-66% of the original ASR on those two models. We test our attack in a real-world OpenClaw agent: in a default OpenClaw Discord deployment, an untrusted user can use a minimally injected image to overwrite this http URL, enabling future sensitive behaviors like remote code execution and secret exfiltration. We show our new attack vector works in cases where adaptive textual prompt injection fails. We discuss potential defenses.

---


### 4. [TIER: Threat Implicitness Benchmark for Evaluating LLM Safety Behaviors](https://arxiv.org/abs/2609.05117)

**<font color=#1a73e8>作者：</font>** Thu-Hien Trinh-Thi, Hai-Yen Vong, Thanh-Ha Ung-Dung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current LLM safety benchmarks largely rely on binary metrics, overlooking how models respond to harmful prompts with varying threat implicitness. We introduce TIER, a Threat Implicitness Benchmark for behavioral safety evaluation of LLMs. TIER covers four risk domains and four threat levels, from explicit harmful requests to sophisticated jailbreaks. Responses are assessed using a six-label behavior scale and two independent LLM judges. Experiments on six open-weight LLMs show that safety behaviors evolve gradually across threat levels rather than shifting directly from refusal to compliance. Contextual prompts yield the most diverse behaviors, while jailbreaks reveal the largest robustness gaps. Furthermore, models with similar Attack Success Rates can exhibit distinct response distributions, highlighting the need for behavior-aware LLM safety evaluation.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
